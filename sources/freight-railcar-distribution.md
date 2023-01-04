# Freight railcar distribution

This formulation is inspired by the model described here:
https://www.scielo.br/j/prod/a/93btRgNKNWPKm5YWXGnhZVN/?lang=en#. The goal is to
minimize the cost of transporting goods across a network of rail terminals while
respecting terminal capacities and travel times.

## Inputs

+ $\S^d_{terminal}: I$, set of rail terminals
+ $\S^p_{horizon}: t^{max} \in \mathbb{N}$, planning horizon
  + $\S^a: T \doteq \lbrace 1 \ldots t^{max} \rbrace$, planning epochs
+ $\S^p_{travelTime[source,target]}: m \in \mathbb{N}^{I \times I}$, travel time
  between terminals
  + $\S^a: M \doteq \lbrace s, d \in I \mid m_{s,d} > 0 \rbrace$, set of edges
    between terminals
  + $\S^a: \forall i \in I, I^{in}_i \doteq \lbrace s \in I \mid (s, i) \in M \rbrace$,
    connected source terminals
  + $\S^a: \forall i \in I, I^{out}_i \doteq \lbrace d \in I \mid (i, d) \in M \rbrace$,
    connected destination terminals
+ $\S^p_{capability}: q \in \mathbb{R}^I$, maximum parking capacity at a
  terminal
+ $\S^p_{demand}: p^d \in \mathbb{R}^I$, maximum demand at a given terminal
+ $\S^p_{parkingCost}: c^{park} \in \mathbb{R}$, cost of parking a railcar
+ $\S^p_{travelCost}: c^{travel} \in \mathbb{R}$, unit cost of moving a railcar

## Outputs

+ $\S^v_{inFlow[source,target,time]}: \sigma^{in} \in \mathbb{N}^{M \times T}$,
  flow of railcars coming from a source into the target terminal at a given time
+ $\S^v_{outFlow[source,target,time]}: \sigma^{out} \in \mathbb{N}^{M \times T}$
  flow of railcars exiting a source terminal towards a target at a given time
+ $\S^v_{parking[terminal,time]}: \xi \in \mathbb{N}^{I \times T}$,
  number of railcars transiting at a given terminal and time
+ $\S^v_{arrival[source,target,time]}: \alpha \in \mathbb{N}^{M \times T}$,
  number of railcars arriving at their final destination at a given time

## Objective

We minimize total weighted cost of parked and traveling railcars.

$$
  \S^o:
  \min \sum_{t \in T} \left(
    c^{park} \sum_{i \in I} \xi_{i, t} +
    c^{travel} \sum_{(s, d) \in M} m_{s,d} \sigma^{out}_{s, d, t}
  \right)
$$

## Constraints

In- and out- railcar flows must be consistent with the number of parked cars at
each terminal.

$$
  \S^c_{parkingConservation}:
  \forall t \in T, i \in I \mid t > 1,
    \xi_{i,t} = \xi_{i,t-1}
      + \sum_{s \in I^{in}_i} \sigma^{in}_{s,i,t}
      - \sum_{d \in I^{out}_i} \sigma^{out}_{i,d,t}
$$

Outgoing railcars arrive at their destination after the corresponding travel
time.

$$
  \S^c_{flowConservation}:
  \forall (s, d) \in M, t \in T \mid t + m_{s,d} \leq t^{max},
    \sigma^{out}_{s,d,t} = \sigma^{in}_{s,d,t+m_{s,d}} + \alpha_{s,d, t+m_{s,d}}
$$

There must be enough railcars at a terminal to back the outgoing flow.

$$
  \S^c_{outFlowAtMostParked}:
  \forall i \in I, t \in T \mid t > 1,
    \sum_{d \in I^{out}_i} \sigma^{out}_{i,d,t} \leq \xi_{i,t-1}
$$

The total number of parked railcars at each terminal must be within its
capacity.

$$
  \S^c_{transitWithinCapability}:
  \forall i \in I, t \in T, \xi_{i,t} \leq q_i
$$

Total arrivals are no greater than the demand at each terminal.

$$
  \S^c_{arrivalWithinDemand}:
  \forall i \in I, \sum_{t \in T, s \in I^{in}_i} \alpha_{s,i,t} \leq p^d_{i}
$$

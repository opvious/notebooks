# Train assignment planning

This formulation is inspired by https://oaktrust.library.tamu.edu/bitstream/handle/1969.1/195170/ALIAKBARI-DISSERTATION-2021.pdf
(page 71). The goal is to compute the optimal train schedule for shipping units
so that they arrive in time to their corresponding destination while respecting
load capacity constraints.

## Inputs

+ $\S^d_{time}: T$, set of time epochs
+ $\S^d_{unit}: U$, set of units to be transported by train
+ $\S^d_{destination}: D$, set of destinations

+ $\S^p_{penalty}: p \in \mathbb{R}^{T \times U}$, lateness penalty per unit
+ $\S^p_{maxPenalty}: p^{max} \in \mathbb{R}$, maximum penalty above which a
  unit will not be accepted
+ $\S^p_{goal}: g \in \lbrace 0, 1 \rbrace^{U \times D}$, indicator parameter
  for each unit's associated destination
  + $\S^a: \forall d \in D, U^D_d \doteq \lbrace u \in U \mid g_{u,d} = 1 \rbrace $,
    convenience set of associated destinations for each unit
+ $\S^p_{minLoad}: l^{min} \in \mathbb{R}$, minimum load per train
+ $\S^p_{maxLoad}: l^{max} \in \mathbb{R}$, maximum load per train
+ $\S^p_{trainCountWeight}: w^{train} \in \mathbb{R}$, objective weight used to
  penalize the number of trains used
+ $\S^p_{totalPenaltyWeight}: w^{penalty} \in \mathbb{R}$, objective weight used
  to penalize unit lateness

## Outputs

+ $\S^v_{shipment}: \sigma \in \lbrace 0, 1 \rbrace^{T \times U}$, indicator
  variable for a unit departing at a given epoch
+ $\S^v_{departure}: \delta \in \lbrace 0, 1 \rbrace^{T \times D}$, indicator
  variable for a train departing for a given destination at a given epoch

## Objective

We minimize the weighted cost of trains and lateness penalties.

$$
  \S^o:
  \min
    w^{train} \sum_{t \in T, d \in D} \delta_{t,d} +
    w^{penalty} \sum_{t \in T, u \in U} p_{t,u} \sigma_{t,u}
$$

## Constraints

Each unit must be shipped on exactly one train.

$$
  \S^c_{exactlyOneShipment}:
  \forall u \in U, \sum_{t \in T} \sigma_{t,u} = 1
$$

Each unit must be shipped to its destination.

$$
  \S^c_{shippedToGoal}:
  \forall u \in U, t \in T, \sigma_{t,u} \leq \sum_{d \in D} \delta_{t,d} g_{u,d}
$$

At most one train can leave per epoch.

$$
  \S^c_{oneTrainAtATime}:
  \forall t \in T, \sum_{d \in D} \delta_{t,d} \leq 1
$$

Each train must be loaded with enough units.

$$
  \S^c_{atLeastMinLoad}:
  \forall t \in T, d \in D, \sum_{u \in U^D_d} \sigma_{t,u} \geq l^{min} \delta_{t,d}
$$

Each train must be not be loaded with too many units.

$$
  \S^c_{atMostMaxLoad}:
  \forall t \in T, d \in D, \sum_{u \in U^D_d} \sigma_{t,u} \leq l^{max} \delta_{t,d}
$$

Each unit must be shipped before its penalty exceeds the maximum allowed.

$$
  \S^c_{atMostMaxPenalty}:
  \forall t \in T, u \in U, \sigma_{t,u} p_{t,u} \leq p^{max}
$$

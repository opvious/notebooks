# Product allocation

## Inputs

+ A set of products, $\S^d_{product}: P$
+ Product sizes, $\S^d_{size}: S$
+ Store locations, $\S^d_{location}: L$
+ Total supply per product and size, $\S^p_{supply}: a^{max} \in \mathbb{N}^{P
  \times S}$
+ Minimum product allocation per store, $\S^p_{minAllocation}: a^{min} \in
  \mathbb{N}^P$
+ Maximum allocation across all stores and product, $\S^p_{maxTotalAllocation}:
  a^{maxTotal} \in \mathbb{N}$
+ Minimum number of available sizes per product, $\S^p_{productDiversity}:
  p^{div} \in \mathbb{N}^P$
+ Marginal demand tiers, $\S^d_{demandTier}: T$
+ Expected demand per tier, $\S^p_{demand}: d \in \mathbb{N}^{T \times P \times
  S \times L}$
+ Estimated value of demand per tier, $\S^p_{demandValue}: v \in \mathbb{N}^{T
  \times P \times S \times L}$

## Outputs

+ Product allocation, $\S^v_{allocation}: \alpha \in \mathbb{N}^{T \times
  P \times S \times L}$
+ Product allocation activation variable $\S^v_{isAllocated}: \alpha^{ind} \in
  \{0,1\}^{P \times S \times L}$

## Constraints

$$
  \begin{align}
    \S^c_{atMostSupply}&:
      \forall t \in T, p \in P, s \in S, l \in L,
        \alpha_{t,p,s,l} \leq a^{max}_{p,s} \\
    \S^c_{atMostDemand}&:
      \forall t \in T, p \in P, s \in S, l \in L,
        \alpha_{t,p,s,l} \leq d_{t,p,s,l} \\
    \S^c_{atMostMaxTotalAllocation}&:
      \sum_{t \in T, p \in P, s \in S, l \in L}
        \alpha_{t,p,s,l} \leq a^{maxTotal} \\
    \S^c_{atLeastMinAllocation}&:
      \forall p \in P,
        \sum_{t \in T, s \in S, l \in L}
          \alpha_{t,p,s,l} \geq a^{min}_p \\
  \end{align}
$$

Diversity related:

$$
  \begin{align}
    \S^c_{allocationActivated}&:
      \forall t \in T, p \in P, s \in S, l \in L,
        \alpha_{t,p,s,l} \leq a^{max}_{p,s} \alpha^{ind}_{p,s,l} \\
    \S^c_{diverseEnough}&:
      \forall p \in P, l \in L,
        \sum_{s \in S}
          \alpha^{ind}_{p,s,l} \geq p^{div}_p \\
  \end{align}
$$

## Objective

We maximize total expected realized demand value:

$$
  \S^o_{maximizeValue}:
    \max \sum_{t \in T, p \in P, s \in S, l \in L}
      v_{t,p,s,l} \alpha_{t,p,s,l}
$$

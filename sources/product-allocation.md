# Product allocation

In this example we allocate products to stores to best meet demand while
satisfying supply and diversity requirements.

## Inputs

+ A set of products, $\S^d_{product}: P$
+ Product sizes, $\S^d_{size}: S$
+ Store locations, $\S^d_{location}: L$
+ Supply per product and size, $\S^p_{supply}: a^{max} \in \mathbb{N}^{P \times S}$
+ Minimum allocation per product, $\S^p_{minAllocation}: a^{min} \in \mathbb{N}^P$
+ Maximum total allocation, $\S^p_{maxTotalAllocation}: a^{maxTotal} \in \mathbb{N}$
+ Minimum number of sizes that must be available when a product is allocated,
  $\S^p_{productDiversity}: p^{div} \in \mathbb{N}^P$
+ Marginal demand tiers, $\S^d_{demandTier}: T$
+ Expected demand, $\S^p_{demand}: d \in \mathbb{N}^{L \times P \times S \times T}$
+ Estimated value of demand per tier, $\S^p_{demandValue}: v \in \mathbb{R}^T$

## Outputs

+ Allocated product quantity, $\S^v_{allocation}: \alpha \in \mathbb{N}^{L \times P \times S \times T}$
+ Product activation variable $\S^v_{isProductAllocated}: \delta^{product} \in \lbrace 0,1 \rbrace^{P \times L}$
+ Size allocation activation $\S^v_{isSizeAllocated}: \delta^{size} \in \lbrace 0,1 \rbrace^{P \times S \times L}$

## Constraints

Allocations must respect aggregated demand and supply requirements:

$$
  \begin{align}
    \S^c_{atMostDemand}&:
      \forall t \in T, p \in P, s \in S, l \in L,
        \alpha_{l,p,s,t} \leq d_{l,p,s,t} \\
    \S^c_{atMostSupply}&:
      \forall p \in P, s \in S,
        \sum_{t \in T, l \in L} \alpha_{l,p,s,t} \leq a^{max}_{p,s} \\
    \S^c_{atMostMaxTotalAllocation}&:
      \sum_{t \in T, p \in P, s \in S, l \in L}
        \alpha_{l,p,s,t} \leq a^{maxTotal} \\
  \end{align}
$$

Each non-zero allocation must meet the minimum size and diversity requirements:

$$
  \begin{align}
    \S^c_{atLeastMinAllocation}&:
      \forall p \in P, l \in L,
        \sum_{t \in T, s \in S} \alpha_{l,p,s,t}
          \geq a^{min}_p \delta^{product}_{p,l} \\
    \S^c_{atLeastMinDiversity}&:
      \forall p \in P, l \in L,
        \sum_{s \in S} \delta^{size}_{p,s,l}
          \geq \delta^{product}_{p,l} p^{div}_p
  \end{align}
$$

Finally, we ensure activation variables are consistent:

$$
  \begin{align}
    \S^c_{sizeActivation}&:
      \forall t \in T, p \in P, s \in S, l \in L,
        \alpha_{l,p,s,t} \leq a^{max}_{p,s} \delta^{size}_{p,s,l} \\
    \S^c_{productActivation}&:
      \forall p \in P, s \in S, l \in L,
        \delta^{size}_{p,s,l} \leq a^{max}_{p,s} \delta^{product}_{p,l} \\
  \end{align}
$$

## Objective

We maximize total expected realized demand value:

$$
  \S^o_{maximizeValue}:
    \max \sum_{t \in T, p \in P, s \in S, l \in L}
      v_t \alpha_{l,p,s,t}
$$
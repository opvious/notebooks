# Portfolio selection

This example finds an allocation of assets which minimizes risk while
satisfying a minimum expected return and allocation per group.

## Inputs

+ Dimensions
  + A collection of assets: $\S^d_{asset}: A$
  + An optional collection of asset groups: $\S^d_{group}: G$
+ Parameters
  + Covariance of the chosen assets: $\S^p_{assetCovariance}: c \in \mathbb{R}^{A \times A}$
  + Expected asset return: $\S^p_{expectedAssetReturn}: m \in \mathbb{R}^A$
  + Minimum portfolio return: $\S^p_{minimumReturn}: r \in \mathbb{R}$
  + Group(s) each asset belongs to: $\S^p_{assetGroup}: g^a \in \lbrace 0, 1 \rbrace^{A \times G} \mathbb{R}$
  + Minimum allocation per group: $\S^p_{minGroupAllocation}: a^{min} \in [0,1]^G$

## Output

The only output is the allocation per asset $\S^v_{allocation}: \alpha \in [0,1]^A$ chosen in order to minimize risk:

$$
\S^o_{risk}:
  \min \sum_{a^l, a^r \in A} c_{a^l,a^r} \alpha_{a^l} \alpha_{a^r}
$$

Subject to the following constraints:

+ $\S^c_{expectedReturnAboveMinimum}: \sum_{a \in A} m_a \alpha_a \geq r$
+ $\S^c_{allocationIsTotal}: \sum_{a \in A} \alpha_a = 1$
+ $\S^c_{groupAllocationAboveMinimum}: \forall g \in G, \sum_{a \in A} \alpha_a g^a_{a,g} \geq a^{min}_g$

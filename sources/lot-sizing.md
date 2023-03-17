# Lot sizing

https://towardsdatascience.com/the-dynamic-lot-size-model-a-mixed-integer-programming-approach-4a9440ba124e

## Inputs

+ $\S^p_{horizon}: t^{max} \in \mathbb{N}$, $\S^a: T \doteq \lbrace 0 \ldots t^{max} \rbrace$
+ $\S^p_{holdingCost}: h \in \mathbb{R}^T$
+ $\S^p_{setupCost}: s \in \mathbb{R}^T$
+ $\S^p_{demand}: d \in \mathbb{R}_+^T$

## Outputs

+ $\S^v_{production}: \alpha \in \mathbb{R}_+^T$
+ $\S^v_{isProducing}: \delta \in \lbrace 0, 1 \rbrace^T$
+ $\S^v_{inventory}: \iota \in \mathbb{R}_+^T$

## Objective

$$
  \S^o_{minimizeCost}: \min \sum_{t \in T} \left( h_t \iota_t + s_t \delta_t \right)
$$

## Constraints

$$
  \begin{align}
    \S^c_{inventoryPropagation}&:
      \forall t \in T \mid t > 0,
        \iota_t = \iota_{t-1} + \alpha_t - d_t \\
    \S^c_{inventorySetup}&:
      \iota_0 = \alpha_0 - d_0 \\
    \S^c_{productionActivated}&:
      \forall t \in T,
        \alpha_t \leq \left( \sum_{w \in T} d_w \right) \delta_t
  \end{align}
$$

# Portfolio selection

+ $\S^d_{asset}: A$
+ $\S^d_{group}: G$

+ $\S^p_{covariance}: c \in \mathbb{R}^{A \times A}$
+ $\S^p_{mean}: m \in \mathbb{R}^A$
+ $\S^p_{return}: r \in \mathbb{R}$
+ $\S^p_{assetGroup}: g^a \in \lbrace 0, 1 \rbrace^{A \times G} \mathbb{R}$
+ $\S^p_{minGroupAllocation}: a^{min} \in [0,1]^G$
+ $\S^v_{allocation}: \alpha \in [0,1]^A$

+ $\S^c_{expectedReturnAboveMinimum}: \sum_{a \in A} m_a \alpha_a \geq r$
+ $\S^c_{allocationIsTotal}: \sum_{a \in A} \alpha_a = 1$
+ $\S^c_{groupAllocationAboveMinimum}: \forall g \in G, \sum_{a \in A} \alpha_a g^a_{a,g} \geq a^{min}_g$

+ $\S^o: \min \sum_{a^l, a^r \in A} c_{a^l,a^r} \alpha_{a^l} \alpha_{a^r}$

# Train assignment planning

https://oaktrust.library.tamu.edu/bitstream/handle/1969.1/195170/ALIAKBARI-DISSERTATION-2021.pdf

+ $\S^d_{time}: T$
+ $\S^d_{unit}: U$
+ $\S^d_{destination}: D$

+ $\S^p_{penalty}: p \in \mathbb{R}^{T \times U}$
+ $\S^p_{maxPenalty}: p^{max} \in \mathbb{R}$
+ $\S^p_{goal}: g \in \{0,1\}^{U \times D}$, $\S^a: \forall d \in D, U^D_d \doteq \{ u \in U \mid g_{u,d} = 1 \}$
+ $\S^p_{minLoad}: l^{min} \in \mathbb{R}$
+ $\S^p_{maxLoad}: l^{max} \in \mathbb{R}$

+ $\S^v_{shipment}: \sigma \in \{0,1\}^{T \times U}$
+ $\S^v_{departure}: \delta \in \{0,1\}^{T \times D}$

$\S^o: \min \sum_{t \in T, d \in D} \delta_{t,d}$

$$
  \S^c_{exactlyOneShipment}:
  \forall u \in U, \sum_{t \in T} \sigma_{t,u} = 1
$$

$$
  \S^c_{shippedToGoal}:
  \forall u \in U, t \in T, \sigma_{t,u} \leq \sum_{d \in D} \delta_{t,d} g_{u,d}
$$

$$
  \S^c_{oneTrainAtATime}:
  \forall t \in T, \sum_{d \in D} \delta_{t,d} \leq 1
$$

$$
  \S^c_{atLeastMinLoad}:
  \forall t \in T, d \in D, \sum_{u \in U^D_d} \sigma_{t,u} \geq l^{min} \delta_{t,d}
$$

$$
  \S^c_{atMostMaxLoad}:
  \forall t \in T, d \in D, \sum_{u \in U^D_d} \sigma_{t,u} \leq l^{max} \delta_{t,d}
$$

$$
  \S^c_{atMostMaxPenalty}:
  \forall t \in T, u \in U, \sigma_{t,u} p_{t,u} \leq p^{max}
$$

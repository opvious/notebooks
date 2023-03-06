# Fantasy Premier League

We'll start by listing our inputs:

* A total budget for player salaries $\S^p_{budget}: b \in \mathbb{R}_+$
* A salary per player $\S^p_{salary}: s \in \mathbb{R}_+^P$, where $\S^d_{player}: P$ is the set of players
* An expected number of points per player $\S^p_{expectedPoints}: v \in \mathbb{R}^P$
* Each player's position, represented as an indicator matrix $\S^p_{playerPosition}: a \in \lbrace 0, 1 \rbrace^{P \times R}$ (1 if the player plays at a given position and 0 otherwise), where $\S^d_{position}: R$ is the set of positions (goalkeeper, ...)
* A lower ( $\S^p_{formationMin}: f^{min} \in \mathbb{N}^R$) and upper ($\S^p_{formationMax}: f^{max} \in \mathbb{N}^R$) bounds on the number of players per position
* Each player's club, represented as another indicator matrix $\S^p_{playerClub}: m \in \lbrace 0,1 \rbrace^{P \times C}$, where $\S^d_{club}: C$ is the set of clubs

Our model has a single binary output $\S^v_{selection}: \sigma \in \lbrace 0, 1 \rbrace^P$ indicating which players are selected for the team. It is chosen to maximize the team's expected points: $\S^o_{totalExpectedPoints}: \max \sum_{p \in P} v_p \sigma_p$ , subject to the following constraints:

* Exactly 11 players are selected: $\S^c_{teamSize}: \sum_{p \in P} \sigma_p = 11$
* The total salary cost is within budget: $\S^c_{withinBudget}: \sum_{p \in P} \sigma_p s_p \leq b$
* At most 3 players are selected per club: $\S^c_{clubDiversity}: \forall c \in C, \sum_{p \in P} \sigma_p m_{p, c} \leq 3$
* The number of players per position is within formation requirements: $\S^c_{formationLowerBound}: \forall r \in R, \sum_{p \in P} \sigma_p a_{p, r} \geq f^{min}_r$ and $\S^c_{formationUpperBound}: \forall r \in R, \sum_{p \in P} \sigma_p a_{p, r} \leq f^{max}_r$

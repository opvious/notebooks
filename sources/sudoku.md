# Sudoku model

We start by defining the sets of possible values
$\S^a: N \doteq \lbrace 1 \ldots 9 \rbrace$ and possible
positions $\S^a: P \doteq \lbrace 0 \ldots 8 \rbrace$. With
these two, we can define the variable we will optimize over:
$\S^v_{output[row,column,value]}: \alpha \in \lbrace 0,1 \rbrace^{P \times P \times N}$.

We do not specify an objective as we only care about finding a feasible solution
to the game's constraints. The first constraint enforces that the output matches
any input hints $\S^p_{input[row,column,value]}: h \in \lbrace 0,1 \rbrace^{P \times P \times N}$:

$$
  \S^c_{mask[row,column,value]}:
  \forall i,j \in P, v \in N, \alpha_{i,j,v} \geq h_{i,j,v}
$$

Then there are four types of unicity constraints, all enforcing that there must
be one of each value. First, per cell:

$$
  \S^c_{onePerCell}:
  \forall i, j \in P,
    \sum_{v \in N} \alpha_{i,j,v} = 1
$$

Then, per row and column:

$$
  \S^c_{onePerRow}:
  \forall v \in N, i \in P,
    \sum_{j \in P} \alpha_{i,j,v} = 1
$$

$$
  \S^c_{onePerColumn}:
  \forall v \in N, j \in P,
    \sum_{i \in P} \alpha_{i,j,v} = 1
$$

Finally, per box:

$$
  \S^c_{onePerBox}:
    \forall v \in N, k^{b} \in P,
    \sum_{k^{c} \in P}
    \alpha_{
        3 \left\lfloor \frac{k^{b}}{3} \right\rfloor
        + \left\lfloor \frac{k^{c}}{3} \right\rfloor,
        3 (k^{b} \bmod 3) + (k^{c} \bmod 3),
        v
    }
    = 1
$$

Note that our reduction to 4-SAT/2-FLIP uses 2-flips very sparingly, only when we switch _f_ (switch which circuit is active). In the reduction to 3-SAT/2-FLIP we use a 2-flip potentially every time we propagate a value through the circuit.

The shadow variables idea does not work here, because we cannot extend the clauses here as they are already 3-clauses.

## Cyclic Polm

We can strengthen the result from Section 3 to cyclic groups with a proof technique similar to the NP-hardness proof for the global optima from [20].

\(\blacktriangleright\) **Theorem 19.** _Polm is PLS-complete even there exists a permutation_ \(\sigma\) _such that all permutations_ \(\pi_i=\sigma^j\).

We reduce from 4-SAT/1-FLIP with lexicographic payoffs, which is PLS-complete according to Theorem 3. Let _F_ be a 4-CNF formula _x_<sub>1</sub>_,...,x<sub>n</sub>_ its variables, and _C_<sub>1</sub>_,...,C<sub>m</sub>_ its clauses from highest-priority to lowest-priority.

Consider the first _n_ prime numbers _p_<sub>1</sub>=2,3,5_,...,p<sub>n</sub>_ and set \(N:=p_1\cdot p_2\cdot\cdots\cdot p_n\). We let Z_<sub>k</sub>_ denote the group (Z_/k_Z,+) and also, by a slight abuse of notation, the set {0,1_,...,k_-1}. By the Chinese remainder theorem, the function

\(f:\mathbb{Z}_N\rightarrow\mathbb{Z}_{p_1}\times\cdots\times\mathbb{Z}_{p_n}\)<br>
\(l\mapsto(lmodp_1,\dots,lmodp_n)\)

is bijective, and both the function and its inverse can be computed in polynomial time.

**The positions.**<br>
Our positions will be arranged in _cycles_, one for each variable and one for each clause. In each cycle, the positions are numbered as 0_,...,l_-1, where _l_ is the length of the cycle. The initial bit string _s_ will place a 1 on each 0-position in each cycle and 0s elsewhere. Each permutation will rotate each cycle by a given amount; thus, each element in the orbit of _s_ will have exactly one 1 on each cycle.

**Variable positions.**<br>
For every variable _x<sub>i</sub>_ we create a cycle of length _pi<sub>i</sub>_ with positions 0,1_,...,pi<sub>i</sub>_-1. An element in the orbit has one 1 per cycle and thus assigns each variable _x<sub>i</sub>_ a value in {0,1_,...,pi<sub>i</sub>_-1}. We call the positions 2_,...,pi<sub>i</sub>_-1 bad-color-positions and make them very expensive (giving them the highest priority) to make sure that a local minimum only assigns values 0 and 1 to the variables. Among bad-color-positions, the order is arbitrary.

**Clause positions.**<br>
Let _C_ be a clause of _F_ and suppose it contains the variables _x<sub>i</sub>,x<sub>j</sub>,x<sub>k</sub>_ and _x<sub>l</sub>_. We create a cycle of length _pi<sub>i</sub>p<sub>j</sub>p<sub>k</sub>p<sub>l</sub>_. Each \(t\in\{0,\dots,pi_ip_jp_kp_l-1\}\) becomes, when taking remainders modulo _pi<sub>i</sub>,p<sub>j</sub>,p<sub>k</sub>,p<sub>k</sub>_, a tuple \((r_i,r_j,r_k,r_l)\in\mathbb{Z}_{pi_i}\times\mathbb{Z}_{p_j}\times\mathbb{Z}_{p_k}\times\mathbb{Z}_{p_l}\). Should this triple be in {0,1}<sup>4</sup> and should it be the unique truth assignment violating clause _C_, we call _t_ the _clause- violating position_ on that cycle. In our lexicographic ordering, we place the clause-violating positions directly after the bad-color-positions; among themselves, we order them as the ordering of the clauses of _F_ dictates: the clause-violating position of clause _C<sub>i</sub>_ has higher priority than that of _C_<sub>_i_+1</sub>.

**The permutations.**<br>
Let \(\pi\) be the permutation that rotates each cycle by one (maps position _t_ on the cycle to position _t_+1, and so on). For \(m\in\mathbb{N}\) the permutation \(\pi^m\) rotates the variable cycle of _x<sub>i</sub>_ by _m_ mod _pi<sub>i</sub>_ and the clause cycle of a clause with variables _x<sub>i</sub>,x<sub>j</sub>,x<sub>k</sub>_ and _x<sub>l</sub>_ by _m_ mod _pi<sub>i</sub>p<sub>j</sub>p<sub>k</sub>p<sub>l</sub>_.




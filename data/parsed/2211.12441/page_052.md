**Algorithm 2** \(\mathrm{MinRInv}(T_v,\rho)\), Dynamic Programming

**Input:** Tree _T<sub>v</sub>_ with child leaf sets _L_<sub>1</sub>_,...,L<sub>k</sub>_, ranking \(\rho\)<br>
Initialize Cost\[_S_\], where _S_ is over all subsets of {1_,...,k_}.<br>
\(\mathrm{Cost}[\varnothing]\leftarrow 0\)<br>
**for** _i_ from 1 to _k_ **do**<br>
**for** all sets _S_ of size _i_ **do**<br>
\(\mathrm{Cost}[S]\leftarrow\mathrm{min}_{s\in S}(\mathrm{Cost}(S\backslash\{s\})+\sum_{j\in S,j\neq s}\mathrm{XInv}_\rho(L_j,L_s)))\)<br>
**return** Cost\[{1_,...,k_}\].

_Proof._ For a graph _G_ with _n_ vertices _v_<sub>1</sub>_,...,v<sub>n</sub>_ and _m_ directed edges _e_<sub>1</sub>_,...,e<sub>m</sub>_, we construct a depth-2 tree _T_ and a ranking \(\rho\) of its leaves. We will assume that _G_ has no isolated vertices; this goes without loss of generality as isolated vertices can be dropped from an instance of minimum arc feedback set without affecting the answer. We also assume that between any two vertices at most one of the two directed edges is present; this is also without loss of generality since dropping the edges in case both are present reduces the answer by one. Finally, for ease of notation, we allow the ranking \(\rho\) to be an injective mapping into the integers; this can be changed easily by replacing each integer by its rank in the range.

In the first layer, the root of _T_ has _n_ children corresponding to _v_<sub>1</sub>_,...,v<sub>n</sub>_. The second layer has leaves with ranks encoding the edges of _G_. For each edge _e<sub>k</sub>_ going from _v<sub>i</sub>_ to _v<sub>j</sub>_, we add two leaves under _v<sub>i</sub>_ with ranks -2_k_ and 2_k_-1, and two leaves under _v<sub>j</sub>_ with ranks -2_k_+1 and 2_k_, as shown in Fig. 18. All ranks are distinct.

Consider the number of inversions in _T_ induced by an ordering \(\sigma\) of _v_<sub>1</sub>_,...,v<sub>n</sub>_. For each edge _e<sub>k</sub>_, the number of inversions between the leaves of rank -2_k_ and 2_k_-1 and the leaves of rank -2_k_+1 and 2_k_ is 1 if \(\sigma(v_i)<\sigma(v_j)\) and 3 if \(\sigma(v_i)>\sigma(v_j)\). These four leaves also form 8(_m_-1) inversions with all other leaves, keeping in mind that these inversions are counted twice when summed up over all edges.

Therefore, the minimum number of inversions in _T_ is given by

\(\mathrm{MinInv}(T,\rho)=\mathrm{min}_\sigma\left(4m(m-1)+m+2\cdot\sum_{e_k\in E}\mathbb{I}[\sigma(v_i)>\sigma(v_j)]\right).\)

The size of the minimum arc feedback set is precisely \(\mathrm{min}_\sigma\left(\sum_{e_k\in E}\mathbb{I}[\sigma(v_i)>\sigma(v_j)]\right)\), which can be<tbc>

G:
ek
T:
n
Vi
vj
Vi
vj
2 degG(vi)
2 degG(vj)
P:
-2k
2k - 1
-2k + 1
2k

Figure 18: Encoding of an edge _e<sub>k</sub>_


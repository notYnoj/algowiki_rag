<tbc>\(\frac{\gamma_*}{2}<\gamma\le\gamma_*\) (recall that \(\gamma_*\) is a multiple of 2 by construction). However, this necessarily yields at least \(\frac{\gamma_*}{2}\) blocking pairs for each of \(x_i^r\) and \(c_j^s\), and therefore \(max_{a_i\in\{x_i^r,c_j^s\}}|bp_{a_i}^J(M')|\ge\frac{\gamma_*}{2}\) . Thus, for every maximum-cardinality \(M'\) of _J_, \(max_{a_r\in A}|bp_{a_r}^J(M')|\ge max_{a_i\in\{x_i^r,c_j^s\}}|bp_{a_i}^J(M')|\ge\frac{\gamma_*}{2}\) as required.

Note that, because we assume that \(n\ge 3\), \(\frac{\gamma_*}{2}>290>1\), so we always introduce a gap. Our claims above establish that if _B_ is a yes-instance (i.e., it is satisfiable), then the optimal value of Minimax-AlmostStable-Max-smi is at most 1. On the other hand, if _B_ is a no-instance (i.e., it is not satisfiable), then the optimal value of Minimax-AlmostStable-Max-smi is at least

\(\frac{\gamma_*}{2}=\frac{2(\lfloor A|^{1/2}\rfloor+1)}{2}=\left\lfloor|A|^{1/2}\right\rfloor+1>|A|^{1/2}.\)

Thus, any approximation algorithm that returns a solution that is at most a square root of the total number of agents away from the optimal solution could decide the NP-complete problem (2,2)-e3-sat. This establishes the inapproximability result as required.

## 7 Exact Integer Linear Programs and Experiments

In the previous section, we explored approximation algorithms as a way to deal with the strong intractability results for minimax almost-stability. However, we also encountered a strong intractability frontier there when seeking approximation guarantees with respect to the number of agents, as seen in Theorem 6.3. Our final contribution consists of two compact integer linear programming formulations (ILP) that solve our central optimisation problems of interest to optimality and some experimental results showing that the minimum maximum number of blocking pairs per agent can be expected to be small.

### 7.1 ILP tions

Let \(I=(A,\succ)\) be a problem instance and consider the ILP below.

\(minr\)<br>
\(\text{s.t.}\sum_{a_j\in A\backslash\{a_i\}}x_{ij}\le 1\forall a_i\in A\)<br>
\(\sum_{a_j:a_j\text{not on}\succ_i}x_{ij}=0\forall a_i\in A\)<br>
\(x_{ij}=x_{ji}\forall a_i,a_j\in A\)<br>
\(b_{ij}=b_{ji}\forall a_i,a_j\in A\)<br>
\(\sum_{a_k:a_k\unknown_ia_j}x_{ik}+\sum_{a_k:a_k\unknown_ja_i}x_{jk}+b_{ij}\ge 1\forall a_i,a_j\in A\)<br>
\(\sum_{a_j\in A\backslash\{a_i\}}b_{ij}\le r\forall a_i\in A\)<br>
\(x_{ij},b_{ij}\in\{0,1\}\forall a_i,a_j\in A\)<br>
\(r\in\mathbb{Z}^{\ge 0}\)

It is easy to see that this ILP corresponds to Minimax-AlmostStable-sri: we introduce binary variables \(x_{ij}\in\{0,1\}\) to indicate matches between pairs of agents \(\{a_i,a_j\}\in A\), as well as binary variables \(b_{ij}\in\{0,1\}\) to indicate blocking pairs between agents _a<sub>i</sub>_ and _a<sub>j</sub>_. We enforce that the _x<sub>ij</sub>_ variables, collectively, represent a matching among acceptable agents in _I_ (allowing for the possibility of an agent being matched to themselves), and enforce the almost-stability<tbc>


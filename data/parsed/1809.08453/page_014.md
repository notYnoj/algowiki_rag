<tbc>to his/her choice of rank 2_j<sub>l</sub>_+2, and his/her weight in the GGI aggregation is \(n_c^{j_l+1}\) because his/her disutility is the highest among the two agents. Hence:

\(\mathtt{GGI}_\mathbf{X}(\mathbf{d}(\mathbf{x}))\ge\Delta_l+\sum_{l=1}^{n_c-k}n_c^{j_l+1}(d(2j_l+2)-d(2j_l+1))\)<br>
\(=\Delta_u-n_c(1+n_c)+\sum_{l=1}^{n_c-k}n_c^{j_l+1}n_c^{-j_l}\)<br>
\(=\Delta_u-n_c(1+n_c)+(n_c-k)n_c\)<br>
\(=\Delta_u-(k+1)n_c\)<br>
\(>\Delta_u-(k+1)(n_c+1)\)

This concludes the proof of the lemma.

## 4 A 2-approximation Algorithm

We now present a polynomial time 2-approximation algorithm for the GGI stable marriage problem.

The 2-approximation algorithm uses a linear programming formulation of the stable marriage problem, based on the rotation poset \[Gusfield and Irving, 1989\]. It is indeed well- known that the set of stable marriages can be characterized by the following set of inequalities where we have one binary variable \(y(\rho)\) for each rotation in the rotation poset and:

\(y(\rho')-y(\rho)\le 0\) (9)

for each pair of rotations such that \(\rho\) precedes \(\rho'\). Variable \(y(\rho)\) is equal to 1 if rotation \(\rho\) is included in the closed set of rotations associated to the stable marriage and 0 otherwise. Importantly, note that the extreme points of the polytope defined by constraints 9 for \(0\le y(\rho)\le 1,\forall\rho\) are in one-to-one correspondence with the stable marriages of the instance \[Gusfield and Irving, 1989\]. Furthermore, the stable marriage **x** characterized by variables \(y(\rho)\) can be inferred by using Equations 10, 11 and 12 below.

To explain this point we introduce some notations. Let \(\Gamma\) denote the set of man-woman pairs included in at least one stable matching. These pairs can be found by looking at the pairs that are created and broken by each rotation. Indeed, note that for each pair \((m,w)\in\Gamma\), there exists exactly one rotation, denoted by \(\rho_\mathtt{get}(m,w)\), that creates this pair (unless this pair is in **x**_<sup>m</sup>_) and exactly one rotation, denoted by \(\rho_\mathtt{break}(m,w)\), that breaks this pair (unless this pair is in **x**_<sup>w</sup>_). Then, one can compute variables _x<sub>ij</sub>_ corresponding to a set of variables \(y(\rho)\) by using the following equations:

\(x_{ij}=1-y(\rho_\mathtt{break}(i,j)),\forall(i,j)\in\Gamma\text{s.t.}x_{ij}^m=1\) (10)

\(x_{ij}=y(\rho_\mathtt{get}(i,j)),\forall(i,j)\in\Gamma\text{s.t.}x_{ij}^w=1\) (11)

\(x_{ij}=y(\rho_\mathtt{get}(i,j))-y(\rho_\mathtt{break}(i,j)),\forall(i,j)\in\Gamma\text{s.t.}x_{ij}^m=x_{ij}^w=0\) (12)

**Example 7** _Let us come back to Example 1. The pairs in_ \(\Gamma\) _are listed in the left column of  2. The rotations_ \(\rho_\mathtt{get}(m,w)\) _and_ \(\rho_\mathtt{break}(m,w)\) _for each pair_ (_m,w_) _are given in the middle and right columns._


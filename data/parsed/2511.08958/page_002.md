<tbc>**ACM subject classification:** Theory of computation: Design and analysis of algorithms; Dynamic programming; Problems, reductions and completeness.

## 1. Introduction

For two sequences _A_\[1_..n_\] and _B_\[1_..m_\] over a totally ordered alphabet, a common subsequence must respect the position order in both inputs. The longest common bitonic subsequence (LCBS) additionally requires a strict increase to one peak, followed by a strict decrease. Purely increasing and purely decreasing sequences are allowed. We write LCBS(_A,B_) for the optimum length, with value zero when the inputs have no common symbol.

The problem combines a simple value-shape constraint with two embedding orders. Let _V_={(_i,j_):_A_\[_i_\]=_B_\[_j_\]} and _M_=|_V_|. For a match _v_, let _I(v_) be the longest increasing common subsequence ending exactly at _v_, and let _D(v_) be the longest decreasing common subsequence starting exactly at _v_. The central identity is

\(LCBS(A,B)=max_{v\in V}\{I(v)+D(v)-1\},\) (1)

with the empty maximum interpreted as zero. Anchoring both halves at the same match makes their embeddings compatible; the peak is counted only once.

Our main algorithm evaluates these endpoint arrays using two sweeps over the matches and standard two-dimensional dominance maxima. Put _S=n+m_ and lg<sub>+</sub>_x_=log<sub>2</sub>(2+_x_). The resulting time bound is

\(O\big(Slg_+S+Mlg_+^2M\big),\) (2)

and total auxiliary space is _O(S+M_lg<sub>+</sub>_M_), including preprocessing. The dynamic-programming structure alone occupies _O(M_lg<sub>+</sub>_M_) space. These bounds include recovery of an optimal subsequence. The distinction between total workspace and the match structure matters when most input positions have no match.

### Contribution and scope.

The contribution is an explicit constructive treatment of the bitonic objective, together with a conditional hardness reduction. The sparse algorithm is a specialization of established dominance dynamic programming, not a new range-searching data structure. The dense algorithm is a baseline built from the usual longest common increasing subsequence (LCIS) scan. Equation (1) explains exactly which LCIS information must be retained: an endpoint value for every candidate common peak, rather than only a global optimum or one optimal increasing subsequence. Any LCIS algorithm exposing this interface can be substituted; we do not claim that existing LCIS algorithms are intrinsically unable to provide it.

Beyond this formulation, a padding construction gives an exact relation between LCIS and LCBS optimum values. Consequently, an \(O(N^{2-\varepsilon})\) algorithm for general length-_N_ LCBS inputs would contradict the known SETH-based LCIS lower bound \[1\]. This makes precise the worst-case limitation under which match-sensitive algorithms remain useful. The accompanying code independently validates the formulation and illustrates the crossover between the dense and sparse implementations.


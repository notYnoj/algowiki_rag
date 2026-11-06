• the recurrence has constant in-degree and is max-type with deterministic tie-breaking (Section 3).

Applying Theorem 2 to this DAG yields the following.

**Corollary 1** (Asymmetric alignment)**.** _Let_ \(A\in\Sigma^m\), \(B\in\Sigma^n\) _with_ \(m\le n\)_, and consider any standard global alignment DP on the_ \(m\times n\) _grid with a max-type scoring scheme and deterministic tie-breaking. Then there is a deterministic algorithm that:_

• _computes an optimal alignment between A and B,_<tbc>

• _runs in time polynomial in mn, and_<tbc>

• _uses space_<tbc>

<tbc>\(\mathsf{SPACE}=O\big(mlog(mn)+polylog(mn)\big),\)<tbc>

<tbc>_measured in tape cells over a fixed finite alphabet._

In particular, for regimes of practical interest such as long-read or genome-to-read alignment where \(m\checkmark n\), the space usage is essentially _O(m_) words, matching the space needed merely to evaluate the DP value using a rolling row (or column) buffer. Classical Hirschberg achieves _O(m+n_) words of space; Corollary 1 shows that in the offline random-access model, traceback can be performed with memory comparable to the _shorter_ sequence length, up to lower-order polylogarithmic terms, independently of the larger dimension _n_.

## 6.2 One-dimensional recurrences

Consider a DP defined on a linear chain _V_={1_,...,T_}, where each state _x<sub>i</sub>_ depends only on the previous _k_ states for some fixed constant _k_:

\(x_i=F(x_{i-1},x_{i-2},\dots,x_{i-k}),i>k,\)

and suppose this recurrence can be encoded as a max-type semiring DP satisfying Assumption 2, with deterministic tie-breaking so that there is a unique optimal witness sequence.

Typical examples include linear recurrences, simple filters, and DP formulations on paths or sequences with constant-width neighborhoods.

• The underlying DAG is a line with bounded backward edges, so any cut between _i_ and _i_+1 needs to retain only the last _k_ values.<tbc>

• Thus \(\omega=\Theta(k)=\Theta(1)\), independent of _T_.

**Corollary 2** (1D traceback)**.** _For any local recurrence on a chain of length T with constant in-degree that fits the framework of Assumption 2 and has a unique optimal witness sequence, the witness sequence can be reconstructed deterministically in space_

\(\mathsf{SPACE}=O\big(polylogT\big)\text{\textit{cells}}.\)

This matches the intuition that traceback on a simple path should be "almost free" in space: the _O_(polylog_T_) term accounts only for indexing and recursion metadata, while the dependence on the structural width parameter is constant. It also aligns with the classical observation that recursive bisection on a line (essentially a one-dimensional Hirschberg) can be implemented in logarithmic space.

## 6.3 Banded alignment

In many bioinformatics applications, the optimal alignment between two sequences is expected to follow the main diagonal of the DP grid up to a bounded deviation. The _banded alignment_ problem restricts the state space to cells (_i,j_) satisfying \(|i-j|\le B/2\) for some bandwidth parameter _B_.

Let _N_=max{_m,n_}, and consider an \(N\times N\) DP grid restricted to a band of width _B_ around the main diagonal.

• The number of states is \(T=\Theta(BN)\).<tbc>

• A column-wise or diagonal-wise topological sweep sees at most _B_ active cells at any cut, so \(\omega=\Theta(B)\).<tbc>


these two inequalities hold simultaneously if and only if

\(q_e=q_o=q.\) (35)

Conversely, under (35), both _V<sub>E</sub>_ and _V<sub>O</sub>_ are ordinary \(q\times q\) Vandermonde matrices. Since the indices _n_<sub>1</sub>_,...,n_<sub>2_q_</sub> are distinct, the eigenvalues \(\lambda_{n_1},\dots,\lambda_{n_{2q}}\), and hence the nodes _x_<sub>_n_<sub>1</sub></sub>_,...,x_<sub>_n_<sub>2_q_</sub></sub>, are pairwise distinct. Therefore both _V<sub>E</sub>_ and _V<sub>O</sub>_ are non-singular. Since the row and column transformations used above are invertible, it follows that

\(det\Lambda_0\neq 0.\)

Thus, the strict parity balance (35) is necessary and sufficient for the leading-order matrix \(\Lambda_0\) to be non-singular. This conclusion concerns \(\Lambda_0\) only; the invertibility of the actual KEG-D coefficient matrix \(\Lambda_N\) requires a separate comparison with \(\Lambda_0\). In particular, (35) explains the choice of exactly _q_ even and _q_ odd indices.

We now study the leading-order structure of the error system (32). Replacing \(\kappa_{n_s}^{(+)}\) and \(\kappa_{n_s}^{(-)}\) by their leading terms from (9) and dividing by _K_<sub>0</sub>, we are led to the linear evaluation map<tbc>

\(\mathcal{E}:\mathcal{P}_q\times\mathcal{P}_q\longrightarrow\mathbb{C}^{2q},\)

<tbc>defined by

\(\mathcal{E}(\Phi^+,\Phi^-):=\big((-1)^{n_s}\Phi^+(x_{n_s})-\Phi^-(x_{n_s})\big)_{s=1}^{2q},\)

where P_<sub>q</sub>_ denotes the space of polynomials of degree at most _q_.

A pair \((\Phi^+,\Phi^-)\) belongs to kerE if and only if

\(W_E(x_{n_s})=0,s\in E,\)<br>
\(W_O(x_{n_s})=0,s\in O,\)

where

\(W_E(x):=\Phi^+(x)-\Phi^-(x),W_O(x):=-\Phi^+(x)-\Phi^-(x).\) (36)

Both _W<sub>E</sub>_ and _W<sub>O</sub>_ have degree at most _q_. We also define

\(\Pi_E(x):=\prod_{s\in E}(x-x_{n_s}),\Pi_O(x):=\prod_{s\in O}(x-x_{n_s}).\) (37)

**Lemma 3.1** (Kernel dimension)**.** _The kernel of_ E _has dimension_ 2 _if and only if_<tbc>

\(q_e\le q+1,q_o\le q+1.\)

<tbc>_Proof._ The correspondence

\((\Phi^+,\Phi^-)\longleftrightarrow(W_E,W_O)\)

defined by (36) is a linear bijection of \(\mathcal{P}_q\times\mathcal{P}_q\) onto itself.

For a pair \((\Phi^+,\Phi^-)\in ker\mathcal{E}\), the corresponding polynomial \(W_E\in\mathcal{P}_q\) must vanish at the _q<sub>e</sub>_ distinct nodes _x<sub>n<sub>s</sub></sub>_, \(s\in E\). Therefore, the space of possible _W<sub>E</sub>_ has dimension<tbc>

\(max\{0,q+1-q_e\}.\)

<tbc>Similarly, the space of possible _W<sub>O</sub>_ has dimension<tbc>

\(max\{0,q+1-q_o\}.\)

<tbc>Hence<tbc>

\(dimker\mathcal{E}=max\{0,q+1-q_e\}+max\{0,q+1-q_o\}.\)


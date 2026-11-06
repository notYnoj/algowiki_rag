<tbc>is the single-particle adjacency matrix of the open path graph _P<sub>n</sub>_, and<tbc>

\(\mathrm{d}\Gamma_k:\mathfrak{gl}(n,\mathbb{C})\rightarrow\mathfrak{gl}\left(W_k\right)\)

<tbc>denotes the _k_-particle second-quantization operator (i.e., the differential of the _k_-th exterior power representation; see, e.g., \[14\]). Explicitly, for any operator \(B\in\mathrm{End}(\mathbb{C}^n)\), its action on elementary wedge products is given by the derivation rule<tbc>

\(\mathrm{d}\Gamma_k(B)\left(v_1\wedge\cdots\wedge v_k\right)=\sum_{m=1}^kv_1\wedge\cdots\wedge\left(Bv_m\right)\wedge\cdots\wedge v_k.\) (B4)

<tbc>As \(\mathrm{d}\Gamma_k\) is a Lie algebra representation, it preserves Lie brackets:<tbc>

\([\mathrm{d}\Gamma_k(A),\mathrm{d}\Gamma_k(B)]=\mathrm{d}\Gamma_k\left([A,B]\right)\forall A,B\in\mathfrak{u}(n).\) (B5)

<tbc>Recall that a quantum system consisting of a single particle constrained to _n_ discrete modes has a single- particle Hilbert space \(\mathcal{H}_1\cong\mathbb{C}^n\) spanned by localized basis states \(\{|1\rangle,|2\rangle,\dots,|n\rangle\}\). The Lie algebra of all skew-Hermitian operators acting on the _n_-dimensional single-particle Hilbert space forms the full unitary Lie algebra u(_n_). Physical generators such as the adjacency matrix _A<sub>P<sub>n</sub></sub>_ (see (B3)) and the local site energy operator \(E_{11}=|1\rangle\langle 1|\) act directly on C_<sup>n</sup>_. Under repeated Lie brackets, these two local operators generate the full single-particle unitary Lie algebra:<tbc>

\(\mathfrak{g}_1:=\left\langle iA_{P_n},iE_{11}\right\rangle_\mathrm{Lie}\cong\mathfrak{u}(n).\) (B6)

<tbc>To establish this, define the elementary basic matrix units for \(j\in\{1,\dots,n-1\}\):<tbc>

\(S_j=i(E_{j,j+1}+E_{j+1,j}),A_j=E_{j,j+1}-E_{j+1,j}.\)

<tbc>Expressing the tunneling generator as \(iA_{P_n}=\sum_{r=1}^{n-1}S_r\), we proceed by induction. Initiating with _D_<sub>1</sub>=_iE_<sub>11</sub>, suppose that _iE<sub>jj</sub>_, _S<sub>j</sub>_, and _A<sub>j</sub>_ have been generated up to index _j_. The nested commutators

\(\left[iE_{jj},iA_{P_n}-\sum_{r<j}S_r\right]=-A_j,[iE_{jj},A_j]=S_j,[S_j,A_j]=2i(E_{j+1,j+1}-E_{jj})\)

successively yield _iE_<sub>_jj_+1</sub>, _S_<sub>_j_+1</sub>, and _A_<sub>_j_+1</sub>. Finally, taking commutators of adjacent off-diagonal matrix units generates all remaining off-diagonal generators, confirming that \(\langle iA_{P_n},iE_{11}\rangle_\mathrm{Lie}=\mathfrak{u}(n)\).

The corresponding dynamical Lie group acts transitively on the single-particle state space, establishing full single-particle controllability. Furthermore, for any excitation number \(1\le k\le n-1\), the _k_-particle second-quantization representation \(\mathrm{d}\Gamma_k\) of u(_n_) on \(W_k\cong\wedge^k\mathbb{C}^n\) is faithful, implying that the corresponding dynamical Lie algebra g_<sub>n,k</sub>_ coincides with the exact image of the single-particle algebra g<sub>1</sub>=u(_n_):<tbc>

\(\mathfrak{g}_{n,k}:=\left\langle iH_M\big|_{W_k},iH_P\big|_{W_k}\right\rangle_\mathrm{Lie}=\left\langle id\Gamma_kA_{P_n},id\Gamma_kE_{11}\right\rangle_\mathrm{Lie}\cong\mathrm{d}\Gamma_k(\mathfrak{u}(n))\cong\mathfrak{u}(n).\) (B7)

<tbc>In particular, its real dimension satisfies

\(\mathrm{dim}_\mathbb{R}(\mathfrak{g}_{n,k})=\mathrm{dim}_\mathbb{R}(\mathfrak{u}(n))=n^2.\) (B8)

For \(k\propto n\), this quadratic scaling is exponentially smaller than that of the full ambient space of skew- Hermitian operators u(_W<sub>k</sub>_), which has dimension \(\genfrac(){pt}{2}{n}{k}^2\).

Recall that the complex Grassmannian Gr(_k,n_) is the complex manifold of _k_-dimensional linear subspaces of C_<sup>n</sup>_:

\(\mathrm{Gr}(k,n):=\left\{V\subseteq\mathbb{C}^n|\mathrm{dim}_\mathbb{C}(V)=k\right\}.\) (B9)

The Grassmannian embeds into the projectivization of the _k_-excitation subspace \(\mathbb{P}(W_k)=\mathbb{P}\left(\wedge^k\mathbb{C}^n\right)\) via the classical Plücker embedding \[11, Chapter 3.2\]:<tbc>

\(\iota_\mathcal{P}:\mathrm{Gr}(k,n)\unknown\rightarrow\mathbb{P}(W_k),\iota_\mathcal{P}\left(\mathrm{span}_\mathbb{C}\{v_1,\dots,v_k\}\right)=[v_1\wedge\cdots\wedge v_k].\) (B10)


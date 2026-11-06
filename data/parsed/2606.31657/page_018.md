**Lemma 4.3** (Theorem 4.5 in \[12\])**.** _Let C<sub>n</sub> be an arbitrary code in Lemma 4.1, and let X denote its LRCC. Then for any_ \(f:X(2)\rightarrow\mathbb{F}_2\)_, we have_

\(\mathbf{Pr}_{g\in X(0)}\left[f|_{X_g}\notin C_g\right]\ge\kappa\cdot\delta_\mathrm{H}(f,C_n).\)

However, the local tests on _X<sub>g</sub>_ are systems of linear equations rather than single linear constraints, so we translate them into tests that query a constant number of variables.

**Lemma 4.4.** _There exists a family of LTCs_ \(\{\tilde{C}_n\}\) _with constant rate, detection probability, distance, variable degree, and query complexity_ 3 _whose local tests are linear equations over_ F<sub>2</sub>.

_Proof._ The codes in Lemma 4.1 are equipped with local tests that evaluate systems of linear equations. To prove the lemma we construct a new family of local tests that

1. consists of individual linear equations (rather than systems of linear equations); and<tbc>

2. has query complexity 3.

We address the two goals steps by step.<br>
**Transform local tests to linear equations.** By the construction of the local low-density parity- check (LDPC) codes (see the proof of Lemma 5.1 in \[12\]), each local code _C<sub>g</sub>_ is of the form \(C_0\otimes C_0\) for some LDPC code _C_<sub>0</sub>. Hence \(f|_{X_g}\in C_g\) if and only if every row and every column of _f|<sub>X<sub>g</sub></sub>_ lies in _C_<sub>0</sub>. We view _X<sub>g</sub>_ as an \(n_0\times n_0\) grid whose entries correspond to the local coordinates, so each row/column is a subset of _X_(2). Let \(r_{g,1},\dots,r_{g,n_0}\subseteq X(2)\) be these rows and _r_<sub>_g,n_<sub>0</sub>+1</sub>_,...,r_<sub>_g,_2_n_<sub>0</sub></sub> be the columns. Denote the parity-check matrix of _C_<sub>0</sub> by _H_, with rows _h_<sub>1</sub>_,...,h_<sub>_k_<sub>0</sub></sub>.

Sample \(g\in X(0)\) uniformly, then sample \(i\in[2n_0]\) and \(j\in[k_0]\) uniformly and independently. Query the coordinates of _f_ indexed by the support of _h<sub>j</sub>_ inside the row (or column) _r<sub>g,i</sub>_ and accept iff \(\langle h_j,f|_{r_{g,i}}\rangle=0\). For a fixed _g_, if \(f|_{X_g}\notin C_g\) then some pair (_i,j_) must violate this parity check, so conditioned on such a _g_ the test rejects with probability at least 1/(2_n_<sub>0</sub>_k_<sub>0</sub>). Averaging over the random choice of _g_ gives<tbc>

\(\mathbf{Pr}_{g,i,j}\left[\langle h_j,f|_{r_{g,i}}\rangle\neq 0\right]\ge\frac{1}{2n_0k_0}\mathbf{Pr}_{g\in X(0)}\left[f|_{X_g}\notin C_g\right].\)

<tbc>Combining this with the local testability guarantee from Theorem 4.5 of \[12\] yields

\(\mathbf{Pr}_{g,i,j}\left[\langle h_j,f|_{r_{g,i}}\rangle\neq 0\right]\ge\frac{\kappa}{2n_0k_0}\delta_\mathrm{H}(f,C_n).\)

Each such check touches at most _q_ variables, where _q_ is the query complexity of the base low-density parity-check code _C_<sub>0</sub> (Lemma 5.2 of \[12\]).

For \(g\in X(0)\), \(i\in[2n_0]\), and \(j\in[k_0]\), let \(S_{g,i,j}\subseteq X(2)\) denote the set of coordinates participating in the parity check \(\langle h_j,f|_{r_{g,i}}\rangle=0\). Let S<sub>1</sub> collect all such _S<sub>g,i,j</sub>_. The tests in S<sub>1</sub> therefore define a new LTC \(\tilde{C}_n\) with local constraints

\(\sum_{s\in S_{g,i,j}}x_s=0\text{for every}S_{g,i,j}\in\mathcal{S}_1,\)

which coincide with the local checks of the LDPC code _C_<sub>0</sub>. Because _n_<sub>0</sub> and _k_<sub>0</sub> are absolute constants, the detection probability \(\kappa':=\kappa/(2n_0k_0)\) is again a constant.

The query complexity and variable degree of this test collection are also constant. Indeed, the LDPC code _C_<sub>0</sub> has query complexity _q_ and variable degree 7 (Lemma 5.1 of \[12\]). A variable _x_ belongs to _S<sub>g,i,j</sub>_ precisely when


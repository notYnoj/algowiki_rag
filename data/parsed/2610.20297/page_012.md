**Claim 3.10.** _The above choice of p_<sup>∗</sup> _maintains Equation_ (2).

_Proof._ Fix \(\mathcal{P}_s^{(\ell)}\). For a uniformly chosen prime \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\), Claim 3.3 gives

\(\mathbb{E}\left[\Phi_{s+1}^{(\ell)}(p')\right]=O\left(\frac{B^{(\ell)}\mathrm{log}U}{P}\right)\Phi_s^{(\ell)}.\)

Indeed, each tuple counted by \(\Phi_s^{(\ell)}\) can be extended in at most \(B^{(\ell)}\) ways, and a fixed nonzero difference is divisible by \(p'\) with probability _O_(log_U/P_). Excluding the constant number of already chosen primes changes this bound by only a constant factor.

By Lemma 3.8 and the definition of _p_<sup>∗</sup>,

\(\Phi_{s+1}^{(\ell)}(p^*)\unknown\frac{2Z_{s+1}(p^*)}{|Q|}\unknown\mathrm{min}_{p^\prime} 2\Phi_{s+1}^{(\ell)}(p')\unknown 2\mathbb{E}_{p^\prime}\left[\Phi_{s+1}^{(\ell)}(p')\right].\)

Starting from \(\Phi_0^{(\ell)}=O(N^3/B^{(\ell)})\) and applying this bound at most constant _t_ times proves Equation (2), and hence Equation (1).

This concludes the proof of Lemma 3.7.

**Step 2: Finding and Verifying a Sparse Certificate.** Lemma 3.7 allows us to find a set of good primes. We now describe how to use the set of good primes to compute a small sparse certificate (i.e. find the set of level \(\ell\) candidates). In contrast to the randomized algorithm, we will interleave the steps of finding and verifying the sparse certificate. Concretely, we will use the data structure of \[AV26, Corollary 31\] to test candidate blocks during a depth-first search.

**Theorem 3.11** (Corollary 31 of \[AV26\])**.** _Let c\>_10 _and_ \(0<\theta<0.9\)_, let_ \(\rho_c:=9/(c-1)\)_, and let_<tbc>

\(g:=\frac{\theta\mathrm{ln}(1/\rho_c)}{\mathrm{ln}4}>0\text{\textit{and}}q:=\frac{H(\theta)+\theta\mathrm{ln}9}{\mathrm{ln}4}.\)

<tbc>_Given as input matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\) _whose entries are integers of absolute value at most N_<sup>_O_(1)</sup>_, where_ \(2\unknown D\unknown N^\varepsilon\) _and_ \(\varepsilon<R_c(g)\) _where_

\(R_c(g):=\frac{\mathrm{ln}4}{c\mathrm{ln}10-\frac{c}{2}H(1/c)-(c-1)\mathrm{ln}3+g\mathrm{ln}4},\)

_we can preprocess them deterministically in O(N_<sup>2</sup>log<sup>2</sup>_D/D<sup>g</sup>_) _time and space, after which any single entry_ (_XY_)\[_i,j_\] _in can be computed deterministically in O(D<sup>q</sup>_log_D_) _time. The constants hidden in the O_() _depend on_ \(c,\theta,\varepsilon\)_. Moreover, R<sub>c</sub>_(0) _increases to_ \(\varepsilon^*=\mathrm{ln}4/(5\mathrm{ln}10)=0.1204\dots\) _as c decreases to_ 10.

Theorem 3.11 allows us to trade-off slower queries for faster preprocessing. At level \(\ell\), we let \(g_\ell=\frac{\theta_\ell\mathrm{ln}(1/\rho_c)}{\mathrm{ln}4}\) so that \(\theta_\ell=\frac{g_\ell\mathrm{ln}4}{\mathrm{ln}(1/\rho_c)}\).

**Lemma 3.12.** _Fix a level_ \(\ell\) _and the set_ \(\mathcal{P}^{(\ell)}\) _of t primes. Suppose_ \(0<\theta_\ell:=\frac{g_\ell\mathrm{ln}4}{\mathrm{ln}(1/\rho_c)}<0.9\), \(2B^{(\ell)}P\unknown N^\varepsilon\)_, and_ \(\varepsilon<R_c(g_\ell)\)_. Given_ \(g_\ell\)_, let_ \(q_c(g_\ell):=\frac{H(\theta_\ell)+\theta_\ell\mathrm{ln}9}{\mathrm{ln}4}\) .

_There is a deterministic data structure that returns_ \(C(i,j,K^{(\ell)},p)\) _for any block_ \(K^{(\ell)}\)_, output pair_ (_i,j), and_ \(p\in\mathcal{P}^{(\ell)}\)_, with preprocessing time_ \(\widetilde{O}\left(N^2P^2+\frac{N^3P}{B^{(\ell)}(B^{(\ell)}P)^{g_\ell}}\right)\) _and query time_ \(\widetilde{O}((B^{(\ell)}P)^{q_c(g_\ell)})\).

_Proof of Lemma 3.12._ For each block \(K^{(\ell)}\), prime \(p\in\mathcal{P}^{(\ell)}\), and residue \(r\in\mathbb{Z}_p\), construct the matrices from Lemma 3.4

\(X[i,(k,a)]=\mathbf{1}[A[i,k]\equiv a(\mathrm{mod}p)],Y_r[(k,a),j]=\mathbf{1}[B[k,j]\equiv r-a(\mathrm{mod}p)].\)


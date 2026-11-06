**Claim 3.5.** _If_ \(K^{(\ell)}\) _is a block witness for_ (_i,j), then_ \((i,j,K^{(\ell)})\) _is a level-_\(\ell\) _candidate. If_ \(\ell\ge 1\) _and_ \((i,j,K^{(\ell)})\) _is a level-_\(\ell\) _candidate, then_ \((i,j,K^{(\ell-1)})\) _is a level-_\((\ell-1)\) _candidate for the unique parent_ \(K^{(\ell-1)}\supseteq K^{(\ell)}\).

_Proof of Claim 3.5._ If \(k\in K^{(\ell)}\) satisfies \(\Delta_{ikj}=0\), then it belongs to every ancestor of \(K^{(\ell)}\) and satisfies \(\Delta_{ikj}\equiv 0(modp)\) for every prime _p_. Thus every ancestor passes the tests for its level. The second assertion follows directly from the definition.

For a given triple \((i,j,K^{(\ell)})\) and modulus _d_, let<tbc>

\(F(i,j,K^{(\ell)},d)=\left|\left\{k\in K^{(\ell)}|\Delta_{ikj}\neq 0\wedge\Delta_{ikj}\equiv 0modd\right\}\right|\)

<tbc>denote the number of false witnesses for (_i,j_) in \(K^{(\ell)}\) with respect to _d_. We define the following potential function

\(\Phi^{(\ell)}=\sum_{i,j,K^{(\ell)}}\prod_{p\in\mathcal{P}^{(\ell)}}F(i,j,K^{(\ell)},p).\)

We claim that this potential upper bounds the number of false level \(\ell\) candidates.

**Claim 3.6.** _The total number of false level_ \(\ell\) _candidates is at most_ \(\Phi^{(\ell)}\).

_Proof of Claim 3.6._ Suppose \((i,j,K^{(\ell)})\) is a false level \(\ell\) candidate. Then, for each \(p\in\mathcal{P}^{(\ell)}\), there exists \(k\in K^{(\ell)}\) such that \(\Delta_{ikj}\equiv 0modp\) and \(\Delta_{ikj}\neq 0\). In particular, we have \(F(i,j,K^{(\ell)},p)>0\) for all \(p\in\mathcal{P}^{(\ell)}\), so that \(\prod_PF(i,j,K^{(\ell)},p)>0\).

Thus, it suffices to bound \(\Phi^{(\ell)}\). Towards this goal, our goal at each level \(\ell\) is to choose \(\mathcal{P}^{(\ell)}\) satisfying the following invariant<tbc>

\(\Phi^{(\ell)}=O\left(\frac{N^3}{B^{(\ell)}}\left(\frac{B^{(\ell)}logU}{P}\right)^t\right)=O\left(\frac{N^3B^{t-1}log^tU}{2^{\ell(t-1)}P^t}\right).\) (1)

<tbc>As in Theorem 1.1, we set \(P\gg BlogU\) for some sufficiently large constant so that<tbc>

\(\Phi^{(\ell)}=O\left(\frac{N^32^\ell}{B}2^{-\ell t}\right)=O\left(\frac{N^3}{B2^{\ell(t-1)}}\right).\)

<tbc>**Lemma 3.7.** _Let_ \(\ell\ge 0\) _and let_ \(t\ge 1\) _be a constant. There exists a deterministic algorithm that finds a set_ \(\mathcal{P}^{(\ell)}\) _consisting of t distinct primes in_ \[_P,_2_P_\] _such that_ \(\Phi^{(\ell)}\) _satisfies Equation_ (1)_, in time_

\(\tilde{O}\left(P^{t+1}log^{t+1}(U)\mathsf{T}_\mathsf{MUL}\left(N,N(B^{(\ell)})^{t-1},N\right)\right).\)

_Proof of Lemma 3.7._ Note that \(|\Delta_{ikj}|\le 4U\), so every nonzero \(\Delta_{ikj}\) has at most \(H:=\lceil log(4U)\rceil\) distinct prime factors. Let _Q_ consist of the first 2_tH_ primes. We will ensure a choice of _P_ such that for sufficiently large _N_, these primes are _\<P_. We construct Q deterministically in \(\widetilde{O}(H)\) time.

We will construct \(\mathcal{P}^{(\ell)}\) iteratively, beginning with \(\mathcal{P}_0^{(\ell)}=\emptyset\). Throughout the construction, we choose the next prime from \(\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\), so all chosen primes are distinct. For \(0\le s\le t\), define the potential<tbc>

\(\Phi_s^{(\ell)}:=\sum_{i,j,K^{(\ell)}}\prod_{p\in\mathcal{P}_s^{(\ell)}}F(i,j,K^{(\ell)},p)\)

<tbc>so that \(\Phi^{(\ell)}=\Phi_t^{(\ell)}\). We maintain the following invariant:

\(\Phi_s^{(\ell)}=O\left(\frac{N^3}{B^{(\ell)}}\left(\frac{B^{(\ell)}logU}{P}\right)^s\right)\) (2)


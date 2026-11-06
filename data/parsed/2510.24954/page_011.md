Recall that \(P\subset S\times L_{\ell,0}\), where \(S\subset L_{0,0}\) is in the first layer. We include in _E_<sub>+</sub> shortcut edges \(E_0\cup E_1\cup\cdots\cup E_{k-1}\) of the following types. For each \(s=((0,0),(p_0,\dots,p_{k-1}))\in S\) and each subdirection \(\vec{v}_0\in\mathcal{B}(r,d)\), we add edges of the following form to _E_<sub>0</sub>.<tbc>

\(\left(((0,0),(p_0,\dots,p_{k-1})),(1,(p_0+\ell\vec{v}_0,\dots,p_{k-1})\right)\in S\times S_1\)

<tbc>Likewise, for each index \(i\in[1,k-2]\), we include in \(E_i\subseteq S_i\times S_{i+1}\) all edges of the following form,<tbc>

\(\left((i,(p_0,\dots,p_i,\dots,p_{k-1})),(i+1,(p_0,\dots,p_i+\ell\vec{v}_i,\dots,p_{k-1}))\right)\in S_i\times S_{i+1}\)

<tbc>where \((i,(p_1,\dots,p_k))\in S_i\) and \(\vec{v}_i\in\mathcal{B}(r,d)\) is a critical subdirection. Finally, \(E_{k-1}\subseteq S_{k-1}\times L_{\ell,0}\) contains all edges of the following form.

\(\left((k-1,(p_0,\dots,p_{k-1})),((\ell,0),(p_1,\dots,p_k+\ell\vec{v}_{k-1}))\right)\in S_{k-1}\times L_{\ell,0},\)

where \((k-1,(p_1,\dots,p_k))\in S_{k-1}\) and \(\vec{v}_{k-1}\in\mathcal{B}(r,d)\) is a critical subdirection.

This completes the construction of our Steiner shortcut _G_<sub>+</sub>. We now argue it is a valid Steiner shortcut (i.e., it does not change the transitive closure restricted to \(V\times V\) ) and satisfies the size and distance claims of Theorem 2.2.

### Size of _G_<sub>+</sub>.

For each \(i\in[1,k-1]\), |_S<sub>i</sub>_|=_N_, so \(|V_+|=kN=\Theta(|V|/\ell)\). Each vertex in _V_<sub>+</sub> has indegree and outdegree at most \(|\mathcal{B}(r,d)|=\Delta\). We conclude that \(|E_+|=O(|V_+|\Delta)=O(|V|\Delta/\ell)\). Then \(|E_+|=O(|E|/\ell)=|E|n^{\Omega(1/(kd))}=|E|/n^{\Omega(1/k)}\) as claimed.

### Transitive closure and diameter.

We now verify that the transitive closure of _G_<sub>+</sub> restricted to the original vertices in _G_ is identical to the transitive closure of _G_. By construction, for any \((s,t)\in V\times V\) , any _s-t_ path in _G_<sub>+</sub> that uses Steiner vertices _V_<sub>+</sub> must be contained in \(W=S\times S_1\times S_2\times\cdots\times S_{k-1}\times L_{\ell,0}\). Let \(s\in S\subseteq L_{0,0}\) and \(t\in L_{\ell,0}\) be a pair of nodes such that there exists an _s-t_ path in _W_. By construction of \(E_+=E_0\cup\cdots\cup E_{k-1}\), this implies \(s=((0,0),p),t=((\ell,0),p+\ell\vec{v})\), where \(\vec{v}=(\vec{v}_0,\dots,\vec{v}_{k-1})\) are the critical subdirections corresponding to the edges along the path. In other words, \((s,t)\in P\) was already in the transitive closure of _G_. Conversely, any such \((s,t)\in P\) has a length-_k_ path in _W_. We conclude that _G_<sub>+</sub> is a valid reachability shortcut of _G_ and that dist<sub>_G_<sub>+</sub></sub>(_s,t_)=_k_ for \((s,t)\in P\).

## 3 Necessity of Thick Steiner Shortcuts

This section has two goals. First, we show that if ideal Steiner shortcuts exist with size _m_<sup>1+_o_(1)</sup> and diameter _m_<sup>_o_(1)</sup>, then they must be _thick_ on some graphs in the family G_<sub>k</sub>(c,d_). Second, we prove that a certain _randomized_ graph class \(\widetilde{\mathcal{G}}_k(c,d,p)\) defined shortly is _strictly_ harder to shortcut than G_<sub>k</sub>(c,d_), and argue that it may in fact be sufficient to refute Conjecture 3.

Our first result is that G_<sub>k</sub>_ cannot be shortcut by any _t_-thick Steiner shortcut unless \(t\ge 0.99k\).

**Theorem 3.1.** _For_ \(k\ge 2\), \(t\le 0.99k\)_, and_ \(m=2^{\omega(k\mathrm{log}k)}\)_, every t-thick Steiner shortcut for the m-edge graph_ \(G\in\mathcal{G}_k\) _requires either_ \(m^{\Omega(1/k)}\) _diameter or_ \(m^{1+\Omega(1/k)}\) _edges._

Theorem 3.1 rules out _t_-thick Steiner shortcuts for _t=o_(log_n/_loglog_n_) and will be proved in Section 3.2. Note that Theorem 3.1’s constraint on _t_ is essentially sharp, as Theorem 2.2 shows that _k_-thick Steiner shortcuts can shortcut all the critical vertex pairs with length-_k_ paths.


Proof. We start by computing a first lower bound to the probability that an execution of BasketSort with initial window size _w<sub>S</sub>=w_, input sequence _S=S<sub>w</sub>_, and \(\mathrm{disl}(S)\le w\) returns a sequence having total dislocation _O(m_).

To this aim, we assume that \(w\ge 1\) (otherwise the total dislocation is trivially 0) and we partition the elements of _S_ into \(k=\left\lfloor\frac{75}{1-\rho}\right\rfloorw>\frac{74}{1-\rho}w=2\cdot\frac{37}{1-\rho}w\) sets _P_<sup>(0)</sup>_,...,P_<sup>(_k_-1)</sup>, where \(P^{(j)}=\{x\in S:x\mathrm{mod}k=j\}\). We define \(D^{(j)}=\sum_{x\in P^{(j)}}\mathrm{disl}(x,S_0)\) as the total dislocation of the elements in _P_<sup>(_j_)</sup> in the returned sequence _S_<sub>0</sub>, and we call its expected value \(\mu^{(j)}=\mathbb{E}[D^{(j)}]=\sum_{x\in P^{(j)}}\mathbb{E}[\mathrm{disl}(x,S_0)]\).

Observe that the final position \(\sigma_0(x)\) of a generic element _x_ in _P_<sup>(_j_)</sup> does not depend on the comparison results that involve other elements in _P_<sup>(_j_)</sup>. Indeed, Lemma 5.18 guarantees that \(\sigma_0(x)\) only depends on \(C_w(\sigma_w(x)\), \(\frac{36}{1-\rho}w)\) and, using \(|x-\sigma_w(x)|\le w\), we have that \(\sigma_0(x)\) is a function of _C<sub>w</sub>(x_, \(\frac{37}{1-\rho}w\)). Therefore, since \(k>2\cdot\frac{37}{1-\rho}w\), the set of the elements considered in _C<sub>w</sub>(x_, \(\frac{37}{1-\rho}w\)) is disjoint from the set of elements considered in _C(y_, \(\frac{37}{1-\rho}w\)) for any \(y\in P^{(j)}\backslash\{x\}\).

We now use Hoeffding’s inequality to prove that \(D^{(j)}\le\mu^{(j)}+\frac{m}{k}\) with high probability. Lemma 5.5 ensures that \(\mathrm{disl}(x,S_0)\le\mathrm{disl}(x,S_w)+|\sigma_w(x)-\sigma_0(x)|\le w+\frac{8}{1-\rho}w<\frac{9}{1-\rho}w\) for all elements _x_, hence we have:<sup>8</sup>

\(\mathrm{Pr}\left(D^{(j)}-\mu^{(j)}\ge\frac{m}{k}\right)\le\mathrm{exp}\left(-\frac{\frac{2m^2}{k^2}}{|P^{(j)}|\cdot(\frac{9}{1-\rho}w)^2}\right)\le\mathrm{exp}\left(-\frac{\frac{2m^2}{k^2}}{2\frac{m}{k}\cdot(\frac{9}{1-\rho}w)^2}\right)\)<br>
\(=\mathrm{exp}\left(-\frac{m(1-\rho)^2}{81kw^2}\right)\le\mathrm{exp}\left(-\frac{m(1-\rho)^3}{6075w^3}\right).\)

Using the union bound, we have that all _j=_0_,...,k_-1 satisfy \(D^{(j)}\le\mu^{(j)}+\frac{m}{k}\) with probability at least \(1-\frac{75}{1-\rho}w\cdot\mathrm{exp}\left(-\frac{m(1-\rho)^3}{6075w^3}\right)\). Whenever this happens, the total dislocation of _S_<sub>0</sub> is \(\sum_{j=0}^{k-1}D^{(j)}<\sum_{j=0}^{k-1}\mu^{(j)}+k\cdot\frac{m}{k}\le(\gamma+1)\cdot m\) with \(\gamma=\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}+\frac{311040}{(1-\rho)^4}\), where we invoked Lemma 5.17.

Notice that such a lower bound already proves the desired claim whenever \(w=o\left(\sqrt{\frac{m}{\mathrm{ln}m}}\right)\). The rest of the proof is devoted to handling arbitrary initial window sizes _w<sub>S</sub>_.

Consider an execution of BasketSort in which _w<sub>S</sub>_ is at least the dislocation of the input sequence _S_ and let \(w'\) be the smallest window size that satisfies \(w'\ge\frac{6}{\kappa(p,q,\rho)}\mathrm{ln}m\) or, if no such window size exists (i.e., if \(w_S<\frac{6}{\kappa(p,q,\rho)}\mathrm{ln}m\)), let \(w'=w_S\). Notice that, since \(\lfloor\rho w'\rfloor<\frac{6}{\kappa(p,q,\rho)}\mathrm{ln}m\), we have \(w'<\frac{6}{\rho\kappa(p,q,\rho)}\mathrm{ln}m+\frac{1}{\rho}<\frac{6}{\rho\kappa(p,q,\rho)}\mathrm{ln}m+\frac{1}{\rho\kappa(p,q,\rho)}\mathrm{ln}m\le\frac{14}{\kappa(p,q,\rho)}\mathrm{ln}m\), where the second inequality follows from \(\kappa(p,q,\rho)\le\frac{1}{3}\le\mathrm{ln}m\) for \(m\ge 2\) and the third inequality follows from \(\rho\ge\frac{1}{2}\).

Denote by S the set of all sequences having dislocation at most \(w'\) that are attainable from the input sequence _S_ with some choice of the observed comparisons, and let \(\mathrm{BS}(S')\) be an indicator random variable for the event "the sequence returned by BasketSort with input sequence \(S'\) and initial window size \(w'\) has a total dislocation of at most \((\gamma+1)\mathrm{ln}m\)". From the discussion in the first part of this proof, all \(S'\in\mathcal{S}\) satisfy:

\(\mathrm{Pr}(\mathrm{BS}(S')=1)\ge 1-\frac{75}{1-\rho}w'\cdot\mathrm{exp}\left(-\frac{m(1-\rho)^3}{6075(w')^3}\right)\)<br>
\(\ge 1-\frac{1050\mathrm{ln}m}{(1-\rho)\kappa(p,q,\rho)}\cdot\mathrm{exp}\left(-\frac{m(1-\rho)^3\kappa(p,q,\rho)}{16669800\mathrm{ln}^3m}\right).\)

<sup>8</sup>We only consider the case |_P_<sup>(_j_)</sup>|_\>_0, since otherwise \(D^{(j)}=\mu^{(j)}=0\) and \(D^{(j)}\le\mu^{(j)}+\frac{m}{k}\) is trivially true.


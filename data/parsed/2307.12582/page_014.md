## 6.2.2 The algorithmic part

Note that the input consists of _n_ pairs (_w<sub>i</sub>,u<sub>i</sub>_), meaning that item _i_ has a weight _w<sub>i</sub>_ and has _u<sub>i</sub>_ copies. Despite that **g** is defined on the transformed 0-1 instance, as we can get and sort _W_ in _O(n_log_n_), constructing it can be done efficiently.

Lemma 6.5. **g** _can be computed in_ \(\widetilde{O}(n)\) _time._

Lemma 6.6. _Assuming_ **g**_, with_ 1-_o_(1) _probability we can determine whether there exists_ \(\mathbf{z}\in\mathbb{Z}^n\), \(0\unknown z_i\unknown u_i\) _such that_ \(\sum_{i\in\mathcal{I}}w_iz_i=t\) _in_ \(\widetilde{O}(w_\mathrm{max}^{3/2})\) _time._

_Proof._ From **g** we define two sets as follows: \(G^-=\{(w_i,u_i^-):u_i^-=g_i\}\), \(G^+=\{(w_i,u_i^+):u_i^+=u_i-g_i\}\). Intuitively, when changing **g** to **z**, _G_<sup>-</sup> and _G_<sup>+</sup> represent copies that may need to be deleted and added, respectively. By Lemma 6.4, the total weight of item copies to be deleted in _G_<sup>-</sup> is at most \(\widetilde{O}(w_\mathrm{max}^{3/2})\), and the total weight of copies to be added from _G_<sup>+</sup> is also at most \(\widetilde{O}(w_\mathrm{max}^{3/2})\).

Let \(t'=(4c_A+2c_B)w_\mathrm{max}^{3/2}\mathrm{log}w_\mathrm{max}\) and \(t_0=\sum_{i\in\mathcal{I}}w_ig_i\). Define \(\mathcal{S}(G^+,t')=\{y\unknown t':y=\sum_{i=1}^nw_ix_i,0\unknown x_i\unknown u_i^+\}\) and \(\mathcal{S}(G^-,t')=\{y\unknown t':y=\sum_{i=1}^nw_ix_i,0\unknown x_i\unknown u_i^-\}\).

We first compute \(\mathcal{S}(G^+,t')\) and \(\mathcal{S}(G^-,t')\) using Bringmann’s algorithm \[6\]. Note that it is a randomized algorithm. We will compute \(S^+\subseteq\mathcal{S}(G^+,t')\) and \(S^-\subseteq\mathcal{S}(G^-,t')\) in \(\widetilde{O}(t')=\widetilde{O}(w_\mathrm{max}^{3/2})\) time such that every number in \(\mathcal{S}(G^-,t')\) and \(\mathcal{S}(G^+,t')\) is contained in _S_<sup>-</sup> and _S_<sup>+</sup> with probability \(1-(n+t')^{-\Omega(1)}\), respectively. Therefore, with probability 1-_o_(1) we get \(\mathcal{S}(G^-,t')\) and \(\mathcal{S}(G^+,t')\). Next, we compute \(\mathcal{S}(G^+,t')-\mathcal{S}(G^-,t')\) via FFT in \(\widetilde{O}(t')=\widetilde{O}(w_\mathrm{max}^{3/2})\) time. Finally, we test whether \(t\in t_0+\mathcal{S}(G^+,t')-\mathcal{S}(G^-,t')\), which takes \(\widetilde{O}(t')=\widetilde{O}(w_\mathrm{max}^{3/2})\) time. Thus, Lemma 6.6 is proved. \(\square\)

**Remark**

We note that very recently, Bringmann \[7\] and Jin \[19\] independently improved the running time to \(\widetilde{O}(n+w_\mathrm{max}^2)\) by generalizing our technique.


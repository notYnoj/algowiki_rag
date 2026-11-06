Clearly each exact triangle in the structured part appears in some instance \((A_\ell,B_\ell,C_\ell)\). To proceed, we distinguish two cases:

2.1. _(Sparse Case:_ \(|X_\ell|\le D/L^2\) _or_ \(|Y_\ell|\le D/L^2\)_)_ In this case one of the matrices \(A_\ell\) or \(B_\ell\) is sparse. Indeed, suppose that \(|X_\ell|\le D/L^2\). Then \(A_\ell\) contains at most _n_<sub>1</sub>_n_<sub>2</sub>_/L_<sup>2</sup> non-\(\perp\) entries, as it contains at most \(|X_\ell|\) distinct entries each of which appears in at most a 1_/D_-fraction of the entries (by the regularity assumption). We thus solve the instance \((A_\ell,B_\ell,C_\ell)\) by brute-force and place all exact triangles in T .<tbc>

2.2. _(Dense Case:_ \(|X_\ell|\ge D/L^2\) _and_ \(|Y_\ell|\ge D/L^2\)_)_ Let \(Z_\ell=X_\ell\cup Y_\ell\cup(X_\ell+Y_\ell)\) and observe that all entries in the three matrices \(A_\ell,B_\ell,C_\ell\) stem from the set \(Z_\ell\). In the remainder we bound the doubling of \(Z_\ell\). The doubling of \(X_\ell\) can be bounded by one application of Ruzsa’s triangle inequality (Lemma 2.17):<tbc>

<tbc>\(|X_\ell+X_\ell|\le\frac{|X_\ell+Y_\ell||X_\ell+Y_\ell|}{|Y_\ell|}\le\frac{O(L^{10}D^2)}{D/L^2}=O(L^{12}D)=O(L^{14})|X_\ell|,\)<tbc>

<tbc>It follows that \(X_\ell\cup\{0\}\) has doubling _O(L_<sup>14</sup>). Symmetrically, \(Y_\ell\cup\{0\}\) has doubling _O(L_<sup>14</sup>). But \(Z_\ell=(X_\ell\cup\{0\})+(Y_\ell\cup\{0\})\), and thus \(Z_\ell\) has doubling at most _O(L_<sup>14</sup>)<sup>8</sup>=_O(L_<sup>112</sup>) by Lemma 4.12. (Again, we have not attempted to optimize this constant.) We pick \(L=\Theta(K^{1/112})\) so that \(Z_\ell\) has doubling at most _K_. The Exact Triangle instance \((A_\ell,B_\ell,C_\ell)\) is therefore a _K_-doubling (and _D_-uniform and 1_/D_-regular) instance as desired, so we place it in I.<tbc>

<tbc>_Running Time:_ \(O(L\cdot(n_1n_2+n_2n_3+n_1n_3))\) in total.

It is clear that this is a potential-adjusting reduction with \(|\mathcal{I}|\le L\le O(K)\) (crudely bounded). It remains to analyze the running time. The initial BSG Covering takes time \(\tilde{O}(D^\omega L)=\tilde{O}(D^3L)=\tilde{O}(n_1n_2DL)\) (crudely bounding \(\omega\le 3\) and \(D\le n_1,n_2\)), so summing over the running time of steps 1 and 2 as analyzed before the total running time is

\(\tilde{O}\big(\frac{n_1n_2n_3}{L}+(n_1n_2+n_2n_3+n_1n_3)DL\big)=\tilde{O}\big(\frac{n_1n_2n_3}{K^{1/112}}+(n_1n_2+n_2n_3+n_1n_3)DK^{1/112}\big),\)

as claimed.

## 4.5 Putting the Pieces Together

We finally put Lemmas 4.10 and 4.13 together to complete the proof of Lemma 4.2.

**Lemma 4.2** (Reduction from Low-Rank to Uniform Low-Doubling Exact Triangle)**.** _For any parameter_ \(K\ge 1\) _there is a potential-adjusting reduction from any r_-rank _Exact Triangle instance to K(n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)<sup>_o_(1)</sup> _instances that are each D_-uniform, 1_/D_-regular _and K_-doubling _for some_ \(D\le r\)_. The reduction runs in deterministic time_ (_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>_/K_<sup>1/98000</sup>+(_n_<sub>1</sub>_n_<sub>2</sub>+_n_<sub>1</sub>_n_<sub>3</sub>+_n_<sub>2</sub>_n_<sub>3</sub>)_rK_)<sup>1+_o_(1)</sup>_. In particular:_

\(\mathrm{ExactTri}(n_1,n_2,n_3|r)\)<br>
\(\le\big(K\cdot\mathrm{ExactTri}(n_1,n_2,n_3|D\le r;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/98000}}+(n_1n_2+n_2n_3+n_1n_3)rK\big)^{1+o(1)}.\)

**Proof.** First run Lemma 4.10 on the given low-rank Exact Triangle instance with parameter _t=K_<sup>1/98000</sup>. Then transform each of the _t_<sup>875</sup>(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)<sup>_o_(1)</sup> resulting uniform regular Exact Triangle instances by running<tbc>

Running Time: O(n1n2n3/L2) per iteration, so time O(n1n2n3/L) in total.

Running Time: O(L (n1n2+n2n3+n1n3)) in total.


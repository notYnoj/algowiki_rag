_Proof._ First, observe that any common subsequence of _x_ and _y_ has a monotone set \(P\subseteq[n]\times[n]\) where _x<sub>i</sub>=y<sub>j</sub>_ for all \((i,j)\in P\). Now, since \(j\in y^{-1}(x_i)\), then the second coordinates of _P_ are also an increasing subsequence of _z_.

Similarly, consider the coordinates of an increasing subsequence \(W\subseteq[n]\times[k]\). Then \(\{(w_1,z_w)\}_{w\in W}\) is a monotone set where _x_<sub>_w_<sub>1</sub></sub>=_y<sub>z<sub>w</sub></sub>_, and hence _x_ and _y_ has a common subsequence of the same length.

Our entire algorithm is merely an efficient implementation of the above reduction, and solving it using Theorem 4. In particular, we show the following:

**Lemma 6.** _Suppose there exists an algorithm_ A_<sub>BL</sub> which_ \(\left(f\left(\frac{|z|}{\lambda n}\right),\lambda n\right)\) _approximates Block-LIS in time_ \(t\left(\frac{|z|}{\lambda n},n\right)\)_. Then, there exists an algorithm_ A<sub>LCS</sub> _approximating_ LCS_<sub>n</sub> up to a factor_ \((1+o(1))\cdot f(n\cdot\mathrm{log}n)\) _in_ \(t\left(O(n\cdot\mathrm{log}(n)),n\right)+O(n)\) _time._

_Proof of Theorem 1 using Theorem 4 and lemma 6._ The proof follow almost immediately from Theorem 4 and lemma 6. However, a direct invocation of the statements only yields _n_<sup>1+_o_(1)</sup> time algorithm. To obtain linear time, we first subsample \(U\subseteq[n]\) i.i.d. at rate _n_<sup>-_o_(1)</sup>, and then apply the statements on _x<sub>U</sub>_ and _y<sub>U</sub>_, noting \(\mathrm{LCS}(x_U,y_U)\in[n^{-o(1)},1]\cdot\mathrm{LCS}(x,y)\). The resulting runtime is |_U_|<sup>1+_o_(1)</sup>=_O(n_) as needed.

## 2.3 Useful lower bound for the LCS using Hölder’s inequality

**Hölder’s inequality.** A classical norm inequality which says that \(\langle x,y\rangle\le\left\|x\right\|_{1/p}\cdot\left\|y\right\|_{1/q}\) for any _p+q_=1. In particular, \(\langle x,y\rangle\le\left\|x\right\|_\infty\cdot\left\|y\right\|_1\). Such inequality can be extended to show the following bound:

**Claim 7.** _Fix_ \(x,y\in\mathbb{R}^n\)_. Then,_ \(\langle x,y\rangle\le\left\|\mathrm{min}\{x,y\}\right\|_\infty\cdot(\left\|x\right\|_1+\left\|y\right\|_1)\).

_Proof._ Let _a_=min{_x,y_} and _b_=max{_x,y_}. Then, by Hölder’s inequality,

\(\langle x,y\rangle=\langle a,b\rangle\le\left\|a\right\|_\infty\cdot\left\|b\right\|_1=\left\|\mathrm{min}\{x,y\}\right\|_\infty\cdot\left\|\mathrm{max}\{x,y\}\right\|_1\le\left\|\mathrm{min}\{x,y\}\right\|_\infty\cdot(\left\|x\right\|_1+\left\|y\right\|_1).\)

**Simple lower bound for the LCS.** We next state a useful fact about the minimal LCS of two strings:

**Fact 8.** \(\mathrm{LCS}(x,y)\ge\left\|\mathrm{min}\{\psi(x),\psi(y)\}\right\|_\infty\).

_Proof._ That fact is immediate, since if each of _x_ and _y_ contain _k_ copies of the same letter _c_, then _c<sup>k</sup>_ is a common subsequence to both _x_ and _y_.

We combine the above to show the following lower bound on the LCS:

**Lemma 9.** \(\mathrm{LCS}(x,y)\ge\frac{|z|}{2n}\) .

_Proof._ Observe that by construction \(|z|=\langle\psi(x),\psi(y)\rangle\). Now, invoking Claim 7 and fact 8, we obtain:

\(|z|\le\left\|\mathrm{min}\{\psi(x),\psi(y)\}\right\|_\infty\cdot(\left\|\psi(x)\right\|_1+\left\|\psi(y)\right\|_1)\le 2n\cdot\mathrm{LCS}(x,y),\)

which implies the Lemma.

One direct implication of the above is a simple deterministic and exact algorithm for LCS in time \(O(n\ell\mathrm{log}(\ell))\), where \(\ell=\mathrm{LCS}(x,y)\). While we do not derive it in this paper, one can observe this can be done by simply reducing the LCS problem to Block-LIS, and solving it directly as a standard LIS problem, which takes _O_(|_z_|log(LIS(_z_))) time.


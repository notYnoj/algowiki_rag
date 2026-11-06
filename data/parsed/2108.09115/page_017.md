Now, going over all disjoint \((a_{2i-1},a_{2i})\in T\), we get for \(\epsilon\le\frac{1}{2}\)

\(\mathrm{ED}(\mu')\le(1+\frac{\epsilon}{(1-\epsilon)})\mathrm{ED}(\mu)\le(1+2\epsilon)\mathrm{ED}(\mu).\)

This completes the proof.

Low-skew mapping will play an impartial role in our algorithm design and analysis.

## 5.3 Reduction to estimating window costs.

Let \(\mathcal{E}:\mathcal{A}\times\mathcal{B}\rightarrow\{0,\dots,d\}\) be an estimate of the edit distance such that \(\mathcal{E}(a,b)\ge\mathrm{ED}(a,b)\) for all \(a\in\mathcal{A},b\in\mathcal{B}\). Given a monotone mapping \(\mu:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\), we define its cost with respect to E as follows:

\(\mathrm{ED}_\mathcal{E}(\mu)=\sum_{a\in\mathcal{A}}\mathcal{E}(a,\mu(a))+\sum_{i=1}^n\left|\#\{a\text{s.t.}i\in\mu(a)\}-1\right|\)

We define ED(E) as the minimal cost \(\mathrm{ED}_\mathcal{E}(\mu)\) over all monotone mappings.

Now, given such an estimation the next lemma (combining ideas from \[Ukk85\] and \[BEG<sup>+</sup>18\]) asserts that one can efficiently compute ED(E).

Instead of computing ED(E) directly, we pick a threshold \(\Delta\), and verify whether \(\mathrm{ED}(\mathcal{E})\le\Delta\). Indeed, if we can answer whether \(\mathrm{ED}(\mathcal{E})\le\Delta\), or \(\mathrm{ED}(\mathcal{E})>(7+o(1))\Delta\) efficiently, then by increasing the threshold by an \((1+\epsilon)\) factor each time, we will be able to compute ED(E) within a (7+_o_(1)) approximation in \(\mathrm{log}_{1+\epsilon} n\) iterations.

**Lemma 12** (Reduction to estimating window costs)**.** _Given an estimate_ E_, one can compute_ ED(E) _in_ \(O(\frac{1}{\epsilon}\frac{n^2}{d^2}\mathrm{log}n)\)_-time._

_Proof._ Pick a threshold \(\Delta\). Set \(\gamma=\frac{\Delta d}{n}\). If \(\gamma_\tau\le\gamma\), then from \(\mathcal{B}^\tau\) pick every \(\lfloor\frac{\gamma}{\gamma_\tau}\rfloor\) windows so that gap between two consecutive windows in \(\mathcal{B}^\tau\) is \(\ge\gamma-1\) for all \(\tau\). Therefore, the total number of windows that we consider in _B_ is \(O(\frac{n}{\gamma})\).

For window _w_, we let _e(w_) denote the index of the last character of _w_; for a set W, _e_(W) denotes the set of last indices. For \(i\in e(\mathcal{W})\), we let \(i.\text{prev}:=\mathrm{max}\{i'\in e(\mathcal{W})\cup\{0\}\wedge i'<i\}\) denote the index of the previous finish in W (or 0 if such an index does not exist).

We abuse notation and let ED(_i,j_) denote the minimum cost of alignment ending at _i,j_ using estimates E. Following \[Ukk85\] we use dynamic programming to fill a table of ED(_i,j_) for every pair \(i,j\in e(\mathcal{A})\times e(\mathcal{B})\) such that \(|i-j|\le 10\Delta\). Notice that the number of such pairs is bounded by:

\(|\mathcal{A}||\mathcal{B}|\frac{10\Delta}{n}=O\left(\frac{n}{d}\cdot\frac{n}{\gamma}\cdot\frac{\Delta}{n}\right)=O\left(\frac{n^2}{d^2}\right).\) (1)

For boundary conditions, we define \(\mathrm{ED}(i,j)=\infty\) whenever \(|i-j|>10\Delta\), and \(\mathrm{ED}(i,0)=\mathrm{ED}(0,i)=i\).

Consider a pair _i,j_ such that _e(a_)=_i_ (notice that there may be \(O_\epsilon(1)B\)-windows ending at _j_). The cost ED(_i,j_) of alignment ending at _i,j_ is given by taking the minimum of:

• Cost of deleting the last _A_-window: _i-i._prev+ED(_i._prev_,j_);<tbc>

• Cost of deleting the last several _B_-characters: _j-j._prev+ED(_i._prev_,j_); and<tbc>


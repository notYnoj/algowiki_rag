**Lemma 5.8** (Restated)**.**<br>
_Let p be the shortest_ \(\langle 0,n_X\rangle\cdot\langle n_X+n_Y,n_Y\rangle\) _path in the Rotated Edit Distance Grid Graph. There exists a path_ \(\widehat{p}\) _with_ \(w(\widehat{p})\le w(p)+n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) _in the Sparsified Edit Distance Grid Graph._

_Similarly, let p be the longest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path in the Rotated LCS Grid Graph. There exists a path_ \(\widehat{p}\) _with_ \(w(\widehat{p})\ge w(p)-n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) _in the Sparsified LCS Grid Graph._

_Proof._ From Lemma 5.9, if we round _p_ on _X_ columns so that the rows that _p_ visit on these columns become multiples of _Y_ , we incur a total additive error of at most \(X\cdot Y\) .

We will perform rounding in _S_ phases, where for each _s_=0,1,2_,...,S_ in order, we generate a new path _p<sub>s</sub>_ that satisfies the rounding condition for columns divisible by _I<sub>s</sub>_. We start by setting _p_<sub>-1</sub>:=_p_.

To go from _p_<sub>_s_-1</sub> to _p<sub>s</sub>_, for every column _x_ that is a multiple of _I<sub>s</sub>_, we round _p(x_) to a multiple of \(I_s/\phi_y\). This incurs an error of at most \((n/I_s)\cdot(I_s/\phi_y)=n/\phi_y\).

Thus after _S_ rounds, we incur an error of \(S\cdot n/\phi_y=n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\).

From now on, unless specified otherwise, vertices, edges and paths refer to those in the Sparsified Grid Graphs. For LCS, our algorithm solves a query-based problem on the Sparsified LCS Grid Graph:

**Lemma 5.10** (Query-Based Approximation for LCS)**.** _Suppose that to know the exact edge weight of any edge from any_ \(\langle x,y\rangle\) _to any_ \(\langle x+\mathcal{B}_x,y'\rangle\) _requires an edge-weight query. We can approximate the problem in Definition 5.7 in o(n_<sup>0.1</sup>) _time with high probability_<sup>19</sup> _using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1-_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>.

We argue that this is sufficient for approximating LCS:

**Lemma 5.11** (Reducing Approximation of LCS to Lemma 5.10)**.** _Suppose that we can approximate the problem in Definition 5.7 in o(n_<sup>0.1</sup>) _time with high probability using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1-_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>_. For any constant_ \(\varepsilon>0\)_, there is a randomized algorithm that runs in time n_<sup>2</sup>/2<sup>\(\Omega\left(\mathrm{log}^{0.009}(n)\right)\)</sup> _and, with high probability,_ \((1-\varepsilon)\)_-approximates LCS for two strings with lengths that sum to n._

_Proof._ Firstly, if the LCS is \(n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\), we can use Lemma 3.4 to compute the answer exactly in \(n^2/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) time. Thus we assume the answer is at least _n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>. Due to Lemma 5.8, (1-_o_(1))- approximating the problem on the sparsified graph suffices for (1-_o_(1))-approximating LCS.

We run the algorithm in Lemma 5.10. To answer an edge weight query, since the Rotated LCS Grid Graph is acyclic and every vertex \(\langle x',y'\rangle\) reachable from \(\langle x,y\rangle\) satisfies \(\mathrm{max}(x'-x,y'-y)\le\mathcal{B}_x\), the longest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path can be found in _O_(B_<sub>x</sub>_<sup>2</sup>) time using standard techniques on acyclic graphs<sup>20</sup>. Since the algorithm only uses \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) edge weight queries. The total running time for this part is

\(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\cdot O(\mathcal{B}_x^2)=n^2\phi_y^2/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\)<br>
\(=n^2/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}.\)

<sup>19</sup>i.e., a probability of 1-1_/n<sup>c</sup>_ for some constant _c\>_0. <sup>20</sup>The shortest/longest path on an acyclic graph can be found in linear time by combining topological sorting with dynamic programming. The optimal path to each vertex only depends its predecessors in the topological order. Thus we compute the optimal path to each vertex using dynamic programming in that order.


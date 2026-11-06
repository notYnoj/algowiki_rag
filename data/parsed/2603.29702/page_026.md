For Edit Distance, our algorithm solves a query-based problem on the Sparsified Edit Distance Grid Graph, assuming that we have a constant-factor approximation of every edge weight:

**Lemma 5.12** (Query-Based Approximation for ED)**.** _Suppose that for every edge from_ \(\langle x,y\rangle\) _to_ \(\langle x+\mathcal{B}_x,y'\rangle\)_, we are given ("for free") a constant-factor approximation_ \(\mathrm{approw}[x,y,x+\mathcal{B}_x,y']\) _of the edge weight_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) _(i.e.,_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\le\mathrm{apprew}[x,y,x+\mathcal{B}_x,y']\le 4\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\)_). To know the exact edge weight requires an edge-weight query. Then we can approximate the problem in Definition 5.6 in o(n_<sup>0.1</sup>) _time with high probability using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1+_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>.

We argue that this is sufficient for approximating Edit Distance:

**Lemma 5.13** (Reducing Approximation of Edit Distance to Lemma 5.12)**.** _Assume that given a constant- factor approximation of pairwise distances, with high probability, by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge weights, we can approximate the problem in Definition 5.6 in o(n_<sup>0.1</sup>) _time up to a multiplicative factor of_ (1+_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>_. For any constant_ \(\varepsilon>0\)_, there is a randomized algorithm that runs in time n_<sup>2</sup>/2<sup>\(^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) _and, with high probability,_ \((1+\varepsilon)\)_-approximates Edit Distance for two strings with lengths that sum to n._

_Proof._ Firstly, if the Edit Distance is \(n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\), we can use Ukkonen’s algorithm (Lemma 3.3) to compute the answer exactly in \(n^2/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) time. Thus we assume the answer is at least _n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>. Due to Lemma 5.8, (1+_o_(1))-approximating the problem on the sparsified graph suffices for (1+_o_(1))- approximating ED.

Notice that the weight of an edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\) is equal to the Edit Distance between a sub-string of either input string. Using Lemma 3.2, we can obtain a constant-factor approximation of each edge weight of the Sparsified Edit Distance Grid Graph in _O(n_<sup>1.61</sup>) time. Since the number of vertices is \(O(n^2\phi_y/\mathcal{B}_x^2)=o(n^{0.03})\), the number of edges is no more than _o(n_<sup>0.06</sup>). Thus the total running time is \(o(n^{1.61}\cdot n^{0.06})=o(n^{1.67})\).

Now we have the ingredients for the algorithm in Lemma 5.12. To answer an edge weight query, since the Rotated Edit Distance Grid Graph is acyclic and every vertex \(\langle x',y'\rangle\) reachable from \(\langle x,y\rangle\) satisfies \(\mathrm{max}(x'-x,y'-y)\le\mathcal{B}_x\), the shortest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path can be found in _O_(B_<sub>x</sub>_<sup>2</sup>) time using standard techniques on acyclic graphs. Since the algorithm only uses \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) edge weight queries, the total running time for this part is

\(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\cdot O(\mathcal{B}_x^2)=n^2\phi_y^2/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\)<br>
\(=n^2/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}.\)

## 6 Algorithm for Edit Distance

In this section, we present our algorithm for Edit Distance:


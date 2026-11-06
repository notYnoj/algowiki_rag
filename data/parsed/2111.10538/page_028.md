**Definition 3.16** (close)**.** Let \(\gamma\in(0,1)\) and \(\lambda\in(0,1)\). We say a pair (_w<sub>i</sub>,w<sub>j</sub>_) of windows is _close_, if there are at least \(k^{1-\gamma}\) windows _w<sub>a</sub>_ such that \(||\mathsf{lc}\mathsf{s}_{w_a}(w_i,w_j)||\ge\lambda^2/2\).

Our first observation is that Algorithm 2 detects all the close pairs with high probability.

**Lemma 3.17.** _Let_ \(\widehat{\mathsf{O}}_{\lambda^3}\in\{0,1\}^{k\times k}\) _be the output of Algorithm 2. For each_ \((i,j)\in[k]\times[k]\)_, if_ (_w<sub>i</sub>,w<sub>j</sub>_) _is close (Definition 3.16), then_ \(\widehat{\mathsf{O}}_{\lambda^3}[i][j]=1\) _holds with probability at least_ 1-1_/k_<sup>3</sup>.

_Proof._ We consider a fixed (_i,j_) such that (_w<sub>i</sub>,w<sub>j</sub>_) is close. By Definition 3.16, there are at least \(k^{1-\gamma}\) windows _w<sub>a</sub>_ such that \(||\mathsf{lc}\mathsf{s}_{w_a}(w_i,w_j)||\ge\lambda^2/2\). If such a _w<sub>a</sub>_ window is sampled in our algorithm, then we detect the edge between the close pair. The probability that none of these windows is sampled is at most

\(\left(1-\frac{k^{1-\gamma}}{k}\right)^{10k^\gamma logk}=\left(1-\frac{1}{k^\gamma}\right)^{10k^\gamma logk}\le\frac{1}{k^5}.\)

Taking a union over at most _k_<sup>2</sup> pairs completes the proof.

Before we proceed to Lemma 3.19, we bring Lemma 3.18 as an auxiliary observation.

**Lemma 3.18** (existence of a correlated pair)**.** _Let_ \(\lambda\in(0,1)\)_. Given a window w<sub>a</sub> and a set T containing at least_ \(2/\lambda\) _windows. If for each_ \(w_i\in T\) _we have_ \(||\mathsf{lc}\mathsf{s}(w_a,w_i)||\ge\lambda\)_, then there exist two windows_ \(w_i,w_j\in T\) _such that both_ \(||\mathsf{lc}\mathsf{s}_{w_a}(w_i,w_j)||\ge\lambda^2/2\) _and_ \(||\mathsf{lc}\mathsf{s}_{w_a}(w_j,w_i)||\ge\lambda^2/2\) _hold._

_Proof._ Let _d_ be the size of the windows. We consider a character-based bipartite graph: On one side, it has _d_ nodes, and on the other side it has _d|T_| nodes. Two nodes _x,y_ in the character-based graph are adjacent iff \((x,y)\in\mathsf{opt}_{a,i}\) where _w<sub>a</sub>_ is the window containing character _x_ and _w<sub>i</sub>_ is the window containing character _y_. Since \(||\mathsf{lc}\mathsf{s}(w_a,w_i)||\ge\lambda\) for every \(w_i\in T\), the total number of edges in character-based bipartite graph is at least \(\lambda|T|d\).

For \(\ell\)-th character in window _w<sub>a</sub>_, we use \(D_\ell\) to denote the degree of the corresponding node in the character-based bipartite graph. The number of 2-walks between pairs of nodes on the side with _d|T_| nodes is at least

\(\sum_{\ell=1}^dD_\ell(D_\ell-1)=\left(\sum_{\ell=1}^dD_\ell^2-\sum_{\ell=1}^dD_\ell\right)\)<br>
\(\ge\left(\frac{1}{d}(\sum_{\ell=1}^dD_\ell)^2-\sum_{\ell=1}^dD_\ell\right)\text{by Cauchy-Schwarz inequality}\)<br>
\(\ge\left(\frac{1}{d}(\lambda|T|d)^2-(\lambda|T|d)\right)\text{by Eq. (8) explained below}\)<br>
\(=\left(\lambda^2d|T|^2-\lambda|T|d\right)\)<br>
\(\ge 1/2\lambda^2d|T|^2\text{by}|T|\ge 2/\lambda\)

The number of 3-tuples (_w<sub>i</sub>,w<sub>a</sub>,w<sub>j</sub>_) is at most |_T_|<sup>2</sup>. Thus, there must exist a pair (_w<sub>i</sub>,w<sub>j</sub>_) such that<tbc>

\(||\mathsf{lc}\mathsf{s}_{w_a}(w_i,w_j)||\ge\lambda^2/2.\)

<tbc>This also means that<tbc>

\(||\mathsf{lc}\mathsf{s}_{w_a}(w_j,w_i)||\ge\lambda^2/2\)


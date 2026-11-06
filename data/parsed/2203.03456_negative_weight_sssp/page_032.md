<tbc>then by Markov’s inequality each version of SPmain terminates with probability at least 1/2, so the probability that none of the versions terminate is at most 1/2<sup>_C_log(_n_)</sup>=1_/n<sup>C</sup>_, as desired.

The rest of this section presents a Las Vegas algorithm SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) that can return a negative cycle when one exists, and whose running time is _O(m_log<sup>8</sup>(_n_)) w.h.p when _G<sub>in</sub>_ satisfies the properties of Assumption 2.1. For this, we require the following definition

**Definition C.2.** Given any graph _G_=(_V,E,w_) and any positive integer _B_, let _G_<sup>+_B_</sup>=(_V,E,w_<sup>+_B_</sup>) be the same as the graph _G_, except that for all \(e\in E\) we have _w_<sup>+_B_</sup>(_e_):=_w(e_)+_B_. (Note that unlike in _G<sup>B</sup>_ of Definition 2.3, here we add _B_ to _all_ edges, including the positive ones.)

**FindThresh**. The key subroutine of SPLasVegas is FindThresh, which computes the smallest integer \(B\ge 0\) such that no negative cycles exist in \(G_{in}^{+B}\). This is done using the algorithm FindThresh of the following lemma. The proof of FindThresh is deferred to Section C.3.

**Lemma C.3.** _Let H be an m-edge n-vertex graph with integer weights and let_ \(s\in V(H)\)_. Then there is an algorithm,_ FindThresh(_H,s_) _which outputs an integer_ \(B\ge 0\) _such that w.h.p.,_

• _If H has no negative cycles then B_=0_, and_<tbc>

• _If H has a negative cycle then B\>_0_, H_<sup>+(_B_-1)</sup> _contains a negative cycle, and H_<sup>+_B_</sup> _does not._

_The running time of_ FindThresh(_H,s_) _is O(m_log<sup>6</sup>(_n_)log<sup>2</sup>(_W<sub>H</sub>_)).

**Definition C.4.** If the high probability event of Lemma C.3 holds, we refer to _B_ as the _correct_ value.

## C.1 The Las Vegas algorithm

We now present the algorithm SPLasVegas mentioned at the beginning of the section, using FindThresh as a black box. Recall our assumption that _G<sub>in</sub>_ satisfies \(w(e)\ge-1\) for each \(e\in E_{in}\). Pseudocode for SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) can be found in Algorithm 6. For intuition when reading the pseudocode, note that we will show that w.h.p. none of the restart events occur.

Correctness of SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) is trivial as the algorithm explicitly checks that its output is correct just prior to halting:

**Lemma C.5.** _If_ SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) _outputs a cycle, that cycle is negative in G<sub>in</sub>. If_ SPLasVegas(_G<sub>in</sub>,s<sub>in</sub>_) _outputs a tree, that tree is a shortest path tree from s<sub>in</sub> in G<sub>in</sub>._

## C.2 Running time

Since all edge weights in _G<sub>in</sub>_ are \(\ge-1\) (Assumption 2.1), we have \(W_{G^\prime}\le n^3\). It follows that if there is no restart of the algorithm then by Theorem C.1 and Lemma C.3, its running time is _O(m_log<sup>8</sup>(_n_)) where the call to \(\mathrm{FindThresh}(G',s_{in})\) dominates. It remains to show that w.h.p., no restart occurs.

When _B_=0, Lemma C.3 implies that w.h.p., \(G'\) and hence _G<sub>in</sub>_ has no negative cycles. By Theorem C.1, w.h.p. no restart occurs in Line 4.

Similarly, when _B\>_0, Lemma C.3 implies that w.h.p., \((G')^{+B}\) has no negative cycles, so by Theorem C.1, w.h.p. no restart occurs in Line 7.

To show that w.h.p., no restart occurs in Line 11, we need Corollary C.7 below which shows that \(G_{\le n}\) preserves all negative cycles from \((G')^{+(B-1)}\).


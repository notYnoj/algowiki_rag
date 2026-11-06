## A.1.1 The matching-completion potential

For even _v_ and \(0\le k\le v/2\), set

\(\Phi_k(v):=\prod_{j=0}^{k-1}(v-2j-1)^{-1},\Phi_0(v)=1.\) (116)

This is the probability that a uniform perfect matching on _v_ vertices contains a specified matching of size _k_.

**Lemma 2** (Prescribed matching)**.** _Consider a round on n vertices in which the next edge is uniform among available pairs. For a specified matching F of size_ \(s\le n/2\),

\(Pr(F\subseteq M,\) (99) _holds throughout_ \(|\text{\textit{past}})\le exp(C\zeta_nslogn)\Phi_s(n),\) (117)

_where C is an absolute constant. The assertion is uniform in the starting graph and in F._

_Proof._ As long as no endpoint of a pending edge of _F_ has been matched incorrectly, assign the state with _v_ free vertices and _k_ pending edges the potential \(\Phi_k(v)\). Otherwise assign it zero. Also set it to zero when the density condition first fails. This is a killed process, not a process conditioned on a future event.

Put \(N=\genfrac(){pt}{2}{v}{2}\). Suppose _M_<sub>0</sub> pairs are missing, including _b_ pairs wholly outside the 2_k_ protected endpoints and _a_<sub>0</sub> prescribed pairs. For _v\>_2_k_, the expected next potential divided by the current one, before any additional killing, equals

\(\frac{N-a_0(v-1)-b(v-1)/(v-2k-1)}{N-M_0}.\) (118)

Indeed, selecting a prescribed edge multiplies the potential by _v_-1, selecting an outside edge multiplies it by (_v_-1)/(_v_-2_k_-1), and every other choice kills it. For the complete graph these contributions sum to _N_.

The excess of (118) above one is at most

\(\frac{M_0-b}{N-M_0}\le\frac{2k\zeta_n(v-1)}{(1-\zeta_n)\genfrac(){pt}{2}{v}{2}}\le\frac{8\zeta_nk}{v}\) (119)

for \(\zeta_n\le 1/2\). When _v_=2_k_, the ratio is at most \((1-\zeta_n)^{-1}\), which obeys the same final bound. Killing can only decrease the expectation.

Now \(k\le s\) and \(\sum_{v=n,n-2,\dots,2}v^{-1}=O(logn)\). Iterating the one-step bound gives (117), since the terminal potential is the indicator of the stated event.

## A.1.2 Port labels and small subgraphs

Use the _D_ symbols

\(\mathcal{P}=\{H^+,H^-,M_1,\dots,M_{D-2}\},\) (120)

with involution <o>_H_<sup>+</sup></o>=_H_<sup>-</sup> and <o>_M_</o><sub>i</sub>=_M<sub>i</sub>_. Traversing an edge with symbol _a_ uses port _a_ at its initial vertex and port \(\bar{a}\) at its terminal vertex. A labelling is _admissible_ if incident ports are distinct. This records which round supplied each edge, and the direction of Hamilton edges.


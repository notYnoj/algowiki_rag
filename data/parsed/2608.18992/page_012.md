Moreover, the _information cost of f with error_ \(\epsilon\) is defined as

\(\mathrm{IC}(f,\epsilon)=\mathrm{inf}_\pi\mathrm{max}_\mu\mathrm{IC}_\mu(\pi),\)

where the infimum is taken over all \(\epsilon\)-error protocols \(\pi\) that compute _f_, and the maximum identifies the worst case input distribution \(\mu\) with respect to the best protocol \(\pi\).

\(\blacktriangleright\) **Definition 3** (Information Cost of Graph Predicate)**.** _Consider a graph predicate P and a function_ \(f:X\times Y\rightarrow\{\mathrm{true},\mathrm{false}\}\)_. We say that P_ has an information cost of \(\mathrm{IC}(f,\epsilon)\) with error \(\epsilon\) for _f, formally_ \(\mathrm{IC}(P,f,\epsilon)=\mathrm{IC}(f,\epsilon)\)_, if there exists an_ \(\ell\)_-separated graph family with respect to f and P. The_ information cost of predicate _P_ with error \(\epsilon\) _is defined as_

\(\mathrm{IC}(P,\epsilon)=\mathrm{sup}_f\mathrm{IC}(P,f,\epsilon),\)

_where the supremum is taken over all functions f, for which there exists an_ \(\ell\)_-separated family w.r.t. P._

\(\blacktriangleright\) **Theorem 4** (Information Cost \(\longrightarrow\) Energy Complexity)**.** _Consider a graph predicate P and some_ \(\epsilon>0\)_. Suppose that_ \(\mathrm{IC}(P,\epsilon)\ge I\)_, where I=O_(poly(_n_))_, i.e., there exists a suitable function_ \(f:X\times Y\rightarrow\{\mathrm{true},\mathrm{false}\}\) _and an_ \(\ell\)_-separated family such that_ \(\mathrm{IC}(P,f,\epsilon)=\mathrm{IC}(f,\epsilon)\ge I\)_. Let s be the cut set size (see Def. 2), and let d<sub>cut</sub> denote the maximum cut degree; see_ (4)_. The following hold for any_ \(\epsilon\)_-error algorithm for P:_

(_a)_ \(|\mathrm{supp}(X)|\le 2^{c\cdot I}\) and \(|\mathrm{supp}(Y)|\le 2^{c\cdot I}\)_, for some positive constant c, then the expected node-averaged energy complexity is_ \(\Omega\big(\frac{\ell-1}{n}\cdot\frac{I}{d_{cut}\cdot\mathrm{log}n}\big)\).

_(b) The worst case energy complexity (per node) is_ \(\Omega\big(\frac{I}{d_{cut}\cdot s\cdot\mathrm{log}n}\big)\)_. Moreover, the energy complexity bounds hold independently of the round complexity of the algorithm._

**Proof.** We first show the bound on the worst-case energy complexity of a given algorithm A. Consider the \(\ell\)-separated graph family G w.r.t. _f_ and _P_, and fix some arbitrary \(i\in[\ell-1]\). Suppose that we use A to run the simulation protocol \(\pi_i\) for the cut \((V_{\le i},V_{\ge i+1})\), for

O
O
O
O
O
O
O
U
U
O
O
O
O
O
O
V1
V2
V3
VB
VA

**Figure 2** An example of the graph construction in the proof of Theorem 4 for a 3-separated graph family. For the node-averaged lower bound, we apply Lemma 1 to both cuts, \((V_1,V_2\cup V_3)\) and \((V_1\cup V_2,V_3)\). The figure depicts this application for the cut \((V_1\cup V_2,V_3)\). Here we assume that the nodes on _V_<sub>3</sub>’s side learn more than _I/_2 bits about _G[V_<sub>1</sub>], and hence we choose the set _U_ to lie on this side and swap _V<sub>A</sub>_ and _V<sub>B</sub>_ accordingly when instantiating Lemma 1.


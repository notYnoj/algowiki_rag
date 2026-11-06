## The reduction.

We provide a parameterized reduction from Multicolored Independent Set parameterized by solution size, which is W\[1\]-hard \[15, 42\].

Multicolored Independent Set<br>
_Input:_ A k-partite graph \(G=(V^1\dot{\cup}V^2\dot{\cup}\cdots\dot{\cup}V^k,E)\) with |_V<sup>i</sup>_|=_n_ for all \(i\in[k]\).<br>
_Task:_ Decide whether _G_ contains an independent set _I_ such that \(I\cap V^i\neq\emptyset\) for all \(i\in[k]\).

Let \(V^i=\{v_1^i,\dots,v_n^i\}\) for every \(i\in[k]\). The basic idea of the reduction is as follows. For every _V<sup>i</sup>_, we add a _vertex-selection gadget_, encoding which vertex from _V<sup>i</sup>_ shall be part of the multicolored independent set. For every edge \(e\in E\), we add an _edge gadget_, ensuring that not both end vertices can be "selected" to be part of the multicolored independent set by the corresponding vertex-selection gadget. Thereby, the edge gadgets ensure that the vertices "selected" to be part of a multicolored independent set indeed form an independent set. Both the vertex-selection gadget and the edge gadget use a third kind of gadget, which we call _cut-off gadget_. A cut-off gadget for a given agent _v_ and a 2-set _t_ ensures that agent _v_ has to be matched at least as good as _t_ in every stable matching.

We now describe these three gadgets, starting with the cut-off gadget.

## Cut-off gadget.

For many agents, the reduction contains a _cut-off gadget_. The cut-off gadget for an agent _a_ "cuts off" the preference list of agent _a_ after a specific 2-set _p<sub>a</sub>_, and enforces _a_ to be matched to a 2-set _p_ with \(p\unknown_ap_a\).

Given an instance I of MDSR-Poset with master poset \(\succ_\text{ML}\), the cut-off gadget for an agent _a_ and a 2-set _p<sub>a</sub>_, denoted by CO_<sub>a</sub>_, contains six agents \(z_a^1,\dots,z_a^6\). The basic idea is that deleting all agents but _a_ and \(z_a^1,\dots,z_a^5\) results in the instance I<sub>instable</sub> (see Section 3.1). Because no stable matching will match agent \(z_a^r\) to a 2-set which \(z_a^r\) prefers to every 2-set {_x,y_} with \(x,y\in\{a,z_a^1,z_a^2,\dots,z_a^6\}\), agent _a_ has to be matched better than every 2-set \(\{z_a^r,z_a^{r^\prime}\}\) for \(r,r'\in[6]\) in every stable matching.

Given a 3DSR-Poset-instance \(\mathcal{I}=(A,(\succ_a)_{a\in A},d,\succ_\text{ML})\), we construct an instance \(\mathcal{I}'\) _arising from_ I _by adding a cut-off gadget for an agent_ \(a\in A\) _and a 2-set p<sub>a</sub>_ if we add six agents \(z_a^1,\dots,z_a^6\) to I, and the preferences of the agents in \(\mathcal{I}'\) are as follows (see Example 5 for an example). The preferences of any agent \(z_a^r\) start with all 2-sets in \(\genfrac(){pt}{2}{B}{2}\cup(W\times\{z_a^\ell:\ell\in[6]\})\), where \(B:=\{b,z_b^\ell:b\succ_\text{ML}a,\ell\in[6]\}\), and are then followed by (ignoring all 2-sets containing the agent itself)

\(\mathcal{A}:=\{a,z_a^1\}\succ\{a,z_a^2\}\succ\{a,z_a^3\}\succ\{a,z_a^5\}\succ\{z_a^1,z_a^4\}\succ\{z_a^2,z_a^3\}\succ\{a,z_a^4\}\succ\{z_a^1,z_a^5\}\succ\{z_a^2,z_a^4\}\succ\{z_a^1,z_a^3\}\succ\{z_a^1,z_a^3\}\succ\{z_a^4,z_a^5\}\succ\{a,z_a^6\}\succ\{z_a^1,z_a^6\}\succ\{z_a^2,z_a^6\}\succ\{z_a^3,z_a^6\}\succ\{z_a^4,z_a^6\}\succ\{z_a^5,z_a^6\}\succ\{z_a^5,z_a^6\}\succ\{z_a^6\}\succ\{z_a^7,z_a^7\}\)

The preferences of _a_ in \(\mathcal{I}'\) arise from the preferences of _a_ in I by inserting after the 2-set _p<sub>a</sub>_ all 2- sets \(\{z_a^r,z_a^{r^\prime}\}\) with \(r,r'\in[6]\) in the same order as in A, and appending all other 2-sets containing an agent \(z_a^r\) at the end of the preferences of _a_. The preferences in \(\mathcal{I}'\) of an agent \(b\in A\backslash\{a\}\) arise from _b_’s preferences in I as follows: If \(a\succ_\text{ML}w\), then we add all 2-sets containing an agent from the cut-off gadget at the beginning of their preference, while otherwise we add all 2-sets containing an agent \(z_a^r\) at the end of their preferences in an arbitrary order (consistent with the master poset).

**Example 5.** Consider the 3DSR-Poset-instance I with four agents _a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub>, and _a_<sub>4</sub>, master poset \(a_1\succ_\text{ML}a_2\succ_\text{ML}a_3\succ_\text{ML}a_4\), and the following preferences:<tbc>

\(a_1:\{a_2,a_3\}\succ\{a_2,a_4\}\succ\{a_3,a_4\},\)


# The Parameterized Complexity of Coloring Discovery

19

those assigned to blocks _P_ with \(\sigma(P)\neq\perp\). Each such color is shared only by _P_ and the clique vertex represented by the same block node; that vertex lies in \(\sigma(P)\), which is anticomplete to _P_ by feasibility.

There are at most \((k+1)^k\in k^{\mathcal{O}(k)}\) partitions P, and for each partition there are at most \((2^k+1)^{|\mathcal{P}|}\le(2^k+1)^k\) maps \(\sigma\). For each feasible guess, the assignment instance has at most _n_ vertices and, after the palette preprocessing, at most _n_ color names. It can therefore be solved in O(_n_<sup>3</sup>) time. Together with the computation of _S_, and using \(n^2\le n^3\), _k_<sup>O(_k_)</sup>=2<sup>O(_k_log_k_)</sup>, and \(2^k+1\le 2^{k+1}\), the running time is

\(\mathcal{O}\big(2^kn^2+k^{\mathcal{O}(k)}(2^k+1)^kn^3\big)\le\mathcal{O}\big((2^k+2^{\mathcal{O}(k\mathrm{log}k)}\cdot 2^{k(k+1)})n^3\big)\)<br>
\(=\mathcal{O}\big((2^k+2^{\mathcal{O}(k^2+k\mathrm{log}k+k)})n^3\big)\)<br>
\(=2^{\mathcal{O}(k^2)}n^3\)

### B The Color-Cycle ILP in Detail

We now prove the equivalence used in Theorem 3. Fix \(\gamma:C\rightarrow[q]\) such that \(\gamma\) is a proper coloring. For a neighborhood class \(R\subseteq I\), let \(A_{R,a}=|R\cap\varphi^{-1}(a)|\). The ILP contains the supply equations \(\sum_cx_{R,a,c}=A_{R,a}\) and the nonnegativity constraints \(x_{R,a,c}\in\mathbb{Z}_{\ge 0}\). If \(c\in\gamma(N(R))\), it also contains _x<sub>R,a,c</sub>_=0.

Define \(T_{a,c}=|\{v\in C:\varphi(v)=a,\gamma(v)=c\}|+\sum_Rx_{R,a,c}\). For every directed simple color cycle _Z_, including each one-vertex loop, let \(y_Z\in\mathbb{Z}_{\ge 0}\). The arc equations are \(\sum_{Z:(a,c)\in E(Z)}y_Z=T_{a,c}\) for all \(a,c\in[q]\). Since a union of directed cycles is balanced at every color, these equations imply \(\sum_CT_{a,c}=\sum_CT_{c,a}\). The left side is the initial multiplicity of _a_ and the right side is its target multiplicity. Thus swap reachability is enforced without a separate histogram constraint.

Given a feasible integer solution, assign final colors within each class _R_ according to the counts _x<sub>R,a,c</sub>_. This is possible because the supply equations account for every vertex in each initial-color subclass. The forbidden-color equations make the resulting coloring proper across edges from _C_ to _I_. Properness on _C_ was checked when \(\gamma\) was guessed, and _I_ has no edges. The _y_-variables decompose its transition multigraph, and the budget inequality plus Lemma 2 supplies a swap sequence of length at most _b_.

In the other direction, let a proper target reachable within at most _b_ color swaps be given. Counting its transitions within every class defines the _x_-variables. Properness gives all forbidden-color equations. Equal histograms make the transition multigraph balanced, so its arcs decompose into directed simple cycles. Choose a decomposition that realizes the minimum swap distance. Lemma 2 shows that its _y_-variables satisfy the budget constraint. This proves both implications.

There are at most 2_<sup>k</sup>q_<sup>2</sup> variables of type _x_ and \(q+\sum_{\ell=2}^q\genfrac(){pt}{2}{q}{\ell}(\ell-1)!<eq!\) variables of type _y_. By Lemma 1, replace _b_ by min{_b,n_-1}. Hence the right-hand sides are polynomial and the encoding length is bounded by \(\mathcal{O}\big(f(k+q)\cdot n^{\mathcal{O}(1)}\big)\) for a computable function _f_. Across the _q<sup>k</sup>_ choices for \(\gamma\), Lenstra’s algorithm proves fixed-parameter tractability.


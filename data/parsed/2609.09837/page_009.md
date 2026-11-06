# The Parameterized Complexity of Coloring Discovery

9

<tbc>introduce a nonnegative integer variable _y<sub>Z</sub>_ for every \(Z\in\Gamma_q\). For every ordered pair (_a,c_) require \(\sum_{Z:(a,c)\in E(Z)}y_Z=T_{a,c}\), and impose the budget constraint \(\sum_{Z\in\Gamma_q}(|Z|-1)y_Z\le b\).

The supply and forbidden-color constraints describe exactly the proper extensions of \(\gamma\) to the independent set _I_. The cycle equations ensure that the transition multigraph is the union of directed simple cycles and therefore enforce equality of the initial and target color multiplicities. Every feasible choice of the _y_-variables specifies a swap sequence of length \(\sum_{Z\in\Gamma_q}(|Z|-1)y_Z\), so the budget constraint implies that the target is reachable within _b_ swaps. Conversely, the transitions of every proper target reachable within at most _b_ swaps satisfy the _x_-constraints. Let \(\psi\) be the coloring prescribed by \(\gamma\) and the _x_-variables. Choosing a decomposition of \(D^\neq(\varphi,\psi)\) with the maximum number of directed simple cycles and taking every loop as a one-vertex cycle supplies _y_-variables whose budget expression is, by Lemma 2, the exact swap distance. Thus the ILP is feasible exactly for the desired targets.

There are \(|\Gamma_q|=q+\sum_{\ell=2}^q\genfrac(){pt}{2}{q}{\ell}(\ell-1)!<eq!\) variables of type _y_ and at most 2_<sup>k</sup>q_<sup>2</sup> variables of type _x_. By Lemma 1, we may replace _b_ by min{_b,n_-1}. Every coefficient and right-hand side then has O(log_n_+log_q_) bits, and the total ILP encoding length is _f(k+q)n_<sup>O(1)</sup> for a computable function _f_. Lenstra’s theorem, applied to each of the _q<sup>k</sup>_ choices for \(\gamma\), gives a running time \(f'(k+q)n^{\mathcal{O}(1)}\).

We remark that this transition-multigraph approach does not seem to extend to slides, since the available moves depend on the positions of the colors in the graph. We therefore could not resolve the complexity of Slide-CD with respect to vc(_G_)+_q_ and leave it as an open question.

### 4 Hardness Results

We now turn to further natural structural graph parameters and show hardness with respect to these. The full details of the longer reductions are given in Appendix C.

#### 4.1 Flipping: treedepth and feedback vertex set

Fiala, Golovach, and Kratochvíl proved that List Coloring is W\[1\]-hard parameterized by vertex cover \[14\]. We reduce from their problem using a list- enforcement gadget that simultaneously bounds the treedepth and the feedback vertex set of the constructed graph in terms of the vertex-cover number of the source instance.

**Theorem 4.** Flip-CD _is_ W\[1\]_-hard parameterized by_ td(_G_)+fvs(_G)._

_Proof (sketch)._ Let (_G,q,L_) be a List Coloring instance. First, delete colors that occur in no list. Let _n_=|_V(G_)| and set _b=n_. Construct a graph _H_ from _G_ as follows. Initially color every original vertex with color 1. For every \(v\in V(G)\) and every forbidden color \(c\notin L(v)\), attach _b_+1 pendent vertices to _v_


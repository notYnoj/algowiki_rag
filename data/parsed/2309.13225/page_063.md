## A.1 Closer Analysis of sparseapasp

Instead of bounding the approximation error simply by using the number of thresholds used in the degree decomposition, we perform a more fine-grained analysis to bound the approximation error based on the structure and degrees of a given path _P_. Recall the definition of blocking vertices and blocking levels.

**Definition 3.4.** _Let u,v be vertices in a graph G and P a path between u,v. Let_ (_D_<sub>1</sub>_,...,D<sub>k</sub>),_ (_E_<sub>1</sub>_,...,E<sub>k</sub>_) _be the outputs of a call to **Decompose** with degree thresholds s_<sub>1</sub>_,...,s_<sub>_k_-1</sub>_. If there is an edge_ \((a,b)\in P\) _such that_ \((a,b)\notin E_{\ell(u)}\)_, the_ **blocking vertex** _of P from u, denoted b(u,P), is the closest vertex to v that is an endpoint to such an edge. If no such edge exists, then b(u,P_)=_v._

_Then, the_ **blocking vertices of** _P **is the set B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} _defined in the following manner:_

1. _x_<sub>0</sub>=_u_<tbc>

2. _x_<sub>1</sub>=_v_<tbc>

_3._ \(x_i=b\left(x_{i-1},P_{x_{i-1},x_{i-2}}\right)\) _where P_<sub>_x_<sub>_i_-1</sub>_,x_<sub>_i_-2</sub></sub> _is the sub-path of P between x_<sub>_i_-1</sub>_,x_<sub>_i_-2</sub>.

_For any_ \(j\ge\ell(v)\), **blocking levels of** _P_ **at level** _j **is the set**_ \(L_B(P,j)=\{\ell(x_i)\text{\textit{s.t.}}x_i\in B(P)\text{\textit{and}}\ell(x_i)<j\}\)_. Denote_ \(L_B(P)=L_B(P,\ell(v))\).

We begin with some simple properties to note about the blocking vertices and blocking levels of a given path _P_.

**Lemma A.1.** _Let P be a shortest path and B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} _be the set of blocking vertices. Then,_

1. \(k\ge\ell(x_1)>\ell(x_2)>\dots>\ell(x_t)\ge 1\).<tbc>

_2. For all_ \(2\le i\le t\), \(x_{i-1}\notin P_{x_i,x_{i-2}}\).<tbc>

_3._ \(B(P_{x_i,x_{i+1}})\subset B(P)\) _and_ \(L_B(P_{x_i,x_{i+1}})\subset L_B(P)\) _for_ \(1\le i\le t-1\).<tbc>

_4._ \(P_{x_{t-1},x_t}\subset P_{x_{t-2},x_{t-1}}\subset\dots\subset P_{x_0,x_1}=P\)

_Proof._ Property 1 follows as for any edge (_a,b_), \(\ell(a,b)=min(\ell(a),\ell(b))\).

Property 2 follows as for all \(i\ge 2\), \(x_i\in P_{x_{i-1},x_{i-2}}\).

\(B(P_{x_i,x_{i+1}})\subset B(P)\) follows by the construction of the blocking vertices, noting that _x<sub>i</sub>,x_<sub>_i_+1</sub> determine the remaining blocking vertices. Then, \(L_B(P_{x_i,x_{i+1}})\subset L_B(P)\) follows as the blocking levels are constructed from the blocking vertices.

Property 4 follows as _x<sub>i</sub>_ is chosen as a vertex on the path _P_<sub>_x_<sub>_i_-2</sub>_,x_<sub>_i_-1</sub></sub>.

We now give the deferred proof that the number of blocking levels directly determines the additive error accumulated on a given path when executing **SparseAPASP** (Algorithm 12).

**Lemma A.2.** _Let u,v be vertices in a graph G and P be a shortest path between u,v. Let B(P_) _be the blocking vertices of P. Then, Algorithm 12 in the_ \(\ell(v)\)_-th iteration computes distance estimate_ \(\hat{\delta}\) _such that,_

\(\hat{\delta}(v^*,u)\le\hat{\delta}_{\ell(v)}(v^*,u)\le\delta(v,u)+2|L_B(P)|+1\)

_For any level_ \(j\ge\ell(v)\)_, if_ \(v\in D_j\),

\(\hat{\delta}(v,u)\le\hat{\delta}_j(v,u)\le\delta(v,u)+2|L_B(P,j)|\)

_Proof._ We proceed by induction. Suppose |_L<sub>B</sub>(P_)|=0. Then, _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>}={_u,v_}. In particular, \(P\subset E_{\ell(v)}\) so that Algorithm 12 finds the exact distance in the \(\ell(v)\)-th iteration.


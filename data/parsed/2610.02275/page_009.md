_Proof._ The empty-prefix case is immediate. Suppose that a later selected vertex _x<sub>i</sub>_ satisfies \(i\le\beta\). A previously selected _Y_ -vertex _y_ has \(r(y)=\beta\) and a selected neighbour _x<sub>h</sub>_ in its component. Claim 9 gives _h\<i_, so \(\ell(y)\le h<i\le r(y)\). Convexity implies \(yx_i\in E(G)\), a contradiction. Thus \(i>\beta\ge\alpha\).

If a later selected _Y_ -vertex _z_ had \(\ell(z)\le\alpha\), its selected neighbour _x<sub>i</sub>_ would satisfy \(\ell(z)\le\alpha<i\le r(z)\). It would therefore be adjacent to the previously selected vertex \(x_\alpha\), again a contradiction.

## 5.2 Dynamic programming table

A _labelled partial solution_ consists of an edge open packing \(D'\) together with barriers \((\alpha,\beta)\). Its components are generated from left to right by the transitions below. The value \(\alpha\) is the exact index of its rightmost selected _X_-vertex, with \(\alpha=0\) only for the empty solution. The recorded barrier \(\beta\) is an upper bound on _r(y_) for every selected \(y\in Y\) . It may exceed their actual maximum; such a conservative barrier restricts the permitted continuation. In every reachable state \(\alpha\le\beta\). The continuation rule requires every future selected _X_-vertex to have index greater than \(\beta\) and every future selected _Y_ -vertex _y_ to satisfy \(\ell(y)>\alpha\).

For \(0\le\alpha,\beta\le p\), let \(F[\alpha,\beta]\) be the maximum number of edges in a reachable labelled partial solution with these barriers, or \(-\infty\) if none exists. Future choices depend only on the barriers, so retaining the largest value for each pair is sufficient. Initialize _F_\[0,0\]=0 and all other entries to \(-\infty\). Each transition strictly increases \(\beta\): its new value is either \(q\ge i>\beta\) or \(r(y)\ge q\ge s>\beta\). The states can therefore be processed in increasing order of \(\beta\).

## 5.3 Transitions

We append one new star component to a reachable partial solution.

**_X_-centred star.** Choose a centre _x<sub>i</sub>_ with \(i>\beta\) and a new right-endpoint barrier \(q\in\{i,\dots,p\}\). Define<tbc>

\(w_X(i,\alpha,q)=\big|\{y\in Y:\alpha<\ell(y)\le i\le r(y)\le q\}\big|.\)

<tbc>If \(w_X(i,\alpha,q)>0\), select all these vertices as leaves and update

\(F[i,q]\leftarrow max\{F[i,q],F[\alpha,\beta]+w_X(i,\alpha,q)\}.\)

The condition \(i>\beta\) excludes edges from the new centre to previously selected _Y_ -vertices, and \(\ell(y)>\alpha\) excludes edges from new leaves to previously selected _X_-vertices. The updated barriers require future _X_-vertices to lie beyond _q_ and future _Y_ -vertices to have left endpoint greater than _i_; hence the new star is also separated from all permitted future components. The recorded value _q_ need not be attained by a selected leaf, which is why conservative barriers are allowed.

**_Y_ -centred star.** Choose a centre \(y\in Y\) with \(\ell(y)>\alpha\), and put \(s=max\{\ell(y),\beta+1\}\). If \(s\le r(y)\), then for every \(q\in\{s,\dots,r(y)\}\) select _x<sub>s</sub>,...,x<sub>q</sub>_ as leaves and update

\(F[q,r(y)]\leftarrow max\{F[q,r(y)],F[\alpha,\beta]+q-s+1\}.\)

The new leaves have indices greater than \(\beta\), so they are nonadjacent to previously selected _Y_ -vertices. The condition \(\ell(y)>\alpha\) separates the new centre from previously selected _X_-vertices. Future _Y_ -vertices have left endpoint greater than _q_, and future _X_-vertices have index greater than _r(y_), so neither can have an edge to the new star.

The algorithm returns \(max_{0\le\alpha,\beta\le p}F[\alpha,\beta]\).

## 5.4 Correctness

**Lemma 11.** _Every solution constructed by the dynamic program is an edge open packing._

_Proof._ Both transitions add a star whose vertices have no edges to earlier selected vertices, as shown above, and preserve the stated barrier invariants. In particular, no previously selected vertex can be reused: a previous _X_-vertex has index at most \(\alpha\le\beta\), while a previous _Y_ -vertex has a selected neighbour of index at most \(\alpha\) and therefore has left endpoint at most \(\alpha\). Inductively, the selected vertices induce disjoint stars, and Observation 1 applies.

**Lemma 12.** _For every edge open packing D, the dynamic program constructs a solution of cardinality at least_ |_D|._


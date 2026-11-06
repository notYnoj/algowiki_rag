<tbc>**Theorem 1.8.** _For every_ \(\alpha\in[\frac{1}{2},1)\) _there is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _with_ \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\)_, w<sub>n</sub>_(T_<sub>n</sub>_)=1 _and_<tbc>

\(\mathtt{cent}^\alpha(\mathcal{T}_n,w_n)\ge\frac{1}{1-\alpha}\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-\frac{\alpha}{1-\alpha}.\)

<tbc>_Proof._ Let T_<sub>n</sub>_ be defined recursively as in Theorem 1.2 and _w<sub>n</sub>_ is defined recursively as follows. Let A, B and _c_ be as in the definition of T_<sub>n</sub>_. Let _w_<sub>A</sub> and _w_<sub>B</sub> be weight functions on A and B respectively, each a copy of _w_<sub>_n_-1</sub>. Then _w<sub>n</sub>_ is given by

\(w_n(v)=\left\{\begin{array}{ c c }
0, & v=c \\
\alpha w_\mathcal{A}(v), & v\in V(\mathcal{A}) \\
(1-\alpha)w_\mathcal{B}(v), & v\in V(\mathcal{B}).
\end{array}\right.\)

Let _C<sub>n</sub>_ and _T<sub>n</sub>_ be the same search trees on T_<sub>n</sub>_ as in the proof of Theorem 1.2. Observe that _C<sub>n</sub>_ is an \(\alpha\)-centroid tree on T_<sub>n</sub>_. With a similar analysis as in Theorem 1.2, we get `cost`_<sub>w<sub>n</sub></sub>(C<sub>n</sub>_)=_n_+1 and \(\mathtt{cost}_{w_n}(T_n)=(1-\alpha)n+1\). From these the required bound follows. Using Theorem 1.7(i), we have \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\).

## 6.3 Optimal STTs

In this section we prove the characterization of optimal STTs as \(\alpha\)-centroid trees.

**Theorem 1.9.** _Let T be an optimal STT of_ (T_,w). Then, T is a_ \(\frac{2}{3}\)_-centroid tree of_ (T_,w)._

For the purpose of proving Theorem 1.9, we define the following transformation on search trees. Let _T_ be a search tree on T and \(v\in V(\mathcal{T})\). We denote by _T<sup>v</sup>_ the search tree on T that is obtained as follows. Set `root`(_T<sup>v</sup>_)=_v_. The subtrees of _T<sup>v</sup>_ rooted at the children of _v_ are all the trees of the form _T_|<sub>H</sub>, where \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-v)\). We say that _T<sup>v</sup>_ is obtained from _T_ by _lifting_ the vertex _v_. (This transformation can also be defined via _rotations_, e.g., see \[BCI<sup>+</sup>20\]. _T<sup>v</sup>_ is obtained by repeatedly rotating the edge between _v_ and its parent until _v_ becomes the root.) For every \(u,v\in V(\mathcal{T})\) we have

\(\mathtt{Path}_{T^v}(u)=\left\{\begin{array}{ c c }
\{v\}, & u=v \\
\{v\}\cup(\mathtt{Path}_T(u)\cap V(\mathcal{H})), & u\in V(\mathcal{H}),\mathcal{H}\in\mathbb{C}(\mathcal{T}-v).
\end{array}\right.\)

_Proof of Theorem 1.9._ Let _T_ be an optimal STT on T , and suppose towards contradiction, that _T_ is not a \(\frac{2}{3}\)-centroid. Assume w.l.o.g., that _w_(T)=1. By taking _T_ to be a minimum height counterexample, we can assume that the root _x_ of _T_ has a child _y_, so that \(w(T_y)>\frac{2}{3}\). Let _B<sub>x</sub>_ denote the set of vertices _not_ in the same component of T-_x_ as _y_, and let _B<sub>y</sub>_ denote the set of vertices not in the same component of T-_y_ as _x_. Finally, let _B<sub>x,y</sub>=V(T_)-_B<sub>x</sub>-B<sub>y</sub>_. By our assumption, \(w(B_y\cup B_{x,y})>\frac{2}{3}\), and thus, \(w(B_x)<\frac{1}{3}\). We distinguish three cases.

### Case 1.

If \(w(B_y)>\frac{1}{3}\), then transform _T_ by lifting _y_. The depths of vertices in _B<sub>y</sub>_ decrease by one and the depths of vertices in _B<sub>x</sub>_ increase by one. The depths of vertices in _B<sub>x,y</sub>_ are unchanged. (See Figure 10.1.) We have

\(\mathtt{cost}_w(T^y)-\mathtt{cost}_w(T)=w(B_x)-w(B_y)<\frac{1}{3}-\frac{1}{3}=0,\)

contradicting the optimality of _T_.

If Case 1 did not occur, we have \(w(B_{x,y})>\frac{1}{3}\), and in particular, \(B_{x,y}\neq\emptyset\). Denote by _z_ the unique child of _y_ in _B<sub>x,y</sub>_.


_Proof of Theorem 1.1._ The proof is by induction on the number of vertices. When |_V_(T)|=1 we have

\(2\cdot\mathtt{OPT}(\mathcal{T},w)-m=2m-m=m=\mathtt{cent}(\mathcal{T},w)\)

as required.

Assume |_V_(T)|_\>_1. Let _C_ be a centroid tree on T and _c_=`root`(_C_). Using Observation 2.1 and the induction hypothesis we have

\(\mathtt{cost}_w(C)\le m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{cent}(\mathcal{H},w)\)<br>
\(\le m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}(2\cdot\mathtt{OPT}(\mathcal{H},w)-w(\mathcal{H}))\)<br>
\(=w(c)+2\cdot\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w),\)

therefore it is enough to show that

\(w(c)+2\cdot\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w)\le 2\cdot\mathtt{OPT}(\mathcal{T},w)-m,\)

which is just a re-arrangement of Lemma 3.1. This concludes the proof.

We note that in the _edge-query model_ of search trees a 2-approximation was shown in \[CJLM14\] using similar techniques. In contrast to that result, however, our approximation guarantee is best possible.

## 3.2 Lower bounds

In the following, we show the tightness of Theorem 1.1 through the following lower bounds.

**Theorem 1.2.**<tbc>

(_i)_ _For every_ \(\varepsilon>0\) _there is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _with w<sub>n</sub>_(T_<sub>n</sub>_)=1_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(\mathtt{cost}_{w_n}(C_n)\ge 2\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-1-\varepsilon.\)<tbc>

_(ii)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>), where w<sub>n</sub> is the uniform distribution on V_(T_<sub>n</sub>), and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(lim_{n\rightarrow\infty}\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,w_n)}=2.\)<tbc>

<tbc>_In both cases_ \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\).<tbc>

<tbc>**Part (i).** We proceed by constructing a sequence (T_<sub>n</sub>,w<sub>n</sub>_) such that for _some_ centroid tree _C<sub>n</sub>_,

\(\mathtt{cost}_{w_n}(C_n)\ge 2\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-1.\)

Using Lemma 2.4, we can then add an arbitrarily small perturbation to _w<sub>n</sub>_ to make _C<sub>n</sub>_ the _unique_ centroid tree. (Observe that for every search tree _T_, `cost`_<sub>w</sub>(T_) is continuous in _w_, therefore so is `OPT`(T_,w_).)

The sequence (T_<sub>n</sub>,w<sub>n</sub>_) is constructed recursively as follows. For the sake of the construction we view T_<sub>n</sub>_ as a rooted tree. The base case T<sub>0</sub> is a tree with a single vertex _v_ and _w_<sub>0</sub>(_v_)=1. For _n\>_0, take two copies (A_,w_<sub>A</sub>) and (B_,w_<sub>B</sub>) of (T<sub>_n_-1</sub>_,w_<sub>_n_-1</sub>). Connect the roots of A and B to a new vertex _c_. Finally, set `root`(T_<sub>n</sub>_)=`root`(A) (see Figure 2). We define _w<sub>n</sub>_ as follows. (observe that _w<sub>n</sub>_(T_<sub>n</sub>_)=1, by induction on _n_.)<tbc>

\(w_n(v)=\left\{\begin{array}{ c c }
0, & v=c \\
\frac{1}{2}w_\mathcal{A}(v), & v\in V(\mathcal{A}) \\
\frac{1}{2}w_\mathcal{B}(v), & v\in V(\mathcal{B}).
\end{array}\right.\)


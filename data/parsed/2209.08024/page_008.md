_Proof._ W.l.o.g., assume that _w_(T)=1. Consider first a vertex \(x\in V(\mathcal{T})-\{u,v\}\). The contraction {_u,v_} does not change the weight of any component \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-x)\). Thus, _x_ is a centroid of (T_,w_) if and only if it is a centroid of \((\mathcal{T}',w')\).

Consider now the vertices _u_, _v_, and _s_. Observe that \(\mathbb{C}(\mathcal{T}-\{u,v\})=\mathbb{C}(\mathcal{T}'-s)\), and the contraction does not affect the weights of these components. If _u_ or _v_ is a centroid of (T_,w_), then no component of C(T-{_u,v_}) has weight more than \(\frac{1}{2}\). Thus, _s_ is a centroid of \((\mathcal{T}',w')\).

On the other hand, suppose that _s_ is a centroid of \((\mathcal{T}',w')\). Consider a component \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-u)\). If H does not contain _v_, then \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-\{u,v\})=\mathbb{C}(\mathcal{T}'-s)\), so \(w(\mathcal{H})\le\frac{1}{2}\) by assumption. In the same way, for each \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-v)\), if H does not contain _u_, then \(w(\mathcal{H})\le\frac{1}{2}\). Now let H_<sub>v</sub>_ be the component of T-_u_ that contains _v_, and let H_<sub>u</sub>_ be the component of T-_v_ that contains _u_. Since H_<sub>v</sub>_ and H_<sub>u</sub>_ are disjoint, we have \(w(\mathcal{H}_v)+w(\mathcal{H}_u)\le 1\), so either \(w(\mathcal{H}_v)\le\frac{1}{2}\) or \(w(\mathcal{H}_u)\le\frac{1}{2}\). Thus, either _u_ or _v_ is a centroid of \((\mathcal{T}',w')\).

## 3 Approximation guarantees for general trees

In this section we prove the general upper and lower bounds on the approximation quality of centroid trees.

### 3.1 Upper bound

**Theorem 1.1.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, and m=w_(T)_. Then_<tbc>

\(\mathtt{cent}(\mathcal{T},w)\le 2\cdot\mathtt{OPT}(\mathcal{T},w)-m.\)

<tbc>We start with a lemma.

**Lemma 3.1.** _Let c be a centroid of_ (T_,w_) _and m=w_(T)_. Then_

\(\mathtt{OPT}(\mathcal{T},w)\ge\frac{m}{2}+\frac{w(c)}{2}+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w).\) (1)

_Proof._ Let _T_ be an arbitrary search tree on T . We will show that `cost`_<sub>w</sub>(T_) is at least the right hand side of Equation (1).

Denote _r_=`root`(_T_). If _r=c_, using Observation 2.1, we have<tbc>

\(\mathtt{cost}_w(T)\ge m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w),\)

<tbc>which implies the claim. Assume therefore that \(r\neq c\). Denote by H<sup>∗</sup> the connected component of T-_c_ where _r_ is. The contribution of vertices of H<sup>∗</sup> to `cost`_<sub>w</sub>(T_) is at least `cost`<sub>_w_<sub>H<sup>∗</sup></sub></sub>(_T_|<sub>H<sup>∗</sup></sub>). For \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)\), \(\mathcal{H}\neq\mathcal{H}^*\) and \(v\in V(\mathcal{H})\), we have \(\mathtt{Path}_T(v)\supseteq\{r\}\cup\mathtt{Path}_{T|_\mathcal{H}}(v)\), therefore the contribution of vertices of every \(\mathcal{H}\neq\mathcal{H}^*\) is at least _w_(H)+`cost`_<sub>w</sub>(T_|<sub>H</sub>). Finally, the contribution of _c_ is at least 2_w(c_), since both \(c,r\in\mathtt{Path}_T(c)\). Summing the contributions of all the vertices, we get

\(\mathtt{cost}_w(T)\ge 2w(c)+\mathtt{cost}_w(T|_{\mathcal{H}^*})+\sum_{\mathcal{H}\neq\mathcal{H}^*}(w(\mathcal{H})+\mathtt{cost}_w(T|_\mathcal{H}))\)<br>
\(\ge m-w(\mathcal{H}^*)+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\ge\frac{m}{2}+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w),\)

where the last inequality follows from _c_ being a centroid.


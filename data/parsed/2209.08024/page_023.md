## Part (i).

The proof of Theorem 1.7(i) is a generalization of the proof of Theorem 1.1. We start with a lemma.

**Lemma 6.1.** _Let c be a_ \(\alpha\)_-centroid of_ (T_,w_) _and m=w_(T)_. Then_<tbc>

\(\mathtt{OPT}(\mathcal{T},w)\ge(1-\alpha)m+\alpha w(c)+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w).\)

<tbc>_Proof._ Let _T_ a search tree on T . Denote _r_=`root`(_T_). If _r=c_, the required follows using Observation 2.1. We assume therefore that \(r\neq c\). Let \(\mathcal{H}^*\in\mathbb{C}(\mathcal{T}-c)\) such that \(r\in V(\mathcal{H}^*)\). Repeating the argument of Lemma 3.1, we get

\(\mathtt{cost}_w(T)\ge m-w(\mathcal{H}^*)+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\ge(1-\alpha)m+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w),\)

where the second inequality follows since _c_ is a \(\alpha\)-centroid.

_Proof of Theorem 1.7(i)._ By induction on the number of vertices. When |_V_(T)|=1 we have

\(\frac{1}{1-\alpha}\mathtt{OPT}(\mathcal{T},w)-\frac{\alpha}{1-\alpha}m=\frac{1}{1-\alpha}m-\frac{\alpha}{1-\alpha}m=m=\mathtt{cent}^\alpha(\mathcal{T},w),\)

as required.

Assume |_V_(T)|_\>_1. Repeating the argument of Theorem 1.1, using the induction hypothesis we get

\(\mathtt{cent}^\alpha(\mathcal{T},w)\le m-\frac{\alpha}{1-\alpha}(m-w(c))+\frac{1}{1-\alpha}\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\le\frac{1}{1-\alpha}\mathtt{OPT}(\mathcal{T},w)-\frac{\alpha}{1-\alpha}m,\)

where the last inequality is exactly Lemma 6.1.

## Part (ii).

We prove Theorem 1.7(ii) through the following lemma.

**Lemma 6.2.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, m=w_(T) _and_ \(\alpha\in[\frac{1}{3},\frac{1}{2}]\)_. Assume that c is an_ \(\alpha\)_-centroid. Then_

\(\mathtt{OPT}(\mathcal{T},w)\ge(2-3\alpha)m+(3\alpha-1)w(c)+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w).\) (6)

_Proof._ Let _T_ be an arbitrary search tree on T . We will show that `cost`_<sub>w</sub>(T_) is at least the right hand side of Equation (6).

Denote _r_=`root`(_T_). If _r=c_, the required follows using Observation 2.1, observing that \(m\ge(2-3\alpha)m+(3\alpha-1)w(c)\). Assume that \(r\neq c\). Let \(\mathcal{H}_0\in\mathbb{C}(\mathcal{T}-c)\) such that \(r\in V(\mathcal{H}_0)\) and denote \(s=\mathtt{LCA}_T(\mathcal{T}-\mathcal{H}_0)\in V(\mathcal{T}-\mathcal{H}_0)\). Consider two cases:

## Case _s=c_.

The contribution of vertices of H<sub>0</sub> to `cost`_<sub>w</sub>(T_) is at least `cost`_<sub>w</sub>(T_|<sub>H<sub>0</sub></sub>). For \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)\), \(\mathcal{H}\neq\mathcal{H}_0\), the contribution of vertices of H is at least 2_w_(H)+`cost`_<sub>w</sub>(T_|<sub>H</sub>), since these vertices have both _c_ and _r_ as predecessors. The contribution of _c_ is at least 2_w(c_). Summing all the above, we get

\(\mathtt{cost}_w(T)\ge 2w(c)+\mathtt{cost}_w(T|_{\mathcal{H}_0})+\sum_{\mathcal{H}\neq\mathcal{H}_0}(2w(\mathcal{H})+\mathtt{cost}_w(T|_\mathcal{H}))\)<br>
\(\ge 2(m-w(\mathcal{H}_0))+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\ge m+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w),\)


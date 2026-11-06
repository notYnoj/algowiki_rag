where the last inequality follows from _c_ being an \(\alpha\)-centroid and \(\alpha\le\frac{1}{2}\).

### Case \(s\neq c\).

Let \(\mathcal{H}_1\in\mathbb{C}(\mathcal{T}-c)\) such that \(s\in V(\mathcal{H}_1)\). Note that \(\mathcal{H}_1\neq\mathcal{H}_0\). The contribution of vertices of H<sub>1</sub> to `cost`_<sub>w</sub>(T_) is at least _w_(H<sub>1</sub>)+`cost`_<sub>w</sub>(T_|<sub>H<sub>1</sub></sub>), since these have _r_ as predecessor. The contribution of _c_ is at least 3_w(c_), since it has both _r_ and _s_ as predecessors. The contribution of all other vertices is bounded from below as in the previous case. Summing up, we get

\(\mathtt{cost}_w(T)\ge 3w(c)+w(\mathcal{H}_1)+2\sum_{\mathcal{H}\neq\mathcal{H}_0,\mathcal{H}_1}w(\mathcal{H})+\sum_\mathcal{H}\mathtt{cost}_w(T|_\mathcal{H})\)<br>
\(\ge 2m-2w(\mathcal{H}_0)-w(\mathcal{H}_1)+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\ge(2-3\alpha)m+w(c)+\sum_\mathcal{H}\mathtt{OPT}(\mathcal{H},w),\)

where the last inequality follows from _c_ being an \(\alpha\)-centroid. (See Figure 9.)

_Proof of Theorem 1.7(ii)._ By induction on the number of vertices. When |_V_(T)|=1 we have

\(\frac{1}{2-2\alpha}\mathtt{OPT}(\mathcal{T},w)-\frac{3\alpha-1}{2-3\alpha}m=\frac{1}{2-3\alpha}m-\frac{3\alpha-1}{2-3\alpha}m=m\ge\mathtt{cent}^\alpha(\mathcal{T},w),\)

as required.

Assume |_V_(T)|_\>_1. Repeating the argument of Theorem 1.1, using the induction hypothesis we get

\(\mathtt{cent}^\alpha(\mathcal{T},w)\le m-\frac{3\alpha-1}{2-3\alpha}(m-w(c))+\frac{1}{2-3\alpha}\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-c)}\mathtt{OPT}(\mathcal{H},w)\)<br>
\(\le\frac{1}{2-3\alpha}\mathtt{OPT}(\mathcal{T},w)-\frac{3\alpha-1}{2-3\alpha}m,\)

where the last inequality is exactly Lemma 6.2.

## 6.2 Lower bound

We show that Theorem 1.7(i) is tight when \(\alpha\ge\frac{1}{2}\).

-
H1
Ho
S
r
C
-
H1

Figure 9: Illustration of case \(s\neq c\) in the proof of Lemma 6.2. Vertices in T-H<sub>0</sub> have both _r_ and _s_ as ancestors.


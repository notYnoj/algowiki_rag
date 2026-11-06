Therefore,

\(\sum_{F\in\mathcal{F}F\cap E(H'_1)\in\mathcal{F}_1^k}y_F=\sum_{F^\prime\in\mathcal{F}_1^k}y(H'_1)_{F^\prime}\)<br>
\(=\sum_{F^\prime\in\mathcal{F}_1^k}\sum_{F\in\mathcal{F}F\cap E(H'_1)=F^\prime} y_F<R_{(\mathcal{G},2w,p)}^k+\epsilon.\)

Note that \(A_c\subseteq\{F\in\mathcal{F}|F\cap E(H'_1)\in\mathcal{F}_1^k\}\). Consider instead

\(A'_a=\{F\in\mathcal{F}|F\cap E(P_{u_1})=\varnothing\}.\)

Then \(A'_a\subseteq\{F\in\mathcal{F}|F\cap E(H'_1)\in\mathcal{F}_1^k\}\) and \(A_c\cap A'_a=\varnothing\). Moreover, since \(\mathcal{F}=A'_a\dot{\cup}\{F\in\mathcal{F}|F\cap E(P_{u_1})\neq\varnothing\}\), we obtain, by applying the edge bound along the path _P_<sub>_u_<sub>1</sub></sub>,<tbc>

\(\sum_{\{F\in\mathcal{F}|F\cap E(P_{u_1})\neq\varnothing\}}y_F\le\sum_{e\in E(P_{u_1})}\sum_{F\in\mathcal{F}e\in F}y_F\le\frac{w}{2}p=\frac{w\cdot p}{2}.\)

<tbc>Hence, since<tbc>

\(1=\sum_{F\in\mathcal{F}}y_F=\sum_{F\in A'_a}y_F+\sum_{\{F\in\mathcal{F}|F\cap E(P_{u_1})\neq\varnothing\}}y_F,\)

<tbc>we conclude<tbc>

\(\sum_{F\in A'_a}y_F\ge 1-\frac{w\cdot p}{2}.\)

<tbc>Consequently,

\(\sum_{F\in A_c}y_F\le\sum_{F\in\mathcal{F}F\cap E(H'_1)\in\mathcal{F}_1^k}y_F-\sum_{F\in A'_a}y_F\)<br>
\(<R_{(\mathcal{G},2w,p)}^k+\epsilon-\left(1-\frac{w\cdot p}{2}\right).\)

Combining (18), (19), (20), we conclude

\(\sum_{F\in A_a\cup A_b\cup A_c\cup A_d}y_F\le 2\left(w\cdot p-1\right)+2\big(R_{(\mathcal{G},2w,p)}^k+\epsilon-(1-\frac{w\cdot p}{2})\big)=3w\cdot p+2R_{(\mathcal{G},2w,p)}^k+2\epsilon-4.\text{(21)}\)

Let \(A^*=A\backslash(A_a\cup A_b\cup A_c\cup A_d)\). Using (17) and (21), we get

\(\sum_{F\in A^*}y_F=\sum_{F\in A}y_F-\sum_{F\in A_a\cup A_b\cup A_c\cup A_d}y_F\ge R_{(\mathcal{G},2w,p)}^k-\left[3w\cdot p+2R_{(\mathcal{G},2w,p)}^k+2\epsilon-4\right]=(4-2\epsilon)-3w\cdot p-R_{(\mathcal{G},2w,p)}^k.\)

By the upper bound in Definition 6, we have \(R_{(\mathcal{G},2w,p)}^k\le\frac{w\cdot p}{2}\) . Therefore,

\(\sum_{F\in A^*}y_F\ge(4-2\epsilon)-3w\cdot p-\frac{w\cdot p}{2}=(4-2\epsilon)-\frac{7}{2}w\cdot p>0,\)

where the last inequality uses the assumption \(w\cdot p<\frac{8}{7}-\frac{4\epsilon}{7}\) . Thus \(A^*\neq\varnothing\), so there exists \(F\in A^*\subseteq A\) with _y<sub>F</sub>\>_0 such that \(F\cap E(P_a)=F\cap E(P_b)=\varnothing\) and \(F\cap E(H'_i)\notin\mathcal{F}_i^k\) for _i_=1,2, completing the proof.


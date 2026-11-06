The bound of Lemma 4.15 has two cases which naturally correspond to whether the maximum is at the boundary of \[0,1\]<sup>3</sup> or in the interior. If \(c(a+b)\le ab\), then the maximum is attained at the vertex (0,1,1) of _Q_. If _c(a+b)\>ab_, the the maximum is attained on the curved part of the boundary.

**Remark 4.16.** The set \(\Delta_\mathbb{F}^\mathfrak{m}\) is invariant under permuting the coordinates (Lemma 4.3(v)), so the convex hull of \(\mathrm{log}\Delta_\mathbb{F}^\mathfrak{m}\) (and therefore _Q_) contains \(\frac{\omega_\mathbb{F}}{3}(1,1,1)\). Whether \(\frac{\omega_\mathbb{F}}{3}(1,1,1)\) lies in \(\mathrm{log}\Delta_\mathbb{F}^\mathfrak{m}\) is not known. See also Figure 4.

## 4.6 Rectangular matrix multiplication

In this subsection we will deduce Theorem 1.2 from Proposition 4.14 and Lemma 4.4. We state it again for convenience of the reader.

**Theorem 1.2.** _For every field_ F _and all real numbers_ \(a\ge b\ge c\ge 0\),

\(\omega_\mathbb{F}(a,b,c)\le\left\{\begin{array}{ c c }
a+b & \text{\textit{if}}c(a+b)\le ab, \\
\frac{(ab+bc+ca)^2}{4abc} & \text{\textit{if}}c(a+b)>ab,
\end{array}\right.\)

_with equality if_ \(c(a+b)\le ab\).

The value \(\omega_\mathbb{F}(a,b,c)\) does not depend on the order of _a_, _b_ and _c_, since permuting the legs does not change the tensor rank (Lemma 2.1(v)). If \(a\ge b\ge c\), then \(\omega_\mathbb{F}(a,b,c)\ge a+b\), since the tensor rank of \(\langle n_1,n_2,n_3\rangle\) is at least \(\mathrm{R}_{(1)}(\langle n_1,n_2,n_3\rangle)=n_1n_2\).

_Proof of Theorem 1.2._ Let \(\phi\in\Delta_\mathbb{F}\). Let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be the logarithms of \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) and \(\phi(\langle 1,2,1\rangle)\). By taking the logarithm of the equality in Lemma 4.4, we see it is sufficient to upper bound _ap_<sub>2</sub>+_bp_<sub>3</sub>+_cp_<sub>1</sub>. Because \(p_1,p_2,p_3\in[0,1]\) (Lemma 4.3(iv)), the logarithm of the inequality of Proposition 4.14 is the hypothesis of Lemma 4.15 for _w_=(_p_<sub>1</sub>_,p_<sub>2</sub>_,p_<sub>3</sub>). This shows the desired upper bound. Equality in the first case follows from the lower bound \(\omega_\mathbb{F}(a,b,c)\ge a+b\), obtained from evaluating the flattening rank R<sub>(1)</sub>.

(0,1,1)
(0,1,1)
W3
W3
(1,1,1)
(1,1,1)
3
(1,0,1)
2
3
(1,1,1)
(1,0,1)
4
W2
W2
(0,0,0)
(0,0,0)
(1,1,0)
(1,1,0)
W1
W1

Figure 4: \(P\subseteq\mathrm{log}\Delta_\mathbb{F}^\mathfrak{m}\subseteq Q\cap\{w:w_1+w_2+w_3\ge 2\}\), for the triangle _P_ on the left, given by Strassen’s support functionals, and the part of _Q_ with \(w_1+w_2+w_3\ge 2\) on the right, shown with level curves of _w_<sub>1</sub>+_w_<sub>2</sub>+_w_<sub>3</sub>. Of course we do not know the position of \(\frac{\omega_\mathbb{F}}{3}(1,1,1)\), but it is on the line between \(\frac{2}{3}(1,1,1)\) and \(\frac{3}{4}(1,1,1)\).


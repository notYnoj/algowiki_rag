Since _tp<sub>i</sub>(x<sub>j</sub>+x<sub>k</sub>_)=4_p<sub>i</sub>x<sub>j</sub>x<sub>k</sub>/S_, we obtain<tbc>

\(R_\sigma(a)^{x_k}R_{\sigma\circ(23)}(a)^{x_j}\ge\big(\frac{n+2}{n+1}\big)^{4p_ix_jx_k/S}.\)

<tbc>If _p<sub>i</sub>_=0, this lower bound holds as well, since the left-hand side is at least 1: \(\phi_\sigma\) and \(\phi_{\sigma\circ(23)}\) are nondecreasing in the second argument (Lemma 4.10(i)). Multiplying over the three pairs and the two values of _a_ gives

\(\frac{G_{n+1}}{G_n}\ge\big(\frac{n+2}{n+1}\big)^{8B/S},\text{so}G_n\ge\big(\frac{n+1}{2}\big)^{8B/S},\)

where we multiply these inequalities and use \(G_1\ge 1\). With the upper bound on _G<sub>n</sub>_, this gives \(((n+1)/2)^{8B/S}\le(nS)^{2S}\) for every integer \(n\ge 1\). Hence \(8B/S\le 2S\), that is, \(4B\le S^2\).

Proposition 4.14 gives an "outer approximation" of the asymptotic spectrum of rectangular matrix multiplication, which we plot in Figure 4. To explain this, let<tbc>

\(\Delta_\mathbb{F}^\mathfrak{m}:=\big\{\big(\phi(\langle 1,1,2\rangle),\phi(\langle 2,1,1\rangle),\phi(\langle 1,2,1\rangle)\big):\phi\in\Delta_\mathbb{F}\big\}\subseteq[1,2]^3\)

<tbc>(Lemma 4.3(iv)), and let \(log\Delta_\mathbb{F}^\mathfrak{m}\subseteq[0,1]^3\) be its image under the logarithm in each coordinate. The flattening ranks R<sub>(1)</sub>, R<sub>(2)</sub> and R<sub>(3)</sub> give the points<tbc>

\(\{(0,1,1),(1,0,1),(1,1,0)\}\subseteq log\Delta_\mathbb{F}^\mathfrak{m},\)

<tbc>and Strassen’s support functionals give the triangle with these vertices \[Str91, Section 6\],<tbc>

\(P:=conv\{(0,1,1),(1,0,1),(1,1,0)\}\subseteq log\Delta_\mathbb{F}^\mathfrak{m}.\)

<tbc>Strassen showed that \(log\Delta_\mathbb{F}^\mathfrak{m}\) lies in the truncated pyramid \(\{w\in[0,1]^3:2\le w_1+w_2+w_3\le\omega_\mathbb{F}\}\) over _P_ \[Str88, Proposition 4.2\]. By Proposition 4.14, we have

\(log\Delta_\mathbb{F}^\mathfrak{m}\subseteq Q:=\big\{w\in[0,1]^3:\forall x\in\mathbb{R}_{\ge 0}^3,4(w_1x_2x_3+w_2x_1x_3+w_3x_1x_2)\le(x_1+x_2+x_3)^2\big\}.\) (4.4)

So \(P\subseteq log\Delta_\mathbb{F}^\mathfrak{m}\subseteq Q\cap\{w:w_1+w_2+w_3\ge 2\}\), and these are the best inner and outer approximations of \(log\Delta_\mathbb{F}^\mathfrak{m}\) that we currently know.

On _Q_, we have \(w_1+w_2+w_3\le\frac{9}{4}\), by the choice _x_<sub>1</sub>=_x_<sub>2</sub>=_x_<sub>3</sub>=1, with equality at \(\frac{3}{4}(1,1,1)\). Since the maximum of _w_<sub>1</sub>+_w_<sub>2</sub>+_w_<sub>3</sub> on \(log\Delta_\mathbb{F}^\mathfrak{m}\) is \(\omega_\mathbb{F}\) (Theorem 4.2 and Lemma 4.3(iv)), this gives Theorem 1.1 again.

Likewise, for real numbers \(a\ge b\ge c\ge 0\), the maximum of _aw_<sub>2</sub>+_bw_<sub>3</sub>+_cw_<sub>1</sub> on _Q_ is as follows:

**Lemma 4.15.** _Let_ \(a\ge b\ge c\ge 0\) _be real numbers, and let_ \(w\in[0,1]^3\) _with_ 4(_w_<sub>1</sub>_x_<sub>2</sub>_x_<sub>3</sub>+_w_<sub>2</sub>_x_<sub>1</sub>_x_<sub>3</sub>+_w_<sub>3</sub>_x_<sub>1</sub>_x_<sub>2</sub>)\(\le(x_1+x_2+x_3)^2\) _for all_ \(x\in\mathbb{R}_{\ge 0}^3\)_. Then_<tbc>

\(aw_2+bw_3+cw_1\le\left\{\begin{array}{ c c }
a+b & \text{\textit{if}}c(a+b)\le ab, \\
\frac{(ab+bc+ca)^2}{4abc} & \text{\textit{if}}c(a+b)>ab.
\end{array}\right.\)

<tbc>_Proof._ If _a_=0, then _a=b=c_=0, and the claim holds. So let _a\>_0. With _x_=(_ab,bc,ca_), the left-hand side of the hypothesis is 4_abc(aw_<sub>2</sub>+_bw_<sub>3</sub>+_cw_<sub>1</sub>), and at _c=ab/(a+b_), where the two cases meet, this vector _x_ is a multiple of (_a+b,b,a_). If \(c(a+b)\le ab\), then, since \(w_1\ge 0\),

\((a+b)(aw_2+bw_3+cw_1)\le(a+b)(aw_2+bw_3)+abw_1\le(a+b)^2,\)

where the second inequality is the hypothesis with (_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>)=(_a+b,b,a_). Dividing by _a+b_ gives the claim. If _c(a+b)\>ab_, then _abc\>_0, and the hypothesis with (_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>)=(_ab,bc,ca_) gives \(4abc(aw_2+bw_3+cw_1)\le(ab+bc+ca)^2\).


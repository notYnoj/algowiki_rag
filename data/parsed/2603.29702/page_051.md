Thus (25) holds since \(\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{(r-l)-|p(r)-p(l)|}=o\left(\frac{1}{M^3}\right)\).

**Step I:** _p<sub>s</sub>(m<sub>i</sub>_) **is not far from** <o>_y_</o><sub>i</sub> Note that for \(a,b\in\mathbb{R}\) and \(c\in\mathbb{R}^+\), if _c|a_ and \(\widehat{b}\) is _b_ rounded to the closest multiple of _c_, then \(\left|a-\widehat{b}\right|\le 2|a-b|\). Since \(I_{s-1}/\phi_y|p_s(m_i)\), we must have

\(\left|p_s(m_i)-(I_{s-1}/\phi_y)\cdot\left|\frac{p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}}{I_{s-1}/\phi_y}\right|\right|\le 2\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|.\) (26)

Plugging (25) (with \(i'=i\cdot M^2\)) to the right-hand side of (26), we have that indeed,<tbc>

\(|p_s(m_i)-\overline{y_i}|=o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\)

<tbc>**Step II:** _p<sub>s</sub>(m<sub>i</sub>-I_<sub>_s_-3</sub>) **is not far from** _p<sub>s</sub>(m<sub>i</sub>_) From (25) we have that

\(\left|p_s(m_i-I_{s-3})-\left(p_s(l)+\left(i\cdot M^2-1\right)\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|=o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\) (27)

((_m<sub>i</sub>-I_<sub>_s_-3</sub>) is the \((i\cdot M^2-1)\)-th _M_<sup>3</sup>-way anchor) and that

\(\left|p_s(m_i)-\left(p_s(l)+i\cdot M^2\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|=o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right).\) (28)

((_m<sub>i</sub>_) is the \((i\cdot M^2)\)-th _M_<sup>3</sup>-way anchor).

Note that for \(a,b,c,d\in\mathbb{R}\), we have \(|a-b|\le|a-c|+|c-d|+|b-d|\) due to triangle inequality. Particularly, this is true for

• _a=p<sub>s</sub>(m<sub>i</sub>-I_<sub>_s_-3</sub>);<tbc>

• _b=p<sub>s</sub>(m<sub>i</sub>_);<tbc>

• \(c=\left(p_s(l)+\left(i\cdot M^2-1\right)\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\);<tbc>

• \(d=\left(p_s(l)+i\cdot M^2\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\).<tbc>

<tbc>From (27) (for |_a-c_|) and (28) (for |_b-d_|), we have that indeed

\(|p_s(m_i-I_{s-3})-p_s(m_i)|\le o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)+\frac{(p_s(r)-p_s(l))}{M^3}+o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\)<br>
\(\le\frac{(p_s(r)-p_s(l))}{M^3}+o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\)

**Claim 7.6** (Restated)**.** _Let p be the path in Lemma 7.3. For a random column x such that the weight of p before x is non-zero, with probability_ \(1-o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\)_, every interval_ \((l,r]\unknown x\) _on an active scale satisfies the following bound:_

\(\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{(r-l)-|p(r)-p(l)|}=o\left(\frac{1}{M^3}\right),\) (24)

_which is the requirement in Claim 7.5 with p<sub>s</sub> replaced by p._


Note that for \(a,b\in\mathbb{R}\) and \(c\in\mathbb{R}^+\), if _c|a_ and \(\widehat{b}\) is _b_ rounded to the closest multiple of _c_, then \(\left|a-\widehat{b}\right|\le 2|a-b|\). For every _i_, since \((I_{s-1}/\phi_y)|p_s(m_i)\), we must have

\(\left|p_s(m_i)-(I_{s-1}/\phi_y)\cdot\left[\frac{p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}}{I_{s-1}/\phi_y}\right]\right|\le 2\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|.\)

Thus to show (10), it suffices to show that

\(\sum_{1\le i<M}\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|=O(MT\mathrm{D}_M(\Delta p_s(l,r])).\) (11)

By telescoping, we have

\(\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|=\left|\left(p_s(l)+\sum_{j\le i}\left(p_s(m_j)-p_s(m_{j-1})\right)\right)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|.\)

The two _p<sub>s</sub>(l_) terms cancel out, thus

\(\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|=\left|\left(\sum_{1\le j\le i}\left(p_s(m_j)-p_s(m_{j-1})\right)\right)-i\cdot\frac{p_s(r)-p_s(l)}{M}\right|\)<br>
\(=\left|\sum_{1\le j\le i}\left(p_s(m_j)-p_s(m_{j-1})-\frac{p_s(r)-p_s(l)}{M}\right)\right|\)<br>
\(\le\sum_{1\le j\le i}\left|p_s(m_j)-p_s(m_{j-1})-\frac{p_s(r)-p_s(l)}{M}\right|\)<br>
\(\le\sum_{1\le j\le M}\left|p_s(m_j)-p_s(m_{j-1})-\frac{p_s(r)-p_s(l)}{M}\right|\)<br>
\(=\mathrm{TD}_M(\Delta p_s(l,r]).\) (12)

Now that we have the bound (12) on every summand we can easily deduce (11):

\(\sum_{1\le i<M}\left|p_s(m_i)-\left(p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}\right)\right|\le\sum_{1\le i<M}\mathrm{TD}_M(\Delta p_s(l,r])\)<br>
\(=O(MT\mathrm{D}_M(\Delta p_s(l,r]))\)

The following ingredient is important towards proving our main regularity lemma:

**Lemma 6.5** (Deviation and weight bounds for arbitrary paths)**.** _Let_ \(p'\) _be any path from_ \(\langle 0,n_X\rangle\) _to_ \(\langle n_X+n_Y,n_Y\rangle\) _on the Sparsified Rotated Edit Distance Grid Graph. Then:_

\(\sum_i\left|(\Delta p')_i\right|\le w(p'),\) (13)


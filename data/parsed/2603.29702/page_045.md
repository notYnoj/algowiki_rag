must also have \(max_{1\le i\le M}w(\overline{p_{m_{i-1},m_i}})=\omega\left(\frac{w(\overline{p_{l,r}})}{M}\right)\). Let \(i'\) be the maximizier of \(w(\overline{p_{m_{i^\prime-1},m_{i^\prime}}})\). We have

\(\mathrm{TD}_M(W(\overline{p_{l,r}}))=\sum_{1\le i\le M}\left|w(\overline{p_{m_{i-1},m_i}})-\frac{w(\overline{p_{l,r}})}{M}\right|\)<br>
\(\ge\left|w(\overline{p_{m_{i^\prime-1},m_{i^\prime}}})-\frac{w(\overline{p_{l,r}})}{M}\right|\)<br>
\(=\left|\omega\left(\frac{w(\overline{p_{l,r}})}{M}\right)-\frac{w(\overline{p_{l,r}})}{M}\right|\)<br>
\(=\omega\left(\frac{w(\overline{p_{l,r}})}{M}\right)\)

### If we do not give up, we obtain a good estimate

Notice that

• For every sub-interval, \(\mathrm{est}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\le\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\);<tbc>

• For the parent interval, \(\mathrm{appr}[l,y_l,r,y_r]=O(w(\overline{p_{l,r}}))\).

If \(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\le\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)\), then for every sub-interval, \(\mathrm{est}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=O\left(\frac{w(\overline{p_{l,r}})}{M}\mathrm{loglog}(n)\right)\). By applying Hoeffding’s Inequality (Lemma 3.1, with \(c:=O\left(\frac{w(\overline{p_{l,r}})}{M}\mathrm{loglog}(n)\right)\) and \(\delta:=\frac{w(\overline{p_{l,r}})\mathrm{loglog}(n)}{\mathrm{log}^{0.03}(n)}=o\left(\frac{w(\overline{p_{l,r}})}{\mathrm{log}^{0.02}(n)}\right)\)), we obtain that

\(\left|2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]-\sum_{i=1}^M\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\right|=o\left(\frac{w(\overline{p_{l,r}})}{\mathrm{log}^{0.02}(n)}\right)\)

holds except with probability \(\mathrm{exp}\left(-\Omega\left(M/\mathrm{log}^{0.06}(n)\right)\right)=\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\).

## 7 Algorithm for LCS

In this section, we present our algorithm for LCS:

**Theorem 7.1.** _For any constant_ \(\varepsilon>0\)_, there exists a randomized algorithm that runs in time_

\(\frac{n^2}{2^{\mathrm{log}^{\Omega(1)}(n)}}\)

_and, with high probability, computes a_ \((1-\varepsilon)\)_-approximation for the longest common subsequence of two strings with total length n._

Our algorithm solves the query-based algorithm on the sparsified grid introduced in Section 5.2.

**Definition 5.7** (Restated)**.** The Sparsified LCS Grid Graph is defined given the following parameters:

• Rounding threshold for columns: \(\mathcal{B}_x:=n/M^S=\widetilde{\Theta}(n^{0.99})\);<tbc>

• Length-relative rounding factor for rows: \(\phi_y:=2^{\left\lfloor\mathrm{log}^{0.009}(n)\right\rfloor}\).<tbc>


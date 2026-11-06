**Upper bound** \(\text{\textit{EstSUM}}(A_I)\le\left(1+O\left(1/\mathrm{log}^{0.02}(n)\right)\right)\sum_{i=1}^Ma_i\);

**Lower bound if there are no outliers** _Let the true mean of A be_ \(\overline{A}:=\sum_ia_i/M\)_. If we have_ \(\mathrm{max}_ia_i\le\mathrm{log}^{0.02}(n)\overline{A}\)_, then_

\(\text{\textit{EstSUM}}(A_I)\ge\left(1-O\left(1/\mathrm{log}^{0.02}(n)\right)\right)\cdot\left(\sum_{i=1}^Ma_i\right).\)

**Algorithm 2** Computation of EstSUM(_A<sub>I</sub>_) via Clipping

1: **function** EstSUM(_A<sub>I</sub>_)

• **requirement 1:** \(I\subset[M]\) is a uniformly randomly chosen subset of _M/_2 indices

• **requirement 2:** _A<sub>I</sub>_ is the sub-sequence \((a_i)_{i\in I}\) of length-_M_ sequence _A_ of non-negative numbers

• **returns:** an estimate of \(\sum_{i=1}^Ma_i\) satisfying the conditions in Claim 7.8

2: \(\widetilde{A}\leftarrow\sum_{i\in I}a_i/\left(\frac{M}{2}\right)\)

3: **return** \(2\sum_{i\in I}\mathrm{min}\left(a_i,2\mathrm{log}^{0.02}(n)\widetilde{A}\right)\)

Using the sub-routine in Claim 7.8, we compute the estimate in the following way:

\(\mathrm{est}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{max}_{\widehat{Y}\in\text{\textbf{✓}}}\sum_{i=1}^M\mathrm{est}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S}, \\
\text{EstSUM}\left((\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}])_{i|\eta_{l,r,i}=1}\right), & \text{if}s\in\widetilde{S}
\end{array}\right.\)

To efficiently maximize over anchor path \(\widehat{Y}\) on passive scale _s_, consider the following "Scale-(_s_-1) Sparsified Grid Graph":

**Definition 7.9** (Scale-(_s_-1) Sparsified Grid Graph)**.** The Scale-(_s_-1)-Sparsified Grid Graph defined on est is as follows:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified LCS Grid Graph with the additional constraint that _I_<sub>_s_-1</sub>|_x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_{s-1},y'\rangle\) (if both exist) such that \(|y'-y|\le I_{s-1}\) with a weight of \(\mathrm{est}[x,y,x+I_{s-1},y']\).

To obtain \(\mathrm{max}_{\widehat{Y}\in\text{\textbf{✓}}}\sum_{i=1}^M\mathrm{est}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i]\), we can simply find the longest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path.

We give the full pseudocode for computing est in Algorithm 3. We use the memoization technique to compute est values on demand (i.e., Line 12-13 and Line 22-23).

## 7.3 Algorithm Analysis

### 7.3.1 Overview

Our goal is to use our algorithm to prove Lemma 7.7:


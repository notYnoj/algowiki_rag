<tbc>We may also fix \(b\ge 2\) and let _Z_<sub>1</sub>=_X_<sub>1</sub>_,...,X<sub>b</sub>_, _Z_<sub>2</sub>=_X_<sub>_b_+1</sub>_,...,X_<sub>2_b_</sub>, _..._. In this case, one gets that lower bounding _B<sub>n</sub>(n_) amounts to finding \(w_1,w_2\in\{0,1\}^b\) and \(\delta>0\) such that for all \(n\ge 1\),

\(\frac{1}{n}\sum_{j=1}^n\left(\mathbb{E}\left(LCS(Z^{j,w_1})-LCS(Z^{j,w_2})\right)\right)^2\ge\delta.\)

For example, intuitively, it is likely to get a larger LCS with _w_<sub>1</sub>=(1,0) than with _w_<sub>2</sub>=(1,1), and with _w_<sub>1</sub>=(1,0,1,0,1) than with _w_<sub>2</sub>=(1,1,1,1,1). Running simulations in Python, Figure 1 seems to indicate that _B<sub>n</sub>(n_) is lower bounded by a strictly positive constant (which would yield the linearity of the variance).

We now pick again _Z_<sub>1</sub>=_X_<sub>1</sub>_,Z_<sub>2</sub>=_X_<sub>2</sub>_,...,Z_<sub>2_n_</sub>=_Y<sub>n</sub>_, and study _B_<sub>1</sub>(2_n_). Note that if _B_<sub>1</sub>(2_n_) was converging to zero, this would rule out the possibility of a linear lower bound on the variance. In the following, we study _B_<sub>1</sub>(2_n_), and find that it is lower bounded by a constant.

Let _X_<sub>1</sub>_,...,X<sub>n</sub>,Y_<sub>1</sub>_,...,Y<sub>n</sub>_ be independent Bernoulli random variables with parameter 1/2, and let \(\upsilon\le n\). We may assume, for ease of notations, that \(n=\upsilon m\) is a multiple of \(\upsilon\), but it is not hard to adapt all the following proofs to the general case. Let \(\mathcal{R}:=\left\{\overrightarrow{r}\in\mathbb{N}^m:1=r_0\le r_1\le\cdots\le r_m=n\right\}\), and, for any \(\overrightarrow{r}\in\mathcal{R}\), let

\(LC_n(\overrightarrow{r})=\sum_{i=0}^{m-1}LCS\left(P_i\right),\)

where \(P_i:=\left((X_{\upsilon i+1},\dots,X_{(\upsilon+1)i}),(Y_{r_i},\dots,Y_{r_{i+1}-1})\right)\) (with the convention \((Y_{r_i},\dots,Y_{r_{i+1}-1})=\emptyset\) if _r<sub>i</sub>=r_<sub>_i_+1</sub>). For any \(\overrightarrow{r}\in\mathcal{R}\), call \(\overrightarrow{r}\) an alignment if \(LC_n=LC_n(\overrightarrow{r})\).

Denote by _N<sub>i</sub>_ the number of letters in the cell _P<sub>i</sub>_, that is \(\upsilon+r_{i+1}-r_i\). For any \(\overrightarrow{r}\in\mathcal{R}\), let \(I_{p_1,p_2}(\overrightarrow{r})=\{i\in\{0,\dots,m-1\};r_{i+1}-r_i\in[\upsilon p_1,\upsilon p_2]\}\), and \((I_{p_1,p_2}(\overrightarrow{r}))^c\) its complement in {0_,...,m_-1}. Next, let \(B_{\varepsilon,p_1,p_2}^n\) be the event that: for any alignment \(\overrightarrow{r}\),<tbc>

\(\sum_{i\in I_{p_1,p_2}(\overrightarrow{r})}N_i\ge\left(1-\frac{\varepsilon}{2}\right)2n.\)

<tbc>Note that, recalling the notation \(A_{\varepsilon,p_1,p_2}^n\) as defined in \[14\], we have \(B_{\varepsilon,p_1,p_2}^n\subset A_{\varepsilon,p_1,p_2}^n\). Indeed, if \(A_{\varepsilon,p_1,p_2}^n\) is not satisfied, there is an alignment \(\overrightarrow{r}\) (in \[14\], the definition of an alignment is with strict inequalities rather than our non-strict inequalities, therefore an alignment as defined in \[14\] is necessarily also an alignment as defined here) such that the cardinality of \(I_{p_1,p_2}(\overrightarrow{r})\) is strictly greater than \(\varepsilon m\), which implies

\(\sum_{i\in(I_{p_1,p_2}(\overrightarrow{r}))^c}N_i>\nu\varepsilon m\)<br>
\(>\varepsilon n,\)

hence \(\sum_{i\in I_{p_1,p_2}(\overrightarrow{r})}N_i<2n-\varepsilon n\), indicating that \(B_{\varepsilon,p_1,p_2}^n\) is not satisfied. Hence \(B_{\varepsilon,p_1,p_2}^n\subset A_{\varepsilon,p_1,p_2}^n\), and \(\mathbb{P}\left(B_{\varepsilon,p_1,p_2}^n\right)\le\mathbb{P}\left(A_{\varepsilon,p_1,p_2}^n\right)\). Therefore, the following is a strengthening of \[14, Theorem 2.2\] (which is the same statement but with \(A_{\varepsilon,p_1,p_2}^n\) in place of \(B_{\varepsilon,p_1,p_2}^n\)).

1.0
0.05
0.8
0.04
0.6
0.03
Bn(m)
0.4
0.02
0.01
0.2
0.00
0.0
0
100
200
300
400
500
0
25
50
75
100
125
150
175
200
number of blocks n
number of blocks n

Figure 1: _B<sub>n</sub>(n_) for _w_<sub>1</sub>=(1,0)_,w_<sub>2</sub>=(1,1) (left), and _w_<sub>1</sub>=(1,0,1,0,1), _w_<sub>2</sub>=(1,1,1,1,1) (right), with the empirical measure over 1000 simulations.


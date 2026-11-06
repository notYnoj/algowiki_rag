Let \((\pi,\eta)\) be the alignment of (_X_<sub>1</sub>_,...,X_<sub>_n_-1</sub>),(_Y_<sub>1</sub>_,...,Y<sub>n</sub>_) which is minimal for the lexicographic order, so \((\pi,\eta)\) is well defined as a (measurable) function of _X_<sub>1</sub>_,...,X_<sub>_n_-1</sub>_,Y_<sub>1</sub>_,...,Y<sub>n</sub>_. Let _F<sub>n</sub>_ be the event "\(\eta_{LC_n}<n\)", in other words, _Y<sub>n</sub>_ does not contribute to the longest common subsequences, then \(\sum_{i=1}^n\Delta_nLC_n^{X_n=\alpha_i,X_n^\prime=\alpha_{m+1}}\ge\mathbb{1}_{F_n}\), hence

\(\mathbb{E}(LC_n)-\mathbb{E}(LC_{n-1,n})\ge p_{X,\mathrm{min}}\mathbb{P}(F_n),\) (4.5)

where \(p_{X,\mathrm{min}}:=\mathrm{min}_{1\le i\le m}p_{X,i}\).

We now combine this bound with some elements already present in \[12\] (with its notations). Let \(V_1=\pi_1-1,V_2=\pi_2-\pi_1-1,\dots,V_{LC_n}=\pi_{LC_n}-\pi_{LC_n-1}-1\), and let _M_ be the number of indices _i_ such that _V<sub>i</sub>\>_0. In terms of \[12\], _M_ is the number of nonempty matches (except that there is also the term _V_<sub>1</sub>). We denote by _I<sub>i,j</sub>_ the event: "inserting \(\alpha_i\) at the _j_-th position in (_X_<sub>1</sub>_,...,X_<sub>_n_-1</sub>),(_Y_<sub>1</sub>_,...,Y<sub>n</sub>_) increases the longest common subsequence". Observe that

\(\mathbb{E}(LC_n)-\mathbb{E}(LC_{n-1,n})=\mathbb{E}\left(LCS(X_1\cdots X_{j-1}X'_1X_j\cdots X_{n-1};Y_1\cdots,Y_n)-LCS(X_1\cdots X_{n-1};Y_1\cdots Y_n)\right)\)<br>
\(=\sum_{i=1}^mp_{X,i}\mathbb{P}(I_{i,j})\)<br>
\(=\frac{1}{n}\sum_{j=1}^n\sum_{i=1}^mp_{X,i}\mathbb{P}(I_{i,j})\)<br>
\(\ge\frac{p_{X,\mathrm{min}}}{n}\mathbb{E}\sum_{j=1}^n\sum_{i=1}^mI_{i,j}\)<br>
\(\ge p_{X,\mathrm{min}}\frac{\mathbb{E}M}{n}.\) (4.6)

From (4.5) and (4.6), we get

\(\mathbb{E}(LC_n)-\mathbb{E}(LC_{n-1,n})\ge\frac{p_{X,\mathrm{min}}}{2}\left(\mathbb{P}(F_n)+\frac{\mathbb{E}M}{n}\right).\) (4.7)

Let \(\gamma^*\) be the limit of E(_LC<sub>n</sub>)/n_, we have \(\gamma^*\le 1-p<1\), i.e., \(0<p<1-\gamma^*\). Fix _k_<sub>0</sub>_\>_0 such that<tbc>

\(\sum_{k>k_0}mk(1-p_{Y,\mathrm{min}})^k\le\frac{1-\gamma^*}{2}.\)

<tbc>When _F<sub>n</sub>_ does not hold, that is, when \(\pi_n=LC_n\), we have<tbc>

\(\sum_{i=1}^{LC_n}V_i=n-LC_n,\)

<tbc>so<tbc>

\(\mathbb{E}\left(\sum_{i=1}^{LC_n}V_i\right)\ge\mathbb{E}\left((n-LC_n)\mathbb{1}_{F_n^c}\right)\ge\mathbb{E}\left(n-LC_n\right)-\mathbb{P}(F_n)n\ge(1-\gamma^*)n-\mathbb{P}(F_n)n.\)

<tbc>Moreover,<tbc>

\(k_0\mathbb{E}M\ge\mathbb{E}\left(\sum_{i=1}^{LC_n}V_i\mathbb{1}_{V_i\le k_0}\right).\)

<tbc>On the other hand, \((\pi,\eta)\) is minimal, so any unmatched gap has (at least) a letter of the alphabet which is not used, namely, the letter used in the next match. Therefore the average number of indices _i_ such that _V<sub>i</sub>=k_ is no more than _nm_(1-_p_<sub>_Y,_min</sub>)_<sup>k</sup>_, and<tbc>

\(\mathbb{E}\left(\sum_{i=1}^{LC_n}V_i\mathbb{1}_{V_i>k_0}\right)\le n\sum_{k>k_0}mk(1-p_{Y,\mathrm{min}})^k\le\frac{1-\gamma^*}{2}n.\)

<tbc>Finally we get<tbc>

\(k_0\mathbb{E}M\ge\frac{1-\gamma^*}{2}n-\mathbb{P}(F_n)n,\)

<tbc>and<tbc>

\(\mathbb{P}(F_n)+\frac{\mathbb{E}M}{n}\ge\frac{k_0\mathbb{E}M+\mathbb{P}(F_n)n}{k_0n}\ge\frac{1-\gamma^*}{2k_0},\)


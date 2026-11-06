_Proof._ Suppose the true order is \(\sigma=(x_1,\dots,x_n)\). Let \(S=\{i\in[n]:(n/k)\nmid i\}\). Note that |_S_|=_n-n/k_. For \(i\in S\), define _W<sub>i</sub>_ to be the number of queries returning _x<sub>i</sub>\<x_<sub>_i_+1</sub>, minus the number of queries returning _x<sub>i</sub>\>x_<sub>_i_+1</sub>. Note that _W<sub>i</sub>_ is a random variable depending on the transcript. Define \(W=\sum_{i\in S}W_i\). Then E\[_W_\]=(1-2_p_)E\[_U_<sup>=</sup>\].

Let us consider the posterior probabilities _q_ of the permutations given a fixed transcript. That is, define<tbc>

\(q_\tau:=\mathbb{P}[\sigma=\tau|Q^m,Y^m].\)

<tbc>By Bayes’ rule, \(q_\tau\) equals \(\frac{\mathbb{P}[Q^m,Y^m|\sigma=\tau]\mathbb{P}[\sigma=\tau]}{\mathbb{P}[Q^m,Y^m]}\) . By symmetry, \(\mathbb{P}[\sigma=\tau]\) are equal for different \(\sigma\) and P\[_Q<sup>m</sup>,Y<sup>m</sup>_\] is constant as we fixed the transcript, so \(q_\tau\) is proportional to \(\mathbb{P}[Q^m,Y^m|\sigma=\tau]\). If \(\tau=(y_1,\dots,y_n)\), then \(\mathbb{P}[Q^m,Y^m|\sigma=\tau]\) equals<tbc>

\(\prod_{1\le i<j\le n}(1-p)^{(\#\text{queries returning}y_i<y_j)}.\prod_{1\le i<j\le n}p^{(\#\text{queries returning}y_i>y_j)}.\) (3)

<tbc>For \(i\in S\), consider the permutation \(\tau_i:=(x_1,\dots,x_{i-1},x_{i+1},x_i,x_{i+2},\dots,x_n)\). Then by comparing \(q_{\tau_i}\) and \(q_\sigma\) using (3), we have

\(\frac{q_\sigma}{q_{\tau_i}}=\frac{(1-p)^{(\#\text{queries returning}x_i<x_{i+1})}p^{(\#\text{queries returning}x_i>x_{i+1})}}{(1-p)^{(\#\text{queries returning}x_i>x_{i+1})}p^{(\#\text{queries returning}x_i<x_{i+1})}}\)<br>
\(=\left(\frac{1-p}{p}\right)^{(\#\text{queries returning}x_i<x_{i+1})}\left(\frac{1-p}{p}\right)^{-(\#\text{queries returning}x_i>x_{i+1})}\)<br>
\(=\left(\frac{1-p}{p}\right)^{W_i}.\)

Thus,

\(q_{\tau_i}=q_\sigma\cdot\left(\frac{1-p}{p}\right)^{-W_i}.\)

Summing over _S_, we have

\(\sum_{i\in S}q_{\tau_i}=q_\sigma\sum_{i\in S}\left(\frac{1-p}{p}\right)^{-W_i}\)<br>
\(\ge q_\sigma|S|\left(\frac{1-p}{p}\right)^{-W/|S|}.\)

Because the error probability is _o_(1), for any \(\epsilon>0\), with probability 1-_o_(1), \(q_\sigma\ge 1-\epsilon\). So

\(|S|\left(\frac{1-p}{p}\right)^{-W/|S|}\le\epsilon/(1-\epsilon)\)

with probability 1-_o_(1).

On the other hand, for any \(\delta>0\), if

\(\mathbb{E}[U^=]\le(1-\delta)\frac{|S|log|S|}{(1-2p)log\frac{1-p}{p}},\)


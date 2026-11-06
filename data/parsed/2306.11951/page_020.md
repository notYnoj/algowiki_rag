<tbc>Taking \(\lambda=np\), \(\eta=\frac{1-2p}{2p}\) in Equation (2) of Lemma A.6, we know that

\(\mathbb{P}(X\ge n/2)\le\left(\frac{e^\frac{1-2p}{2p}}{(1/2p)^{(1/2p)}}\right)^{np}\)<br>
\(=\left(2p\cdot exp(1-2p)\right)^{n/2}\)<br>
\(<exp\left(log(1/\delta)\cdot\frac{2(1-2p+log(2p))}{(1-2p)^2}\right)\)<br>
\(<\delta.\)

Here the last inequality uses the fact that \(\frac{(1-2p+log(2p))}{(1-2p)^2}<-1/2\) for all \(p\in[0,1/2)\). This shows that the final failure probability is bounded by \(\delta\) when the true elements are all 0.

Consider the second case where there exists at least a 1 in the original elements \(X_1,\cdots,X_K\). Without loss of generality, we assume that _X_<sub>1</sub>=1. Let X_<sup>i</sup>_ be the remaining list of elements at the beginning of _i_-th iteration. We let E_<sub>i</sub>_ be the event that the first element in X_<sup>i</sup>_ is 1 while the first element in X<sup>_i_+1</sup> is 0. This event only happens when the second element in X_<sup>i</sup>_ is 0 and gets more 1’s in the noisy queries than the first element. Let A denote the event that the only left element is 1 in the last round, we have

\(\mathbb{P}(\mathcal{A})\ge 1-\mathbb{P}\left(\bigcup_{i=1}^{\lceil log_2(K)\rceil}\mathcal{E}_i\right)\)<br>
\(\ge 1-\sum_{i=1}^{\lceil log_2(K)\rceil}\mathbb{P}(\mathcal{E}_i)\)<br>
\(\ge 1-\sum_{i=1}^{\lceil log_2(K)\rceil}\mathbb{P}(Y_i-X_i\ge 0),\)

where _X<sub>i</sub>∼B(n<sub>i</sub>,n<sub>i</sub>_(1-_p_)) and _Y<sub>i</sub>∼B(n<sub>i</sub>,n<sub>i</sub>p_), with \(n_i=\lceil\frac{4(2i-1)log(1/\delta)}{(1-2p)^2}\rceil\). Let _Z<sub>i</sub>=Y<sub>i</sub>-X<sub>i</sub>+n<sub>i</sub>_, we know that the random variable _Z<sub>i</sub>∼B_(2_n<sub>i</sub>,n<sub>i</sub>p_). Thus we have

\(\mathbb{P}(\mathcal{A})\ge 1-\sum_{i=1}^{\lceil log_2(K)\rceil}\mathbb{P}(Z_i\ge n_i)\)<br>
\(>1-\sum_{i=1}^{\lceil log_2(K)\rceil}\delta^{2(2i-1)}\)<br>
\(>1-\frac{\delta^2}{1-\delta^2}.\)

Following the same argument on Binomial distribution, we can upper bound the error probability under event A with \(\delta\). Thus the total failure probability is upper bounded by \(\delta+\delta^2/(1-\delta^2)<2\delta\) when \(\delta<1/2\).

□

## APPENDIX JPROOF OF THEOREM VI.1

### A. Lower Bounds

First, note that all our lower bounds for fixed-length can be adapted to variable-length by replacing _T_ with E\[_T_\]. The bound of mutual information in Fano’s inequality in Section D can be proven using the same argument as Lemma 27 in Gu and Xu (2023), and the divergence decomposition lemma (Lemma A.3) still holds for variable length due to Lemma 15 in Kaufmann et al. (2016).


Let X be the total number of columns before which the weights of _p_ and \(\widehat{p}\) differ. Then to prove the lemma we just need to show \(\mathcal{X}=o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) with probability at least 19/20. Let<tbc>

\(X_k:=\left\{\begin{array}{ c c }
\text{tr}\mathrm{TD}_{M,\{S-k+1\}}(\Delta p_{S-k+1}), & \text{if}S-k+1\in\widetilde{S} \\
0, & \text{if}S-k+1\notin\widetilde{S}
\end{array}\right.,\)

<tbc>which captures the additive error introduced on scale (_S-k_+1) due to Claim 6.4 (scaled by roughly a factor of 1_/M_). From Claim 6.4, We have \(\mathcal{X}=O\left(M\cdot\sum_{k\in[S]}X_k\right)\). Moreover, since each scale _s_ is added to \(\widetilde{S}\) with probability 1_/S_<sup>0.98</sup>, the expectation of _X<sub>k</sub>_, given _X_<sub>1_...k_-1</sub>, over whether \((S-k+1)\in\widetilde{S}\), is<tbc>

\(\mathbf{E}_{(S-k+1)\in\widetilde{S}}[X_k|X_1,\dots,X_{k-1}]=\frac{\text{tr}\mathrm{TD}_{M,\{S-k+1\}}(\Delta p_{S-k+1})}{S^{0.98}}=:Y_k.\) (15)

<tbc>Thus the random process \(Z_K=\sum_{k\le K}\left(X_k-Y_k\right)\) is a martingale over the randomness of \(\widetilde{S}\) and we have<tbc>

\(\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}X_k\right]=\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}Y_k\right].\) (16)

<tbc>Now we can write out the following equation for \(\mathbf{E}_\widetilde{S}[\mathcal{X}]\):

\(\mathbf{E}_\widetilde{S}[\mathcal{X}]=O\left(M\cdot\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}X_k\right]\right)\)<br>
\(=O\left(M\cdot\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}Y_k\right]\right).\text{from (16)}\) (17)

Recall that our goal is to give an upper bound on X. From (17), an upper bound on \(\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}Y_k\right]\) can give an upper bound on \(\mathbf{E}_\widetilde{S}[\mathcal{X}]\) and we can then use Markov’s inequality to convert that to a probabilistic bound.

## An upper bound on \(\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}Y_k\right]\)

For any fixed \(\widetilde{S}\), note that

\(\sum_{k\in[S]}Y_k:=\frac{1}{S^{0.98}}\sum_{s\in[S]}\text{tr}\mathrm{TD}_{M,\{s\}}(\Delta p_s).\) (18)

Unfortunately, \(\sum_{s\in[S]}\text{tr}\mathrm{TD}_{M,\{s\}}(\Delta p_s)\) is not equal to the total tree deviation of any particular sequence. To get around this, note that since there are only \(\left|\widetilde{S}\right|\) active scales, the number of distinct _p<sub>s</sub>_ is at most \(\left|\widetilde{S}\right|\). Therefore, \(\sum_{s\in[S]}\text{tr}\mathrm{TD}_{M,\{s\}}(\Delta p_s)\) is at most the sum of the tree total deviations of \(\Delta p'\) for \(\left|\widetilde{S}\right|\) distinct paths \(p'\). Due to (14), this is the sum of \(O(w(p')\cdot S^{0.51})\) for \(\left|\widetilde{S}\right|\) distinct paths \(p'\). Let \(s'\in\widetilde{S}\) be the maximizer of \(w(p_{s^\prime})\). We have<tbc>

\(\sum_{s\in[S]}\text{tr}\mathrm{TD}_{M,\{s\}}(\Delta p_s)\le O(\left|\widetilde{S}\right|w(p_{s^\prime})S^{0.51}).\)


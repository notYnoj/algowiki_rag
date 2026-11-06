## Appendix A. Proof of Equation (1.3)

_Proof._ Let \(D\in\{0,1\}^N\) be the deletion pattern applied by the channel to obtain _Y_ from _X_. For each _i_=1_,...,N_, we set _D<sub>i</sub>_=1 if bit _i_ of _X_ was deleted, and _D<sub>i</sub>_=0 otherwise; note that \(D\sim Ber(p)^{\otimes N}\). We have

\(I(X;Y)=H(Y)-H(Y|X)\)<br>
\(=H(Y)-(H(D,Y|X)-H(D|X,Y))\)<br>
\(=H(Y)-H(D|X)+H(D|X,Y)\)<br>
\(=H(Y)-H(D)+H(D|X,Y),\)

where in the third step we used that _Y_ is deterministic given _X_ and _D_, and in the last step we used that _D_ and _X_ are independent. When _X_ is uniformly random, _Y_ is uniform in {0,1}<sup>|_Y_|</sup>, with E|_Y_|=(1-_p)N_. Setting \(\alpha:=1-p\), this leads to<tbc>

\(lim_{N\rightarrow\infty}\frac{1}{N}I(X;Y)=\alpha log2-h(\alpha)+lim_{N\rightarrow\infty}\frac{1}{N}H(D|X,Y).\)

<tbc>It remains to show that \(H(D|X,Y)=\mathbb{E}[logZ_{X,Y}^\mathrm{pl}]\). Given _X_ and _Y_, define the set of deletion patterns consistent with the observation:<tbc>

\(\mathcal{D}(X,Y)=\{D\in\{0,1\}^N:D(X)=Y\},\)

<tbc>where _D(X_) denotes the string obtained by deleting bit _X<sub>i</sub>_ whenever _D<sub>i</sub>_=1. Since \(D\sim Ber(p)^{\otimes N}\) independently of _X_, and all \(D\in\mathcal{D}(X,Y)\) have the same number of ones (namely _N_-|_Y_|), the conditional distribution of _D_ given (_X,Y_) is uniform on D(_X,Y_). Therefore

\(H(D|X,Y)=\mathbb{E}[log|\mathcal{D}(X,Y)|].\)

Finally, there is a natural bijection between D(_X,Y_) and the embedding set _S<sub>X,Y</sub>_: each \(D\in\mathcal{D}(X,Y)\) determines a unique \(\sigma\in S_{X,Y}\) by letting \(\sigma(j)\) be the index of the _j_-th retained bit, and vice versa. Hence \(|\mathcal{D}(X,Y)|=Z_{X,Y}^\mathrm{pl}\), and \(H(D|X,Y)=\mathbb{E}[logZ_{X,Y}^\mathrm{pl}]\).

It remains to verify that the limit on the right-hand side of (1.3) is well-defined with _M_ fixed at \(\alpha N\) rather than random. In the deletion channel, \(M=|Y|\sim Bin(N,\alpha)\) concentrates around \(\alpha N\) with deviations of order \(\sqrt{N}\). We couple a random \(\lfloor\alpha N\rfloor\)-subsequence of _X_ with the deletion channel output _Y_ by inserting or deleting \(|M-\alpha N|\) bits. Each single-bit change affects log_Z<sub>X,Y</sub>_ by at most log_N_. Since \(\mathbb{E}[|M-\alpha N|]=O(\sqrt{N})\), this gives

\(\frac{1}{N}\left|\mathbb{E}_M\left[\mathbb{E}[logZ_{X,Y}|M]\right]-\mathbb{E}[logZ_{X,Y^\prime}]\right|=O\left(\frac{\sqrt{N}logN}{N}\right)=o(1),\)

where \(Y'\) denotes a uniform random \(\lfloor\alpha N\rfloor\)-subsequence of _X_. □

## Appendix B. A Combinatorial Consequence of Theorem 1.1

The existence of the weak limit of (1.7) alone is enough to easily deduce the relative asymptotic behavior between \(f_\mathrm{null}(\alpha)\) and \(f_\mathrm{null}^\mathrm{ann}(\alpha)\) in the \(\alpha<1/2\) regime. Indeed, we let \(\alpha<\tilde{\alpha}<1/2\), and we assume that \(f_\mathrm{null}(\tilde{\alpha})=f_\mathrm{null}^\mathrm{ann}(\tilde{\alpha})\). For \((X',Y)\) drawn from the null model with density parameter \(\alpha\), we can write

(B.1) \(Z_{X^\prime,Y}=\left(\begin{array}{ c }
N-\alpha N \\
(\alpha/\tilde{\alpha})N-\alpha N
\end{array}\right)^{-1}\sum_{S\in\genfrac(){pt}{2}{[N]}{(\alpha/\tilde{\alpha})N}}Z_{X^\prime|_S,Y}.\)

Each summand on the RHS of (B.1) has the same law as the null partition function with density parameter \(\tilde{\alpha}\), where the embedded string is of length \(\alpha N\). It now follows from a standard argument (e.g., via invoking Markov’s inequality to control the number of "bad summands" that do not behave like \((\alpha/\tilde{\alpha})Nf_\mathrm{null}^\mathrm{ann}(\tilde{\alpha})\) in the exponential) that typically, most of these summands behave like \((\alpha/\tilde{\alpha})Nf_\mathrm{null}^\mathrm{ann}(\tilde{\alpha})\) in the exponential.


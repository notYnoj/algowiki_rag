## APPENDIX DPROOF FOR THEOREM IV.1

_Proof._ We begin with the first half, i.e.<tbc>

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(X))\ge\frac{1}{4}\cdot exp\left(-T\cdot D_\mathsf{KL}(p\|1-p)\right).\)

<tbc>To see this, simply consider the case of _K_=1, and we need to determine whether _X\<X_<sub>1</sub> or _X\>X_<sub>1</sub> from their pairwise comparisons. We consider two instances _X_<sup>(0)</sup>_,X_<sup>(1)</sup>, where _X_<sup>(0)</sup>_\<X_<sub>1</sub>_\<X_<sup>(1)</sup>. From Le Cam’s lemma, we have

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(\theta))\ge\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_{X^{(0)}},\mathbb{P}_{X^{(1)}}))\)<br>
\(\ge\frac{1}{4}exp(-T\cdot D_\mathsf{KL}(p\|1-p)).\)

Next, we aim to prove the second half, namely

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(X))\)<br>
\(\ge\frac{1}{2}\cdot\left(1-\frac{T\cdot(1-H(p))+log(2)}{log(K)}\right).\)

Now we design _K_ instances \(X^{(0)},\cdots,X^{(K-1)}\). We let _X_<sup>(0)</sup>_\<X_<sub>1</sub>, and \(X^{(l)}\in(X_l,X_{l+1})\). From Le Cam’s lemma, we have

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(\theta))\)<br>
\(\ge inf_\hat{\mu}sup_{X\in\{X^l\}_{l\in[K]}}\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(\theta))\)<br>
\(\ge inf_\Psi\frac{1}{2K}\sum_{l\in[K]}\mathbb{P}_{X^{(l)}}(\Psi\neq l).\)

Now by Fano’s inequality, we have

\(inf_\Psi\frac{1}{2K}\sum_{l\in[K]}\mathbb{P}_{^{(l)}}(\Psi\neq l)\)<br>
\(\ge\frac{1}{2}\cdot\left(1-\frac{I(V;Y)+log(2)}{log(K)}\right).\)

Here \(V\sim\mathsf{Unif}(\{0,1,\cdots,K-1\}))\) and _Y_ satisfies P<sub>_Y|V=l_</sub>=P<sub>_X_<sup>(_l_)</sup></sub>. Following the same argument as the proof of Theorem 3 in Wang et al. (2022), we know that \(I(V;Y)\le T\cdot(1-H(p))\). Thus overall we have

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(X))\ge\frac{1}{4}\cdot\left(1-\frac{T\cdot(1-H(p))}{log(K)}\right).\)

Thus the queries required to recover the true value with probability at least \(1-\delta\) is lower bounded by \(\Omega(log(K)/(1-H(p))+log(1/\delta)/D_\mathsf{KL}(p\|1-p))\). □

## APPENDIX EPROOF FOR THEOREM IV.3

_Proof._ Let _T<sub>i</sub>_ be the random variable that denotes the number of times _X_ is compared with _X<sub>i</sub>_. Since \(\sum_{i\in[K]}\mathbb{E}[T_i]=T\), there must exists some _i_ such that \(\mathbb{E}[T_i]\le T/K\). Now we construct the first instance


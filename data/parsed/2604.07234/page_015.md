<tbc>with the _o<sub>p</sub>_(1) term being _O_(1). Since \(\bar{\mu}\) and \(\bar{\nu}\) are deterministic, the \(\sqrt{M}\) pairs<tbc>

\(\left(X_\bar{\mu}^{^\prime(i)},Y_\bar{\nu}^{^\prime(i)}\right)\)

<tbc>are independent, so the corresponding summands in (2.11) are also independent. We conclude that

\(\mathrm{Var}\left(\frac{1}{N}\mathrm{log}Z_{X^\prime,Y}\right)=\mathrm{Var}\left(\frac{1}{\sqrt{N}}\sum_{i=1}^{\sqrt{M}}\frac{1}{\sqrt{N}}\mathrm{log}Z_{X_\bar{\mu}^{^\prime(i)},Y_\bar{\nu}^{^\prime(i)}}\right)+o(1)\)<br>
\(=\frac{\sqrt{M}\cdot\mathrm{Var}\left(\frac{1}{\sqrt{N}}\mathrm{log}Z_{X_\bar{\mu}^{^\prime(1)},Y_\bar{\nu}^{^\prime(1)}}\right)}{N}+o(1)=O\left(N^{-1/2}\right)+o(1)\checkmark 1.\) (2.12)

The desired weak law now follows from Lemma 2.2, (2.12), and Chebyshev’s inequality. □

## 2.2. Planted model.

We now prove the weak limit part of (1.6), the analogue of (1.7) for the planted setting. We begin by proving Proposition 2.3, a deletion channel variant of this weak limit which settles \[PIW24, Conjecture 1\].

**Proposition 2.3** (Deletion channel planted limit; \[PIW24, Conjecture 1\])**.** _Fix_ \(\alpha\in(0,1)\)_. Let_ \(\mathsf{BDC}_{1-\alpha}(X)\) _denote the outcome of passing_ \(X\in\{0,1\}^N\) _through a deletion channel with deletion probability_ \(1-\alpha\)_. There exists a constant_ \(f_\mathrm{pl}(\alpha)>0\) _such that_<tbc>

(2.13) \(\frac{1}{N}\mathrm{log}Z_{X,\mathsf{BDC}_{1-\alpha}(X)}-\rightarrow^{a.s.}f_\mathrm{pl}(\alpha).\)

<tbc>_Proof._ It is clear that for any \(N_1,N_2\in\mathbb{N}\), we have that

\(\mathrm{log}Z_{X_{1:N_1+N_2},\mathsf{BDC}_{1-\alpha}(X_{1:N_1+N_2})}\)<br>
\(\ge\mathrm{log}Z_{X_{1:N_1},\mathsf{BDC}_{1-\alpha}(X_{1:N_1})}+\mathrm{log}Z_{X_{N_1+1:N_1+N_2},\mathsf{BDC}_{1-\alpha}(X_{N_1+1:N_1+N_2})}.\) (2.14)

Specifically, (2.14) holds for the following reason. The partition function in the LHS of (2.14) counts unconstrained subsequence embeddings of \(\mathsf{BDC}_{1-\alpha}(X_{1:N_1+N_2})\) into _X_<sub>1:_N_<sub>1</sub>+_N_<sub>2</sub></sub>. On the other hand, the expression on the RHS counts the logarithm of the number of constrained such subsequence embeddings for which \(\mathsf{BDC}_{1-\alpha}(X_{1:N_1})\) is mapped into _X_<sub>1:_N_<sub>1</sub></sub> and \(\mathsf{BDC}_{1-\alpha}(X_{N_1+1:N_1+N_2})\) is mapped into _X_<sub>_N_<sub>1</sub>+1:_N_<sub>1</sub>+_N_<sub>2</sub></sub>. If one of the partition functions of (2.14) vanishes, then \(\mathsf{BDC}_{1-\alpha}\) has deleted every bit of the corresponding string. In that case the relevant logarithmic term is 0 by convention, and (2.14) is readily checked to remain valid. Therefore, invoking the superadditive ergodic theorem \[Kin73\] on the integrable random variables

\(g_N:=\mathrm{log}Z_{X_{1:N},\mathsf{BDC}_{1-\alpha}(X_{1:N})},\)

noting that the corresponding transformation is ergodic as it is effectively a Bernoulli shift, yields the desired. □

_Proof of weak limit of_ (1.6). We couple the random string \(\mathsf{BDC}_{1-\alpha}(X)\) with _Y_ by defining _Y_ via inserting or deleting \(|M-\alpha N|\) bits uniformly at random. If the planted string \(Y'\) of _X_ is obtained from the planted string _Y_ of _X_ by including a bit of _X_ in its appropriate position, then it holds that<tbc>

\(|\mathrm{log}Z_{X,Y^\prime}-\mathrm{log}Z_{X,Y}|\le N,\)

<tbc>so the log-partition function increases by an additive margin of at most log_N_. Indeed, this crude bound follows via choosing one of the _N_ bits of _X_ that the new bit is mapped to when forming \(Y'\) from _Y_ , as the remaining bits of _Y_ must still correspond to a valid subsequence embedding. This observation, together with Proposition 2.3 and the standard fact that

\(|\mathsf{BDC}_{1-\alpha}(X)|\sim\mathrm{Bin}(N,\alpha)\)

concentrates about \(\alpha N=M\) with \(O(\sqrt{N})\checkmark N\) deviations is now enough to derive the desired result. We leave the straightforward details to the reader. □


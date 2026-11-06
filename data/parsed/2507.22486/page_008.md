**Algorithm 2** Better-Approx-LCS(_x,y_)

**foreach** \(f\in\{2^i|i\in[0..\lfloor logn]\rfloor\}\) **do**

**2** \(x'\leftarrow\mathsf{Project}(x,\Sigma_{[f..n]}(x))\);

**3** \(L\leftarrow^\mathrm{max}\mathsf{Approx-LCS}(x',y)\); ;

**return** _L_;

## Running Time.

The while loop of the algorithm runs _O_(log_n_) times. In each iteration, filtering out the least frequent symbols can be straight-forwardly implemented in \(\tilde{O}(n)\) time. Then, running algorithm Approx-LCS\((x',y)\) takes \(\tilde{O}(n)\) time. Thus, the total running time is \(\tilde{O}(n)\).

## Correctness.

The algorithm returns a common subsequence obtained by Approx-LCS\((x',y)\) for some subsequence \(x'\) of _x_ due to the correctness of Algorithm 1. Since \(x'\) is a subsequence of _x_, the output is a common subsequence of _x_ and _y_.

## Approximation Ratio.

Let _L_ be some longest common subsequence of _x_ and _y_. We observe that for some power 2_<sup>i</sup>_ of 2, a significant fraction of _L_ consists of symbols that appear roughly 2_<sup>i</sup>_ times in _L_.

\(\blacktriangleright\) **Lemma 8.** _For some_ \(f\in\{2^i|i\in[0..\lfloor logn]\rfloor\}\)_, we have_

\(|\mathsf{Project}(L,\Sigma_{[f..2f)}(L))|\ge\frac{|L|}{2\mathrm{log}n}.\)

**Proof.** The claim follows directly from the pigeonhole principle. Formally,

\(|L|=\sum_{\sigma\in\Sigma}\#_\sigma(L)=\sum_{f\in\{2^i|i\in[0..\lfloor logn]\rfloor\}}\sum_{\sigma\in\Sigma_{[f..2f)(L)}}\#_\sigma(L)\)<br>
\(=\sum_{f\in\{2^i|i\in[0..\lfloor logn]\rfloor\}}|\mathsf{Project}(L,\Sigma_{[f..2f)}(L))|.\)

By the pigeonhole principle, at least one of the summands must be at least |_L_| divided by the number of summands, which is at most \(1+\mathrm{log}n\le 2\mathrm{log}n\). Thus, the claim follows. \(\blacktriangleleft\)

Let _f_ be some \(f\in\{2^i|i\in[0..\lfloor logn]\rfloor\}\), such that \(|\mathsf{Project}(L,\Sigma_{[f..2f)}(L))|\ge\frac{|L|}{2\mathrm{log}n}\) (the existence of _f_ follows from Lemma 8). Denote \(L'=\mathsf{Project}(L,\Sigma_{[f..2f)}(L))\). We proceed to analyze the approximation ratio achieved by running Approx-LCS\((x',y)\) for \(x'=\mathsf{Project}(x,\Sigma_{[f,n]}(x))\). In particular we will show that Approx-LCS\((x',y)\) returns an _O(n_<sup>3/4</sup>log_n_)-approximation for LCS(_x,y_). A useful property of \(x'\), is that for any \(\sigma\in\Sigma\) that occurs in _x_ we have \(\#_\sigma(x)\ge f\).

Clearly, if |LCS(_x,y_)|=0 the algorithm would not find any common subsequence, which is a satisfactory answer. If \(|\mathsf{LCS}(x,y)|\ge 1\), in particular there is a common symbol occurring both in \(x'\) and in _y_. It immediately follows that \(\mathsf{BestMatch}(x',y)\) returns a common subsequence of length at least 1, which is an _n_<sup>3/4</sup>-approximation if \(|\mathsf{LCS}(x,y)|\le n^{3/4}\). Let us assume from now on that |_L_|=|LCS(_x,y_)|_\>n_<sup>3/4</sup>. In particular, let \(0<t\le 1/4\) be the number such that |_L_|=_n_<sup>3/4+_t_.

Assume that \(f\ge n^{1/4}\). Then, in particular, there is some symbol \(\sigma\in\Sigma_{[f..2f)}(L)\subseteq\Sigma_{[f..n)}(x)\) such that \(\#_\sigma(L')\ge f\ge n^{1/4}\), and \(|\mathsf{BestMatch}(x',y)|\ge\mathsf{Match}(x',y,\sigma)\ge\#_\sigma(L')\ge n^{1/4}\). It follows that \(\mathsf{BestMatch}(x',y)\) is an _n_<sup>3/4</sup>-approximation of LCS(_x,y_). We therefore assume from now on that _f\<n_<sup>1/4</sup>.


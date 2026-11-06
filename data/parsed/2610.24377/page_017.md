We can also apply our algorithm to obtain (static) string pattern matching with wildcards. Let \(\Sigma=\Sigma'\cup\{\star\}\) be the alphabet. Given a pattern _p_ over \(\Sigma\) and a sub-string \(s'\) over \(\Sigma\), we say \(s'\) matches _p_ if on every index _i_ either _p<sub>i</sub>=⋆_, \(s'_i=\star\), or \(p_i=s'_i\). Assume, WLOG, that \(|\Sigma|\le(n+m)+1\) (including wildcard symbol ⋆) and \(m\le n\) for length-_m_ pattern _p_ and length-_n_ string _s_.

**Corollary 4.9** (Wildcard String Matching)**.** Assume strings \(s\in\Sigma^n\) and \(p\in\Sigma^m\) are provided as input. There exists a catalytic algorithm using time \(\widetilde{O}\left(n\right)\), _O(n_log<sup>2</sup>_n_) dirty space, and _O_(log_n_) clean space computing an indicator vector _v_ where _v<sub>i</sub>_=1 iff pattern _p_ matches substring _s_<sub>_i:i+m_-1</sub>.

_Proof._ The alphabet symbols are provided as positive integers of magnitude at most _n+m_. Replace any ⋆ in _p_ and _s_ with zeros. An algorithm of \[CC07\] proceeds by computing, for each _i_, the quantity

\(q_i=\sum_{j=0}^{m-1}p_js_{i+j}\left(p_j-s_{i+j}\right)^2=\)<br>
\(\sum_{j=0}^{m-1}p_j^3s_{i+j}-2p_j^2s_{i+j}^2+p_js_{i+j}^3.\)

This quantity _q<sub>i</sub>_ is 0 if pattern _p_ matches substring _s_<sub>_i:i+m_-1</sub> and positive otherwise.

The squared and cubed values in the quantities can be computed by an _O(n_)-size circuit with multiplicative depth 2. The individual terms can then be computed and accumulated using polynomial multiplication over a sufficiently large ring Z_/c_Z (_c_=poly(_n_)) to avoid modular overflow. Overall, this is a multiplicative depth 3 arithmetic circuit. Therefore, by Theorem 4.3 along with the construction of Corollary 4.7, we can compute this quantity _q<sub>i</sub>_ for all \(1\le i\le n-m+1\) in time \(n\cdot poly(logn)\) catalytically into registers. Finally, convert this modular ring register vector output to XOR output form by Lemma A.2. Then, apply Theorem 1.1 to a small depth fan-in 2 circuit (size \((n-m+1)\cdot poly(logn)\), depth _O_(loglog_n_)) over each register value which outputs 1 if _q<sub>i</sub>_=0 and outputs 0 otherwise. In total, this uses \(n\cdot poly(logn)\) time and \(O(nlogn)\cdot O(logn)\) dirty space.

## 4.3 Application: Matrix Multiplication

Another problem with nontrivial algorithms of low multiplicative depth is matrix multiplication. Here, even though we don’t know the optimal runtime, we know that it is achievable catalytically. We observe the following:

**Definition 4.10.** The matrix multiplication exponent \(\omega\) is the infimum over all _r_ such that \(n\times n\) matrices over C can be multiplied by arithmetic circuits<sup>12</sup> of size _O(n<sup>r</sup>_).

**Corollary 4.11.** There is a catalytic algorithm which, given \(m\ge 2\) and \(A,B\in(\mathbb{Z}/m\mathbb{Z})^{n\times n}\), computes _AB_ using clean space _O_(log_n_+log_m_), time \(n^{\omega+o(1)}\mathsf{polylog}(m)\), and dirty space \(n^{\omega+o(1)}\mathsf{polylog}(m)\).

_Proof._ By standard results from the matrix multiplication literature \[BCS97; Sch81\], for every \(\varepsilon>0\) there is a bilinear algorithm over Q that multiplies \(k\times k\) matrices for some _k_ using at most \(k^{\omega+\varepsilon}\) products.<sup>13</sup> By doing a brute-force search over all such bilinear algorithms with small (e.g. at most logloglog(_n_)) size and bit complexity, we can therefore find one using at most \(k^{\omega+o(1)}\) products for some _k_.<sup>14</sup> This is a<tbc>

<sup>12</sup>_Non-uniform_ arithmetic circuits with allowed division gates. <sup>13</sup>It is known that the exponent of matrix multiplication (over fields) can only depend on the characteristic of the field, if at all \[Sch81\]. <sup>14</sup>Instead of iterating over small arithmetic circuits, we can also simply brute force the coefficients witnessing a rank upper bound of the \(\langle k,k,k\rangle\) matrix multiplication tensor rank. (The arithmetic matrix exponent and the infimum of the logarithm base _k_ of this "tensor rank" are _equivalent_ over characteristic zero fields. See e.g. \[Str73\].) Using this method, brute forcing over the possible rank bounds for \(k\le logloglogn\) and bit complexity (of the Q coefficients) logloglog_n_ is sufficient for our purposes to achieve \(\omega+o(1)\). Observe this is stronger than \(\omega+\varepsilon\) for all \(\varepsilon>0\) as, in that case, the algorithm’s leading constant would depend on \(\varepsilon\).


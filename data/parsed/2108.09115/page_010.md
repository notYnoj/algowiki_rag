## 4.1 Preprocessing Algorithm

Given \(Y\in\Sigma^n\), we sample each index in \[1_,n_\] uniformly at random with probability \(\frac{\mathrm{log}^2n}{k}\) . Let _S_={_i_<sub>1</sub>_,i_<sub>2</sub>_,...,i<sub>s</sub>_} denote the sampled indices. Create the following substrings

\(B^d=b_{i_1+d}b_{i_2+d}\dots b_{i_s+d},\forall d=-k,-k+1,\dots,0,\dots,k-1,k.\)

By a standard application of the Chernoff bound, we can assume with probability at least \(1-\frac{1}{n^3}\), the number of sampled indices \(s=\Theta(\frac{n\mathrm{log}^2n}{k})\).

The preprocessing algorithm constructs log(_s_)+1 hash tables just like in Section 3, but for each _B<sup>d</sup>_, \(d\in[-k,k]\). The \(\ell\)-th hash table corresponds to window size \(2^\ell\) of _B<sup>d</sup>_. Since there are log_s_+1 levels, the overall preprocessing time is \(O(k*\frac{n}{k}\mathrm{log}^2n\mathrm{log}s)\)=\(\tilde{O}(n)\) with probability \(1-\frac{1}{n^3}\). Let \(H_B^d[\ell]\) store all the hashes for windows of length \(2^\ell\) of _B<sup>d</sup>_ for _d_=\[-_k,k_\].

## 4.2 Query Algorithm

Given \(A\in\Sigma^n\). We create a sampled substring _A<sub>S</sub>=a_<sub>_i_<sub>1</sub></sub>_a_<sub>_i_<sub>2</sub></sub>_...a<sub>i<sub>s</sub></sub>_. We construct log(_s_)+1 hash tables for _A<sub>S</sub>_. Again, the \(\ell\)-th hash table corresponds to window size \(2^\ell\) of _A<sub>S</sub>_. Since there are log_s_+1 levels, the overall time to compute the hashes of _A<sub>S</sub>_ is \(O(\frac{n}{k}\mathrm{log}^2n\mathrm{log}s)=\tilde{O}(\frac{n}{k})\) with probability \(1-\frac{1}{n^3}\). Let \(H_A[\ell]\) store all the hashes for windows of length \(2^\ell\) of _A<sub>S</sub>_

We now define an approximate _Equal(i,d_), _Approx-Equal(i,d_) query as follows. Let \(n(i)\ge i\) be the nearest index to _i_ present in _S_. Define

\(Approx-Equal(i,d)=\mathrm{max}_{q\ge i}(q|q\in S,X_S[n(i),q]=Y^d[n(i),q])\)

We now run the same algorithm from Section 3 except that we replace _Equal(i,d_) with _Approx-Equal(i,d_). Let us use \(\hat{L}^h\) to denote the _h_-wave computed by using _Approx-Equal(i,d_) for \(h\in[0,k]\) and \(d\in[-k,k]\). If the algorithm computes \(\hat{L}^h(0)\ge n\) for \(h\le k\), the algorithm returns YES. Else, it returns NO.

Clearly, the running time of the algorithm is \(\tilde{O}(\frac{n}{k}+k^2)\). We now show that the algorithm solves the quadratic gap problem.

### Analysis

When comparing a symbol _x<sub>i</sub>_ with _y<sub>j</sub>_, if they do not match, we call it a ’mismatch’. The following is an easy lemma which shows we cannot miss too many mismatches due to sampling.

**Lemma 4.** _Given_ \(i\in[1,n]\) _and_ \(d\in[-k,k]\)_, let_ \(i'\ge i\) _be the smallest index such that_ \(x_ix_{i+1}\dots,x_{i^\prime}\) _and_ \(y_{i+d}y_{i+1+d}\dots y_{i^\prime+d}\) _have at least_ \(k'=\frac{k}{\mathrm{log}n}\) _m mismatches. Let_ \(i\le j_1,j_2,\dots,j_{k^\prime}=i'\) _be the indices such that_ \(x_{j_h}\neq y_{j_h}+d\)_. Define a bad event B(i,d_) _to be the event that none of these_ \(k'\) _mismatch indices are sampled. Then_ \(Prob(Bad(i,d))\le 1-\frac{1}{n^3}\)_. Moreover, all bad events are avoided with probability at least_ \(1-\frac{1}{n}\).

_Proof._ Since the sampling probability is \(\Theta(\frac{\mathrm{log}^2n}{k})\), the expected number of points sampled from \(j_1,j_2,\dots,j_{k^\prime}\) is \(\Theta(\mathrm{log}n)\). Now, by the Chernoff bound, the probability that none of them are sampled can be made to be \(1-\frac{1}{n^3}\) (by choosing the constants in the sampling probability appropriately).

Then by a union bound over all \(i\in[1,n]\) and \(d\in[-k,k]\), with probability \(\ge 1-\frac{1}{n}\) none of the bad events _Bad(i,d_) happen.

Therefore, we can assume all bad events are avoided. The above lemma leads to the following direct corollary.


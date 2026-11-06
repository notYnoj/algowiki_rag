Since a lower bound for \(\gamma\)-approximate Bichromatic Closest Pair implies a lower bound for \(\gamma\)-ANN with polynomial preprocessing time \[WW18\], Theorem 1.3 implies the following corollary.

**Corollary 1.4** (Informal)**.** _Assuming SETH, for any_ \(\delta>0\) _and_ \(\gamma<3\)_, there exists a constant c\>_0 _such that_ \(\gamma\)_-ANN on instances with dimension d=c_log_N under the_ \(\ell_\infty\) _norm cannot be solved with polynomial preprocessing and_ \(N^{1-\delta}\) _query time._

Furthermore, we show that any naive gadget reduction from Orthogonal Vectors (Definition 2.2), which essentially captures most known reduction techniques from SETH, to \(\gamma\)-approximate Bichromatic Closest Pair cannot show hardness for any approximation factor larger than 3 (Theorem 3.9). This essentially follows from the triangle inequality. We note that this limitation was mentioned in \[Rub18\] as well. Hence, showing any hardness with an approximation factor larger than 3 would require a novel technique bypassing the naive gadget reduction techniques. Therefore, our hardness result for ANN under \(\ell_\infty\) is tight in this sense.

We note that the result of \[Rub18\], who showed hardness under the \(\ell_2\) norm, already implies the hardness of ANN under the \(\ell_\infty\) norm since one can embed \(\ell_2\) into a subspace of \(\ell_\infty\) with low distortion \[Ind03\]. This reduction is similar to that of \[RR06\], who showed that \(\ell_2\) is, in a certain sense, the "easiest norm" for lattice problems. However, hardness under the \(\ell_\infty\) norm through this reduction only holds for _d_=pollog_N_ (as opposed to _d=O_(log_N_) in our results) because of the embedding’s dimension blow-up. Moreover, our reductions are simpler and do not require the distributed PCP \[ARW17\] machinery used in \[Rub18\]. Our Corollary 1.4 is also stronger in the sense that it holds for larger (and known) approximation factors. The approximation factor for hardness in \[Rub18\] is exponentially small in \(\delta\) and depends on an unspecified relation between the reduction parameters due to SETH.

## 1.3 Future Directions

Our result shows that the hardness of ANN under \(\ell_\infty\) for approximation factor 3 is the best one can hope for with current reduction techniques. The difficulty of proving hardness beyond 3- approximation was hinted in \[Rub18\], but no norm which explicitly instantiates this barrier was known previously.

An obvious next direction is determining whether hardness of \(\gamma\)-ANN under \(\ell_\infty\) for \(\gamma>3\) can be shown, as it is widely believed \[ACP08; PTW10; BK18\] that the tradeoff between the required preprocessing/query time and approximation guarantee given by Indyk’s algorithm \[Ind01\] is optimal. However, it is not clear whether such a result can be obtained from SETH. Our connection between \(\gamma\)-ANN and \(\gamma\)-SVP<sup>{0,1}</sup> suggests a direction for overcoming this technical barrier. Instead of basing hardness on SETH, consider the following conjecture on \(\mathsf{SVP}_\infty^{\{0,1\}}\).

**Conjecture 1.5.** _For any_ \(\varepsilon\in(0,1/2)\)_, there exists_ \(\gamma=\omega(1)\) _such that there is no_ \(2^{(1-\varepsilon)n}\) _time algorithm for_ \(\gamma\)-\(\mathsf{SVP}_\infty^{\{0,1\}}\).

It is straightforward to see that Lemma 3.1 and 3.2 (formal version of Theorem 1.1) together with Conjecture 1.5 would imply hardness of \(\omega(1)\)-ANN under \(\ell_\infty\). We remark that almost all instances arising in NP-hardness proofs of \(\gamma\)-\(\mathsf{SVP}_\infty\) are indeed captured by \(\mathsf{SVP}_\infty^{\{0,1\}}\) \[MG02; Din02; BGSD17\].<sup>2</sup>

One potential direction is to prove Conjecture 1.5 assuming SETH. However, this would then overcome the barrier of 3-approximation for ANN, suggesting that such a result would be difficult to<tbc>

<sup>2</sup>\[Din02\] generates a lattice in which coefficients of the short lattice vector take values in {-1,0,1} instead of {0,1}. Still, there are only 3_<sup>n</sup>_ many candidates for the short vector, so our reduction applies to this case as well with minor modifications.


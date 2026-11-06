After handling these easy cases, our approach is to restrict _A_ and _B_ to binary strings and invoke the frequency arguments from previous work. As we noted before, we cannot directly use the reduction in Corollary 5 because the better than 1/2 approximation of [21] only applies when the inputs have the same length. It turns out however, that the arguments of [21] _do_ hold for strings of differing length as long as the inputs satisfy a nice frequency condition. The following lemma demonstrates how by careful choice of subalphabets we can find restrictions meeting this condition. To describe this condition, we introduce some new notation: given a string _A_ from an alphabet \(\Sigma\), for any symbol \(\sigma\in\Sigma\) we let \(\sigma(A)\) denote the number of times \(\sigma\) appears in _A_.

\(\blacktriangleright\) **Lemma 12** (Binary Restriction)**.** _Suppose neither A nor B are_ \(\rho\)_-balanced. Then there exists_ \(\Sigma'\subseteq\Sigma\) _with_ \(|\Sigma'|=2\) _such that the restrictions of A and B to_ \(\Sigma'\) _are not_ \(\rho/s\)_-balanced._

**Proof.** Let \(\alpha_1\le\cdots\le\alpha_s\) be the number of times the distinct symbols \(\sigma_1,\dots,\sigma_s\) of \(\Sigma\) appear respectively in _A_, so that \(\sigma_s\) is the most frequent symbol of _A_ and \(\sigma_1\) is the least common character in _A_. By averaging we know that \(\alpha_s\ge n/s\ge\alpha_1\). Since _A_ is not \(\rho\)-balanced we deduce that

\(\alpha_s-\alpha_1>\rho n.\)

We can decompose the left hand side of the above equation to

\(\alpha_s-\alpha_1=\sum_{i=2}^s(\alpha_i-\alpha_{i-1}).\)

Since all the summands on the right hand side are positive, there exists some index _j_ with

\(\alpha_j-\alpha_{j-1}>(\rho/s)n.\) (2)

Note that we can find such a _j_ in linear time by scanning through _A_ and _B_ and keeping counts of all the characters that appear. Now, consider the (_s_-1) two-element sets

\(\{\sigma_s,\sigma_{j-1}\},\{\sigma_{s-1},\sigma_{j-1}\},\dots,\{\sigma_j,\sigma_{j-1}\},\{\sigma_j,\sigma_{j-2}\},\dots,\{\sigma_j,\sigma_1\}.\) (3)

We claim that one of these sets satisfies the properties of \(\Sigma'\) from the lemma statement. First, note that Equation (2) ensures that the restriction of _A_ to any of the above sets is not \(\rho/s\)-balanced, so it suffices to verify that the restriction of _B_ will not be balanced for one of these sets. Suppose to the contrary that none of the sets from Equation (3) satisfies the desired conditions. We will use a triangle-inequality argument on the character frequencies of _B_ to derive a contradiction. Let _M_ and _m_ be indices such that \(\sigma_M\) is the most frequent character of _B_ and \(\sigma_m\) is the least frequent. Since _B_ is not \(\rho\)-balanced, we know that \(M\neq m\). If \(M\ge j>m\) we may write

\(|\sigma_M(B)-\sigma_m(B)|\le|\sigma_M(B)-\sigma_{j-1}(B)|+|\sigma_{j-1}(B)-\sigma_j(B)|+|\sigma_j(B)-\sigma_m(B)|.\)

By assumption, the restrictions of _B_ to the sets \(\{\sigma_M,\sigma_{j-1}\}\), \(\{\sigma_j,\sigma_{j-1}\}\), and \(\{\sigma_j,\sigma_m\}\) are \((\rho/s)\)-balanced. Thus, each addend on the right hand side of the above inequality is bounded above by \((\rho/s)n\). It follows that

\(|\sigma_M(B)-\sigma_m(B)|\le(3\rho/s)n.\)


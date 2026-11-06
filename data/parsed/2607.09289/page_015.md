**Theorem 5.2.** _Assume that the minimum solution ratio satisfies_ \(\ell'\in(1/2,0.8)\)_. For every constant_ \(\alpha\) _satisfying_ \(0.45\le\alpha\le 1/2\)_, there is a Monte Carlo algorithm for ESS that uses_ \(O^*(2^{\alpha n})\) _space and runs in_ \(O^*(2^{\tau_\text{rrb}(\ell^\prime,\ell^\prime-\phi\mathrm{i}^{-1}(1-\alpha))n})\) _time. Here,_ phi<sup>-1</sup> _denotes the inverse of the restriction of_ phi _defined in_ (4) _to the interval_ \[0.4,1/2\]_, on which_ phi _is bijective._

_Proof._ Set \(k'=\ell'-\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\). Since \(\alpha\in[0.45,1/2]\), we have \(\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\in[0.4,1/2]\). Also, \(k'\ge 0\) follows from \(\ell'>1/2\) and \(\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\le 1/2\). Moreover, since \(\ell'<0.8\) and \(\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\ge 0.4\), we have \(2k'=2(\ell'-\mathrm{phi}\mathrm{i}^{-1}(1-\alpha))\le\ell'\). Thus, the condition \(0\le k'\le\ell'/2\) is satisfied, and we can apply Theorem 3.8. Since \(\ell'-k'=\mathrm{phi}\mathrm{i}^{-1}(1-\alpha)\le 1/2\), the space exponent is

\(\sigma_\text{rrb}(\ell',k')=1-\mathrm{phi}(\ell'-k')=1-\mathrm{phi}(\mathrm{phi}\mathrm{i}^{-1}(1-\alpha))=\alpha.\)

Therefore, the space complexity is \(O^*(2^{\sigma_\text{rrb}(\ell^\prime,k^\prime)n})=O^*(2^{\alpha n})\). The claimed running time follows directly from Theorem 3.8 with the above choice of \(k'\).

## 5.3 Space-Bounded Modification of the Balanced ESS Algorithm

Input: Input set S and minimum solution size \(\ell\)<br>
Output: An ESS solution for S if one exists; otherwise, NO<br>
Space bound: \(O^*(2^{\alpha n})\)<br>
Set<br>
\(p_\mathrm{max}=\left\{\begin{array}{ c c }
\mathrm{min}\{2^{n-\ell},\lfloor 2^{\alpha n}\rfloor\} & \text{if}\ell>n/2, \\
\mathrm{min}\left\{\genfrac(){pt}{2}{n-\ell}{\lfloor(\ell-1)/2\rfloor},\lfloor 2^{\alpha n}\rfloor\right\} & \text{otherwise.}
\end{array}\right.\)<br>
Pick a random prime p in \[p<sub>max</sub>,2p<sub>max</sub>\], and a random residue r in \[0,p-1\].<br>
Let \(C=\{X\subseteq S|\sum(X)\equiv_pr\}\). Prepare the data structure DS of Lemma 5.4 in O(np) time and space, so that DS supports random access to the elements of C and stores the value |C|. If \(|C|>n^d\cdot 2^n/p_\mathrm{max}\) for a fixed constant d\>2, halt and return NO.<br>
Consider the list L whose i-th element is the sum of the i-th element of C. Using DS, each entry of L can be computed on the fly in poly(n) time. Apply Lemma 5.3 to L to find \(X,Y\in C\) such that \(\sum(X)=\sum(Y)\), using \(O^*(\mathrm{min}\{|C|,2^{\alpha n}\})\) space. If no such pair exists, return NO.<br>
Return (X\\Y,Y\\X).

We introduce Algorithm 3, which combines the _BalancedEqualSubsetSum_ algorithm of \[25\] with a low-space algorithm for Element Distinctness. We use the following time-space tradeoff for Element Distinctness due to \[23\]. Although the statement in \[23\] is phrased for positive integers, the same bound applies to nonnegative integers by adding 1 to every array entry, which preserves all collisions.

**Lemma 5.3** (\[23\])**.** _Given random access to an array of N nonnegative integers a_<sub>1</sub>_,...,a<sub>N</sub>, with_ \(a_i\le\mathrm{poly}(N)\) _for all_ \(i\in[N]\)_, there is a Monte Carlo algorithm that either returns a colliding pair_ (_i,j_) _such that_ \(i\neq j\) _and a<sub>i</sub>=a<sub>j</sub>, or reports that no such pair exists. The algorithm runs in O(t(N_)polylog(_N_)) _time and uses O(s(N_)polylog(_N_)) _space, for any complexity bounds_ \(s,t:\mathbb{N}\rightarrow\mathbb{N}\) _satisfying_ \(s(N)\le N\) _and_ \(s(N)^{1/2}\cdot t(N)\ge N^{3/2}\).

We use the _Fast Subset-Sum Oracle_ of \[1, Section 3.1\] to support random access to the elements of the set C in Algorithm 3.

**Algorithm 3:** SpaceBoundedBalancedESS


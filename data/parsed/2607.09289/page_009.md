_Proof._ For a fixed prime _p_, each subset \(X\subseteq S'\) falls into _C_ with probability 1_/p_, since the residue _r_ is chosen uniformly at random from \[0_,p_-1\]. Since \(p\ge p_\mathrm{max}\), this probability is at most 1_/p_<sub>max</sub> for any _p_. Thus, the result follows by linearity of expectation.

Since Claim 3.6 holds for every fixed outcome of \(S'\), it also holds for the conditional expectation given F. Hence, \(\mathbb{E}[|C||\mathcal{F}]\le 2^n/p_\mathrm{max}\). Consider the complement of G, namely the event G_<sup>c</sup>_ that Algorithm 2 halts in Line 3, i.e., the event that \(|C|>n^d\frac{2^n}{p_\mathrm{max}}\) occurs. By Markov’s inequality, we have

\(\mathbb{P}[\mathcal{G}^c|\mathcal{F}]\le\frac{\mathbb{E}[|C||\mathcal{F}]}{n^d\cdot 2^n/p_\mathrm{max}}\le\frac{1}{n^d}.\) (3)

We are now ready to prove \(\mathbb{P}[(\mathcal{G}\cap\mathcal{H})|\mathcal{F}]\ge\Omega^*(1)\):

\(\mathbb{P}[(\mathcal{G}\cap\mathcal{H})|\mathcal{F}]=\mathbb{P}[\mathcal{H}|\mathcal{F}]-\mathbb{P}[(\mathcal{G}^c\cap\mathcal{H})|\mathcal{F}]\)<br>
\(\ge\Omega(1/n^2)-1/n^d\text{by}(2)\text{and}(3)\)<br>
\(=\Omega(1/n^2)=\Omega^*(1),\text{since}d>2.\)

This completes the proof of Lemma 3.4.

We now turn to the time and space complexity analysis.

**Lemma 3.7.** _The set C can be enumerated in O_<sup>∗</sup>(max{|_C|,_2<sup>_n/_2</sup>}) _time and O_<sup>∗</sup>(max{|_C|,_2<sup>_n/_4</sup>}) _space._

_Proof._ This is the modular variant of the Subset-Sum problem, and the technique of Schroeppel and Shamir \[29\] can compute it in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time and _O_<sup>∗</sup>(2<sup>_n/_4</sup>) space, excluding the output size. See \[8, Section 3.2\] for pseudocode of the modular version. The pseudocode requires scanning the subset sums of the two halves of \(S'\) in ascending and descending order with respect to their values modulo _p_. A straightforward implementation would enumerate and sort all _O_<sup>∗</sup>(2<sup>_n/_2</sup>) sums, using _O_<sup>∗</sup>(2<sup>_n/_2</sup>) space. In Appendix B.2, we explain that a minor modification of the technique of Schroeppel and Shamir \[29\] performs the same scan using only _O_<sup>∗</sup>(2<sup>_n/_4</sup>) space.

Since we enumerate all elements of \(C'\), Line 5 of Algorithm 2 can be implemented in _O_<sup>∗</sup>(|_C_|) time and space. Specifically, we sort the elements of \(C'\) by the key \((\sum(X),v_X)\). Then, for each group of elements with the same value of \(\sum(X)\), we scan the corresponding vectors _v<sub>X</sub>_ and search for the complementary vector **1**-_v<sub>X</sub>_ by binary search. If such a vector is found in the same group, then we obtain a pair \((X,v_X),(Y,v_Y)\in C'\) such that \(\sum(X)=\sum(Y)\) and _v<sub>X</sub>+v<sub>Y</sub>_=**1**.

Both Algorithm 1 and the recovery of the ESS solution for the original input set _S_ require only polynomial time. Therefore, the bottleneck in Algorithm 2 is the enumeration of the set _C_. Choosing the prime-bound parameter as in Lemma 3.4 yields Theorem 3.8.

**Theorem 3.8.** _Let_ \(\ell\) _be the minimum solution size, where_ \(\epsilon n\le\ell\le(1-\epsilon)n\) _for some constant_ \(\epsilon>0\)_, and let_ \(\ell'=\ell/n\)_. Let_ \(k'\) _be a real parameter satisfying_ \(0\le k'\le\ell'/2\)_, and set the replacement count to_ \(k=\lfloor k'n\rfloor\)_. Define_ \(\mathrm{repl}(\ell',k')=H(2k')-\ell'H(2k'/\ell')\) _and_

\(\mathrm{phi}(x)=(1-x)H\left(\frac{x}{2(1-x)}\right).\) (4)

_Then there is a Monte Carlo algorithm for ESS with time complexity_ \(O^*(2^{\tau_\mathrm{rrb}(\ell^\prime,k^\prime)n})\) _and space complexity_ \(O^*(2^{\sigma_\mathrm{rrb}(\ell^\prime,k^\prime)n})\)_, where_

\(\tau_\mathrm{rrb}(\ell',k')=\left\{\begin{array}{ c c }
\ell'-k'+\mathrm{repl}(\ell',k') & \text{\textit{if}}\ell'-k'>1/2, \\
\mathrm{max}\{1-\mathrm{phi}(\ell'-k'),1/2\}+\mathrm{repl}(\ell',k') & \text{\textit{otherwise.}}
\end{array}\right.\) (5)


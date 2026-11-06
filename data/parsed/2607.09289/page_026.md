**Lemma B.1** (\[29\])**.** _Given two integer lists A and B of size at most N, the multiset_ \(C=\{\{a+b|a\in A,b\in B\}\}\) _has size at most N_<sup>2</sup> _and can be generated in ascending or descending order in O(N_<sup>2</sup>log_N_) _time using only O(N_) _additional space._

In Lemma 3.7, we use a modular version of Lemma B.1, which generates the values in ascending or descending order of their residues modulo _p_. We give pseudocode for the ascending-order version in Algorithm 5, obtained by slightly modifying the implementation of Schroeppel and Shamir \[29\].

The main modification is that we use an additional array _D_ to specify the cyclic rotation of _B_ for each element of _A_. Although Algorithm 5 outputs only the generated values, we can also return the corresponding index pair \((i,j)\in[m]\times[n]\) together with each value. The descending-order version can be obtained analogously. This gives Lemma B.2.

**Lemma B.2.** _Given two integer lists A and B of size at most N, the multiset C_={{(_a+b_)mod_p|a_\(\in A,b\in B\}\} _of size at most N_<sup>2</sup> _can be generated in ascending or descending order in O(N_<sup>2</sup>log_N_) _time using only O(N_) _additional space._

### B.3 Small-Space Algorithm for Unbalanced Equal Subset Sum

We can reduce the space usage of the _UnbalancedEqualSubsetSum_ algorithm of \[25\] from \(O^*(\genfrac(){pt}{2}{n/2}{\ell/2}2^{\ell/2})=O^*(2^\frac{n}{2}(H(\ell^\prime)+\ell^\prime))\) to \(O^*(\genfrac(){pt}{2}{n/4}{\ell/4}2^{\ell/4})=O^*(2^\frac{n}{4}(H(\ell^\prime)+\ell^\prime))\) by applying Lemma B.1. Recall that _n_ is assumed to be divisible by 12 in Section 2. For simplicity, we further assume here that \(\ell\) is divisible by 4. The case where \(\ell\) is not divisible by 4 can be handled similarly, although the floors and ceilings make the notation more cumbersome. We show the pseudocode in Algorithm 6.

Let \(A,B\subseteq S\) be a fixed minimum solution with \(|A\cup B|=\ell\). The probability that the random four-way split satisfies \(|(A\cup B)\cap S_i|=\ell/4\) for all \(i\in[4]\) is<tbc>

\(\frac{\genfrac(){pt}{2}{\ell}{\ell/4,\ell/4,\ell/4}\genfrac(){pt}{2}{n-\ell}{\genfrac(){pt}{2}{n-\ell}{n-\ell/4,(n-\ell)/4,(n-\ell)/4}}}{\genfrac(){pt}{2}{n}{n/4,n/4,n/4,n/4}}}\ge\frac{4^{\ell}{4^{n-\ell}}\genfrac(){pt}{2}{n+3}{3}^24^n}=\frac{1}{\genfrac(){pt}{2}{n+3}{3}^2}\)

<tbc>where we use

\(\frac{4^N}{\genfrac(){pt}{2}{N+3}{3}}\le\genfrac(){pt}{2}{N}{N/4,N/4,N/4,N/4}\le 4^N.\)

Thus, by repeating the algorithm poly(_n_) times, we can amplify the success probability to a constant without affecting the running time in \(O^*(\cdot)\) notation. Compared to the _UnbalancedEqualSubsetSum_ algorithm of \[25\], Algorithm 6 stores _D<sub>i</sub>_ for \(i\in[4]\) instead of _C<sub>i</sub>_ for \(i\in[2]\). Thus, the space usage is reduced from \(O^*(|C_i|)=O^*(2^\frac{n}{2}(H(\ell^\prime)+\ell^\prime))\) to \(O^*(|D_i|)=O^*(2^\frac{n}{4}(H(\ell^\prime)+\ell^\prime))\). The elements of _C<sub>i</sub>_ can be generated in the required ascending or descending order using Lemma B.1. This takes _O_<sup>∗</sup>(|_D<sub>i</sub>_|) space and _O_<sup>∗</sup>(|_C<sub>i</sub>_|) time.

## C Generalization to Target Equal-Subset-Sum

We restate Lemma 5.10 here.

**Lemma 5.10** (\[25, Appendix E of the full version\])**.** _The_ Target Equal-Subset-Sum (Target ESS) Problem _is defined as follows. Given an input set S of n integers and a target integer_ \(\kappa\)_, the task is to find two distinct subsets_ \(A,B\subseteq S\) _such that_ \(\sum(A)-\sum(B)=\kappa\)_, or to report that no such pair of subsets exists. If such subset pairs exist, let_ \(\ell\) _denote the minimum value of_ |_A_|+|_B_| _over all pairs of distinct subsets_ \(A,B\subseteq S\) _satisfying_ \(\sum(A)-\sum(B)=\kappa\)_. We define a minimum solution_<tbc>


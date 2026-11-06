<tbc>red) keys in stripe _i_. The notation \(\ell\) and _s_ are chosen to correspond with the later sections when red elements will be small and blue elements will be large.

**Theorem 1.** 2RAMSORT _has the following comparison cost complexity for the case_ \(a\le b\le c\):

\(\Theta(anlogn+b(klogn+nlogn)+c\sum_{i=1}^k\ell_ilog\ell_i)\)

_Proof._ We are interested in the version that is most relevant to us, the case when _a\<b\<c_. This is because red elements can be considered small, blue elements can be considered large, and under the natural setting where comparisons involving red elements cost less than those involving blue elements, we get that _a\<b\<c_.

**Lower bounds.** First, the number of permutations any algorithm for 2RAMSORT must achieve is at least _n_!. Any comparison reduces these by a factor of at most 2, and the cheapest comparison costs _a_, thus giving a \(alogn!=\Omega(anlogn)\) lower bound.

Second, consider the instance where the red elements are already sorted for free, the stripes of blue elements are already provided for free, and one is required to finish sorting. In this case, no comparison involving a red element is useful, the only comparisons available cost _c_, and these must be used to sort the contents of each stripe separately. This gives us a lower bound of \(\Omega(c\sum_{i=1}^k\ell_i)\).

Proving the second term as a lower bound involves the batched predecessor problem. Consider the instance where the red elements are sorted for free, and the algorithm is just required to discover the content of the _k_ blue stripes. This is identical to the batched predecessor problem on the blue elements, and any sorting algorithm also solves this subproblem.

There are at least \(\genfrac(){pt}{2}{n}{k}S(n,k)\) permutations to consider, where _S(n,k_) is the _Stirling number of the second kind_<sup>2</sup>. This is because there are \(\genfrac(){pt}{2}{n}{k}\) positions to place the blue stripes among the red elements in, and _S(n,k_) distinct possibilities for the contents of the blue stripes.

An easy lower bound on _S(n,k_) is _k_<sup>_n-k_</sup>, which is achieved by fixing an ordering of the _n_ blue elements, sending the first _k_ to a distinct subset, and now for the remaining _n-k_ blue elements one has _k_ possibilities for each one.

<sup>2</sup>this is the number of ways to partition a set of size _n_ into _k_ non-empty, disjoint subsets.


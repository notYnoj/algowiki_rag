From  2 of \[AV26\], we instantiate the constants as \(\varepsilon=0.056\), \(\kappa=0.5\), and \(\gamma=0.0653\). Then, note that \(2(\kappa-\gamma)-1=-2\gamma\) so that it suffices to balance<tbc>

\(\tilde{O}\left(N^3B^{-2\gamma} logU+N^2B^2log^2U\right).\)

<tbc>Subject to the constraint \(2BP\le N^\varepsilon\) and \(P\gg BlogU\), we set \(B\checkmark N^{\varepsilon/2}/\sqrt{logU}\) for some sufficiently small constant. Since Theorem 1.2 requires that \(\varepsilon<\varepsilon^*\) and \(\gamma\le\kappa\) which we have chosen to be \(\kappa=1/2\), the running time is

\(\tilde{O}\left(N^{3-\gamma\varepsilon} logU\right)=\tilde{O}\left(N^{2.9963432}logU\right).\)

We prove the remaining required reduction to (min,+)-Witness Equality for completeness. The proof is essentially identical to \[JPSX26\], with the only change being that the input and output matrices are not required to be monotone.

_Proof of Lemma 3.2._ We recurse on the value of _U_. In the base case where _U_=1, return (_A∗B_)\[_i,j_\]=2 for all (_i,j_).

Then, suppose _U\>_1. Without loss of generality, suppose _U_ is a power of 2. We begin by constructing matrices \(A',B'\) as follows<tbc>

\(A'=\lceil A/2\rceil,B'=\lceil B/2\rceil\)

<tbc>and recursively compute \(X'=A'*B'\). It is easy to see that \(A',B'\) have values in \[_U/_2\].

Let _X=A⋆B_. For every triple _i,k,j_, observe that<tbc>

\(2(A'[i,k]+B'[k,j]-1)\le A[i,k]+B[k,j]\le 2(A'[i,k]+B'[k,j]).\)

<tbc>Taking minima over _k_ yields

\(2X'[i,j]-2\le X[i,j]\le 2X'[i,j]\)

for every pair (_i,j_). Thus, \(X[i,j]\in\{2X'[i,j]-2,2X'[i,j]-1,2X'[i,j]\}\).

For each \(s\in\{-2,-1,0\}\) run the (min,+)-Witness Equality algorithm with candidate matrix \(C_s[i,j]=2X'[i,j]+s\in[2U]\) since \(2\le X'[i,j]\le U\). For every (_i,j_), return the smallest \(2X'[i,j]+s\) for which the (min,+)-Witness Equality algorithm reports that there exists _k_ such that

\(A[i,k]+B[k,j]=2X'[i,j]+s.\)

Note that this algorithm is correct since \(X[i,j]\in\{2X'[i,j]-2,2X'[i,j]-1,2X'[i,j]\}\), so that the minimum value with a witness must be the true value of the (min,+) product.

Let _M(N,U_) denote the time required to compute the product of two \(N\times N\) matrices with entries in \[_U_\]. By the master theorem, the total time required is

\(M(N,U)=M(N,U/2)+O\left((T(N,U)+N^2)\right)=O\left((T(N,U)+N^2)logU\right).\)

## 3.1 Derandomization

Next, we discuss how to derandomize Theorem 1.1.

_Proof of Theorem 1.3._ Observe that in the proof of Theorem 1.1 the only randomization required is to sample primes in Step 2, finding a sparse certificate. We discuss how to choose these primes deterministically below. To exploit the resulting sparsity, we search the candidate blocks depth-first and stop after finding the first witness for each output pair. We use the data structure version of Theorem 1.2 (see Corollary 31 of \[AV26\]), with parameters depending on the level, to answer the queries made by this search.


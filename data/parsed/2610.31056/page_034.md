Applying the above lemma on the random variable C with \(\theta=0\), we get

\(\mathbb{P}_\mathbf{a}\left(\text{Algorithm 3 succeeds}\right)=\mathbb{P}_\mathbf{a}(\mathcal{C}>0)\ge\frac{\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)^2}{\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)}\)<br>
\(=\Omega\left(1\right).\)

This completes the proof of Lemma 6.0.1.

## 6.2 Complexity Analysis

**Lemma 6.0.6.** _Let M,n,p, and q be the same as defined in the above problem **ACM-RESS**. Then Algorithm 3 runs in expected time_ O_<sup>⋆</sup>(M_<sup>1/4</sup>) _over the random choice of the input vector_ **a**_. Let_ T _be the running time of the algorithm. Then, we also have the following tail bound_<tbc>

\(\mathbb{P}_\mathbf{a}\left(\mathsf{T}\ge poly(n)M^{1/4}\right)=\mathcal{O}\left(\frac{1}{poly(n)}\right).\)

<tbc>_Proof._ Constructing the lists \(B_{n/2,s_0}^{(L)}\) and \(B_{n/2,s_1}^{(R)}\) can be achieved by constructing two mod-_p_ DP tables with _n/_2 elements and then by backtracking the DP table [JW24, JWZ25], this step takes time O(_np_), i.e., O(_nM_<sup>1/4</sup>). Constructing the final list requires sorting the two lists generated and then performing a binary search. This step takes time \(\tilde{\mathcal{O}}(L)\), where

\(L:=max\left\{\left|B_{n/2,s_0}^{(L)}\right|,\left|B_{n/2,s_1}^{(R)}\right|,\left|B_{s_0,s_1,s_2}\right|\right\}.\)

Hence, we need to compute the expected size of the lists generated in the algorithm.

**Expected Size of the lists.** Let \(\mathbf{v}\in\{0,1\}^{n/2}\backslash\{0^{n/2}\}\), then the probability of this vectors surviving the first level of the algorithm is 1_/p_, hence we have

\(\mathbb{E}_{\mathbf{a}^{(L)}}\left(\left|B_{n/2,s_0}^{(L)}\right|\right)=\frac{2^{n/2}-1}{p},\)<br>
\(=\mathcal{O}\left(M^{1/4}\right).\)

Since **a**<sup>(_L_)</sup> and **a**<sup>(_R_)</sup> are sets of random variables with the same distribution, we have<tbc>

\(\mathbb{E}_{\mathbf{a}^{(R)}}\left(\left|B_{n/2,s_1}^{(R)}\right|\right)=\mathbb{E}_{\mathbf{a}^{(L)}}\left(\left|B_{n/2,s_0}^{(L)}\right|\right)=\mathcal{O}\left(M^{1/4}\right).\)

<tbc>Similarly, for any vector \(\mathbf{v}\in\mathsf{A}\), the probability of these vectors surviving both levels of the algorithm is 1_/p_<sup>2</sup>_q_, hence we have

\(\mathbb{E}_\mathbf{a}\left(\left|B_{s_0,s_1,s_2}\right|\right)=\frac{\left(2^{n/2}-1\right)^2}{p^2q}=\mathcal{O}\left(M^{1/4}\right).\)


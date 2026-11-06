**Theorem 1.3.** _There is a deterministic algorithm computing the_ (min,+)_-product of two_ \(N\times N\) _matrices A,B with polynomially bounded integer entries in time_ \(\tilde{O}\left(N^{2.9963432}\right)\).

For the sake of simplicity, we present our randomized algorithm in its entirety, and then present the deterministic algorithm separately. We leave as an interesting future direction to further improve the exponent of (min,+) Matrix Multiplication, e.g. by improving the running time of thin matrix product, or to extend our improvements to real-valued matrices.

### Ongoing Work.

The main goal of this note was to give a simplified, modular approach to (min,+) Matrix Multiplication and APSP, and to contextualize the new breakthrough through existing frameworks, thereby facilitating a better intuitive understanding. Any improvement in exponents is a byproduct of that. After prompting ChatGPT with our algorithm, it has suggested further improvements of the running time, as well as extending exponent improvements to real-valued matrices using known reductions \[CVX22\], Lemma 37 of \[AV26\] and re-optimizing the parameters. We are trying to understand if these improvements fit within our simple framework.

### Statement on AI Usage.

For the randomized algorithm, we used publicly available ChatGPT Pro for verification of our approach, optimization of parameters and for numerical calculations. The subsequent ideas for the deterministic algorithm are due to ChatGPT Pro with mild supervision. We have evaluated all proposed arguments, and refined the proof and exposition of the claimed results. The paper was written by the authors, and we take full responsibility for the final manuscript.

## 2 Preliminaries

Let \[_U_\]={1_,...,U_}. log is base 2 and ln is base _e_ unless otherwise specified. For \(p\in[0,1]\), we use _H(p_)=-_p_ln_p_-(1-_p_)ln(1-_p_) to denote entropy. For a matrix _A_, let _A_\[_i,k_\] denote the (_i,k_)-th entry of _A_. For matrices _A,B_, let _AB_ denote the standard matrix product and _A∗B_ denote the (min,+) product. Let T<sub>MUL</sub>(_N_<sub>1</sub>_,N_<sub>2</sub>_,N_<sub>3</sub>) denote the time required to compute the product of a \(N_1\times N_2\) matrix and \(N_2\times N_3\) matrix. We use \(\omega\) to denote the matrix multiplication exponent, i.e. the infimum over all constants such that two \(N\times N\) matrices can be multiplied in \(N^{\omega+o(1)}\) time. It is known \(\omega\le 9/4\) \[Ope26\], although for our purposes, weaker bounds on \(\omega\) will suffice. Our algorithm makes use of the prime number theorem.

**Theorem 2.1** (Prime Number Theorem)**.** _Let_ \(\pi(x)\) _denote the number of primes at most x. The prime number theorem states that_<tbc>

\(\pi(x)=\frac{x}{lnx}(1+o(1)).\)

<tbc>_As a corollary, for any sufficiently large integer R, the number of primes in the interval_ \[_R,_2_R_\] _is_

\(\pi(2R)-\pi(R)=\Theta(R/logR).\)

## 3 Faster \(\left(min,+\right)\) Matrix Multiplication

We present the proof of Theorem 1.1.

_Proof of Theorem 1.1._ By a standard reduction (e.g. shifting all entries by a large constant), we may assume that every input value is a positive integer. We follow the framework of previous algorithms for Bounded Difference and Monotone (min,+) Matrix Multiplication.


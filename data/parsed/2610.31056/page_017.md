## Step 1: Preprocessing.

We begin by computing a sufficiently short basis of the input lattice. The following lemma provides the required basis-reduction procedure. As this is a standard step and follows from the previous works \[Sch87, SE94, GN08, ALNSD20\] we deferred the proof to Section B.

**Theorem 5.1.** _For any_ \(\kappa>0\)_, there exists a constant C\>_0 _and an algorithm such that, given an n- dimensional lattice_ L_, computes a basis_ **D**=\[**d**<sub>1</sub>_,...,_**d**_<sub>n</sub>_\] _of_ L _in time_ \(\mathcal{O}(2^{Cn/\kappa})\) _such that_ \(\|\mathbf{D}\|_2=max_{i\in[n]}\|\mathbf{d}_i\|_2\le B\cdot\lambda_n(\mathcal{L})\)_, where_ \(B=C\cdot n^\kappa\).

Let _N_ and _B_ be parameters to be chosen later. We will set them so \(\Omega(nlogn)\le N\le B\checkmark 2^{N/n}\), but for now, let us not consider an exact exponent in _n_. This parameter will correspond to the size of the instance First, it sets \(s:=4\pi\sqrt{n}N\|\mathbf{D}\|_2\) and samples _N_ lattice points using Theorem 5.2.

**Theorem 5.2.** _Let_ \(\mathcal{L}\subseteq\mathbb{R}^n\) _be a full-rank lattice. Let_ **B** _be a basis of_ L_. Then there is a randomized algorithm that on input_ **B** _and_ \(s\ge 4\pi\sqrt{n}\|\mathbf{B}\|_2\)_, outputs N_ (_independent_) _lattice points_ **x**<sup>(1)</sup>_,...,_**x**<sup>(_N_)</sup>∼D<sub>L_,s_</sub> _where_ \(N\ge 2\) _such that_

1. _The running time of the algorithm is_ \(N\cdot poly(n,bitlength(\mathbf{B}),log(s))\).<tbc>

_2._ _For any_ \(R\ge s\sqrt{nlog(N)}\)_, except with probability at most_ 2<sup>-_n_</sup>_, we have that_ \(x_j\in\mathcal{L}\cap Ball_\infty(0,R)\) _for all_ \(j\in[N]\).

An exact definition of the distribution D<sub>L_,s_</sub> is not important for the rest of the proof, as we will only use the properties of the Theorem 5.2. Sampling is a standard tool and as Theorem 5.2 follows from \[MR07\] we defer the proof to Section A

Notice that using the above theorem, the reduction can efficiently generate samples whose joint distribution is negligibly close to that of _N_ independent samples from D<sub>L_,s_</sub>. Moreover, this choice of _s_ also yields the \(\ell_\infty\) bound on all sampled vectors required later in the analysis, except with probability at most 2<sup>-_n_</sup>. The sampler may produce the same lattice point more than once. One could simply abort in this case, since such an event occurs with negligible probability. However, this is unnecessary for our proof, as repeated samples are handled directly in the correctness analysis.

## Step 2: From Lattice Samples to a Candidate Lattice Vector.

Next, the reduction converts the sampled lattice points into positive integers. To do this, it first samples _r_<sub>1</sub>_,...,r<sub>n</sub>_ independently and uniformly from the set of primes in {1_,...,N_<sup>3</sup>}. This can be implemented by enumerating all primes in {1_,...,N_<sup>3</sup>} in time _N_<sup>O(1)</sup> \[AKS04\] and then sampling uniformly from this set<sup>12</sup>. It also samples _s_<sub>1</sub>_,...,s<sub>n</sub>_ independently and uniformly from {1_,...,N_<sup>2</sup>}.

Next, the reduction enumerates powers of two in the range \([2^{\lceil log(\|\mathbf{D}\|)\rceil},\dots,2^{\lceil log(\|\mathbf{D}\|-log(B))\rfloor}]^\text{13}\) to obtain a value \(\tilde{\lambda}_n\) satisfying \(\lambda_n(\mathcal{L})\le\tilde{\lambda}_n\le 2\lambda_n(\mathcal{L})\). For each guess, the reduction performs the following two steps.

## Step 2a: Integer Encoding.

Using the random choices \(\{r_j,s_j\}_{j\in[n]}\), define

\(f(\mathbf{x}):=W^n+\sum_{j=1}^nW^{j-1}\left\lfloor\frac{(\mathbf{x})_j\cdot\tilde{\lambda}_n^{-1}+s_j}{r_j}\right\rfloor,\)

where _W_:=8_BN_<sup>3</sup>. Finally, for each \(i\in[N]\), the reduction sets _a<sub>i</sub>_:=_f_(**x**<sup>(_i_)</sup>) and defines the PESS instance as A:=(_a_<sub>1</sub>_,...,a<sub>N</sub>_).

Notice that the parameter _W_ is chosen large enough so that, for the correct guess \(\tilde{\lambda}_n\), there are no carries between different base-_W_ digits, while the additive term _W<sup>n</sup>_ ensures that _f_(**x**) is positive for every sampled lattice point **x**<sup>(_i_)</sup> except with negligible probability.

<sup>12</sup>Alternatively, one could repeatedly sample a random integer and test whether it is prime. However, this would yield only an expected-time procedure for sampling a uniformly random prime from the interval. <sup>13</sup>From Theorem 5.1, we have \(\|\mathbf{D}\|_2\le B\cdot\lambda_n(\mathcal{L})\) which implies \(\lambda_n(\mathcal{L})\ge\|\mathbf{D}\|_2/B\). On the other hand, \(\lambda_n(\mathcal{L})\le\|\mathbf{D}\|_2\).


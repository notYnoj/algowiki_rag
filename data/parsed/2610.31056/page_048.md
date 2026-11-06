## A Sampling Lattice Points

**Definition 5** (Discrete Gaussian Distribution over a Lattice)**.** _For any vector_ \(\mathbf{c}\in\mathbb{R}^n\)_, real s\>_0 _and a lattice_ \(\mathcal{L}\subset\mathbb{R}^n\)_, the probability distribution_ D<sub>L_,s,_**c**</sub> _over_ L _is defined as_

\(\mathcal{D}_{\mathcal{L},s,\mathbf{c}}(x)=\frac{\rho_{s,\mathbf{c}}(x)}{\rho_{s,\mathbf{c}}(\mathcal{L})},\forall\mathbf{x}\in\mathcal{L}\)

_where_ \(\rho_{s,\mathbf{c}}(\mathbf{x})=e^{-\pi\|(\mathbf{x}-\mathbf{c})/s\|^2}\) _and_ \(\rho_{s,\mathbf{c}}(\mathcal{L})=\sum_{\mathbf{x}\in\mathcal{L}}\rho_{s,\mathbf{c}}(\mathbf{x})\).

For simplicity, we use D<sub>L_,s_</sub> to denote D<sub>L_,s,_**0**</sub> and \(\rho_s\) to denote \(\rho_{s,\mathbf{0}}\).

**Definition 6** (\[MR07\])**.** _For any n-dimensional lattice_ L _and positive real_ \(\epsilon>0\)_, the smoothing parameter_ \(\eta_\epsilon(\mathcal{L})\) _is the smallest real s\>_0 _such that_ \(\rho_{1/s}(\mathcal{L}^*\backslash\{0\})\le\epsilon\)_. Here,_ \(\mathcal{L}^*=\{\mathbf{y}\in\mathbb{R}^n|\langle\mathbf{x},\mathbf{y}\rangle\in\mathbb{Z},\forall\mathbf{x}\in\mathcal{L}\}\) _is the dual lattice of_ L.

**Theorem A.1** (\[GPV08, Lemma 3.1\])**.** _For any n-dimensional lattice_ L _spanned by a basis_ **B** _and positive real_ \(\epsilon>0\)_, we have_

\(\eta_\epsilon(\mathcal{L})\le B\sqrt{\frac{log(2n(1+1/\epsilon))}{\pi}}\)

_where_ \(B=\|\mathbf{B}\|_2\)_. In particular, for_ \(\epsilon=2^{-n}\)_, we have_ \(\eta_\epsilon(\mathcal{L})\le 2B\sqrt{n}\).

**Theorem A.2** (Discrete Gaussian sampling from a basis \[GPV08, Theorem 4.1\])**.** _Let_ \(\mathcal{L}\subset\mathbb{R}^n\) _be a full-rank lattice and let_ **B**=(**b**<sub>1</sub>_,...,_**b**_<sub>n</sub>_) _be any basis of_ L_. Let_ \(\widetilde{\mathbf{B}}=(\widetilde{\mathbf{b}}_1,\dots,\widetilde{\mathbf{b}}_n)\) _be the Gram-Schmidt orthogonalization of_ **B**_. Fix any center_ \(c\in\mathbb{R}^n\) _and any parameter_

\(s\ge\|\widetilde{\mathbf{B}}\|_2\cdot\omega(\sqrt{logn}).\)

_Then there exists a randomized algorithm_ SampleD(_B,s,c_) _running in time_ poly(_n,_bitlength(**B**),log_s_) _that outputs a vector_ \(\mathbf{x}\in\mathcal{L}\) _whose distribution is within negligible statistical distance of the discrete Gaussian distribution_ D<sub>L_,s,_**c**</sub> _over_ L.

The goal of this section is to prove the following theorem:

**Theorem 5.2.** _Let_ \(\mathcal{L}\subseteq\mathbb{R}^n\) _be a full-rank lattice. Let_ **B** _be a basis of_ L_. Then there is a randomized algorithm that on input_ **B** _and_ \(s\ge 4\pi\sqrt{n}\|\mathbf{B}\|_2\)_, outputs N (independent) lattice points_ **x**<sup>(1)</sup>_,...,_**x**<sup>(_N_)</sup>∼D<sub>L_,s_</sub> _where_ \(N\ge 2\) _such that_

1. _The running time of the algorithm is_ \(N\cdot poly(n,bitlength(\mathbf{B}),log(s))\).<tbc>

_2._ _For any_ \(R\ge s\sqrt{nlog(N)}\)_, except with probability at most_ 2<sup>-_n_</sup>_, we have that_ \(x_j\in\mathcal{L}\cap Ball_\infty(0,R)\) _for all_ \(j\in[N]\).

_Proof of Theorem 5.2._ We describe the sampler and then prove the claimed properties.

### The sampler.

Sample **x**<sup>(1)</sup>_,...,_**x**<sup>(_N_)</sup> independently from the discrete Gaussian distribution D<sub>L_,s_</sub> over L, and output these samples. This can be performed using the algorithm in Theorem A.2 in time poly(_n,_bitlength(**B**),log(_s_)) given a basis **B** of L and _s_ which is clearly satisfy the theorem condition. Hence _N_ independent samples can be generated in time \(N\cdot poly(n,bitlength(\mathbf{B}),log(s))\).<tbc>


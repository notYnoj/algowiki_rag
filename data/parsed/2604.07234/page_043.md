<tbc>where \(\langle\cdot\rangle_{N,M}\) denotes the Gibbs average, i.e., the expectation with respect to the uniform law over the (random) set _S<sub>X,Y</sub>_. Assuming that the cavity field \(\langle\sigma_1\neq 1\rangle_{N,M}\) converges in law to a random variable \(P(\alpha)\) as \(N,M\rightarrow\infty\) with \(M/N=\alpha\), then that would imply

\(f_\mathrm{pl}(\alpha)=-\int_0^{1-\alpha}\mathbb{E}\left[\mathrm{log}P\big(\frac{\alpha}{\alpha+x}\big)\right]dx.\)

Thus, the challenge in this approach is to derive a plausible closed-form description for the limit law of the cavity field \(P(\alpha)\). In the context of mean-field spin glasses, this is often obtained as a consequence of a self-consistency relation. We have not been able to find such a relation.

### 5.2. Mean-field versus rank-one free energies.

The natural mean-field version of the null Random Subsequence Model is where one replaces the "rank one" matrix \(B_{ij}=\unknown\{X_i=Y_j\}\) by a matrix with i.i.d. entries drawn from a common distribution D (see Section 1.1.3). The choice of D closest to the true Random Subsequence Model is D=Unif{0,1}, which has been studied under the name "Bernoulli Matching Model" in relation to the longest common subsequence problem \[Bou99; MN05\]. The case where D=Gamma(_a,b_) corresponds to the Strict-Weak lattice polymer \[CSS15\]. Let \(f^\mathrm{BMM}(\alpha)\) and \(f^\mathrm{SW}(a,b)(\alpha)\) denote their (quenched) free energies, respectively. To what extent do these quantities relate to or control the Random Subsequence Model’s free energy? We pose the following conjecture.

**Conjecture 5.2.** _For all_ \(\alpha\in[0,1]\)_, it holds that_

\(f_\mathrm{null}(\alpha)\le f^\mathrm{BMM}(\alpha)\le f^{\mathrm{SW}(1,1/2)}(\alpha).\)

We recall that the experience in the directed polymers literature suggests that only problems with special algebraic structure admit exact analytic solutions, which represents an important barrier to obtaining exact formulas for the free energy of the Random Subsequence Model. Moreover, while the solvable Strict-Weak Polymer Model is an analogue of the null Random Subsequence Model, as far as the authors are aware, no solvable analogue (in this sense) of the _planted_ Random Subsequence Model is known. Indeed, the planted structure already seems to break the requisite algebraic structure. The next open problem suggests such an analogue. We see this model as breaking the algebraic structure in the minimal way, and hence view it as a promising stepping stone towards the Random Subsequence Model.

**Problem 5.3.** _Let_ \(B\in\mathbb{R}_+^{N\times M}\) _have i.i.d._ Gamma(_a,b_) _entries. Independently, sample_ \(\sigma^*\sim\Sigma_{NM}\)_, and for every j_=1_,...,M, over-write_ \(B_{\sigma(j),j}=1\)_. Let Z<sub>NM</sub> be the corresponding free energy obtained from_ (1.5)_, and define_

\(f_\mathrm{pl}^{\mathrm{SW}(a,b)}(\alpha)=\mathrm{lim}_{N,M\rightarrow\infty M/N=\alpha}\frac{1}{N}\mathbb{E}\left[\mathrm{log}Z_{NM}\right].\)

_Find an exact analytic formula for_ \(f_\mathrm{pl}^{\mathrm{SW}(a,b)}(\alpha)\).

### 5.3. Asymptotics in the likely deletion regime.

Corollary 1.2 establishes that the uniform capacity of the deletion channel is strictly positive for every _p\<_1. However, the explicit lower bound extracted from our argument in Theorem 3.13 is too small to capture the asymptotic behavior of \(f_\mathrm{pl}(\alpha)\) as \(\alpha=1-p\rightarrow 0\). It remains open to determine the asymptotic order of magnitude of \(f_\mathrm{pl}(\alpha)\) as \(\alpha\rightarrow 0\), which would be very interesting.

## Acknowledgments

R.J. would like to thank Robin Pemantle for early encouragement to work on this problem and for responding to several ideas and questions that he had over its duration. We both especially thank Brice Huang, and F.P. especially thanks Hang Du, for several valuable discussions about this project. We are grateful to Amir Dembo, Nike Sun, Shuangping Li, and Tselil Schramm for helpful conversations while this work was in development. Finally, we thank Timo Seppäläinen for answering our questions on the work \[CSS15\].


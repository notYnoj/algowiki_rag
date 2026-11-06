An \((\varepsilon,\delta)\)-approximation of ED/LCS is an estimate within \([A,(1+\varepsilon)A+\delta]\) where _A_ is the true ED/LCS.

**Lemma A.1** (Estimate-to-Search)**.** _Given an algorithm_ A _that runs in time_ \(n^2/2^{\mathrm{log}^{\Omega(1)}(n)}\) _and estimates the ED/LCS between two input strings X,Y of lengths n<sub>X</sub>,n<sub>Y</sub>=O(n_) _to within_ \((\varepsilon(n),2^{\mathrm{log}^{\Omega(1)}(n)})\)_-approximation (i.e., the multiplicative approximation factor is a function on n), we obtain an algorithm_ \(\mathcal{A}'\) _that, runs in time_ \(n^2/2^{\mathrm{log}^{\Omega(1)}(n)}\) _and finds a transformation whose answer is an_ \((\varepsilon(\Theta(\sqrt{n})),2^{\mathrm{log}^{\Omega(1)}(n)})\)_-approximation of the optimal answer._

_Proof._ Let \(\gamma=2^{\mathrm{log}^c(n)}\) for some constant _c\>_0 be such that the running time of A is \(T(\mathcal{A},n)=O\left(n^2/2^{\mathrm{log}^{2c(n)}}\right)\). Let \(\mu=2^{\lfloor\mathrm{log}(n)/2\rfloor}=\Theta(\sqrt{n})\). We say a path _p_ on the Rotated Edit Distance/LCS Grid Graph is \(\gamma\)-rounded if for every \(\mu|x\), we have \(\lfloor\mu/\gamma\rfloor|p(x)\).

We can round the optimal path _p_ to a \(\gamma\)-rounded path using Lemma 5.9, incurring an additive error of only \(O(\sqrt{n}\cdot(\sqrt{n}/\gamma))=O(n/\gamma)=n/2^{\mathrm{log}^{\Omega(1)}(n)}\). Thus it suffices to find the optimal \(\gamma\)-rounded path.

Using A, we can approximate the length of the optimal \(\langle x,y\rangle\)-\(\langle x+\mu,y'\rangle\) path for every \(\mu|x\), \(\lfloor\mu/\gamma\rfloor|y,y'\) with \(|y-y'|\le\mu\). Since for each path we only need a \(\Theta(\mu)\cdot\Theta(\mu)\) sub-grid, the total running time is

\(O\left(\underbrace{\sqrt{n}\cdot 2^{\mathrm{log}^c(n)}\sqrt{n}}_\text{total number of sub-grids}\cdot\underbrace{\left(\sqrt{n}\right)^2/2^{\mathrm{log}^{2c}(\sqrt{n})}}_\text{time for each sub-grid}\right)=n^2/2^{\mathrm{log}^{\Omega(1)}(n)}.\)

We can use standard dynamic programming on a \(\gamma\)-rounded path \(\widehat{p}\) that is optimal with respect to the estimates computed by A. This gives us an \((\varepsilon(\Theta(\sqrt{n})),2^{\mathrm{log}^{\Omega(1)}(n)})\)-approximation of the optimal answer. This gives us \(\widehat{p}(x)\) for every column \(\mu|x\).

Finally we can fully recover \(\widehat{p}\) by using an exact algorithm for each of the sub-grids that contain a sub-path of \(\widehat{p}\). The exact algorithm runs in time quadratic in the side-length of the underlying sub-grids. Hence the total time of this part is

\(O\left(\underbrace{\sqrt{n}}_\text{number of sub-paths}\cdot\underbrace{\sqrt{n}\cdot\sqrt{n}}_\text{time for each sub-path}\right)=O(n^{1.5}).\)

## B An Information-Theory-Based Tree Total Deviation Upper Bound

In this section, we present an alternative proof for a stronger version of Lemma 4.1 using information- theoretic tools. Specifically, we relate the notion of tree total deviation to the relative entropy (Kullback- Leibler divergence) between the normalized sequence _A_ and the uniform distribution.

**Lemma B.1.** _Let A_=(_a_<sub>1</sub>_,...,a<sub>n</sub>_) _be a sequence of real numbers with n=M<sup>S</sup>. Let_ \(\|A\|_1:=\sum_x|a_x|\) _and_ \(\|A\|_\infty:=\mathrm{max}_x|a_x|\)_. Then,_<tbc>

\(\includegraphics{}\text{\textit{T}}_{M,S}(A)\le\|A\|_1\sqrt{2S\mathrm{ln}\left(\frac{n\|A\|_\infty}{\|A\|_1}\right)}.\)


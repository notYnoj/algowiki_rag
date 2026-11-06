with probability at least 1/2. Combining this with the earlier comparison between the original and modified reductions, we conclude that the original reduction fails with probability at most

\(\frac{1}{2}+2^{-n}+\mathcal{O}\left(\frac{n}{N}+\frac{nlog(BN)logN}{N^2}\right)+\text{PESS}_\text{err}.\)

where PESS<sub>err</sub> is the probability that the PESS algorithms fails to return a valid solution. Since \(\Omega(nlogn)\le N\le B\checkmark 2^{N/n}\), and assuming the PESS<sub>err</sub> is negligible (or even smaller than than 1/2-1/poly(_n_)), the additive term above is 1-1/poly(_n_). Therefore, by repeating the original reduction independently polynomially many times and returning the shortest nonzero vector obtained, the overall failure probability becomes negligible. This concludes the proof of Property Item (3).

## 5.3 Proof of Theorem 1.2

In this section, we conclude the proof of Theorem 1.2. First, we prove a bit more precise statement for the \(M^{\Omega(1/logN)}\) lower bound:

**Lemma 5.2.1.** _Under Hypothesis 1, there exists_ \(\varepsilon>0\) _such that there does not exist an algorithm that is given a set_ \(S\subseteq\{1,\dots,M\}\) _of size N, with probability_ \(>3/4\) _finds two different_ \(A,B\subseteq S\)_, and runs in time_ \(poly(N)\cdot M^{\varepsilon/logN}\) _(even when_ \(M=2^{\Theta(\sqrt{N}logN)}\)).

_Proof._ We set _N=n_<sup>2</sup>. Let _c_:=10. By Hypothesis 1, there exists \(\delta_H>0\) such that there is no algorithm running in time \(2^{\delta_Hn}\) that given an _n_-dimensional lattice L find a non-zero vector _v_ with \(\|v\|\le n^{10}\cdot\lambda_n(\mathcal{L})\). Based on this, we select \(\kappa:=C/(2\delta_H)\), where _C_ is a constant in Theorem 5.1, and use Theorem 5.1 to compute a basis **D** in time \(\mathcal{O}(2^{Cn/\kappa})\le\mathcal{O}(2^{\delta_Hn/2})\). This fixes the choice of \(B=C\cdot n^\kappa\).

Notice that indeed \(\Omega(nlogn)\le N\le B\checkmark 2^{N/n}\), hence the parameters are set up correctly. Recall that _W_=8_BN_<sup>3</sup> and _M_=2_W<sup>n</sup>_, hence \(M\le 2^{2\kappa nlogn}\), because we can assume that \(\kappa,C\checkmark n\) as otherwise the instance can be solved in constant time (as \(\kappa\) and _C_ are constant). Notice that \(M=2^{\Theta(\sqrt{N}logN)}\)

We now analyze the running time of Algorithm 2 and derive the final contradiction to Hypothesis 1.

### Running time of the reduction.

We bound the running time of each stage of the algorithm, except that the oracle call to PESS is:

• By Theorem 5.1, the initial basis-reduction step runs in time \(\mathcal{O}(2^{\delta_Hn/2})\) time.<tbc>

• The sampling step uses Theorem 5.2 with \(s=4\pi\sqrt{n}N\left\|\mathbf{D}\right\|_2\). Since \(\left\|\mathbf{D}\right\|_2\le B\lambda_n(\mathcal{L})\), we have \(logs=\tilde{\mathcal{O}}(n)\), and hence this step runs in time \(N\cdot poly(n\cdot\text{bitlength}(\mathbf{D})\cdotlogs)\) which is polynomial in _n_.<tbc>

• Sampling the primes _r_<sub>1</sub>_,...,r<sub>n</sub>_ and the shifts _s_<sub>1</sub>_,...,s<sub>n</sub>_ takes time _N_<sup>O(1)</sup>, since primality testing is polynomial-time in the bitlength of the input \[AKS04\].<tbc>

• Constructing the integers _a_<sub>1</sub>_,...,a<sub>N</sub>_ and the corresponding PESS instance takes time polynomial in _N_, namely \(N\cdot poly(n\cdot logW)\).<tbc>

• The remaining vector-reconstruction and final minimization steps take time at most poly(_n_). The loop over guesses of \(\tilde{\lambda}_n\) runs for only \(poly(n\cdot log\left\|\mathbf{D}\right\|_2)\) iterations, and this factor is absorbed into the \(\mathcal{O}(\cdot)\) notation. All these steps, took time \(poly(n)\cdot 2^{\delta_Hn/2}\). It remains to analyze the cost of the PESS oracle. Assume for the sake of contradiction that for every \(\varepsilon>0\), there exists an algorithm that solves PESS in time \(poly(N)\cdot M^{\varepsilon/logN}\). Set \(\varepsilon=\delta_H/(4\kappa)\) and observe that we have poly(_n_) calls<tbc>


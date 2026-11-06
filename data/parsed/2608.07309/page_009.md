The pseudocode is presented in Algorithm 1.

**Algorithm 1** Quantum _k_-SUM Algorithm

**Input:** Integer lists _A_<sub>1</sub>_,...,A<sub>k</sub>_, block sizes _k_<sub>1</sub>_,k_<sub>2</sub>_,k_<sub>3</sub>_,k_<sub>4</sub>, and a parameter \(r\in(0,\mathrm{min}\{k_2,k_4\}]\).

**Output:** A tuple of indices \((i_1,\dots,i_k)\in[n]^k\) satisfying \(\sum_{j=1}^kA_j[i_j]=0\), if one exists, and NO otherwise.

1: Partition the lists into four blocks of sizes (_k_<sub>1</sub>_,k_<sub>2</sub>_,k_<sub>3</sub>_,k_<sub>4</sub>)

2: Set \(m\leftarrow\lfloor n^r/2\rfloor\) and choose a prime \(p\in_R\mathcal{P}\)

3: Run a quantum walk over G:

4: Quantum search over \(q\in\mathbb{Z}_p\)

5: Construct _F<sub>v,q</sub>_ and _G<sub>v,q</sub>_ and run Claw Finding on them

6: **if** a claw is found **then**

7: **return** the indices corresponding to the found claw

8: **end if**

9: **return** NO

## 3.3 Correctness

The algorithm cannot output an incorrect solution; so it remains to show that, whenever a solution exists, the algorithm finds one with constant probability. Fix a solution \(\alpha^*=(\alpha_1^*,\alpha_2^*,\alpha_3^*,\alpha_4^*)\), and let \(z_2^*=\Sigma_2(\alpha_2^*)\) and \(z_4^*=\Sigma_4(\alpha_4^*)\). We say that \(z_2^*\) is _exposed_ at a vertex if the canonical representative of its residue has exact sum \(z_2^*\), and define exposure of \(z_4^*\) analogously.

Let V<sup>∗</sup> be the set of vertices whose two sampled subsets contain \(\alpha_2^*\) and \(\alpha_4^*\). For a fixed prime _p_, call a vertex \(v\in\mathcal{V}^*\) _successful_ if both target sums \(z_2^*\) and \(z_4^*\) are exposed at _v_. Call _p good_ if at least half of the vertices in V<sup>∗</sup> are successful.

**Lemma 3.1.** _A prime_ \(p\in_R\mathcal{P}\) _is good with constant probability._

_Proof._ Fix a vertex \(v\in\mathcal{V}^*\). For \(i\in\{2,4\}\), an entry \(x\in S_i\) with \(\Sigma_i(x)\neq z_i^*\) can lie in the same residue bucket as \(z_i^*\) only if _p_ divides \(\Sigma_i(x)-z_i^*\). The difference \(\Sigma_i(x)-z_i^*\) is nonzero and has absolute value \(\widetilde{O}(n^k)\), therefore applying Proposition 2.3 bounds the collision probability by

\(O\left(\frac{\mathrm{log}\widetilde{O}(n^k)}{m\mathrm{log}^2n}\right)=O\left(\frac{k}{m\mathrm{log}n}\right)=O\left(\frac{1}{m\mathrm{log}n}\right),\)

where the last equality uses that _k_ is fixed. A union bound over at most 2_m_ tuples in the two sampled subsets shows that, except with probability _O_(1/log_n_), both relevant buckets contain only entries of exact sums \(z_2^*\) and \(z_4^*\), respectively; in particular, _v_ is successful. So, the expected fraction of unsuccessful vertices of V<sup>∗</sup> is _O_(1/log_n_). Markov’s inequality now implies that more than half of the vertices of V<sup>∗</sup> are unsuccessful with probability _O_(1/log_n_).

Every successful vertex belongs to M_<sub>p</sub>_, hence if _p_ is good, at least half of V<sup>∗</sup> is contained in M_<sub>p</sub>_, and then

\(\frac{|\mathcal{M}_p|}{|V(\mathcal{G})|}\ge\frac{1}{2}\frac{|\mathcal{V}^*|}{|V(\mathcal{G})|}=\frac{1}{2}\frac{m^2}{n^{k_2+k_4}}=\Omega(n^{2r-k_2-k_4}).\) (1)

By Lemma 3.1, the bound in Equation (1) holds with constant probability over the choice of _p_. The residue search and the claw-finding procedure are amplified to error \(n^{-\omega(1)}\), as required by Theorem 2.6. Thus the algorithm finds a solution with constant probability whenever one exists.<tbc>


To complete the proof of Lemma 2.1, note that Corollary 2.4 gives the desired runtime and approximation ratio in expectation. Thus it suffices to run multiple iterations of this algorithm to obtain our desired probability of failure.

_Proof of Lemma 2.1._ Let _G_ be a given 3-colorable graph. Let B(_G,r_) denote the algorithm given by Corollary 2.4, and let \(T'(n,r)=O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}r}{r^3}\right)\right)\right)\) denote the expected runtime of _B(G,r_). We run _B(G,r/_2) _r_ times and output the maximum independent set given. If the total runtime exceeds \(5rT'(n,r/2)\), we terminate the algorithm.

By construction, this algorithm runs in time \(O(rT'(n,r/2))=O^*\left(exp\left(\tilde{O}\left(\frac{nlogr}{r^3}\right)\right)\right)\). By Markov’s inequality, the probability that the total runtime exceeds \(5rT'(n,r/2)\) is at most \(\frac{1}{5}\). Thus it remains to bound the error probability given that we successfully complete _r_ iterations of _B(G,r/_2).

Fix a single run of _B(G,r/_2), and let _S_ be the resulting independent set. To bound the probability that _S_ is small, note that \(\mathbf{Pr}[|S|\le\alpha(G)/r]=\mathbf{Pr}[\alpha(G)-|S|\ge\alpha(G)(1-1/r)]\). Since \(|S|\le\alpha(G)\), we can apply Markov’s inequality to obtain

\(\mathbf{Pr}[\alpha(G)-|S|\ge\alpha(G)(1-1/r)]\le\frac{\mathbf{E}[\alpha(G)-|S|]}{\alpha(G)(1-1/r)}=\frac{\alpha(G)(1-2/r)}{\alpha(G)(1-1/r)}=1-\frac{1}{r-1}.\)

Thus the probability that none of the _r_ runs of _B(G,r/_2) give an independent set of size at least \(\alpha(G)/r\) is at most \((1-1/(r-1))^r\le 1/e\). Combining with the runtime error, we get a total probability of failure of at most \(\frac{1}{5}+\frac{4}{5e}<1/2\).

## 2.2 Graph Coloring

In this section, we refer to the algorithm given by Lemma 2.1 as IS(_G,r_) for consistency with the notation used in \[3\]. To prove Theorem 1.1, we follow the same general approach outlined by Bansal et. al. in \[3\] with IS(_G,r_) as a subroutine. For completeness, we describe the full algorithm and analysis below. Let \(t=\frac{n}{r^3}\), \(r'=r/log(n/t)=\frac{r}{logr^3}\).

**Algorithm 1** _r_-Approximate Graph Coloring

1: \(c\leftarrow 0\)

2: **while** \(|V|\ge t\) **do**

3: \(c\leftarrow c+1\)

4: \(C_c\leftarrow\emptyset\)

5: **for** _i_=1_,...,n_ **do**

6: \(C_c\leftarrow argmax(|C_c|,|\text{IS}(G[V],r')|)\)

7: **end for**

8: \(V\leftarrow V\backslash C_c\)

9: **end while**

10: \((C_{c+1},C_{c+2},C_{c+3})\leftarrow\) brute force optimum coloring of _G_\[_V_\]

11: **return** (_C_<sub>1</sub>_,...,C_<sub>_c_+3</sub>)

**Claim 2.5.** _For a fixed iteration c of Algorithm 1,_ \(C_c\ge\frac{|V|}{3r'}\) _with probability at least_ 1-(1/2)_<sup>n</sup>._

_Proof._ At iteration _c_, _G_\[_V_\] must have an independent set of size at least |_V_|/3, since _G_ is 3-colorable and removing vertices cannot increase the chromatic number. By Lemma 2.1, for each \(i\in[n]\), the<tbc>


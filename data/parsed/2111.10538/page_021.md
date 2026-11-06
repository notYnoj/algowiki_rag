_Proof._ By Lemma 3.7, we assume that no edge (_i,j_) in \(\mathsf{NG}_\lambda\) is well-connected. In other words, for all pairs of windows (_w<sub>i</sub>,w<sub>j</sub>_) that are connected in \(\mathsf{NG}_\lambda\), there are at most \(k^{2-\gamma}\) pairs of windows (_w<sub>a</sub>,w<sub>b</sub>_) such that \(\langle w_i,w_a,w_b,w_j\rangle\) is \((\epsilon,\lambda)\)-constructive.

Recall that for a tuple \(\langle w_i,w_a,w_b,w_j\rangle\) to be undetected-constructive, edge (_i,j_) should belong to \(\mathsf{NG}_\lambda\). For a fixed (_i,a,b,j_), the probability that we keep it in \(\mathsf{NF}_\lambda\) is _p_<sup>4</sup>. Therefore, the expected number of undetected-constructive tuples in \(\mathsf{NF}_\lambda\) is bounded by

\(\mathbb{E}[\#\text{undetected-constructive tuple}]\le k^2k^{2-\gamma}\cdot p^4=1/256\)

where the last step follows from \(p=k^{-1+\gamma/4}/4\).

By Markov’s inequality, we have

\(\mathrm{Pr}[\#\text{undetected-constructive tuple}\ge 1/2]\le\frac{\mathbb{E}[\#\text{undetected-constructive tuple}]}{1/2}<1/100.\)

Thus, with probability 0.99, there is no undetected-constructive tuple in \(\mathsf{NF}_\lambda\).

## 3.1.2 Proof of Lemma 3.4, part 2: \(\mathsf{NF}_\lambda\) contains an undetected-constructive tuple

Now we assume by contradiction that the \(\mathsf{NG}_\lambda\) is dense. To simplify the notation, we introduce another parameter,

\(\beta:=\gamma\epsilon\lambda^3/(80\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap}).\)

Note that \(\beta<\gamma-\Omega(1)\).

We are able to show that if \(\mathsf{NG}_\lambda\) is dense, so is \(\mathsf{NF}_\lambda\).

**Claim 3.9** (\(\mathsf{NF}_\lambda\) is a dense graph)**.** _If for some_ \(0<\beta<\gamma/4-\Omega(1)\), \(\mathsf{NG}_\lambda\) _contains is at least_ \(k^{2-\beta}\) _edges then with probability at least_ 0.98 _we have_

\(|E(\mathsf{NF}_\lambda)|\ge\frac{|V(\mathsf{NF}_\lambda)|^{2-4\beta/\gamma}}{128}.\)

The proof of Claim 3.9 uses the following elementary graph theory fact:

**Fact 3.10.** _In every graph G_=(_V,E), we have_<tbc>

\(\sum_v\mathrm{deg}(v)^2\le 2|V||E|.\)

<tbc>_Proof._

\(\sum_v\mathrm{deg}(v)^2\le|V|\sum_v\mathrm{deg}(v)\le 2|V||E|.\)

_Proof of Claim 3.9._ Based on the sampling rate, we know that the following holds in expectation:

\(\mathbb{E}[|V(\mathsf{NF}_\lambda)|]=p|V(\mathsf{NG}_\lambda)|=k^{\gamma/4}/4,\) (1)

and<tbc>

\(\mathbb{E}[|E(\mathsf{NF}_\lambda)|]\ge p^2|E(\mathsf{NG}_\lambda)|\ge k^{\gamma/2-\beta}/16.\)


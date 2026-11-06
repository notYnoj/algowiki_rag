as a result, the good men can only be incident with a small fraction of blocking pairs.

**Lemma 4.2** ((2_/k_)-blocking-stability of good men)**.** Let \(m\in G\) be good. Then _m_ is not incident with any (2_/k_)-blocking pairs.

_Proof._ Suppose \(m\in G\) and that (_m,w_) is (2_/k_)-blocking. First consider the case where _m_ is matched, \(p(m)\neq\emptyset\). Since _m_’s preferences are divided into _k_ quantiles, _w_ must be in a strictly better quantile than _p(m_). Thus, _m_ must have proposed to _w_ in a strictly earlier call to **QuantileMatch** than the call in which he was matched with _p(m_). Thus, by Lemma 3.2, _m_ must have been rejected by _w_, implying that _w_ was matched with a man \(m'\) in the same or better quantile than _m_ in this round. By Lemma 3.1, _w_’s partner when **ASM** terminates is at least as desirable as \(m'\). This contradicts that (_m,w_) is \(\varepsilon\)-blocking.

On the other hand, if \(p(m)=\emptyset\), then since _m_ is good, he must have been rejected by all of his acceptable partners, and in particular, by _w_. Thus, as in the previous paragraph, _w_ must be matched with a man in the same or better quantile than _m_.

**Lemma 4.3** (Few non-(2_/k_)-blocking pairs)**.** There are at most 4|_E|/k_ blocking pairs which are not (2_/k_)-blocking.

_Proof._ Suppose (_m,w_) is a blocking pair which is not (2_/k_)-blocking. Thus, we have<tbc>

\(P^m(w)-P^m(p(m))\le 2deg(m)/k\text{or}P^w(m)-P^w(p(w))\le 2deg(w)/k,\) (1)

<tbc>where by convention we take \(P^m(\emptyset)=deg(m)+1\). Let _E<sub>N</sub>_ denote the set of blocking pairs which are not (2_/k_)-blocking. For each _m_, the number of edges satisfying the first inequality in (1) is at most 2deg(_m)/k_, and similarly for the women. Thus

\(|E_N|\le\sum_{m\in Y}2deg(m)/k+\sum_{w\in X}2deg(w)/k=4|E|/k,\)

as desired.

Lemma 4.3 shows that no good player is involved in any (2_/k_)-blocking pairs. Combining Lemmas 4.2 and 4.3, we can bound the number of blocking pairs incident with good men. All that remains is to bound the number of (2_/k_)-blocking pairs incident with bad men. In the next section, we show that the proportion of bad men is small (at most \(\delta n\)), and bound the number of (2_/k_)-blocking pairs they contribute. We remark that by Lemma 4.3 and the lower bound of Kipnis and Patt-Shamir \[9\], we cannot hope to have all men be good in \(o(\sqrt{n}/logn)\) rounds.

## 4.2 Bounding blocking pairs from bad players

In this section, we prove the following bound on the number of blocking pairs contributed by the bad men at the termination of **ASM**. Throughout the section, for simplicity of notation, we assume that log_n_ is an integer.

**Lemma 4.4** (Bad men guarantee)**.** At the termination of **ASM**, for any \(\delta\le\frac{1}{2}\) the bad men contribute at most \(4\delta|E|(2/k)\)-blocking pairs.

The proof of Lemma 4.4 is in two parts corresponding to guarantees for each of the two nested loops in **ASM**. We refer to men _m_ with \(|Q^m|\ge 2^i\) as **_active in the ith iteration_** of the outer loop; the remaining men are **_inactive_** in the _i_th iteration.

**Lemma 4.5** (Few bad men)**.** When the inner loop in **ASM** terminates, at most a \(\delta\)-fraction of active men are bad.


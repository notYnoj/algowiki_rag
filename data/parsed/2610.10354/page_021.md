**Proof of Theorem 3.5.** We choose \(k=k(c,\epsilon)\) as in Lemma 3.6. Given _A_, we first apply Lemma 3.3 to compute a set _P_ satisfying (with high probability) that

\(\mathrm{Pop}^k(A;p)\subseteq P\subseteq\mathrm{Pop}^k(A;p/2).\)

If \(P=\emptyset\), then we have certified that \(\mathrm{Pop}^k(A;p)=\emptyset\). So suppose otherwise that _P_ contains some element _z_. We are guaranteed that _z_ is a _p/_2-popular _k_-sum in _A_. We call Lemma 3.6 on the set \(A^*=\pm(A\cup\{z\})\) with parameter _p/_2. As before, it holds that \(T_k(A^*)\ge p/2\) and thus Lemma 3.6 computes a set \(H\subseteq\mathbb{Z}\) which is as claimed, except that instead of the third condition we have \(|A^*\cap H|\ge|A|/K\). However, as _A_<sup>∗</sup> is a union of four copies of _A_, possibly translated and negated, one of the corresponding translations and/or negations of _H_ must satisfy the claim. We test all four and verify each in linear time. The total time is dominated by the calls to Lemmas 3.3 and 3.6, running in time \(\tilde{O}(|A|^k/p)=\tilde{O}(|A|^{1+c})\) and \(O(|A|^{1+c+\epsilon})\), respectively.

**Proof of Lemma 3.6.** Following the proof of Lemma 3.4, we design a recursive algorithm. If _T<sub>k</sub>(A_) is sufficiently large as in the lemma statement, then the algorithm returns _H_ satisfying the claimed properties with high probability. If the bound on _T<sub>k</sub>(A_) does not hold, then the algorithm may simply fail.

In the first case of the proof of Lemma 3.4, the set _A_ satisfies that \(T_{k-1}(A)\ge|A|^{2(k-1)-1-c+\delta}\), for some constant \(\delta\). Without knowing if this previous condition is actually satisfied, we regardless call the algorithm recursively for _k_-1. If it reports _H_ as claimed, then we are done. Otherwise, we can infer that we instead in the second case.

In that second case, we construct sets _Q<sub>D</sub>_ approximating the sets _P<sub>D</sub>_ from the proof of Lemma 3.4 as follows. Here, _D_ ranges of all powers of 2 at least |_A_|<sup>_k_-1-_c-o_(1)</sup>. Each set _Q<sub>D</sub>_ is required to satisfy that (i) each \(x\in Q_D\) has multiplicity at least _D/_2 and less than 4_D_ as a _k_-sum in _A_ and (ii) each _k_-sum in _A_ with multiplicity at least _D_ and less than 2_D_ is contained in _Q_. Each such set _Q<sub>D</sub>_ can be computed in time \(\tilde{O}(|A|^{1+c})\) by a constant number of calls to Lemma 3.3. Then, by the same proof as in Lemma 3.4 we have that

\(T_k(A)\le O((k\mathrm{log}|A|)^2)\cdot\mathrm{max}_D(D^2\cdot E(A,Q_D)),\)

and thus

\(E(A,Q_D)\ge\frac{|A|^2|Q_D|}{|A|^{\delta+o(1)}}\)

for some choice of _D_. In this case we apply the asymmetric BSG theorem on _A_ and _Q<sub>D</sub>_. In the algorithm, we do not know the optimal value of _D_, so we simply try all _O_(log|_A_|) options. The algorithmic version of the asymmetric BSG theorem (Theorem 2.4) then returns the claimed set _H_ in time \(\tilde{O}((|A|+|Q_D|)K)=O(|A|^{1+c+\epsilon+o(1)})\). (The _o_(1) overhead can be removed by reducing \(\epsilon\) further.)

## 4 Subquadratic-Time Algorithm for Low-Rank 3SUM

In this section we design a subquadratic-time algorithm for low-rank 3SUM.


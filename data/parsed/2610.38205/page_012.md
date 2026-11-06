**Algorithm 3.1** PartialVoteCover \((\mathcal{S}_\beta,U,\mathsf{opt},C,c)\)

**Input:** A set system \(\mathcal{S}_\beta\), a set of elements _U_ to cover, a guess `opt` of \(\mathsf{OPT}_\beta(s)\), and constants _C,c\>_0.

**Output:** A partial cover \(\mathcal{C}\subseteq\mathcal{S}_\beta\) that covers at least |_U|/_2 elements from _U_.

1: \(\mathcal{C},V\leftarrow\varnothing\)

2: \(K\leftarrow\) a multiset of \(C\cdot\mathsf{optln}n\) independent samples from _U_

3: **while** \(K\neq\varnothing\) **do**

4: \(v\leftarrow\) element sampled uniformly at random from _K_

5: \(K\leftarrow K\backslash v\)

6: **if** \(v\in\bigcup_{S\in\mathcal{C}}S\) **then** \(\triangleright\) Check if any sets containing _v_ (via SetOf) are in C

7: **continue**

8: \(V\leftarrow V\unknown\{v\}\)

9: \(S^*\leftarrow\mathrm{argmax}_{S\in\mathcal{S}_\beta}|V\cap S|\)

10: **if** \(|V\cap S^*|\ge c\mathrm{ln}n\) **then**

11: \(\mathcal{C}\leftarrow\mathcal{C}\cup\{S^*\}\)

12: \(V\leftarrow V\backslash S^*\triangleright\) Remove all votes cast by elements covered by _S_<sup>∗</sup>, including duplicates

13: **return** C

_Proof._ Each set added to the cover in PartialVoteCover consumes _c_ln_n_ voters. That is, the _c_ln_n_ samples that voted for that set are removed from _V_ and their votes eliminated from all sets. Since the initial number of samples in _K_ is \(C\cdot\mathsf{optln}n\), the algorithm can successfully find a set exceeding the vote threshold at most \(\frac{C\mathsf{optln}n}{c\mathrm{ln}n}=\frac{C}{c}\cdot\mathsf{opt}\) times.

**Observation 3.3.** _Before or after any iteration of the while-loop of Algorithm 3.1, every set_ \(S\in\mathcal{S}\) _satisfies_ \(|V\cap S|<c\mathrm{ln}n\).

_Proof._ We prove this by induction. It is trivially true at the start of the algorithm since _V_ is empty. Now assume that it holds at the start of a given iteration, i.e. \(|V\cap S|<c\mathrm{ln}n\) for all \(S\in\mathcal{S}\). Observe that on each iteration, _V_ grows by at most one element, _v_, so any \(|V\cap S|\) likewise grows by at most one, up to a maximum of _c_ln_n_. If any sets _S_ now satisfy \(|V\cap S|=c\mathrm{ln}n\), then Line 10 triggers, and one such set is subtracted from _V_ . However, all satisfying sets share the element _v_, so this subtraction necessarily removes at least one element, _v_, from all their intersections with _V_ . Therefore, all sets once again satisfy \(|V\cap S|<c\mathrm{ln}n\).

**Observation 3.4.** _Of the points initially in K, the partial cover_ C _returned by PartialVoteCover leaves fewer than_ \(c\cdot\mathsf{OPT}_\beta(s)\mathrm{ln}n\) _uncovered._

_Proof._ At the end of PartialVoteCover, the points initially in _K_ that are not covered by C are exactly those that remain in _V_ . By definition of \(\mathsf{OPT}_\beta(s)\), the elements of \(V\subseteq U\) can be fully covered by at most \(\mathsf{OPT}_\beta(s)\) sets, i.e. by the optimum cover of _U_. However, by Observation 3.3, each of the sets in this optimum cover contains fewer than _c_ln_n_ of the elements in _V_ . Thus, the number of points in _V_ is bounded by \(|V|<c\cdot\mathsf{OPT}_\beta(s)\mathrm{ln}n\) via the Pigeonhole Principle.

Using these observations, we now prove that an appropriate choice of the constants _C_ and _c_ ensures that PartialVoteCover covers at least half of the elements in _U_ with high probability.

**Lemma 3.5.** _If_ \(\mathsf{OPT}_\beta(s)\le\mathsf{opt}\le 2\mathsf{OPT}_\beta(s)\)_, then there are sufficiently large constants C and c such that the partial cover_ C _on s returned by PartialVoteCover (Algorithm 3.1) covers at least half of U, i.e._ \(|U\backslash\bigcup_{S\in\mathcal{C}^*}S|\le|U|/2\)_, with probability_ \(\ge 1-1/n\).


## 3.5 Foveal Verification and Exactness

The fovea needs the threshold _U_ before the retina pass and the exact distances of the survivors after it. Before the pass, CertEx samples every _s_-th retina vector, for a stride _s_, and scores the sampled vectors by the same computed product \(\widehat{P}\) as the retina pass. Among them, the sampled vectors with the largest products become the _anchors_ A(**q**). The threshold _U_ is then the _k_-th smallest exact distance among the anchors. Because the anchors are at least _k_ distinct vectors of X, \(U\ge r_k(\mathbf{q})\) holds for every query. After the pass, the fovea computes the exact distance of each survivor from the full-precision difference **q**-**x** and returns the _k_ smallest per query.

**Proposition 4** (Exactness)**.** _CertEx returns_ N_<sub>k</sub>_(**q**) _for every query_ **q**.

_Proof._ Every **x** with \(\|\mathbf{q}-\mathbf{x}\|\le U\) satisfies \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le U\) by Proposition 2 and survives by Proposition 3. The retina is therefore a certified exclusion test. Since \(U\ge r_k(\mathbf{q})\), Proposition 1 yields the claim.

The anchors, the rotation **V**, and the width _m_ therefore influence only the cost of CertEx. For instance, a loose threshold admits more survivors and more exact distances but cannot remove a true neighbor. To quantify this cost, Proposition 5 bounds the number of survivors. For this purpose, we write \(\rho(\mathbf{x}):=\|(\mathbf{I}-\mathbf{V}^\top\mathbf{V})(\mathbf{x}-\mathbf{c})\|\) for the last coordinate of \(\ell(\mathbf{x})\), which is the norm of the component of **x**-**c** that is orthogonal to the rows of **V**. Similarly, we denote by \(\eta(\mathbf{q})\) the _slack_ that \(\mu(\mathbf{q})\) and the rounded-up coordinates add to the squared threshold, which is of the order of the unit roundoff times the squared norms.

**Proposition 5** (Survivor ball)**.** _Every vector that the retina keeps for the threshold U satisfies_ \(\|\mathbf{q}-\mathbf{x}\|^2\le U^2+\eta(\mathbf{q})+4\rho(\mathbf{q})\rho(\mathbf{x})\).

_Proof._ The proof reuses the notation of the proof of Proposition 2. There, **u**=**q**-**c** and **v**=**x**-**c** split as **u**=**u**<sub>1</sub>+**u**<sub>2</sub> and **v**=**v**<sub>1</sub>+**v**<sub>2</sub>, where **u**<sub>1</sub>,**v**<sub>1</sub> lie in the row space of **V** and **u**<sub>2</sub>,**v**<sub>2</sub> are orthogonal to it. The norms of **u**<sub>2</sub> and **v**<sub>2</sub> are the last coordinates \(\rho(\mathbf{q})\) and \(\rho(\mathbf{x})\) of the lifted projections. The proof proceeds in three steps.

First, the retina keeps **x** only if its lifted distance is small. By the definition of the slack \(\eta(\mathbf{q})\), every kept vector satisfies

\(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2\le U^2+\eta(\mathbf{q}).\) (16)

Second, the squared distance exceeds the squared lifted distance by a term that involves only **u**<sub>2</sub> and **v**<sub>2</sub>. Eqs. (6), (5), and (4) give \(\|\mathbf{q}-\mathbf{x}\|^2=\|\mathbf{u}_1-\mathbf{v}_1\|^2+\|\mathbf{u}_2-\mathbf{v}_2\|^2\) and \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2=\|\mathbf{u}_1-\mathbf{v}_1\|^2+(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2\). Subtracting the second equation from the first and expanding both<tbc>

<tbc>squares,

\(\|\mathbf{q}-\mathbf{x}\|^2-\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2=\|\mathbf{u}_2-\mathbf{v}_2\|^2-(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2=\big(\|\mathbf{u}_2\|^2-2\langle\mathbf{u}_2,\mathbf{v}_2\rangle+\|\mathbf{v}_2\|^2\big)-\big(\|\mathbf{u}_2\|^2-2\|\mathbf{u}_2\|\|\mathbf{v}_2\|+\|\mathbf{v}_2\|^2\big)=2\big(\|\mathbf{u}_2\|\|\mathbf{v}_2\|-\langle\mathbf{u}_2,\mathbf{v}_2\rangle\big).\text{(17)}\)

Third, the Cauchy-Schwarz inequality bounds this excess. It gives \(-\langle\mathbf{u}_2,\mathbf{v}_2\rangle\le\|\mathbf{u}_2\|\|\mathbf{v}_2\|\), so that the right- hand side of Eq. (17) is at most \(4\|\mathbf{u}_2\|\|\mathbf{v}_2\|=4\rho(\mathbf{q})\rho(\mathbf{x})\). Adding this bound to Eq. (16) yields \(\|\mathbf{q}-\mathbf{x}\|^2\le U^2+\eta(\mathbf{q})+4\rho(\mathbf{q})\rho(\mathbf{x})\), which is the claim.

The survivors therefore lie between two balls. Specifically, the inner ball has radius _r<sub>k</sub>_(**q**), and its vectors always survive. In contrast, the outer ball is slightly larger, by an excess that grows with \(\rho(\mathbf{q})\) and \(\rho(\mathbf{x})\). Because the anchors are the best of every _s_-th vector, _U_ approximates the distance to the (_ks_)-th nearest neighbor. The number of survivors thus approaches _ks_ when the width captures most of the variance of the data. A batch of _B_ queries then costs _BN(m_+5) half-precision multiply-ads plus about _ks_ exact distances per query, whereas exhaustive search costs _BND_ full-precision multiply-ads and a selection among all _N_ candidates.

## 3.6 Certified Exclusion at Any Threshold

Certified exclusion holds for every threshold, so that CertEx answers any query that fixes its threshold in advance exactly and without the anchors. Specifically, Definition 1 and Proposition 3 hold for every \(U\ge 0\), so that the test of the retina is certified whatever threshold a query uses. The anchors of Section 3.5 have a different role: they choose the threshold _U_ when a query does not fix it. For instance, kNN search does not fix its threshold, because Proposition 1 requires \(U\ge r_k(\mathbf{q})\) and the distance _r<sub>k</sub>_(**q**) becomes known only after the search. In contrast, a _range query_ with radius _r_ asks for all database vectors within _r_ of the query, so that its threshold is _r_ from the start. CertEx thus answers a range query by setting _U_:=_r_, without any anchors. Since the retina may also keep vectors farther than _r_, the fovea computes their exact distances and removes them. CertEx therefore returns exactly the vectors within _r_, by Propositions 2 and 3.

In particular, near-duplicate detection fixes its threshold in advance as well, because it asks for all pairs of database vectors whose distance is at most a given radius _r_. We call the set of these pairs the _similarity self-join_. The self-join therefore consists of the range queries of all database vectors against the database, which CertEx answers exactly as above. Because each pair appears in two of these range<tbc>


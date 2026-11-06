and hence the multiset _B_\\_S_ has size<sup>12</sup>

\(|B\backslash S|\ge\frac{\Sigma(B)-\Sigma(S)}{N}>\frac{\Sigma(X)/3}{N}\)<br>
\(\ge\frac{d|X|^2}{4r}\cdot\frac{1}{3N}\) (by Eq. (32))<br>
\(\ge d.\) (by \(|X|^2\ge C_\delta\cdot\mu_X\cdot N\))

So we can pick an arbitrary size-_d_ subset \(\{b_1,b_2,\dots,b_d\}\subseteq B\backslash S\), and by the pigeonhole principle, there exist \(0\le j<j'\le d\) such that \(b_1+\cdots+b_j\equiv b_1+\cdots+b_{j^\prime}\) (mod _d_), and hence \(b_{j+1}+\cdots+b_{j^\prime}\) is a multiple of _d_. Denote \(S'=\{b_{j+1},\dots,b_{j^\prime}\}\subseteq B\backslash S\), with \(|S'|\le d\) and \(\Sigma(S')\equiv 0\) (mod _d_). Then, the subset sum \(\Sigma(S\cup S')\in\mathcal{S}(B)\) is also a multiple of _d_. By our definition of \(s=\Sigma(S)\), we must have \(\Sigma(S\cup S')>\Sigma(X)/2\) due to the maximality of \(\Sigma(S)\), which means

\(\Sigma(S)>\Sigma(X)/2-\Sigma(S')\ge\Sigma(X)/2-Nd.\) (34)

Now we verify that \(\Sigma(S)\) belongs to the interval defined in Eq. (33). The upper bound \(\Sigma(S)\le\Sigma(X)/2\) is guaranteed by the definition of _S_. For the lower bound, first note that

\(Nd\le N\cdot 4r\Sigma(X)/|X|^2\le N\cdot 4r\Sigma(X)/(C_\delta rN)\le 0.1\Sigma(X).\)

Combined with Eq. (34), this implies

\(\Sigma(S)\ge\Sigma(X)/2-Nd\ge 0.4\Sigma(X).\)

Then, note that the lower bound of the interval Eq. (33) is

\(C_2rN\Sigma(X)/|X|^2\le C_2rN\Sigma(X)/(C_\delta rN)\le 0.3\Sigma(X).\)

Thus, \(\Sigma(S)\in[0.4\Sigma(X),0.5\Sigma(X)]\) belongs to the interval in Eq. (33). Since \(\Sigma(S)\) is a multiple of _d_, this implies \(\Sigma(S)\in\mathcal{S}(X)\subseteq\mathcal{S}(A)\). Since \(\Sigma(S)>0\), we conclude \(\Sigma(S)\in\mathcal{S}^*(A)\cap\mathcal{S}^*(B)\).

We have proved the weaker version of Lemma 3.6. In comparison, the statement of the original Lemma 3.6 only requires \(|\mathrm{supp}_r(A)|\ge C\sqrt{N/r}\cdot\sqrt{\mathrm{log}(2N)}\) instead of \(|\mathrm{supp}_r(A)|\ge C\sqrt{N/r}\cdot\sqrt{\mathrm{log}(2N)}\mathrm{log}(2r)\) (Eq. (26)). Inspecting the proof above, we note that this extra log(2_r_) factor comes from the \(\mathrm{log}(2\mu_X)\) factors in Eqs. (28) and (29) in the statement of Lemma B.2 from \[BW21\]. In the proof of Lemma B.2 in \[BW21, Section 4.4\], these \(\mathrm{log}(2\mu_X)\) factors were incurred in the step that transforms a possibly non-uniform multiset _X_ to a uniform multiset, where a multiset _X_ is called _uniform_ if the multiplicity \(\mu_X(x)\) is the same for all elements \(x\in X\); see \[BW21, Lemma 4.28\]. When we apply Lemma B.2 in our proof, the multiset _X_ is already uniform (Eq. (30)), so we can avoid this transformation step in \[BW21\] and thus avoid the extra \(\mathrm{log}(2\mu_X)\) factors in Eqs. (28) and (29). In this way we can prove Lemma 3.6 without the extra log(2_r_) factor.

## B.4 Proof of Lemma 4.9

**Lemma 4.9** (Deterministic balls-and-bins)**.** _Given integer r, and m sets_ \(S_1,S_2,\dots,S_m\subseteq[n]\) _such that_ \(|S_i|\le r\mathrm{log}_2(2m)\) _for all i, there is an O(mr_log_m_log_r+n_log_r)-time deterministic algorithm that finds an r-coloring_ \(C:[n]\rightarrow[r]\)_, such that for every_ \(i\in[m]\) _and every color_ \(c\in[r]\),

\(|\{j\in S_i:C(j)=c\}|\le O(\mathrm{log}m).\)

<sup>12</sup>For two multisets \(S\subseteq B\), the difference _B_\\_S_ is naturally defined by subtracting the multiplicities of elements.


**Lemma 6.3** (number of pseudo-solutions)**.** _For each_ \(i\in[\sqrt{n}]\)_, let_ cd_<sub>i</sub> be a set of at most k_<sup>2</sup> _candidate domain intervals. Let t denote the number of pseudo-solutions constructed in Algorithm 9. Then, we have_ \(t\le k^2/(\lambda\epsilon)\).

_Proof._ Note that for each subarray we have at most _k_<sup>2</sup> candidate domain intervals. Since there are \(\sqrt{n}\) subarrays, then in total we have \(\sqrt{n}k^2\) candidate domain intervals. Each time we construct a pseudo-solution, the total number of the candidate domain intervals is decreased by at least \(\epsilon\sqrt{n}\lambda\). Thus, the total number of pseudo-solutions _t_ can be upper bounded,

\(t\le\frac{\sqrt{n}k^2}{\epsilon\sqrt{n}\lambda}\le\frac{k^2}{\lambda\epsilon}.\)

**Lemma 6.4** (quality of pseudo-solutions)**.** _Let_ ps<sub>1</sub>,ps<sub>2</sub>_,...,_ps_<sub>t</sub> be the pseudo-solutions constructed by Algorithm 9. If_ \(\mathsf{lis}(A)\ge n\lambda\) _holds, then with probability at least_ \(1-\mathrm{exp}(-\Omega(\sqrt{n}\lambda))\)_, there exists an_ \(i\in[t]\) _such that_<tbc>

\(\mathsf{q}(\mathsf{ps}_i)\ge\frac{\mathsf{lis}(A)}{2t}.\)

<tbc>_Proof._ Let us focus again on the actual solution domains<tbc>

\([\mathsf{sm}(\mathsf{sa}_1),\mathsf{lg}(\mathsf{sa}_1)],[\mathsf{sm}(\mathsf{sa}_2),\mathsf{lg}(\mathsf{sa}_2)],\dots,[\mathsf{sm}(\mathsf{sa}_\sqrt{n}),\mathsf{lg}(\mathsf{sa}_\sqrt{n})].\)

<tbc>We define set \(S\subseteq[\sqrt{n}]\) such that<tbc>

\(\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}\ge\epsilon\sqrt{n}\lambda,\forall i\in S.\)

<tbc>Using Corollary 6.2 with \(\epsilon\le 1/10\), we know that there is a monotone pseudo-solution \([\alpha_i,\beta_i]_{i\in T}\) (\(T\subseteq S\)) such that \([\alpha_i,\beta_i]\) are candidate domain intervals and<tbc>

\(\sum_{i\in T}\mathsf{lis}^{[\alpha_i,\beta_i]}(\mathsf{sa}_i)\ge(1-4\epsilon)\mathsf{lis}(A).\)

<tbc>Denote this pseudo-solution as sol. At the time we terminate Algorithm 9, there are at most \(\epsilon\sqrt{n}\lambda\) candidate domain intervals of sol that do not belongs to any pseudo-solution of the pseudo-solution set. Also, since each candidate domain interval contributes at most \(\sqrt{n}\) to the quality of the pseudo- solution containing the interval, we have

\(\sum_{i=1}^t\mathsf{q}(\mathsf{ps}_i)\ge(1-4\epsilon)\mathsf{lis}(A)-\epsilon\sqrt{n}\lambda\cdot\sqrt{n}\ge(1-4\epsilon)\mathsf{lis}(A)-\epsilon\mathsf{lis}(A)=(1-5\epsilon)\mathsf{lis}(A).\)

Thus, there exists an \(i\in[t]\) such that

\(\mathsf{q}(\mathsf{ps}_i)\ge(1-5\epsilon)\mathsf{lis}(A)/t\ge\mathsf{lis}(A)/(2t).\)

**Lemma 6.5** (running time)**.** _For each_ \(i\in[\sqrt{n}]\)_, let_ cd_<sub>i</sub> be a set of at most k_<sup>2</sup> _candidate domain intervals. Let t denote the number of pseudo-solutions. The running time of Algorithm 9 is bounded by_ \(O(tk^2\sqrt{n}\mathrm{log}n)\).


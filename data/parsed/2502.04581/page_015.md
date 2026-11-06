**Proof.** We proceed with a heavy-light approach. Assume there exists an \(O(n^{\lceil k/2\rceil-\epsilon})\) algorithm for the #_k_-SUM problem. Set \(c:=(k-1)(\lceil k/2\rceil)\). Firstly, we count the number of solutions \((a_1,\dots,a_k)\in A_1\times\cdots\times A_k\), where \(n_{a_1},\dots,n_{a_k}\le n^{\epsilon/c}\) using Lemma 16. This takes time

\(\tilde{O}\left((n\cdot(n^{\epsilon/c})^{k-1})^{\lceil k/2\rceil-\epsilon}\right)=\tilde{O}\left(\left(n^{1+\frac{\epsilon}{\lceil k/2\rceil}}\right)^{\lceil k/2\rceil-\epsilon}\right)\)<br>
\(=\tilde{O}\left(n^{\lceil k/2\rceil-\epsilon+\epsilon-\frac{\epsilon^2}{\lceil k/2\rceil}}\right)\)<br>
\(=O\left(n^{\lceil k/2\rceil-\epsilon^\prime}\right),\)

where \(\epsilon'>0\). It remains to calculate the number of witnesses (_a_<sub>1</sub>_,...,a<sub>k</sub>_), where for at least one \(i\in\{1,\dots,k\}\), we have high multiplicity, meaning \(n_{a_i}>n^{\epsilon/c}\) holds. Consider the case that \(a_1\in A_1\) is a high-multiplicity number (the case where \(a_i\in A_i\) with \(i\neq 1\) is a high-multiplicity number is analogous). For each high-multiplicity number _a_<sub>1</sub> in _A_<sub>1</sub> we do the following. Solve the (_k_-1)-SUM instance with sets _A_<sub>2</sub>_,...,A<sub>k</sub>_ and target _t-a_<sub>1</sub>. There are at most \(n^{1-(\epsilon/c)}\) many high-multiplicity numbers in _A_<sub>1</sub>, and solving the (_k_-1)-SUM instance takes time _O(n_<sup>(_k_-1)/2</sup>), since _k_ is odd. We get a total runtime of

\(n^{1-\frac{\epsilon}{c}}\cdot\tilde{O}(n^{(k-1)/2})=\tilde{O}(n^{1-(\epsilon/c)+(k-1)/2})\)<br>
\(=\tilde{O}(n^{(k+1)/2-(\epsilon/c)})\)<br>
\(=O(n^{\lceil k/2\rceil-\epsilon^{\prime\prime}}),\)

where \(\epsilon''>0\), which concludes the proof.

\(\blacktriangleright\) **Theorem 2.** _Let_ \(k\ge 3\) _be odd. If there is_ \(\epsilon>0\) _such that we can count the number of witnesses for k-SUM in time_ \(O(n^{\lceil k/2\rceil-\epsilon})\)_, then for all problem P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists k)\)_, there is some_ \(\epsilon'>0\) _such that we can count the number of witnesses for P in time_ \(O(n^{\lceil k/2\rceil-\epsilon^\prime})\).

By combining the subquadratic equivalence between 3-SUM and #3-SUM due to Chan et al. [22] and the above theorem, we obtain the following corollary.

\(\blacktriangleright\) **Corollary 3.** _For all problems P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists^3)\)_, there is some_ \(\epsilon_P>0\) _such that we can count the number of witnesses for P in randomized time_ \(O(n^{2-\epsilon_P})\) _if and only if there is some_ \(\epsilon'>0\) _such that_ 3_-SUM can be solved in randomized time_ \(O(n^{2-\epsilon^\prime})\).

The above proof can also be adapted for the special case _k_=3 to count for each \(a_1\in A_1\) the number of witnesses involving _a_<sub>1</sub>, by plugging in the appropriate All-ints versions; see the full version of the paper for details. Together with the equivalence between #All-ints 3-SUM and 3-SUM of Chan et al. [22], we get

\(\blacktriangleright\) **Corollary 19.** _For all problems P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists^3)\)_, we are able to count for each_ \(a_1\in A_1\) _the number of witnesses involving a_<sub>1</sub> _in randomized time_ \(O(n^{2-\epsilon})\) _for an_ \(\epsilon>0\)_, if_ 3_-SUM can be solved in randomized time_ \(O(n^{2-\epsilon^\prime})\) _for an_ \(\epsilon'>0\).

As Theorem 1 establishes 3-SUM as the complete problem for the class \(\mathsf{FOP}_\mathbb{Z}(\exists\exists\exists)\), we would like to similarly explore complete problems for other quantifier structures. All proofs in this section are deferred to the full version. Let us recall our main geometric problems.

## 5 Completeness Theorems for General Quantifier Structures


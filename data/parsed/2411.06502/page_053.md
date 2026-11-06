where the first and third summand can be obtained from Main Theorem 4 and Theorem 4.1 on the forests **F[ l(s) .. l(q) )**, \(F'[l(s') .. l(q')\) **)** and **F[ r(q) .. r(s) )**, \(F'[l(s') .. l(q')\) **)**, respectively, and the second summand from Input (ii) of the \((s,s',q,q')\)-DISED instance. The computation can then be performed by max-plus products of three \((n'+1)\times(n'+1)\) matrices. Overall, the time to compute Output (ii) is

\(\mathcal{O}(\mathrm{T}_\mathrm{MUL}(n')+n'^{2+o(1)})\)

Finally, we note that Output (iii) can be obtained using similar arguments as Output (ii).

Next, we consider the case where _s_ immediately precedes _q_.

**Lemma 5.13.** _Consider an_ \((s,s',q,q')\)_-UDISED instance of size_ \((m,n')\) _such that s immediately precedes q. Then, we can solve the_ \((s,s',q,q')\)_-UDISED instance in time_ \((m/n')^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MUL}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MonMUL}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathrm{T}_\mathrm{MonMUL}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\).

**Proof.** We begin with Output (i). We perform a case distinction on where/whether _s_ is mapped by \(\mathrm{sim}(\mathrm{sub}(s),F'[x'.. y'))\) for all \(x'\in[l(s')..l(q')]\) and \(y'\in[\mathrm{r}(q')..\mathrm{r}(s')]\).

If _s_ is not mapped to any node of \(F'[x'.. y')\), then

\(\mathrm{sim}(\mathrm{sub}(s),F'[x'.. y'))=\mathrm{sim}(F[l(s)..l(q))+F[l(q)..\mathrm{r}(s)),F'[x'..y'))\)

as the spine node _s_ does not contribute to the similarity of the two forests. Via Proposition 3.10(i) we compute

\(\mathrm{sim}(\mathrm{sub}(s),F[x'.. y'))=\mathrm{max}_{z^\prime\in F^\prime[x^\prime.. y^\prime):w^\prime\ge z^\prime\ge x^\prime w^\prime\in F^\prime[x^\prime.. y^\prime):z^\prime\le w^\prime\le y^\prime}\big\{\mathrm{sim}(F[l(s)..l(q)),F[x'..z'))+\mathrm{sim}(F[l(q)..\mathrm{r}(q)),F[z'..w'))+\mathrm{sim}(F[\mathrm{r}(q)..\mathrm{r}(s)),F[w'..y'))\big\}.\)

We can combine these values using a max-plus product of three \((n'+1)\times(n'+1)\) matrices, which requires time \(\mathcal{O}(\mathrm{T}_\mathrm{MUL}(n'))\). In the unweighted setting, we note that all three matrices are row-monotone or column-monotone and have entries bounded by \(O(n')\). In particular, the matrix multiplication requires time \(\mathcal{O}(\mathrm{T}_\mathrm{MonMUL}(n'))\). It remains to describe how to obtain the appropriate inputs. To do so, we proceed by case analysis on \(z',w'\).

If \(z',w'\in[l(s')..l(q')]\), then the first summand can be obtained from applying Theorem 4.15 to **F[ l(s) .. l(q) )** and \(F'\) where the required inputs are supplied as the first forest contains no spine nodes. The second summand can be obtained from Input (ii) of the \((s,s',q,q')\)-UDISED instance. The last summand can be obtained from applying Theorem 4.15 to **F[ r(q) .. r(s) )** and \(F'\) where again the first forest contains no spine nodes.

The case \(z',w'\in[l(q')+1..\mathrm{r}(s')]\) can be handled analogously. We note that the range \([l(q')+1..\mathrm{r}(s')]\) is equivalent to the range \([\mathrm{r}(q')..\mathrm{r}(s')]\) with respect to sim since \(F'[l(q')+1..\mathrm{r}(s')]=F'[\mathrm{r}(q')..\mathrm{r}(s')]\).

If \(z'\in[l(s')..l(q')]\), \(w'\in[l(q')+1..\mathrm{r}(s')]\) then the first and third summand can be obtained from Theorem 4.15 and the second summand from Input (i) of the \((s,s',q,q')\)-UDISED instance. For the second summand, we note that \(F'[z'..l(q')+1)=F'[z'..l(q')]\) so we can retrieve this input from Input (ii) instead. For the first and third summand, we compute UFED on forests **F[ l(s) .. l(q) )**, \(F'\) and **F[ r(q) .. r(s) )**, \(F'\), respectively, noting that in both cases the first forest contain no spine nodes so the inputs are at our disposal.

■ If _s_ is not mapped to any node of \(F'[x'..y')\), then


In all cases, the computational bottleneck is the application of Theorem 4.15, which requires time \((m/n')^{1+o(1)}\cdot(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)})\). In the unweighted case, we use Theorem 2.3 which requires time \((m/n')^{1+o(1)}\cdot(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}g(n'))\).

If _s_ is mapped to a node \(r'\in\mathbf{S}'\) such that \(s'\le r'<q'\), then

\(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}[x'..y'))=\)<br> \(\mathrm{max}_{r^\prime\in\mathbf{S}^\prime:s^\prime\le r^\prime<q^\prime}\big\{\eta(s,r')+\mathrm{sim}(\mathbf{F}[x..l(q)))+\mathsf{sub}(q)+\mathbf{F}[\mathsf{r}(q)..y),\mathbf{F}'[l(r')+1..\mathsf{r}(r')-1))\big\}.\)

Note, we already computed the values \(\mathrm{sim}(\mathbf{F}[x..l(q)))+\mathsf{sub}(q)+\mathbf{F}[\mathsf{r}(q)..y),\mathbf{F}'[l(r')+1..\mathsf{r}(r')-1)\) in the previous case, so there is nothing more left to calculate in this case.

If _s_ is mapped to any node contained in \(q'=\mathsf{sub}(q')\), then \(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}[x'..y'))=\mathrm{sim}(\mathsf{sub}(s),\mathsf{sub}(q'))=\eta(s,q')\) which can easily be computed.

If _s_ is mapped to any node contained in \(\mathbf{F}'[x'..l(q'))\), then we have that \(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathsf{sub}(s),\mathsf{sub}(v'))\) for some \(v'\in\mathbf{F}'[x'..l(q'))\) and \(v'\notin\mathbf{S}'\). Note, all these values are already at our disposal in the SED Problem.

Lastly, if _s_ is mapped to any node contained in \(\mathbf{F}'[\mathsf{r}(q')..y')\), then we can apply reverse symmetry obtaining the previous case.

We now discuss Outputs (ii) and (iii). We will explicitly describe the algorithm for computing Output (ii), noting that Output (iii) can be computed analogously. If _s\<q_ is aligned by \(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}'[x'..y'))\), then we apply Lemma 4.10 to sub(_s_), \(\mathbf{F}',\mathbf{S},q\) as in Lemma 5.12 noting that on our unbalanced instance, the algorithm requires time \((m/n')^{1+o(1)}\cdot(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)})\). On the other hand, if _s_ is not aligned, we argue similarly as in Lemma 5.12. We can write

\(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[l(s)..l(q)))+\mathbf{F}[l(q)..r(s)),\mathbf{F}'[x'..y'))\)

as _s_ does not contribute to the similarity. Via Proposition 3.10(i) we compute

\(\mathrm{sim}(\mathsf{sub}(s),\mathbf{F}[x'..y'))=\mathrm{max}_{z^\prime\in\mathbf{F}^\prime[l(s^\prime)..l(q^\prime)):w^\prime\ge z^\prime\ge x^\prime w^\prime\in\mathbf{F}^\prime[l(s^\prime)..l(q^\prime)):z^\prime\le w^\prime\le y^\prime}\big\{\mathrm{sim}(\mathbf{F}[l(s)..l(q)),\mathbf{F}[x'..z'))\)<br> \(+\mathrm{sim}(\mathbf{F}[l(q)..r(q)),\mathbf{F}[z'..w'))\)<br> \(+\mathrm{sim}(\mathbf{F}[r(q)..r(s)),\mathbf{F}[w'..y'))\big\},\)

where the first and third summand can be obtained from Main Theorem 4 and Theorem 4.1 on the forests **F**[l(_s_)_..l(q_)), \(\mathbf{F}'[l(s')..l(q'))\) and **F**[r(_q_)_..r(s_)), \(\mathbf{F}'[l(s')..l(q'))\), respectively, and the second summand from Input (ii) of the \((s,s',q,q')\)-DISED instance. The computation can then be performed by max-plus products of three \((n'+1)\times(n'+1)\) matrices.

To bound the overall running time, we note that obtaining the outputs of Theorem 4.15 takes time \((m/n')^{1+o(1)}\cdot(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)})\). In the unweighted setting, we instead obtain \((m/n')^{1+o(1)}\cdot(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}g(n'))\).

## 5.5.3 Computing SED on Unbalanced Instances with UDISED

We give the result for both weighted and unweighted SED.

**Theorem 5.18.** _There is an_ \((n/n')^{1+o(1)}\cdot\big(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)}\big)\) _time algorithm for SED, where n_=|**F**|, \(n'=|\mathbf{F}'|\) _and_ \(n\ge n'\).


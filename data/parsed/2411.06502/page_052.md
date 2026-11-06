For (24), note that (24) is equal to (23) under reverse symmetry.

For (25), note that (25) is a subset of the output of the \((r,s',q,q')\)-UDISED instance.

It remains to explain how to retrieve Inputs (ii), (iii) of the \((s,s',r,q')\)-DISED instance. Note, Inputs (ii) and (iii) are Outputs (ii) and (iii) of the \((r,s',q,q')\)-UDISED instance.

With all the inputs at our disposal, we can call also the subroutine on the \((s,s',r,q')\)-UDISED instance, and retrieve the outputs. Towards this, we observe that the \((s,s',r,q')\)-UDISED provides the outputs to the \((s,s',q,q')\)-UDISED instance.

## 5.5.2 Handling the Base Cases

Recall that \(s'=r'\) is the root of \(\mathbf{F}'\) and \(q'=b'\) is the bottom node of the spine of \(\mathbf{F}'\). In particular, \(\mathrm{sub}(s')\backslash\mathrm{sub}(q')=\mathbf{F}'\backslash\{q'\}\). First, we show that when \(m=\mathcal{O}(n')\), we can use our DISED to compute the UDISED instance.

**Lemma 5.12.** _Consider an_ \((s,s',q,q')\)_-UDISED instance of size_ \((m,n')\) _such that_ \(m=\mathcal{O}(n')\)_. Then, we can solve the_ \((s,s',q,q')\)_-UDISED instance in time_ \(\mathcal{O}(\mathsf{T}_\text{\textit{MUL}}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \(\mathcal{O}(\mathsf{T}_\text{\textit{MonMUL}}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathsf{T}_\text{\textit{MonMUL}}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\).

**Proof.** In this case, we can treat the instance as a \((s,s',q,q')\)-DISED instance and apply Corollary 5.5. Note that such a instance is a DISED instance of size \(\mathrm{max}(m,n')=\mathcal{O}(n')\) and global tree size \(\mathcal{O}(n')\) regardless of the size of sub(_s_). To apply Corollary 5.5, note that we must supply the missing inputs. First, we complete Input (i) by computing \(\mathrm{sim}(\mathbf{F}[x..y),\mathrm{sub}(q'))\) for \(x\in[\mathrm{l}(s)..\mathrm{l}(q)]\) and \(y\in[\mathrm{r}(q)..\mathrm{r}(s)]\). Since \(\mathrm{sub}(q')\) is a single node, we can compute these inputs using dynamic programming as in the DISED algorithm (see the computation of Input (7) in Main Theorem 3) in time O(_m_<sup>2</sup>)=O(_n_<sup> ́2</sup>), noting that we are already given \(\mathrm{sim}(\mathrm{sub}(q),\mathrm{sub}(q'))\) as part of the input to the UDISED instance. Similarly, since \(\mathrm{sub}(q')\) is a single node, we can supply the missing Inputs (ii) and (iii) for DISED.

Finally, we show that we can obtain the outputs to the UDISED instance given outputs to the DISED instance. In particular, for Output (i), note \((\mathrm{l}(s),x')\in\mathsf{B}_\mathrm{r}^\perp(s,s',q,q')\) and \((\mathrm{r}(s),y')\in\mathsf{B}_\mathrm{r}^\perp(s,s',q,q')\). Note that computing the DISED instance requires time \(\mathcal{O}(\mathsf{T}_\text{MUL}(n')+n'^{2+o(1)})\) by Corollary 5.5. In the unweighted setting, the DISED instance with both size and global tree size bounded by \(\mathcal{O}(n')\) requires time \(\mathcal{O}(\mathsf{T}_\text{MonMUL}(n')+n'^{2+o(1)}g(n'))\).

For Output (ii), we consider two cases. If _t\<q_ is aligned by \(\mathrm{sim}(\mathrm{sub}(s),\mathbf{F}'[\mathrm{l}(s')..\mathrm{l}(q'))\), we apply Lemma 4.10 on \(\mathrm{sub}(s),\mathbf{F}'[\mathrm{l}(s')..\mathrm{l}(q'))\), **S**_,q_ which requires time O(T<sub>MUL</sub>(_m_)+_m_<sup>2+_o_(1)</sup>)=O(T<sub>MUL</sub>(_n_<sup> ́</sup>)+_n_<sup> ́2+_o_(1)</sup>). Observe that all the required inputs are given in the SED instance since \(\mathbf{F}'[\mathrm{l}(s')..\mathrm{l}(q'))\) has no spine nodes.

On the other hand, if no spine node _t\<q_ is aligned, then we can write

\(\mathrm{sim}(\mathrm{sub}(s),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[\mathrm{l}(s)..\mathrm{l}(q))+\mathbf{F}[\mathrm{l}(q)..\mathrm{r}(s)),\mathbf{F}'[x'..y'))\)

as no nodes _t\<q_ contribute to the similarity of the two forests. Via Proposition 3.10(i) we compute

\(\mathrm{sim}(\mathrm{sub}(s),\mathbf{F}[x'..y'))=\mathrm{max}_{z^\prime\in\mathbf{F}^\prime[\mathrm{l}(s^\prime)..\mathrm{l}(q^\prime)):w^\prime\ge z^\prime\ge x^\prime w^\prime\in\mathbf{F}^\prime[\mathrm{l}(s^\prime)..\mathrm{l}(q^\prime)):z^\prime\le w^\prime\le y^\prime}\big\{\mathrm{sim}(\mathbf{F}[\mathrm{l}(s)..\mathrm{l}(q)),\mathbf{F}[x'..z'))\)<br> \(+\mathrm{sim}(\mathbf{F}[\mathrm{l}(q)..\mathrm{r}(q)),\mathbf{F}[z'..w'))\)<br> \(+\mathrm{sim}(\mathbf{F}[\mathrm{r}(q)..\mathrm{r}(s)),\mathbf{F}[w'..y'))\big\},\)


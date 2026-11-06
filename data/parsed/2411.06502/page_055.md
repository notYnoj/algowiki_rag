**Theorem 2.2.** _There is an_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\) _algorithm for unweighted SED, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\), \(n\ge n'\)_, and_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\) _for some functions f, g._

Since the proof is essentially identical, we prove both results, pointing out modifications where necessary.

**Proof of Theorem 5.18 and Theorem 2.2.** As in Main Theorem 3, we fix \(s,s'\) as the roots of \(\mathbf{F},\mathbf{F}'\) and \(q,q'\) as the last nodes in the spines of \(\mathbf{S},\mathbf{S}'\). The algorithm then runs A<sub>UDISED</sub> on the \((s,s',q,q')\)-UDISED instance and thus takes time \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}\right)\). In the unweighted setting, UDISED only takes time \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\).

We claim that this computes all required outputs \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for \((v,v')\in\mathbf{S}\times\mathbf{S}'\). Fix a pair \((v,v')\in\mathbf{S}\times\mathbf{S}'\). Assume we always recurse on the instance satisfying \(u\le v<w\) and \(u'\le v'<w'\) until we reach one of the following:

A \((u,u',w,w')\)-UDISED where _u_ immediately precedes _w_ and \(u'\le v'<w'\). In this case sim(sub(_v_),sub(_v_)) is among the outputs of the UDISED instance.

A \((u,u',w,w')\)-DISED. In this case, the outputs are computed following identical arguments as Main Theorem 3.

To conclude the proof, we bound the run-time of obtaining the inputs to the \((s,s',q,q')\)-UDISED instance. We begin with Input (i) and rewrite the input indices as

\(\{(x,x',y,y'):(x,x')\in[\mathrm{l}(s)..\mathrm{l}(q)]\times\mathrm{l}(q'),(y,y')\in\mathrm{r}(q)\times[\mathrm{r}(q')..\mathrm{r}(s')]\}\) (26)

\(\cup\{(x,x',y,y'):(x,x')\in\mathrm{l}(q)\times[\mathrm{l}(s')..\mathrm{l}(q')],(y,y')\in[\mathrm{r}(q)..\mathrm{r}(s)]\times\mathrm{r}(q')\}\) (27)

\(\cup\{(x,x',y,y'):(x,x')\in\mathrm{l}(q)\times[\mathrm{l}(s')..\mathrm{l}(q')],(y,y')\in\mathrm{r}(q)\times[\mathrm{r}(q')..\mathrm{r}(s')]\}.\) (28)

We can compute the similarity for the various subsets of indices (26), (27) and (28) as follows.

For (26), we apply Theorem 4.15 to the forests **F**[l(_s_)...r(_q_)) and \(\mathbf{F}'[\mathrm{l}(q')..\mathrm{r}(s')]\). Note that both forests do not contain any spine nodes so we are given as inputs to the SED instance all required inputs to the UFED instance, and thus we may compute \(\mathrm{sim}(\mathbf{F}[x..\mathrm{r}(q)),\mathbf{F}'[\mathrm{l}(q')..\mathrm{r}(s')])\) in time \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}\right)\).

For (27), we likewise apply Theorem 4.15 but this time to the forests **F**[l(_q_)...r(_s_)) and \(\mathbf{F}'[\mathrm{l}(s')..\mathrm{r}(q')]\). Following similar arguments as (26), we note that the required similarities \(\mathrm{sim}(\mathbf{F}[\mathrm{l}(q)..y),\mathbf{F}'[x'..\mathrm{r}(q')])\) are given by Output (2) in time \((n/n')^{1+o(1)}\cdot\mathsf{T}_{MUL}(n')\).

For (28), we observe that sub(_q)=q_ is a single node so we can compute the necessary entries using dynamic programming in \(O(n'^2)\) time.

Finally, for Inputs (ii), (iii) we again note that sub(_q)=q_ is a single node so we can obtain the necessary entries in \(O(n'^2)\) time.

In the unweighted setting, computing UFED takes time \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\).

## 6 Reduction from Spine Edit Distance to Tree Edit Distance

In this section, we prove Lemma 2.1, i.e., we reduce TED on SED.<sup>7</sup>

<sup>7</sup> Although \[BGHS19\] briefly mentions the existence of this reduction, it does so only in a footnote.


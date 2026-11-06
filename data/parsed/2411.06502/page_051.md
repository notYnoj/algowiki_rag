As in balanced case, we begin with the proof of a useful lemma.

**Lemma 5.16.** _Suppose we are provided with the input of an_ \((s,s',q,q')\)_-UDISED instance of size_ \((m,n')\)_. Further, let_ \(r\in\mathbf{S}\) _such that s\<r\<q. Then, we can compute_ \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{y}),\mathbf{F}'[x'..y'\mathbf{y}))\) _for all_ \((x,x')\in([l(s)..l(r)\mathbf{y})\times l(q'))\) _and_ \((y,y')\in(\mathbf{r}(r)\times[\mathbf{r}(q')..\mathbf{r}(s')\mathbf{y}))\) _in time_ \((m/n')^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MUL}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MonMUL}(n')+n'^{2+o(1)}g(n''))\) _where_ \(\mathrm{T}_\mathrm{MonMUL}(n',n',n',D)=\mathcal{O}(f(n')g(D))\).

**Proof.** Observe that \(x\in[l(s)..l(r)\mathbf{y})\) so that

\(\mathbf{F}[x..y\mathbf{y})=\mathbf{F}[x..\mathbf{r}(r)\mathbf{y})=\mathbf{F}[x..l(r)\mathbf{y})+\mathrm{sub}(r)\)

By Proposition 3.7 there exists \(z'\in[l(q')..y'\mathbf{y}]\) such that \((l(r),z')\) is an anchor of \(\mathrm{sim}(\mathbf{F}[x..\mathbf{r}(r)\mathbf{y}),\mathbf{F}'[l(q')..y'\mathbf{y}))\). Then we compute for the similarity \(\mathrm{sim}(\mathbf{F}[x..\mathbf{r}(r)\mathbf{y}),\mathbf{F}'[l(q')..y'\mathbf{y}))\) as

\(\mathrm{sim}(\mathbf{F}[x..\mathbf{r}(r)\mathbf{y}),\mathbf{F}'[l(q')..y'\mathbf{y}))\)<br>
\(=\mathrm{max}_{z^\prime\in[l(q^\prime)..y^\prime]}\big\{\mathrm{sim}(\mathbf{F}[x..l(r)\mathbf{y}),\mathbf{F}'[l(q')..z'\mathbf{y}))+\mathrm{sim}(\mathbf{F}[l(r)..\mathbf{r}(r)\mathbf{y}),\mathbf{F}'[z'..y'\mathbf{y}))\big\},\)

where the first summand can be computed from the output of Theorem 4.15 applied to **F**[l(_s_)..l(_r_)**)** (which contains no spine nodes) and \(\mathbf{F}'[l(q')..\mathbf{r}(s')\mathbf{y})\). Thus, since the inputs are at our disposal, we may apply Theorem 4.15 in time \(\mathcal{O}((m/n)^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MUL}(n')+n'^{2+o(1)}))\). We obtain the second summand in two steps. First, note \(\mathrm{sim}(\mathrm{sub}(r),\mathbf{F}'[l(q')..y'\mathbf{y}))\) is a subset of Output (i) of the \((r,s',q,q')\)-UDISED instance. To obtain the remaining values, we note that the remaining values \(\mathrm{sim}(\mathrm{sub}(r),\mathbf{F}'[z'..y'\mathbf{y}))\) are given by Output (iii) of the \((r,s',q,q')\)-UDISED instance. Finally, the computation can be performed by a max-plus product of an \((m+1)\times(n'+1)\) matrix and a \((n'+1)\times(n'+1)\) matrix in time \(\mathcal{O}(\mathrm{T}_\mathrm{MUL}(m,n',n'))=\mathcal{O}(m/n'\cdot\mathrm{T}_\mathrm{MUL}(n'))\).

Note that if the input instance is unweighted, the latter matrix is monotone, as for each fixed \(y'\) we have that similarity must not increase as \(z'\) increases (i.e. each column is non-increasing). Furthermore, since both matrices have entries corresponding to similarities between forests where the smaller forest has at most \(\mathcal{O}(n')\) nodes, both matrices have entries bounded by \(\mathcal{O}(n')\). In particular, we can combine them in time \(\mathcal{O}(\mathrm{T}_\mathrm{MonMUL}(m,n',n',n'))=\mathcal{O}(m/n)\cdot\mathrm{T}_\mathrm{MonMUL}(n')\). Furthermore, we instead apply Theorem 2.3 which only takes time \((m/n')^{1+o(1)}\cdot(\mathrm{T}_\mathrm{MonMUL}(n')+n'^{2+o(1)}g(n'))\).

We can finally prove Lemma 5.14.

**Proof of Lemma 5.14.** As before, the inputs of the \((r,s',q,q')\)-UDISED instance are a subset of the inputs of the \((s,s',q,q')\)-UDISED instance, so we can already assume the outputs of the \((r,s',q,q')\)-UDISED at our disposal.

\(\unknown\) Claim 5.17. _Given the outputs to the_ \((r,s',q,q')\)_-UDISED instance, we can compute the inputs for the_ \((s,s',r,q')\)_-UDISED instance in time_ \((m/n')^{1+o(1)}\cdot\mathrm{T}_\mathrm{MUL}(n')\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot\mathrm{T}_\mathrm{MonMUL}(n')\).

Proof. We rewrite the indices for Input (i) as

\(\{(x,x',y,y'):(x,x')\in[l(s)..l(r)]\times l(q'),(y,y')\in\mathbf{r}(r)\times[\mathbf{r}(q')..\mathbf{r}(s')]\}\) (23)

\(\cup\{(x,x',y,y'):(x,x')\in l(r)\times[l(s')..l(q')],(y,y')\in[\mathbf{r}(r)..\mathbf{r}(s)]\times\mathbf{r}(q')\}\) (24)

\(\cup\{(x,x',y,y'):(x,x')\in l(r)\times[l(s')..l(q')],(y,y')\in\mathbf{r}(r)\times[\mathbf{r}(q')..\mathbf{r}(s')]\}.\) (25)

Now, we describe how to compute \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{y}),\mathbf{F}[x'..y'\mathbf{y}))\) for the index sets (23), (24), and (25).

For (23), note that (23) is computed by Lemma 5.16.


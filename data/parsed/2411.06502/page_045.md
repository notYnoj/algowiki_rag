identical to the ones for Lemma 5.7. Thus, to prove Lemma 5.8, it suffices to compute the similarities for the ranges of _x_ that are left out in Lemma 5.7. That is, we need to compute \(\mathrm{sim}(F[x..x'),F'[y..y'))\) for

\((x,x')\in([\mathrm{I}(s)..\mathrm{I}(r)]\times\mathrm{r}(q'))\text{and}(y,y')\in(\mathrm{r}(r)\times[\mathrm{r}(q')..\mathrm{r}(s')])\cup([\mathrm{r}(q)..\mathrm{r}(r)]\times\mathrm{r}(s')).\)

To this end, observe that for such values of _x_ and _y_, we have **F**[_x...y_]=**F**[_x..._I(_r_)]+**F**[I(_r)..y_]. By Proposition 3.7, we have that \(\mathrm{I}(r)\times[\mathrm{r}(q')..\mathrm{r}(s')]\) serves as an anchor set for \(\mathrm{sim}(F[x..y),F'[x'..y'))\). Consequently, for such ranges of \(x,y,x',y'\) we can write:

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{z^\prime\in[\mathrm{r}(q^\prime)..\mathrm{r}(s^\prime)]:z^\prime\le y^\prime}\big\{\mathrm{sim}(F[x..\mathrm{I}(r)),F'[x'..z'))\)<br>
\(+\mathrm{sim}(F[\mathrm{I}(r)..y),F'[z'..y'))\big\}.\)

Recall that we are considering the case \(x'=\mathrm{r}(q')\). Additionally, note that one of _y_ and \(y'\) is always fixed, specifically either _y=_r(_r_) or \(y=\mathrm{r}(s')\). This means that, in the final expression, we are always working with at most two of \(x,y,x',y'\) which are not fixed. As before, this expression can be computed as a max-plus product, with \(z'\) traversing the hidden dimension of the product. In this computation, the second summand is obtained from Lemma 5.7, while the first summand is calculated by applying Main Theorem 4 on **F**[I(_s).._I(_r_)] and \(F'[\mathrm{r}(q')..\mathrm{r}(s'))\). In the unweighted setting, we again observe that the matrices are monotone and have entries bounded by the global tree size O(D), and apply Theorem 4.1 to compute FED.

**Lemma 5.9.** _Suppose we are provided with the input of an_ \((s,s',q,q')\)_-DISED instance of size m. Further, let_ \(r\in\mathbf{S}\) _such that s\<r\<q. Then, we can compute_ \(\mathrm{sim}(F[x..y),F'[x'..y'))\) _for all_ \((x,x')\in([\mathrm{I}(s)..\mathrm{I}(r)]\times\mathrm{I}(q'))\) _and_ \((y,y')\in(\mathrm{r}(r)\times[\mathrm{r}(q')..\mathrm{r}(s')])\cup([\mathrm{r}(q)..\mathrm{r}(r)]\times\mathrm{r}(s'))\) _in time_ O(T<sub>MUL</sub>(_m_)+_m_<sup>2+o(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm requires time_ O(T<sub>_MonMUL_</sub>(_m,m,m,_D)+_m_<sup>2+o(1)</sup>_g_(D)) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)).

**Proof.** Observe that for such ranges of \(x',y'\) (refer to Figure 12 for a visualization), we may write

\(F'[x'..y')=F'[\mathrm{I}(q')..y')=\mathrm{sub}(q')+F'[\mathrm{r}(q')..y').\)

By Proposition 3.7, we have that \(\mathsf{B}:=[\mathrm{I}(s)..\mathrm{r}(r)]\times\mathrm{r}(q')\) is an anchor set of \(\mathrm{sim}(F[x..y),F'[x'..y'))\). Now, consider the subset \(\mathsf{B}'\subseteq\mathsf{B}\) defined as \(\mathsf{B}':=[\mathrm{I}(q)..\mathrm{r}(r)]\times\mathrm{r}(q')\). We distinguish two cases.

(1) There is an anchor \((z,z')\in(\mathsf{B}\backslash\mathsf{B}')\), then we compute the similarity \(\mathrm{sim}(F[x..y),F'[x'..y'))\) as

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{z\in[\mathrm{I}(s)..\mathrm{I}(q)]:x\le z\le y}\big\{\mathrm{sim}(F[x..z),\mathrm{sub}(q'))+\mathrm{sim}(F[z..y),F'[\mathrm{r}(q')..y'))\big\},\)

using as first summand the input of the \((s,s',q,q')\)-DISED instance, and as second summands the values obtained via Lemma 5.8. In the unweighted setting, observe that entries are bounded by global tree size O(D).

(2) There is an anchor \((z,z')\in\mathsf{B}'\). Notice that for every \((z,z')\in\mathsf{B}'\), we have

\(F[z..y)=F[z..\mathrm{r}(q))+F[\mathrm{r}(q)..y).\)

By Proposition 3.7, we have that \(\mathsf{B}'':=\mathrm{r}(q)\times[\mathrm{r}(q')..y']\) is an anchor set of \(\mathrm{sim}(F[x..z),F[x'..z'))\). But since \((z,z')\) is an anchor of \(\mathrm{sim}(F[x..y),F'[x'..y'))\), by Proposition 3.8(ii), we obtain that \(\mathsf{B}''\) is anchor set of \(\mathrm{sim}(F[x..y),F'[x'..y'))\). Therefore, we can calculate

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{(z,z^\prime)\in\mathsf{B}''}\big\{\mathrm{sim}(F[x..z),F'[x'..z'))+\mathrm{sim}(F[z..y),F'[z'..y'))\big\}.\)


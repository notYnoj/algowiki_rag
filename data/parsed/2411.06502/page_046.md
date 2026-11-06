In this last expression, we can get the first summand from the input of the \((s,s',q,q')\)-DISED instance, and the second term from Main Theorem 4 applied on **F[r(q)..r(r))** and \(F'[r(s')..r(s'))\). In the unweighted setting, observe that entries are bounded by global tree size O(D), and we use Theorem 4.1 to compute FED.

**Lemma 5.3.** _Suppose we are given an_ \((s,s',q,q')\)_-DISED instance of size m, and let_ \(r\in\mathbf{S}\) _be such that s\<r\<q. Then, we can reduce the_ \((s,s',q,q')\)_-DISED instance to the_ \((s,s',r,q')\)_-DISED and_ \((r,s',q,q')\)_-DISED instances in time_ O(T<sub>MUL</sub>(m)+m<sup>2+o(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the reduction takes time_ O(T<sub>MonMUL</sub>(m,m,m,D)+m_<sup>2+o(1)</sup>g(D)) _where_ T<sub>MonMUL</sub>(m,m,m,D)=O(f(m)g(D)) _for some functions f,g._

**Proof.** Note, as the inputs of the \((r,s',q,q')\)-DISED instance are a subset of the inputs of the \((s,s',q,q')\)-DISED instance, we can already assume the outputs of the \((r,s',q,q')\)-DISED at our disposal. In the unweighted setting, we observe that all matrices are monotone and have entries bounded by O(D).

Claim 5.10. _With all the values at our disposal so far, we can compute the inputs for the_ \((s,s',r,q')\)_-DISED instance in time_ O(T<sub>MUL</sub>(m)+m<sup>2+o(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then we can do so in time_ O(T<sub>MonMUL</sub>(m,m,m,D)+m<sup>2+o(1)</sup>g(D)) _where_ T<sub>MonMUL</sub>(m,m,m,D)=O(f(m)g(D)).

Proof. We rewrite the indices for Input (i) as (see Figure 12)

\(\{(x,x',y,y'):(x,x')\in\mathrm{B}_\mathrm{T}^\mathrm{T}(s,s',r,q'),(y,y')\in\mathrm{B}_\mathrm{r}^\mathrm{T}(s,s',r,q')\}=\)<br>
\(\{(x,x',y,y'):(x,x')\in[|l(s)..l(r)]\times|l(q'),(y,y')\in[\mathrm{r}(r)..\mathrm{r}(s)]\times\mathrm{r}(q')\}\) (15)

\(\cup\{(x,x',y,y'):(x,x')\in[|l(s)..l(r)]\times|l(q'),(y,y')\in\mathrm{r}(r)\times[\mathrm{r}(q')..\mathrm{r}(s')]\}\) (16)

\(\cup\{(x,x',y,y'):(x,x')\in|l(r)\times[|l(s')..l(q')],(y,y')\in[\mathrm{r}(r)..\mathrm{r}(s)]\times\mathrm{r}(q')\}\) (17)

\(\cup\{(x,x',y,y'):(x,x')\in|l(r)\times[|l(s')..l(q')],(y,y')\in\mathrm{r}(r)\times[\mathrm{r}(q')..\mathrm{r}(s')]\}.\) (18)

Now, we describe how to compute sim(**F[x...y),F[x’..y’))** for the index sets (15), (16), (17), and (18).

For (15), note that (15) is a subset of the input of the \((s,s',q,q')\)-DISED instance.

For (16), note that (16) is a subset of the outputs of Lemma 5.9.

For (17), observe that (17) is equal to (16) under reverse symmetry.

For (18), note that (18) is a subset of the output of the \((r,s',q,q')\)-DISED instance.

It remains to explain how to retrieve Inputs (ii), (iii), (iv), (v) of the \((s,s',r,q')\)-DISED instance. Note, Inputs (ii) and (iii) are a subset of the input of the \((s,s',q,q')\)-DISED instance. Conversely, Input (iv) can be obtain using Lemma 5.8 on the \((s,s',r,q')\)-DISED instance, and Input (v) equals to Input (iv) under reverse symmetry.

With all the inputs at our disposal, we can call also the subroutine on the \((s,s',r,q')\)-DISED instance, and retrieve the ouputs. We can therefore assume that also the outputs of the \((s,s',r,q')\)-DISED instance are at our disposal. We now show how to compute the output of the \((s,s',q,q')\)-DISED instance.

Claim 5.11. _With all the values at our disposal so far, we can compute the outputs of the_ \((s,s',q,q')\)_-DISED instance in time_ O(T<sub>MUL</sub>(m)+m<sup>2+o(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then we can do so in time_ O(T<sub>MonMUL</sub>(m,m,m,D)+m<sup>2+o(1)</sup>g(D)) _where_ T<sub>MonMUL</sub>(m,m,m,D)=O(f(m)g(D)).


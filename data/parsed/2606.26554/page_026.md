**Case 1:** \(\left|N\left(V_i^{(b)}\right)\right|\le\frac{n}{|S_\mathrm{in}|}\). An iteration of the while loop requires time \(O\left(\left|S'(t)\right|\left|V_i^{(b)}\right|\left|N\left(V_i^{(b)}\right)\right|\right)\) (since the running time is dominated by the time taken to relax all edges from \(\mathcal{A}(s)\cap V_i^{(b)}\subseteq V_i^{(b)}\) to \(N\left(\mathcal{A}(s)\cap V_i^{(b)}\right)\subseteq N\left(V_i^{(b)}\right)\)). Over all iterations in _T(i,b_), the total time is

\(\sum_{t\in T(i,b)}O\left(\left|S'(t)\right|\left|V_i^{(b)}\right|\left|N\left(V_i^{(b)}\right)\right|\right)=O\left(\left|V_i^{(b)}\right|\left|N\left(V_i^{(b)}\right)\right|\left|S_\mathrm{in}\right|d\right)\)<br>
\(=O\left(\left|S_\mathrm{in}\right|\left|V_i^{(b)}\right|\frac{dn}{|S_\mathrm{in}|}\right)\)<br>
\(=O\left(\left|V_i^{(b)}\right|dn\right).\)

In the first equality, we use \(\sum_t|S'(t)|=O\left(\left|S_\mathrm{in}\right|d\right)\) by Lemma 5.17. In the second equality, we apply our upper bound on |_N(V<sub>i</sub>_)|.

**Case 2:** \(\left|N\left(V_i^{(b)}\right)\right|>\frac{n}{|S_\mathrm{in}|}\). Following Theorem 5.1, we obtain the time bound

\(O\left(\sum_{t\in T(i,b)}\mathsf{T}_\mathrm{MPP}\left(S'(t),N(V_i^{(b)}),N(V_i^{(b)})|B\right)\right)\)<br>
\(=\tilde{O}\left(\frac{d\phi n\mathrm{log}B}{\left|N\left(V_i^{(b)}\right)\right|}\mathsf{T}_\mathrm{MPP}\left(\frac{\left|S_\mathrm{in}\right|\left|N\left(V_i^{(b)}\right)\right|}{2\phi n\mathrm{log}B},N(V_i^{(b)}),N(V_i^{(b)})|B\right)\right)\)<br>
\(=\frac{n^{1+o(1)}\mathrm{log}B}{\left|N\left(V_i^{(b)}\right)\right|}\mathsf{T}_\mathrm{MPP}\left(\frac{\left|S_\mathrm{in}\right|\left|N\left(V_i^{(b)}\right)\right|}{n},N(V_i^{(b)}),N(V_i^{(b)})|B\right)\)

over all iterations. Here, we use Lemma 5.9 instead of BMM to compute the matrix product _X∗Y_ . In the first equality, we apply Lemma 5.7 and Lemma 5.18. In the second, we plug in our values \(d,\phi\leftarrow n^{o(1)}\).

Finally, to bound the time of the fourth step, we fix a source \(s\in S_\mathrm{in}\). Since \(\hat{L}(s,r)\) are disjoint so are A(_s,b_) over different iterations with distinct level(_s,b_), the total time required by all updates to \(\hat{L}\), A, and score variables is \(\widetilde{O}\left(n\right)\). Updating level(_s,b_) requires \(\widetilde{O}\left(Bn\right)\) time. Overall, the fourth step over all sources requires \(\tilde{O}\left(\left|S_\mathrm{in}\right|Bn\right)=\tilde{O}\left(Bn^2\right)\) time.

Summing over all \(V_i^{(b)}\) (again bucketing \(N\left(V_i^{(b)}\right)\) by size in increasing powers of 2), we obtain the total time bound

\(\mathrm{max}_{\frac{n}{|S_\mathrm{in}|\le T\le n}}\frac{n^{2+o(1)}\mathrm{log}B}{T^2}\mathsf{T}_\mathrm{MPP}\left(\frac{|S_\mathrm{in}|T}{n},T,T|B\right)=n^{o(1)}\mathrm{log}B\mathsf{T}_\mathrm{MPP}\left(\left|S_\mathrm{in}\right|,n,n|B\right)\)

where we apply Claim 5.8 to argue that the time is maximized when _T=n_. This concludes the proof of Theorem 1.3.

We prove the remaining lemmas. We begin with a few useful claims.

**Claim 5.19.** level(_s,b_) _increases only in iterations where_ level(_s,b_)=level(_s_) _at the start of the iteration._

_Proof of Claim 5.19._ We prove this claim inductively. The base case follows as initially all level(_s_) and level(_s,b_)=0. Consider the first iteration where \(\mathrm{level}(s)=\ell\), \(\mathrm{level}(s,b)>\ell\), and level(_s,b_) is incremented. Thus, we can assume \(\mathrm{level}(s,b)=\ell'>\ell\) is the smallest multiple of _b_ greater than \(\ell\). Note that level(_s,b_) can only increase via increaseLevel or updateScores. In increaseLevel, we only increase level(_s,b_) if level(_s,b_)=level(_s_). Otherwise, we run extendPaths and call updateScores if \(\mathcal{A}(s,b)=\emptyset\). In particular, in this iteration, since \(s\in S'\), a cluster \(V_i^{(b)}\) is selected such that \(\mathcal{A}(s,b)\cap V_i^{(b)}\neq\emptyset\).


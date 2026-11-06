**Case 2:** \(|N(V_i)|>\frac{\phi n\mathrm{log}n}{|S_\mathrm{in}|}\)**.** Similarly, the running time of each while loop is dominated by the boolean matrix product between \(S'\times V_i\) matrix _X_ and \(V_i\times N(V_i)\) matrix _Y_ . Summing over all iterations, we bound the total time as

\(O\left(\sum_{t\in T(i)}\mathsf{T}_\mathrm{BMM}(S'(t),V_i,N(V_i))\right)=O\left(\frac{d\phi n\mathrm{log}n}{|N(V_i)|}\mathsf{T}_\mathrm{BMM}\left(\frac{|S_\mathrm{in}||N(V_i)|}{\phi n\mathrm{log}n},N(V_i),N(V_i)\right)\right)\)

using Lemma 5.5, Lemma 5.6, the fact that \(V_i\subseteq N(V_i)\), and the following lemma.

**Lemma 5.7.** _Let a_<sub>1</sub>_,...,a<sub>p</sub> be positive integers with_ \(a_1+a_2+\cdots+a_p=a\)_, and q be a positive integer. Then,_

\(\sum_{j=1}^p\mathsf{T}_\mathrm{BMM}(a_j,q,q)=O\left(p\mathsf{T}_\mathrm{BMM}(a/p,q,q)\right).\)

_The result holds also for Min-Plus matrix multiplication (i.e._ T<sub>MPP</sub>_)._

_Proof of Lemma 5.7._ For all _a<sub>j</sub>_, we need to compute the product between an \(a_j\times q\) matrix _X_ and a \(q\times q\) matrix _Y_ . To do so, we construct \(\lceil\frac{a_j}{a/p}\rceil\) instances of matrix multiplication between \(\lceil\frac{a}{p}\rceil\times q\) and \(q\times q\) matrices, where each product computes \(\lceil a/p\rceil\) rows of the \(a_j\times q\times q\) matrix product. Formally, we split _X_ by its rows into \(\lceil\frac{a_j}{a/p}\rceil\) blocks of size \(\lceil\frac{a}{p}\rceil\times q\) and multiply each block by _Y_ . Overall, we need

\(O\left(\sum_j\left\lceil\frac{a_j}{a/p}\right\rceil\right)=O\left(p\right)\)

such matrix products.

Finally, we are ready to bound the running time over all clusters. First, for clusters with \(|N(V_i)|\le\frac{\phi n\mathrm{log}n}{|S_\mathrm{in}|}\) , the total time spent over all iterations of the while loop is then \(O\left(\sum_i|V_i|\phi nd\mathrm{log}n\right)=O\left(n^2\phi d\mathrm{log}n\right)\). For clusters with \(|N(V_i)|>\frac{\phi n\mathrm{log}n}{|S_\mathrm{in}|}\) , we observe that for any _k\>_0, there are at most 2_<sup>k</sup>_ clusters with \(|N(V_i)|\ge\frac{\phi n}{2^k}\) . Summing over _O_(log_n_) values of _k_, we obtain total running time:

\(O\left(d\phi^2n^2(\mathrm{log}n)^2\mathrm{max}_{T>\frac{\phi n\mathrm{log}n}{|S_\mathrm{in}|}}\frac{\mathsf{T}_\mathrm{BMM}\left(\frac{|S_\mathrm{in}|T}{\phi n\mathrm{log}n},T,T\right)}{T^2}\right)=O\left(d\phi^2n^2(\mathrm{log}n)^2\mathrm{max}_{T>\frac{n}{|S_\mathrm{in}|}}\frac{\mathsf{T}_\mathrm{BMM}\left(\frac{|S_\mathrm{in}|T}{n},T,T\right)}{T^2}\right).\)

We use the following claim to upper bound the final term.

**Claim 5.8.** _Let_ 0_\<z\<Z be constants independent of T. Then,_

\(\mathrm{max}_{z<T\unknown Z,T=2^k}\frac{\mathsf{T}_\mathrm{BMM}\left(T/z,T,T\right)}{T^2}=Z^{\omega\left(p\left(Z\right),1,1\right)-2+o\left(1\right)}\)

_where p_:=_p(Z_) _is defined so that T<sup>p</sup>=T/z._

_Furthermore, if_ T<sub>BMM</sub> _satisfies_

\(\mathsf{T}_\mathrm{BMM}(2m,2n,2n)\ge 4\mathsf{T}_\mathrm{BMM}(m,n,n)\)

_for all_ \(m,n\ge 1\)_, then_

\(\mathrm{max}_{z<T\unknown Z}\frac{\mathsf{T}_\mathrm{BMM}\left(T/z,T,T\right)}{T^2}=O\left(\frac{\mathsf{T}_\mathrm{BMM}\left(Z/z,Z,Z\right)}{Z^2}\right)\)

_The claim holds also if we replace_ T<sub>BMM</sub> _with_ T<sub>MPP</sub>.


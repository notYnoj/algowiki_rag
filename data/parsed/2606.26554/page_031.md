order, so it suffices to compute the transitive closure of _G_\[_L,R_\], a graph of _O_(1) vertices. Next, compute Equation (4) in _O_(|_S_<sub>in</sub>|) time, which bounds the running time of the base case.

Consider an invocation of the algorithm when \(R-L=\ell\). In this case, we make two recursive calls to intervals of size \(\ell/2\) and compute a \(S_\mathrm{in}\times\ell\times\ell\) matrix product in \(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\) time. In other words, we obtain the recursion

\(T(\ell)=2T(\ell/2)+\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\)

which we claim resolves to \(T(\ell)=\widetilde{O}\left(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\right)\). Formally, we first show the following claim.

**Claim 6.3.** _For any_ \(\ell\ge 0\),

\(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\ge 2\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell/2,\ell/2).\)

_The claim holds also if we replace_ T<sub>BMM</sub> _with_ \(\mathsf{T}_\mathrm{MPP}(S_\mathrm{in},\ell,\ell|B_1,B_2)\).

_Proof._ Let _A,B_ be arbitrary \(S_\mathrm{in}\times\ell/2\) boolean matrices (resp. integer matrices with finite entries in \[_B_<sub>1</sub>\]) and _C,D_ be arbitrary \(\ell/2\times\ell/2\) boolean matrices (resp. integer matrices with finite entries in \[_B_<sub>2</sub>\]). Then, define

\(X=\left(AB\right),Y=\left(\begin{array}{ c c }
C & 0_{\ell/2\times\ell/2} \\
0_{\ell/2\times\ell/2} & D
\end{array}\right)\)

so that \(XY=\left(ACBD\right)\). In particular, we compute two arbitrary \(S_\mathrm{in}\times\ell/2\times\ell/2\) matrix products with one \(S_\mathrm{in}\times\ell\times\ell\) matrix product.

Then, we can bound the running time of one recursive call as

\(T(\ell)=2T(\ell/2)+\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\)<br>
\(=O\left(\sum_{0\unknown i\unknown\mathrm{log}\ell}\frac{\ell}{2^i}\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},2^i,2^i)\right)\)<br>
\(=O\left(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},\ell,\ell)\mathrm{log}\ell\right)\)

where in the final inequality we apply Claim 6.3.

In fact, our algorithm, with minor modifications, can be used to compute MSSP on unweighted directed acyclic graphs.

**Theorem 1.6.** _There is a deterministic algorithm computing_ MSSP _on unweighted directed acyclic graphs in_ \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}(|S_\mathrm{in}|,n,n|n,1)\right)\) _time._

We in fact prove a slightly stronger result.

**Proposition 6.4.** _Let_ \(B,D\ge 1\)_. Then, there is a deterministic algorithm computing_ MSSP _on directed acyclic graph with edge weights in_ {0_,...,B_} _and_ \(\mathrm{diam}(G)\le D\) _in_ \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}(S_\mathrm{in},n|D,B)\right)\) _time._

Theorem 1.6 follows by applying _B_=1 and _D=n_.

_Proof._ As before, we assume the graph is sorted in topological order, and keep the same notation as Theo rem 1.5. We let \(\widehat{\mathsf{d}}(s,v)\) denote the estimated distance between \(s\in S_\mathrm{in}\) and \(v\in V\) , with all values initialized to \(\infty\). We then run the following algorithm, replacing reach with \(\widehat{\mathsf{d}}\) and BMM with MPP.

complete(_G,S_<sub>in</sub>_,L,R_):<br>
**Input:** Topologically sorted DAG _G_, sources S<sub>in</sub>, and interval endpoints \(L\le R\).<br>
(Assume \(\widehat{\mathsf{d}}(s,v)=\mathrm{dist}(s,v)\) is computed for \(s\in S_\mathrm{in}\) and _v_ where either \(v\le L\) or \(\mathrm{pred}(s,v)\le L\).)<br>
1. If \(R-L\le 2\), compute \(\widehat{\mathsf{d}}(s,v)\) for all \(s\in S_\mathrm{in}\) and \(L<v\le R\).


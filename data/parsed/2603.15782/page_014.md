<tbc>from valid cuts (_S_<sub>cut</sub>_,T_<sub>cut</sub>) to element cuts (_X,Y,U_) by setting \(X=\{x\in V:x^+,x^-\in S_\text{cut}\}\), \(Y=\{x\in V:x^+,x^-\in T_\text{cut}\}\), _U=V-X-Y_ . The lemma below gives some structural properties of this construction.

**Lemma 12.** _(a) For each element cut_ (_X,Y,U), the cost of a minimum valid cut_ (_S_cut_,T_cut) _that maps to_ (_X,Y,U_) _equals_

\(\Phi(X,Y,U):=\frac{w(U)}{2}+w(E(X,Y))+\mu|A\cap Y|+\mu|B\cap X|\ge\frac{1}{2}\text{\texttt{cost}}(X,Y,U)\)

_In particular, if_ (_S_cut_,T_cut) _is a minimum valid cut in_ \(\mathcal{N}(A,B,\mu)\) _and_ (_X,Y,U_) _is the corresponding element cut then_ \(F:=\text{\texttt{cost}}(S_\text{cut},T_\text{cut})=\Phi(X,Y,U)=min_{(X^\prime,Y^\prime,U^\prime)}\Phi(X',Y',U')\)_. If in addition_ |_A_|=|_B_|=_k and_ \(F\le\mu k/2\) _then_ (_X,Y,U_) _is k/_(2_n)-balanced.<br>
(b) s-t flows in_ \(\mathcal{N}(A,B,\mu)\) _are equivalent, with the same value, to nonnegative weightings f<sub>p</sub> of simple A-B paths satisfying_

\(\sum_{p:x\in p}f_p\le w(x)/2,\sum_{p:e\in p}f_p\le w(e),\sum_{p:x\in\partial p}f_p\le\mu\)

_for all nodes_ \(x\in V\) _and edges_ \(e\in E\)_. If D is the demand graph of such f and_ \(\lambda_e=\sum_{p:e\in p}f_p\) _then_

\(deg(G^\lambda)\le w|_V,\lambda_e\le w(e),\sum_pf_pt_p-\sum_e\lambda_eL_e=-\mathcal{L}(D),\|\mathcal{L}(D)\|\le 2\mu.\)

_Proof._ **(a)** The first claim can be checked mechanically. If \(F\le\mu k/2\), then \(|A\cap Y|,|B\cap X|\le F/\mu\le k/2\). As |_A_|=|_B_|=_k_, at least _k/_2 vertices lie outside each of _X,Y_ , proving balance.

**(b)** Each simple _A-B_ path _p_=(_x_<sub>0</sub>_,...,x<sub>k</sub>_), with _e<sub>i</sub>=x_<sub>_i_-1</sub>_x<sub>i</sub>_, lifts to the _s-t_ path

\((s,x_0^+,x_0^-,e_1^-,e_1^+,x_1^+,x_1^-,\dots,e_k^-,e_k^+,x_k^+,x_k^-,t)\)

in \(\mathcal{N}(A,B,\mu)\). Conversely, every simple _s-t_ path has this form: traversing an edge gadget back to the same vertex, or revisiting an original vertex, would repeat its split nodes. Thus, removing flow cycles and decomposing the remaining flow into simple paths gives the inverse transformation without changing its value. The split-arc, edge-bottleneck and source/sink capacities give exactly the vertex, edge and endpoint load bounds, respectively, proving the first claim and \(\lambda_e\le w(e)\). Each path uses at most two edges incident to any vertex, proving the degree bound. The Laplacian identity follows by cancelling the edge Laplacians along each path, leaving its negative endpoint Laplacian. Finally, the endpoint bound gives \(deg(D)\le\mu\) and hence \(\|\mathcal{L}(D)\|\le 2\mu\).

Graph \(\mathcal{N}(A,B,\mu)\) has _O(m_) nodes and arcs. Note that infinite capacities can be replaced with \(n\mu+1\) without affecting Lemma 12 (since the total flow cannot exceed \(n\mu\)).

We will use graph \(\mathcal{N}(A,B,\mu)\) inside the following subroutine, which takes a vector in R_<sup>d</sup>_ as an input. (Parameter \(\mu\) is assumed to be fixed).

\(\text{\textbf{Algorithm 3:} \textbf{DirectionalFlowCut}}(u)\text{\textbf{.}
\textbf{1} compute}h_x=\langle x,u\rangle\text{for each}x\in S\text{( "height" of}x\text{in the direction}u\text{)
\textbf{2} sort}\{h_x\}_{x\in S}\text{and let}A,B\subseteq S\text{, with}|A|=|B|=2c'n\text{, contain the smallest and largest heights, respectively, breaking ties by a fixed rule
\textbf{3} construct graph}G'=\mathcal{N}(A,B,\mu)\text{\textbf{4} compute a maximum}s-t\text{flow}f'\text{in}G'\text{and a minimum valid cut}(S_\text{cut},T_\text{cut})\text{; let}F\text{be their common value
\textbf{5} remove cycles from}f'\text{and implicitly decompose it into simple paths; project these to a weighted}A\text{-}B\text{path routing}f\text{in}G\text{as in Lemma 12(b)
\textbf{6} compute demands}d_{xy}=\sum_{p:\partial p=\{x,y\}}f_p\text{for}x\in A,y\in B\text{; let}D\text{be the undirected graph with edge weights}d_{xy}\text{\textbf{7} construct the element cut}(X,Y,U)\text{from}(S_\text{cut},T_\text{cut})\text{as in Lemma 12(a), and return}A,B,h,F,f,D,(X,Y,U)\)


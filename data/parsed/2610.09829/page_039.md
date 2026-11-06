where we additionally know the best such choice for \(\widetilde{\beta}_{i-1}\cap\widetilde{\gamma}_{i-1}\). Now for a "guessed" choice of the subpath \(\widetilde{\gamma}_q[u_q,v_q]=\widetilde{\beta}_q\cap\widetilde{\gamma}_q\), we will find the "best" choices of the cycles for each \(i\in[q-1]\), by querying the entries for computed up to _q_-1. Here, the crux of why this dynamic programming works is that a cycle \(\widetilde{\beta}_i\) can only "non-trivially" intersect with cycles \(\widetilde{\beta}_{i-1}\) and \(\widetilde{\beta}_{i+1}\). In the above, when we say "non-trivial" we mean the case where the common edge set is not exactly \(\widetilde{\gamma}_i\cap\widetilde{\gamma}_{i^\prime}\), for \(i'\in[b]\). The above is due to the construction of _H_. We additionally remark that an edge can belong to at most two of the cycles from \(\widetilde{\beta}_{i-1},\widetilde{\beta}_i,\widetilde{\beta}_{i+1}\) due to Observation 5.4.

For those \(i'\in[b]\), where \(\beta_{i^\prime}\cap\widetilde{\beta}_q\) must be the same as \(\gamma_{i^\prime}\cap\widetilde{\gamma}_q\), the contribution of this intersection will be a fixed number when we are looking for solutions that are "\(\theta_i\)-abiding", for each \(i\in[b]\). Thus the above part of the intersections can be handled separately, as \(\widetilde{\gamma}_i\)s alone determine the above discussed number.

**Useful notations.** We introduce some notations that will help us in defining/computing the states of our dynamic programming table over connected components of _H_.

To capture such pairwise edge intersections (outside P) of cycles we define the following. For two subgraphs _G_<sub>1</sub> and _G_<sub>2</sub> of _G_, let \(\zeta_{G_1,G_2}\) denote the weight of the edges common to both graphs that are not in P, i.e., \(\zeta_{G_1,G_2}=w\big(E(G_1\cap G_2)\backslash E(\mathcal{P})\big)\).

Consider a connected component \(\widetilde{H}\) of _H_, and we let \(\widetilde{H}=(\widetilde{\gamma}_1,\widetilde{\gamma}_2,\cdots,\widetilde{\gamma}_\widetilde{p})\), which is a cycle or a path (see Observation 5.9). Note that \(V(\widetilde{H})\subseteq R_\mathsf{o}\), and for \(i\in[\tilde{p}]\), we let \(i_j\in[b]\) such that \(\gamma_{i_j}=\widetilde{\gamma}_i\). Furthermore, let \(\widetilde{h}_i=h_{i_j}\), \(\widetilde{\psi}_i=\psi_{i_j}\), \(\widetilde{\tau}_i=\tau_{i_j}\), \(\widetilde{\theta}_i=\theta_{i_j}\), and \(\widetilde{\Gamma}_i=\Gamma_{i_j}\). For \(i\in[\tilde{p}]\), let \(\widetilde{P}_i\) be the path _P<sub>i<sub>j</sub></sub>_, which is the unique maximal path of vertices of degree 2, between \(\widetilde{\gamma}_i^\mathsf{s}=\gamma_{i_j}^\mathsf{s}\) and \(\widetilde{\gamma}_i^\mathsf{t}=\gamma_{i_j}^\mathsf{t}\) in \(\mathcal{T}_{\gamma_i}\) (see Figure 14).

In our dynamic programming, we will start from _q_=1 till \(q=\tilde{p}\), and at state for _q_, we will "guess" the subpath \(\beta_q^*\cap\gamma_q\). To this end we introduce the following notation. For \(\gamma\in V(\mathcal{T})\), and distinct \(u,v\in V(\gamma)\), \(\gamma[u,v]\) is the sub-path of \(\gamma\) starting from _u_ till _v_ (inclusive of both _u_ and _v_) in the clockwise ordering \(\gamma^\circ\). For \(q\in[\tilde{p}]\) and distinct \(u,v\in V(\widetilde{\gamma}_q)\), let \(\mathcal{D}_{q,u,v}=\{\beta\in V(\widetilde{P}_i)|\beta\cap\widetilde{\gamma}_q=\)<tbc>

Vp
Bp
7i
Bi
Vi
u12
B1
C
71
Vi-1
ui
Vi
ui-1
72
Bi-1
7i-1

Figure 17: Illustration for the case when \(\widetilde{H}=(\widetilde{\gamma}_1,\widetilde{\gamma}_2,\dots,\widetilde{\gamma}_\widetilde{p})\) is a cycle. The gray closed curves illustrate the embedding of the cycles \(\widetilde{\gamma}_i\)s on the plane. The curly closed curves in red and blue colors illustrate \(\widetilde{\beta}_1\) and \(\widetilde{\beta}_\widetilde{p}\), respectively. Also, \(\widetilde{\beta}_i\cap\widetilde{\gamma}_i=\widetilde{\gamma}_i[u_i,v_i]\), for \(i\in[\tilde{p}]\). The thick curly green curve illustrates \(\widetilde{\beta}_1\cap\widetilde{\beta}_\widetilde{p}\).


\(B_\pi^{v_1},B_\pi^{v_2},\dots,B_\pi^{v_{2r-1}}\) where \(B_\pi^{v_i}\) have vertex set \(\{b(\tau,v_i,\pi)|\tau\in S_\pi\}\). They are crossing in the middle, i.e., \(B_\pi^{h_r}=B_\pi^{v_r}\).

For every even block we add a co-matching towards the previous block and a matching towards the next block. That is, for \(\tau,\tau'\in S_\pi\) with \(\tau\neq\tau'\) and even \(i\in[2r-1]\), add to \(C_\pi^r\) edges between

\(b(\tau,h_i,\pi)\) and \(b(\tau',h_{i-1},\pi);b(\tau,h_i,\pi)\) and \(b(\tau,h_{i+1},\pi)\);

\(b(\tau,v_i,\pi)\) and \(b(\tau',v_{i-1},\pi);b(\tau,v_i,\pi)\) and \(b(\tau,v_{i+1},\pi)\).

Additionally, for each odd \(i\in[2r-1]\), add

vertices \(a_1(h_i,\pi)\) and \(a_2(h_i,\pi)\) complete to \(B_\pi^{h_i}\); and

vertices \(a_1(v_i,\pi)\) and \(a_2(v_i,\pi)\) complete to \(B_\pi^{v_i}\).

Note that since _r_ is odd, a pair of such vertices is created for \(B_\pi^{h_r}=B_\pi^{v_r}\). This is done to guarantee that a vertex is picked in each odd block. The endpoints of the paths are called _border blocks_, and any other block in \(C_\pi^r\) is called an _interior block_.

We construct \(G_\mathcal{S}^r\) by taking the disjoint union of all the \(C_\pi^r\) for \(\pi\in[k]^2\). Additionally, to ensure that the same first or second component is selected between adjacent gadget cells, we add the following vertices and edges.

For each \(\pi\in[k-1]\times[k]\), add a set of vertices \(\{r(i,\pi)|i\in[n]\}\) and edges between \(b((i,\text{\_}),h_{2r-1},\pi)\in B_\pi^{h_{2r-1}}\) and \(r(j,\pi)\) for \(i,j\in[n]\) with \(i\neq j\); and \(b((i,\text{\_}),h_1,\pi_\blacktriangleright)\in B_{\pi^\blacktriangleright}^{h_1}\) and \(r(i,\pi)\) for \(i\in[n]\).

For each \(\pi\in[k]\times[k-1]\), add a set of vertices \(\{d(i,\pi)|i\in[n]\}\) and edges between \(b((\text{\_},i),v_{2r-1},\pi)\in B_\pi^{v_{2r-1}}\) and \(d(j,\pi)\) for \(i\neq j\in[n]\); and \(b((\text{\_},i),v_1,\pi_\triangledown)\in B_{\pi_\triangledown}^{v_1}\) and \(d(i,\pi)\) for \(i\in[n]\).

This concludes the construction of \(G_\mathcal{S}^r\) and note that \(|V(G_\mathcal{S}^r)|=\mathcal{O}(rn^2k^2)\).

The following claims can be shown similarly to their counterparts in Theorem 3. For the equivalence of Grid Tiling and _k_-Dominating Set instances, it follows from the fact that the only dominating sets of size 2_r_-1 of a gadget cell \(C_\pi^r\) are of the form

\(Dom_\pi:=\{b(\tau,h_{2i-1},\pi),b(\tau,v_{2i-1},\pi)|i\in[r]\}\)

for some \(\tau\in S_\pi\). Moreover, the vertices added between adjacent gadget cells force any dominating set to select the corresponding component in a dominating set of size (2_r_-1)_k_<sup>2</sup>.

\(\triangleright\) Claim 18. (S_,k,n_) is a positive Grid Tiling instance if and only if \(G_\mathcal{S}^r\) is a positive (2_r_-1)_k_<sup>2</sup>-DS instance.


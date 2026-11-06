between \(b(\tau,v_i,\pi)\) and \(b(\tau',v_{i+1},\pi)\).<br>
Let us name the endpoints of the paths after the four directions _up_, _down_, _left_, and _right_:<br>
\(L_\pi=B_\pi^{h_1}R_\pi=B_\pi^{h_r}U_\pi=B_\pi^{v_1}D_\pi=B_\pi^{v_r}\)<br>
We call these blocks the _border blocks_, and any other block in \(C_\pi^r\) is called an _interior block_. We construct \(G_\mathcal{S}^r\) by taking the disjoint union of all the \(C_\pi^r\) for \(\pi\in[k]^2\), and adding edges between border blocks of adjacent cells. Specifically, we add an edge between<br>
\(b(\tau,h_r,\pi)\in R_\pi\) and \(b(\tau',h_1,\pi_\blacktriangleright)\in L_{\pi_\blacktriangleright}\) if and only if \(\tau\) and \(\tau'\) have a different first component, for all \(\pi\in[k-1]\times[k]\), and<br>
\(b(\tau,v_r,\pi)\in D_\pi\) and \(b(\tau',v_1,\pi_\triangledown)\in U_{\pi_\triangledown}\) if and only if \(\tau\) and \(\tau'\) have a different second component, for all \(\pi\in[k]\times[k-1]\). This concludes the construction of \(G_\mathcal{S}^r\). Note that \(|V(G_\mathcal{S}^r)|=\mathcal{O}(rn^2k^2)\).<br>
\(\triangleright\) Claim 15. (S_,k,n_) is a positive Grid Tiling instance if and only if \(G_\mathcal{S}^r\) is a positive (2_r_-1)_k_<sup>2</sup>-Independent Set instance.<br>
Proof. Assume there is a solution for (S_,k,n_) using tiles \(s(\pi)\in S_\pi\) for every \(\pi\in[k]^2\). We claim that<br>
\(I=\bigcup_{\pi\in[k]^2}I_\pi\text{with}I_\pi:=\{b(s(\pi),h_i,\pi),b(s(\pi),v_i,\pi)|i\in[r]\}\)<br>
is an independent set of size (2_r_-1)_k_<sup>2</sup>. Clearly, _I_ has the desired size. For each cell \(\pi\), \(I_\pi\) is an independent set since it comprises only copies of the same tile \(s(\pi)\). By construction, two vertices in distinct sets \(x\in I_\pi\) and \(y\in I_{\pi^\prime}\) can only be adjacent if, up to symmetry, either<br>
\(\pi'=\pi_\blacktriangleright\), and \(x\in R_\pi\) and \(y\in L_{\pi_\blacktriangleright}\) have a different first component; or<br>
\(\pi'=\pi_\triangledown\), and \(x\in D_\pi\) and \(y\in U_{\pi_\triangledown}\) have a different second component.

C5 π
C5 π
U π
S π
S π
(1,1)
(1,3)
(2,2) (2,3)
(2,1)
L π
R π
L π
(3,3)
(3,2) (3,3)
(1,1)
(1,3)
(2,1)
(3,3)
S πv
D π
C5 πv
U πv

**Figure 1** Construction of a gadget cell \(C_\pi^5\) for a cell \(\mathcal{S}_\pi\), and its edge-relation with the right and down gadget cells. Any set of vertices in a black box forms a clique. Two black boxes linked with a black thick edge form a biclique minus the edges in blue, which are non-edges.


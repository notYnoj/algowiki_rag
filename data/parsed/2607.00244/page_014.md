Both possibilities are ruled out due to the \(s(\pi)\) forming a solution to Grid Tiling. Hence, _I_ is indeed an independent set.

Conversely, assume there exists an independent set _I_ of size (2_r_-1)_k_<sup>2</sup>. Since we constructed the _k_<sup>2</sup> graphs \(C_\pi^r\) from 2_r_-1 cliques each, _I_ must contain exactly 2_r_-1 vertices from each \(C_\pi^r\). Since those 2_r_-1 vertices are pairwise non-adjacent, they must be of the form

\(I_\pi:=\{b(s(\pi),h_i,\pi),b(s(\pi),v_i,\pi)|i\in[r]\}\)

for some common \(s(\pi)\in S_\pi\). We now argue that the tiles \(s(\pi)\) form a Grid Tiling solution for (S_,k,n_). For every \(\pi\in[k-1]\times[k]\), we have that \(b(s(\pi),h_r,\pi)\in R_\pi\) and \(b(s(\pi)_{\blacktriangleright},h_1,\pi_{\blacktriangleright})\in L_{\pi_{\blacktriangleright}}\) are part of the same independent set _I_ and hence non-adjacent. By construction, we must have that \(s(\pi)\) and \(s(\pi_{\blacktriangleright})\) agree on the first component. Analogously, for every \(\pi\in[k]\times[k-1]\), the tiles \(s(\pi)\) and \(s(\pi_\triangledown)\) agree on the second component. This concludes the proof of the correctness of the reduction. \(\triangleleft\)

We now upper-bound the radius-(_r_-1) merge-width of the produced graphs.

\(\vartriangleright\) Claim 16. \(\mathrm{mw}_{r-1}(G_\mathcal{S}^r)\unknown 4r-3\).

Proof. We will construct a merge sequence for \(G:=G_\mathcal{S}^r\) of radius-(_r_-1) width 4_r_-3. First, we define the following sets:

Let _N<sub>in</sub>_ be the set of all the non-edges between consecutive copies of \(B_\pi\) inside a cell gadget \(C_\pi^r\) for all \(\pi\in[k]^2\). These are the blue edges within the same cell gadget in Figure 1.

Let _N<sub>out</sub>_ be the set of all the non-edges between adjacent border blocks of adjacent cell gadgets in _G_. These are the blue edges between two cell gadgets in Figure 1.

Define the _layers_ of each border block:

We can define the following merge sequence. We use the letter _F_ for the set of resolved pairs, since _R_ is taken by the right border blocks.

**1.** Let P<sub>1</sub> be the partition of _V(G_) into singletons and _F_<sub>1</sub>:=_N<sub>in</sub>_.

**2.** The parts of P<sub>2</sub> are each interior block of each cell gadget, and for each \(i\in[n]\) and \(X\in\{L,R,U,D\}\), each layer \(X_\pi^i\). We keep _F_<sub>2</sub>:=_F_<sub>1</sub>.

**3.** The parts of P<sub>3</sub> are each block of each cell gadget. We set \(F_3:=F_2\cup N_{out}\).

**4.** We finally let P<sub>4</sub>:={_V(G_)} and \(F_4:=F_3\cup E(G)\).

By construction P_<sub>i</sub>_ is coarser than P<sub>_i_-1</sub>, \(F_i\subseteq F_{i+1}\), and P_<sub>i</sub>_ is homogeneous modulo _F<sub>i</sub>_. We now argue that the radius-(_r_-1) width of the sequence

\((\mathcal{P}_1,F_1),(\mathcal{P}_2,F_2),(\mathcal{P}_3,F_3),(\mathcal{P}_4,F_4)\)

is at most 4_r_-3.

The radius-(_r_-1) (in fact the radius-\(\infty\)) width of (P<sub>1</sub>_,F_<sub>2</sub>=_N<sub>in</sub>_) is at most 2_r_-1 since every connected component of (_V(G),F_<sub>2</sub>) has exactly 2_r_-1 vertices.

For (P<sub>2</sub>_,F_<sub>3</sub>), observe that for any vertices _x_ and _y_ in the same border block \(B_\pi\) of \(C_\pi^r\) but in different layers, \(dist_{F_3}(x,y)\unknown 2r\). Indeed, if there is a path of length at most 2_r_ between them, then it must be of the form \(x,\dots,x',z,y',\dots,y\) where \(x'\) and \(y'\) are the respective copies of _x_ and _y_ in another border block \(B'_\pi\) of \(C_\pi^r\), and _z_ is a vertex in the border block adjacent to \(B'_\pi\) such that \(x'z,y'z\in N_{out}\). Since \(dist_{F_3}(x,x')=dist_{F_3}(x,y')=r-1\), it follows

\begin{tabular}{ccc}
\(L_\pi^i:=\{b(\tau,h_1,\pi)|\tau\in S_\pi,\tau=(i,\text{\_})\},\) & \(R_\pi^i:=\{b(\tau,h_r,\pi)|\tau\in S_\pi,\tau=(i,\text{\_})\},\) & \\
\(U_\pi^i:=\{b(\tau,v_1,\pi)|\tau\in S_\pi,\tau=(\text{\_},i)\},\) & \(D_\pi^i:=\{b(\tau,v_r,\pi)|\tau\in S_\pi,\tau=(\text{\_},i)\}.\) & \\
\end{tabular}


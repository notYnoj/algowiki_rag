The first step uses the same moment partition and positivity; the second step uses \(d(U)\ge\delta\) and the choice of \(\ell\). Assign weights _w<sub>j</sub>_:=2<sup>-(_j_+2)</sup>, whose sum is less than 1. Some class contributes at least \((3\delta/4)w_j\) to this moment sum. Averaging within that class replaces Eq. (3) by

\(|W|\ge\frac{3\delta}{8}2^{-(j+1)(\ell+1)}|U|,\nu_v(u)\ge(1+2^j)\nu(u)(u\in W).\)

The size bound follows by substituting _w<sub>j</sub>_ and dividing by \(2^{(j+1)\ell}\); the marginal bound follows from the conditioning identity and \(M(u,v)\ge 2^j\). Geometric weights avoid a loss depending on the number of scales.

#### Step 3: Charge vertex loss to marginal gain.

Put \(\Lambda:=h+log(16/3)\), \(c_i:=(j_i+1)(\ell+1)+\Lambda\), and \(K:=2(\ell+1)+2\Lambda=O(h)\). Here _c<sub>i</sub>_ includes the loss from deleting the conditioned vertex. Set \(\tau_{i+1}:=(1+2^{j_i})\tau_i\) and let _m_ be the number of conditioning steps. Lemma 4.2 replaces the fixed cost in Eq. (4) by

\(\sum_{i<m}c_i\le K\sum_{i<m}log(1+2^{j_i})=Klog(\tau_m/\tau_0)\le K(t+1).\)

The first step sums the bounds from Lemma 4.2, the second step uses the threshold product, and the third step uses \(\tau_m\le 1\). For \(N\ge 2^{(2K+1)(t+1)}\), Lemma 4.3 retains at least 2<sup>-(_K_+1)(_t_+1)</sup>_N_ vertices. Every gain is at least 3/2, so sparsity is reached after _O(t_) steps. Lemma 4.5 accounts for the singleton case and the slack in the objective, giving \(|U|\ge 2^{-O(th)}N\).

#### Step 4: Enumerate conditioning sets and thresholds.

The SDP setup and shift \(t\mapsto t+1\) are unchanged. We again require \(\mu(S)>0\). The threshold now depends on the gains, so Eq. (5) is replaced by

\(U_{S,w}:=\{u\in V\backslash S:\mu_S(u)\ge\mu_S(w)\},|S|\le 2t+3,w\in V\backslash S.\)

Choosing a vertex _w_ with minimum marginal in the desired set recovers that set exactly. Enumer ating both _S_ and _w_ preserves the running time _N_<sup>_O(t_)</sup> for _h=O(t_).

#### Step 5: Apply greedy extraction with the improved size bound.

The greedy bound in Eq. (6) is unchanged. With _h=t_+1, the improved size estimate becomes

\(|U|\ge 2^{-O(t^2)}N,d(U)\le 2^{-(t+1)}.\)

The proof of Theorem 4.6 establishes \(|U|\ge 2^{t+1}\) for \(t\le\sqrt{logN}/12\). The resulting independent set has size at least 2_<sup>t</sup>_, giving an approximation ratio of \(N/2^{\Omega(\sqrt{logN})}\) in quasi-polynomial time.

## 3 Preliminaries

Throughout this paper, logarithms are to base 2. For a vector _x_, we use \(x^\top\) to denote its transpose. We use \(\circ\) to denote Hadamard product. For real symmetric matrices _A_ and _B_ of the same size, we write \(A\unknown B\) if _B-A_ is positive semidefinite.

For a nonempty set \(U\subseteq V\) , define its edge density by

\(d(U):=\frac{|\{(u,v)\in U\times U:uv\in E\}|}{|U|^2}=\frac{2|E(G[U])|}{|U|^2}.\) (7)

The first step defines _d(U_), and the second step follows because each edge contributes two ordered pairs. For an integer \(k\ge 0\), let \(\mathcal{V}_k:=\{A\subseteq V:|A|\le k\}\).


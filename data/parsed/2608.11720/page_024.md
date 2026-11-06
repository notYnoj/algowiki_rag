## A.2. Chain teleportation.

Here we prove Lemma 6.1, which states that if teleportation is performed in parallel in a chain of nodes, the overall effect is a relabelling of the registers (see Figure 3).

**Lemma 6.1.** _Consider_ \(n\ge 2\) _vertices in a chain, with each vertex_ \(p\in[n]\) _holding three d- dimensional registers_ X(_p),_ Y(_p),_ Z(_p). For each_ \(p\in[n-1]\)_, the registers_ Y(_p_) _and_ Z(_p_+1) _share a maximally entangled state_ \(|\Phi\rangle_{\mathsf{Y}(p)\mathsf{Z}(p+1)}\).

_Let_ E _be a finite-dimensional environment and let_ \(\rho\) _be a state on_ \(\mathsf{X}(1)\mathsf{X}(2)\cdots\mathsf{X}(n-1)\mathsf{E}\)_. Suppose that each vertex_ \(p\in[n-1]\) _measures_ X(_p_)Y(_p_) _in the maximally entangled basis, obtains outcome k<sub>p</sub>, and the corresponding correction P<sub>k<sub>p</sub></sub> is applied on_ Z(_p_+1)_. Then the resulting state on_ \(\mathsf{Z}(2)\mathsf{Z}(3)\cdots\mathsf{Z}(n)\mathsf{E}\) _is the reduced state obtained from_ \(\rho\) _by relabelling each_ X(_p_) _as_ Z(_p_+1)_, for_ \(p\in[n-1]\).

_Proof._ Let the initial state be

\(\sigma=\rho_{\mathsf{X}(1)\mathsf{X}(2)\cdots\mathsf{X}(n-1)\mathsf{E}}\otimes\otimes_{p=1}^{n-1}|\Phi\rangle\langle\Phi|_{\mathsf{Y}(p)\mathsf{Z}(p+1)},\)

where we consider Z(1),X(_n),_Y(_n_) as part of the environment register E.

Decompose \(\rho\) as

\(\rho=\sum_{i=1}^r\lambda_i|u_i\rangle\langle u_i|_{\mathsf{X}(1)\mathsf{X}(2)\cdots\mathsf{X}(n-1)\mathsf{E}}\)

(cf. Eq (4)), where \(\lambda_1,\dots,\lambda_r\in\mathbb{R}_{>0}\) and \(|u_1\rangle,\dots,|u_r\rangle\in\mathsf{X}(1)\mathsf{X}(2)\cdots\mathsf{X}(n-1)\mathsf{E}\). Let us apply the teleportation identity (Eq (7)) to the X(1)Y(1)Z(2) registers of \(\sigma\). This yields

\(\sigma=\frac{1}{d^2}\sum_{i=1}^r\lambda_i\sum_{k,\ell\in[d]^2}|\Phi_k\rangle\langle\Phi_\ell|_{\mathsf{X}(1)\mathsf{Y}(1)}\otimes(\overline{P_k}\otimes\mathbb{1})|u_i^{(1)}\rangle\langle u_i^{(1)}|(\overline{P_\ell}\otimes\mathbb{1})^\dagger\otimes\otimes_{p=2}^{n-1}|\Phi\rangle\langle\Phi|_{\mathsf{Y}(p)\mathsf{Z}(p+1)},\)

where \(|u_i^{(1)}\rangle:=|u_i^{(1)}\rangle_{\mathsf{Z}(2)\mathsf{X}(2)\mathsf{X}(3)\dots\mathsf{X}(n-1)\mathsf{E}}\) is obtained from |_u<sub>i</sub>_〉 by relabelling X(1) to Z(2), the unitary <o>_P_</o><sub>k</sub> acts on Z(2), and the identity on \(\mathsf{X}(2)\mathsf{X}(3)\cdots\mathsf{X}(n-1)\mathsf{E}\).

P
X(1)X(2)X(3)E
E
X(1)
X(2)
X(3)
Φ
Φ
Y(1)
Z(2)
Y(2)
Z(3)
Y(3)
Z(4)
k1
k2
k3
P
P k1
P k2
P k3
O
Z(2)Z(3)Z(4)E

**Figure 3.** Parallel teleportation for a chain of _n_=4 nodes. The input state \(\rho_{\mathsf{X}(1)\mathsf{X}(2)\mathsf{X}(3)\mathsf{E}}\) is equal to the output state \(\sigma_{\mathsf{Z}(2)\mathsf{Z}(3)\mathsf{Z}(4)\mathsf{E}}\) up to a relabelling of the registers.


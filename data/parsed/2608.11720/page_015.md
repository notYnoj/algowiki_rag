<tbc>To conclude, it remains to argue about matrices of A having the claimed block form. It suffices to prove it for matrices \(M\in S\) since products of matrices of this form remain of such form. Given the definition of _M_, there exists matrices \(A\in V\) and \(B\in\mathrm{Mat}_d(\mathbb{C})\) for which \(M=(A\otimes B)P\). For a vector \(|x\rangle\otimes|y\rangle\in\mathbb{C}^d\otimes\mathbb{C}^d\), we have \(M(|x\rangle\otimes|y\rangle)=A|y\rangle\otimes B|x\rangle\in\mathrm{im}(A)\otimes\mathbb{C}^d\subseteq U\otimes(W\oplus W^\perp)\). This implies that the last two rows of the block matrix of _M_ are zeros. On the other hand, _A|y_〉=0 when \(|y\rangle\in W^\perp\), so \(M(|x\rangle\otimes|y\rangle)=0\) when \(|x\rangle\otimes|y\rangle\in\mathbb{C}^d\otimes W^\perp=(U\oplus U^\perp)\otimes W^\perp\), which implies that the second and fourth column of the block matrix of _M_ are only zeros. This concludes the proof of Lemma 5.2.

## 6. Round Reduction (Theorem 3)

In this section, we prove our second main technical contribution.

**Theorem 3.** _Let_ \(r\in\mathbb{N}\) _and_ \(n\ge 4\) _and_ \(T\unknown\lfloor\frac{n-r}{2}\rfloor\)_. Suppose there is a T-round quantum- PN algorithm_ \(\mathscr{A}=(U_0,U_1,\dots,U_T,\Pi)\) _of local dimension_ \(d\in\mathbb{N}\) _with outputs in_ \(\Sigma\) _and no monochromatic r-block in its support. Then there exists a 1-round algorithm_ B _with outputs in_ \([d]^{4T}\times\Sigma\) _and no monochromatic_ (2_T+r)-block in its support._

The mechanism behind algorithm B is that each vertex locally instantiates _T_ maximally entangled states with local dimension _d_ for each of its two neighbors, and uses the unique communication round to send the halves of each of those entangled states to the respective neighbor. Each pair of neighbouring vertices thus shares 2_T_ maximally entangled states. Using these states, nodes can attempt to simulate the original _T_-round algorithm A through wishful teleportation (see Figure 2). At the end of B, each vertex outputs the outcome of the attempted simulation of A together with all generated keys used for wishful teleportation.

### 6.1. Background on Teleportation.

Suppose we have a state \(|\psi\rangle_\mathsf{EX}\), where E is an environment register and X is a register held by some node. We wish to turn this state into \(|\psi\rangle_\mathsf{EZ}\) where Z is held by a different node but without using quantum communication. This can be achieved with quantum teleportation \[BBCJPW93\]. Fix the standard maximally entangled vector \(|\Phi\rangle=d^{-1/2}\sum_{i=1}^d|ii\rangle\) in \(\mathbb{C}^d\otimes\mathbb{C}^d\). Let \(\{P_k:k\in[d^2]\}\) be an orthonormal unitary basis and \(|\Phi_k\rangle=(\mathbb{1}\otimes P_k^\top)|\Phi\rangle\) the associated maximally entangled basis. With these conventions, the teleportation identity is

(7) \(|\psi\rangle_\mathsf{EX}\otimes|\Phi\rangle_\mathsf{YZ}=\frac{1}{d}\sum_{k\in[d^2]}|\Phi_k\rangle_\mathsf{XY}\otimes(\mathbb{1}_\mathsf{E}\otimes P_k^\dagger)|\psi\rangle_\mathsf{EZ}.\)

Suppose registers XY are measured in the maximally entangled basis, yielding an outcome \(k\in[d^2]\). Then, by applying the correction _P<sub>k</sub>_ on register Z, we recover the state \(|\psi\rangle_\mathsf{EZ}\), provided _k_ is known to the party holding Z. The explicit environment will be important in our proof, and we emphasize that when the state is teleported, correlations between X and E are preserved between Z and E. This is detailed further in Section A.1.

Now consider the case of a chain of vertices, each holding local registers X(_p_), Y(_p_), Z(_p_) for \(p\in[n]\). Assume each pair of registers Y(_p_) and Z(_p_+1) hold a \(|\Phi\rangle\) state, and that the vertices simultaneously teleport the state in their registers X(_p_) to registers Z(_p_+1), for \(p\in[n-1]\). The next lemma states that the overall effect is a relabelling of the X(1)_..._X(_n_-1) registers to Z(2)_..._Z(_n_). See Section A.2 for a proof.

**Lemma 6.1.** _Consider_ \(n\ge 2\) _vertices in a chain, with each vertex_ \(p\in[n]\) _holding three d- dimensional registers_ X(_p_), Y(_p),_ Z(_p). For each_ \(p\in[n-1]\)_, the registers_ Y(_p_) _and_ Z(_p_+1) _share a maximally entangled state_ \(|\Phi\rangle_{\mathsf{Y}(p)\mathsf{Z}(p+1)}\).


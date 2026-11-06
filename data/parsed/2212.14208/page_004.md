<tbc>_H_<sup>-1</sup>_S)x=b in the sense that it produces the same iterates if we have the same initial guess. Freund’s MR with the H-inner product for iI+H_<sup>-1</sup>_B is, in the same sense, identical to Rapoport’s method for I+H_<sup>-1</sup>_S._

There such equivalent to Freund’s ME seems to have been published so far.

**3.1. Right preconditioning.** Right preconditioning of _H+S_ with _H_<sup>-1</sup> gives rise to the system<tbc>

\((I+SH^{-1})\hat{x}=b,x=H^{-1}\hat{x}.\)

<tbc>As with left preconditioning, there is a direct and simple correspondence with the "Hermitian" formulation on which we will focus in what follows, i.e.

\((i\sigma I+BH^{-1})\hat{x}=ib,\text{with}B=iS\text{hermitian and}\sigma\in\mathbb{R}.\)

Herein, _W=BH_<sup>-1</sup> is _H_<sup>-1</sup>-selfadjoint, and we again obtain short recurrence methods GAL, MR, ME by using the _H_<sup>-1</sup> inner product in the methods and algorithms of \[5\].

Proposition 3.2. _There exist short recurrence GAL, MR and ME methods for the right preconditioned system i_\(\sigma I+BH^{-1}\)_. These give rise to short recurrence methods for i_\(\sigma H+B\) _when using the H_<sup>-1</sup> _inner product._

Although it might not be obvious at first sight, the implementation of right preconditioning can be done by investing one multiplication with _B_, one with _H_ and just one solve with _H_ per iteration. The idea is to carry an additional vector \(\tilde{v}\) which stores _H_<sup>-1</sup>_v_ for the current Lanczos vector _v_. Details are given in Algorithm 3.1 in which, when solving the linear system (3.1), we take the initial vector _w_ as the initial residual \(ib-(i\sigma H+B)x_0\). We note that an implementation with similar cost is possible for left preconditioning. Also note that in the algorithm we have

\(\langle w,\widetilde{v}_{k-1}\rangle=\langle(i\sigma I+BH^{-1})v_k,H^{-1}v_{k-1}\rangle\)<br>
\(=\langle H^{-1}v_k,(-i\sigma I+BH^{-1})v_{k-1}\rangle\)<br>
\(=\langle H^{-1}v_k,(i\sigma I+BH^{-1})v_{k-1}\rangle\text{(since}\langle v_k,v_{k-1}\rangle_{H^{-1}}=0\text{)}\)<br>
\(=\langle H^{-1}v_k,\beta_{k-1}v_k-\alpha_{k-1}v_{k-1}-\beta_{k-2}v_{k-2}\rangle\)<br>
\(=\beta_{k-1},\)

which is why we can use \(\beta_{k-1}\) in the _H_<sup>-1</sup>-orthogonalization of _w_ against _v_<sub>_k_-1</sub> in line 6.

**Algorithm 3.1** _m_ steps of Lanczos for \(i\sigma I+BH^{-1}\) with the _H_<sup>-1</sup> inner product. \(\langle\cdot,\cdot\rangle\) denotes the standard inner product

1: choose initial vector _w_, compute \(\widetilde{w}=H^{-1}w,\beta_0=\langle w,\widetilde{w}\rangle\)<br>
2: put \(v_1=w/\beta_0,\widetilde{v}_1=\widetilde{w}/\beta_0,v_0=0\)<br>
3: for k=1,...,m do<br>
   \(w=i\sigma v_k+B\widetilde{v}_k\) {we have \(\widetilde{v}_k=H^{-1}v_k\) from the previous iteration}<br>
   \(\alpha_k=\langle w,\widetilde{v}_k\rangle\)<br>
   \(w=w-\alpha_kv_k-\beta_{k-1}v_{k-1}\)<br>
   \(\widetilde{w}=H^{-1}w\)<br>
   \(\beta_k=\langle w,\widetilde{w}\rangle^{1/2}\)<br>
   \(v_{k+1}=w/\beta_k\)<br>
   \(\widetilde{v}_{k+1}=\widetilde{w}/\beta_k\) {now \(\widetilde{v}_{k+1}=H^{-1}v_{k+1}\)}<br>
end for


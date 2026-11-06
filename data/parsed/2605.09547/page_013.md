## Lewis weights \(\overline{\tau^t}\in\mathbb{R}^m\)

In Section 3.1 we established that in each iteration of the interior point method, the Lewis-weights are computed via \(\widetilde{O}(1)\) repetitions of

\(w_e^{(j)}\leftarrow((w_e^{(j-1)})^{2/p-1}(\sigma((\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{M})_e+\frac{n}{m}))^{p/2}.\) (10)

where \(\mathbf{M}=\Phi''(x^t)\mathbf{A}\). We start with _w_<sup>0</sup>=1-vector, and assign \(\overline{\tau^t}=w^{(k)}\) for some \(k=\widetilde{O}(1)\). For each _t_, all _w_<sup>(0)</sup>_,...,w_<sup>(_k_)</sup> are stored, so that we can compute \(w_e^{(j)}\) recursively from \(w_e^{(j-1)}\) whenever an edge _e_ is received.

Here the main issue is calculating the \(\widetilde{O}(n)\) space representation of \(\sigma((\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{M})\in\mathbb{R}^m\). We discussed in Section 3.1 that this value can be represented via a Johnson-Lindenstrauss matrix **S**<sup>(_j_)</sup> and by computing

\(\mathbf{S}^{(j)}(\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{M}(\mathbf{M}^\top(\mathbf{W}^{(j-1)})^{1-2/p}\mathbf{M})^{-1}.\) (11)

Since an approximation suffices, we can replace \(\mathbf{M}^\top(\mathbf{W}^{(j-1)})^{1-2/p}\mathbf{M}\) by a spectral approximation, computed in one pass via Lemma 2.1 (for any given edge _e_, we have access to the corresponding row of \(\mathbf{M}=\Phi''(x^t)\mathbf{A}\) because we have access to \(x_e^t\).)

Once we have the spectral sparsifier, we can compute (11) from left to right via one additional pass over the input. This is explained in more detail in Section 4.3.

## Constructing \(y^t,\delta_y^t,\delta_c^t\)

These vectors are _n_-dimensional and can thus be computed/stored explicitly. We have by (9) that

\(\mathbf{H}^t\approx_{1/O(logm)}(\mathbf{A}^\top(\overline{\mathbf{T}^t})^{-1}\Phi''(x^{t-1})^{-1}\mathbf{A})\) (12)

\(\delta_y^t=(\mathbf{H}^t)^{-1}\mathbf{A}^\top\Phi''(x^{t-1})^{-1/2}g^t\)<br>
\(\delta_c^t=(\mathbf{H}^t)^{-1}(\mathbf{A}^\top x^{t-1}-b)\)<br>
\(y^t=y^{t-1}+\delta_y^t\)

Note that when receiving edge _e_ on the stream, we can query \(x_e^{t-1}\) (and thus \(\Phi''(x^{t-1})_e\)) and \(\overline{\tau_e^t}\) via previous paragraph. Thus **H**_<sup>t</sup>_ can be constructed in one pass over the input, by constructing spectral sparsifier via Lemma 2.1. This takes \(\widetilde{O}(n)\) space. We can then compute \(\delta_y^t,\delta_c^t\) from right to left in one additional pass over the input.

## Constructing gradient \(g^t\in\mathbb{R}^m\)

We are left with discussing how to construct vector _g<sup>t</sup>_ from (9), which can be seen as some gradient. We uses a potential function of the form \(\Phi(v^t):=\sum_{e\in[m]}cosh(\lambda(v_e^t))\) for some fixed \(\lambda=O(logm)\) and vector \(v^t\in\mathbb{R}^m\) where

\(v_e^t:=\frac{s_e^t+\mu^t\overline{\tau_e^t}\phi'_e(x_e^t)}{\mu^t\overline{\tau_e^t}\sqrt{\phi''_e(x_e^t)}}\)

for each \(e\in[m]\). Here the gradient is \(\nabla\Phi(v):=-\sum_{e\in[m]}\lambda sinh(\lambda(v_e^t))\). Observe that to obtain \((\nabla\Phi(v^t))_e\) for any \(e\in[m]\), we only need to compute \(v_e^t\). Further, \[BLL<sup>+</sup>21\] proves that one does not need to compute the exact gradient \(\nabla\Phi(v^t)\). Instead, it suffices to compute \(\nabla\Phi(\widetilde{v}^t)\) where \(\widetilde{v}_e^t\) is the appropriate vector in terms of \(\widetilde{x}^t,\widetilde{s}^t,\widetilde{\tau}^t\), which are each element-wise \((1\pm\epsilon)\) multiplicative approximations of \(x^t,s^t,\tau(x^t)\) respectively for some \(\epsilon=O(1/logm)\).

To obtain _g<sup>t</sup>_ from \(\nabla\Phi(\widetilde{v}^t)\), \[BLL<sup>+</sup>21\] defines

\(g^t=\nabla\Psi(\widetilde{v})^{\mathsf{b}(\widetilde{\tau})}:=argmax_{\|h\|_{\widetilde{\tau}+\infty}=1}h^\top\nabla\sum_{e=1}^mcosh(\lambda\widetilde{v}_e).\) (13)

The maximization problem in (13) can be efficiently solved when rounding each entry of \(\widetilde{v}^t\) and \(\widetilde{\tau}^t\) to a multiple of some small \(\delta=O(\epsilon)\). The additional approximation error from this rounding process can be charged to the approximation \(\widetilde{\tau}^t\approx\tau^t\), \(\widetilde{v}^t\approx v^t\). Since the gradient is bounded, this discretization essentially reduces the optimization problem onto some smaller polylog-dimensional space, because we obtain at most some polylog distinct multiples of some \(\epsilon=1/O(logn)\).


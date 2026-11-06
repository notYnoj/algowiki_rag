# The Power Watershed as a Differentiable Layer

19

the measure is uniform over them, and that uniform average is what the plateau solve of the PW algorithm computes.

With _K_ labels the same theorem, applied with the _K_+1 label nodes as the deleted set, gives \(x_i^k\) as the probability that _i_ lies in the tree of label _k_ when a (_K_+1)-forest, each tree containing exactly one label node, is drawn with probability proportional to its weight. Since every pixel lies in exactly one tree, the \(x_i^k\) sum to one, which is the combinatorial form of Appendix B.3.

### B.2 The adjoint gradient

Take \(E(x,w)=\sum_{e=\{u,v\}}w_e(x_u-x_v)^2+\sum_ia_i^1(x_i-1)^2+\sum_ia_i^0x_i^2\). Stationarity gives _Ax=a_<sup>1</sup> with _A=L(w_)+diag(_a_<sup>0</sup>+_a_<sup>1</sup>). Differentiating with respect to one parameter \(\theta\), \(A\partial x/\partial\theta=\partial a^1/\partial\theta-(\partial A/\partial\theta)x\), so for a loss \(\ell(x)\) and \(\lambda=A^{-1}\partial\ell/\partial x\) (using the symmetry of _A_), \(\partial\ell/\partial\theta=\lambda^\top(\partial a^1/\partial\theta-(\partial A/\partial\theta)x)\). For \(\theta=w_e\), \(\partial A/\partial w_e\) is the elementary edge Laplacian, whose product with _x_ has entries _x<sub>u</sub>-x<sub>v</sub>_ at _u_ and _x<sub>v</sub>-x<sub>u</sub>_ at _v_, giving \(\partial\ell/\partial w_e=-(x_u-x_v)(\lambda_u-\lambda_v)\). For \(\theta=a_i^1\), \(\partial a^1/\partial a_i^1=e_i\) and \((\partial A/\partial a_i^1)x=x_ie_i\), giving \(\lambda_i(1-x_i)\); for \(\theta=a_i^0\) only the second term survives, giving \(-\lambda_ix_i\). The chain rule through _w<sub>e</sub>=e_<sup>-_pc<sub>e</sub>_</sup> contributes -_pw<sub>e</sub>_, whose growth in _p_ is the algebraic counterpart of the conditioning blow-up.

### B.3 Multi-label solutions sum to one

With _K_ labels, \(A_K=L(w)+\mathrm{diag}(\sum_ka^k)\) and _A<sub>K</sub>x<sup>k</sup>=a<sup>k</sup>_. Summing over _k_, \(A_K\sum_kx^k=\sum_ka^k=A_K\mathbf{1}\) since _L_**1**=0; _A<sub>K</sub>_ is positive definite, hence \(\sum_kx^k=\mathbf{1}\).

### B.4 The exact limit with _K_ labels

The plateau algorithm of Couprie et al. processes the edges by decreasing weight and merges the nodes of a plateau unless the plateau connects nodes with two or more distinct known labels, in which case the _q_=2 energy is minimised on the plateau with the known nodes as boundary. For two labels the boundary values are scalars; for _K_ labels we solve one system per label with one-hot boundary values and assign the argmax, which is the limit of the multi-label RW on the plateau. Singleton plateaus (continuous costs) are processed by a scalar union- find; plateaus of at most 64 edges by a pure-Python union-find; larger plateaus by the vectorised path.

### B.5 Fixed-point reweighting

The following variant of the WS layer is studied in the experimental record below (sections on reweighting) but is not used in the instance pipeline of the main text.


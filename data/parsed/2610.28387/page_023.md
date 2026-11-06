_For tie-free observations and fixed moment dimension, the full covariance matrix of the sample means, the second and third L-comoments, and the marginal second L-moments can be computed in O(n_<sup>2</sup>) _arithmetic and O(n_<sup>2</sup>) _memory using bivariate rank-prefix sums. The calculation is algebraically identical to_ (4.13)_; the result is therefore not guaranteed to be PSD either._

_Proof._ Let \(\widetilde{D}_{ms,n}^{ab}\) denote (4.12) with centered kernels. Over all ordered pairs of disjoint index sets, each _J_ appears equally often, so the average of \(H_s^b(Z_J)\) is \(U_{n,s}^b\), and similarly for \(H_m^a(Z_I)\). Hence \(\widetilde{D}_{ms,n}^{ab}=D_{ms,n}^{ab}-U_{n,m}^aU_{n,s}^b\), that is, \(\widehat{C}_{ms,n}^{ab}=-\widetilde{D}_{ms,n}^{ab}\). Applying \(\mathbf{1}\{I\cap J=\varnothing\}=\sum_{K\subseteq I\cap J}(-1)^{|K|}\) to the centered disjoint-subset sum yields (5.2); the \(K=\varnothing\) term is \((\sum_I\widetilde{H}_m^a)(\sum_J\widetilde{H}_s^b)=0\). The specialized _O(n_<sup>2</sup>) evaluation is established in Appendix C, and Section 6.4 confirms the quadratic scaling numerically.

The projection estimator of Theorem 4.4 is cheaper still, because its empirical first projections are leave-one-out differences of the sample L-comoments.

**Proposition 5.2** (Leave-one-out representation)**.** _For a kernel of order m, let_ \(U_{n-1}^{a,(-i)}\) _denote the corresponding U-statistic computed from the sample without observation i. Then_

\(\widehat{M}_{m,1}^a(Z_i)=\frac{\genfrac(){pt}{2}{n}{m}U_{n,m}^a-\genfrac(){pt}{2}{n-1}{m}U_{n-1}^{a,(-i)}}{\genfrac(){pt}{2}{n-1}{m-1}},i=1,\dots,n.\) (5.3)

_Moreover, for m_=2,3,4_, write_ \(P_{m-1}(u)=\sum_{k=0}^{m-1}p_{m-1,k}^*u^k\) _as in_ (2.2)_, and define, for a sample of size N,_

\(w_{m,q}^{(N)}=\frac{1}{N}\sum_{k=0}^{m-1}p_{m-1,k}^*\frac{\genfrac(){pt}{2}{q-1}{k}}{\genfrac(){pt}{2}{N-1}{k}},q=1,\dots,N.\) (5.4)

_Let v<sub>q</sub>=X_<sub>\[_q:n_\]</sub>_, q_=1_,...,n, be the concomitants in the order of the Y values, so that_ \(\widehat{\lambda}_m^{[XY]}=\sum_{q=1}^nw_{m,q}^{(n)}v_q\)_; for m_=2,3 _the weights_ \(w_{m,q}^{(n)}\) _are those in_ (2.8)_. Define the prefix and suffix sums_

\(A_k=\sum_{q=1}^kw_{m,q}^{(n-1)}v_q,S_k=\sum_{q=k}^nw_{m,q-1}^{(n-1)}v_q,\) (5.5)

_with A_<sub>0</sub>=_S_<sub>_n_+1</sub>=0_. If observation i has rank r among the Y values, then_

\(U_{n-1}^{[XY],(-i)}=A_{r-1}+S_{r+1}.\) (5.6)

_The same formulas hold for the_ \[_YX_\] _direction with X and Y exchanged, and for the marginal sample L-moments with v<sub>q</sub> replaced by the order statistics X_<sub>_q:n_</sub> _or Y_<sub>_q:n_</sub>_. Consequently, for tie-free observations, all n leave-one-out statistics, the empirical first projections_ (4.10)_, and_ \(\widehat{\Omega}_n\) _are computed in O(n_log_n_) _time for fixed moment dimension._

_Proof. Step 1._ The subsets of size _m_ that contain _i_ are exactly the subsets of the full sample that are not subsets of the sample without _i_. Hence \(\sum_{I\unknown i,|I|=m}\mathbf{H}_m(Z_I)=\genfrac(){pt}{2}{n}{m}U_{n,m}-\genfrac(){pt}{2}{n-1}{m}U_{n-1}^{(-i)}\).<tbc>


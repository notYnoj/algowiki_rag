which is linear in each variable and of total degree at most two, not quadratic in each variable. Squaring a kernel of a single direction instead produces \(X_k^2\) or \(Y_k^2\).

Construct two-dimensional prefix tables on the joint rank grid for<tbc>

\(1,X,Y,X^2,Y^2,XY.\) (C.2)

<tbc>Each open rectangle contributes its count, first moments, and quadratic moments through four prefix-table lookups. The rectangle boundaries use the ranks of _i_ and _j_, so both anchor observations are omitted from all nine rectangles. Empty intervals and rectangles contribute zero. Consequently, for each fixed pair, the vector and matrix

\(F_{ij}=\sum_{k\neq i,j}\mathbf{H}_3(Z_i,Z_j,Z_k),G_{ij}=\sum_{k\neq i,j}\mathbf{H}_3(Z_i,Z_j,Z_k)\mathbf{H}_3(Z_i,Z_j,Z_k)^\top\) (C.3)

can be computed in constant time after prefix-table construction. Only one-dimensional prefix sums are needed for _F<sub>ij</sub>_; the joint rank rectangles are needed for the off-diagonal, cross-direction entries of _G<sub>ij</sub>_. Its same-direction diagonal entries can also be calculated from one-dimensional prefix sums of squared coordinates.

The resulting singleton and total third-order incidence sums are

\(\sum_{I\unknown i,|I|=3}\mathbf{H}_3(Z_I)=\frac{1}{2}\sum_{j\neq i}F_{ij},\sum_{|I|=3}\mathbf{H}_3(Z_I)=\frac{1}{3}\sum_{i<j}F_{ij},\sum_{|I|=3}\mathbf{H}_3(Z_I)\mathbf{H}_3(Z_I)^\top=\frac{1}{3}\sum_{i<j}G_{ij}.\) (C.4)

For the pair-level cross products in (5.2), use \(\mathcal{I}_{a,\{i,j\}}=H_2^a(Z_i,Z_j)\) for an order-two component and \(\mathcal{I}_{a,\{i,j\}}=F_{ij}^a\) for an order-three component. In particular, the _c_=2 contribution to the (3,3) block is obtained from the centered pair-incidence vectors built from _F<sub>ij</sub>_ alone. The _c_=3 contribution uses the centered triple-kernel outer products, whose uncentered sum is the last expression in (C.4) and is computed from _G<sub>ij</sub>_.

The centered incidence products are formed by subtracting the appropriate multiples of _U<sub>a</sub>_. Thus each of the three overlap levels, and every entry of the fixed-dimensional covariance matrix, is obtained with _O(n_<sup>2</sup>) work after constructing _O(n_<sup>2</sup>) prefix storage. The associated R implementation supplied with this article also includes marginal second L-moments so that Corollary E.1 is directly computable. Ties require an ordering convention or a separate treatment and are excluded from this complexity statement.

## D Proof of Theorem 4.4

Each summand in (4.11) is an outer product, so \(\widehat{\Omega}_n\) is positive semidefinite. A fixed subset of _m_ observations contributes to the sum of \(\widehat{M}_{m,1}(Z_i)\) exactly _m_ times; therefore<tbc>

\(\frac{1}{n}\sum_{i=1}^n\widehat{M}_{m,1}(Z_i)=\widehat{\unknown}_m,\sum_{i=1}^n\widehat{\unknown}_i=0.\)


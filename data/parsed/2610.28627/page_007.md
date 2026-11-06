All vector spaces and linear maps are over Q unless a formal parameter is displayed. A polynomial has _length a_ in a variable if its degree in that variable is less than _a_; for several variables, the bounds apply separately. We identify a polynomial with its coefficient list, write \([\mathbf{z}^\unknown]A\) for a coefficient, and set coefficients outside the specified bounds to zero. Input _coefficient sizes_ \(p\times q,q\times r\) mean that each coefficient of _A_ is a \(p\times q\) matrix and each coefficient of _B_ is a \(q\times r\) matrix.

For lists, a linear map has the form \(E(U)_k=\sum_ie_{ki}U_i\); we use _E(U_) and _EU_ interchangeably. The bilinear maps used for polynomial products have the form

\(F(A,B)_k=\sum_{i,j}f_{ijk}A_iB_j,f_{ijk}\in\mathbb{Q}.\) (1)

The same formula defines the map on scalars and on compatible matrix coefficients. In particular, it commutes with concatenating or splitting column blocks of _B_. The numbers _f<sub>ijk</sub>_ are its coefficient array. Each map includes its input spaces and output space in its specification.

We write \[_m_\]={1_,...,m_}, use natural logarithms, and allow constants in \(O_c(\cdot)\) to depend on _c_. An explicit construction is a finite algorithm producing its parameters and rational linear maps.

## 2.1 Packing and composition

A packing computes prescribed target maps using linear encodings, a list of source maps, and linear decoding. Keeping the two input encodings separate will allow transposition and substitution of matrix blocks.

**Definition 2.1** (Packing)**.** Let _T_ and \(S_1,\dots,S_\alpha\) be bilinear maps on specified finite-dimensional spaces. A _packing_ of _T_ using these sources consists of linear encoders _E<sub>j</sub>,H<sub>j</sub>_ into the input spaces of _S<sub>j</sub>_ and linear decoders _D<sub>j</sub>_ from the output space of _S<sub>j</sub>_ to that of _T_, satisfying

\(\sum_{j=1}^\alpha D_j(S_j(E_j(X),H_j(Y)))=T(X,Y)\) (2)

for all inputs (_X,Y_) of _T_. It is _same-left_ if every _E<sub>j</sub>_ is the identity. A packing _modulo_ \(\varepsilon\) allows coefficients in \(\mathbb{Q}[\varepsilon,\varepsilon^{-1}]\) in the linear maps and replaces (2) by \(Z_\varepsilon=T+\varepsilon R_\varepsilon\), where \(Z_\varepsilon\) is the decoded map and \(R_\varepsilon\) is bilinear with coefficients in \(\mathbb{Q}[\varepsilon]\).

We write \(D(W_1,\dots,W_\alpha)=\sum_{j=1}^\alpha D_j(W_j)\) for the combined decoder. For a list of independent targets, take _T_(**A**,**B**)=(_T<sub>i</sub>(A<sub>i</sub>,B<sub>i</sub>_))_<sub>i</sub>_; for a same-left list, take _T(A,_**B**)=(_T<sub>i</sub>(A,B<sub>i</sub>_))_<sub>i</sub>_. If all sources equal _S_, we say that the packing uses \(\alpha\) copies of _S_. Packings of polynomial products or their coefficient windows are _polynomial packings_ (PP); SL-PP denotes the same-left case. The parameter \(\varepsilon\) is distinct from the polynomial variables.

We recall two standard closure properties of bilinear algorithms: composition and combination on separate indices; see \[BCS97, Chapters 14-15\]. We give proofs in our notation for completeness.

When replacing a source computation by a packing, we use a sufficiently high power of \(\varepsilon\) in the replacement to preserve correctness modulo \(\varepsilon\).

**Lemma 2.2** (Composition)**.** _Suppose T has a packing modulo_ \(\varepsilon\) _using_ \(S_1,\dots,S_\alpha\)_, and each S<sub>j</sub> has a packing modulo_ \(\varepsilon\) _using_ \(R_{j,1},\dots,R_{j,\beta_j}\)_. For a computable positive integer K, replacing each source S<sub>j</sub> by its packing with_ \(\varepsilon\) _replaced by_ \(\varepsilon^K\) _gives a packing of T modulo_ \(\varepsilon\) _using_ (_R<sub>j,k</sub>)<sub>j,k</sub>._


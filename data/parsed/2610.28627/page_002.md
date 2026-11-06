## 1 Introduction

The exponent \(\omega\) of matrix multiplication is the infimum of all \(\tau\) such that two \(n\times n\) matrices can be multiplied with \(O(n^\tau)\) arithmetic operations. Strassen \[Str69\] showed \(\omega\le log_27<2.81\). Later bounds follow a scheme developed by Bini, Capovani, Romani, and Lotti \[BCRL79, Bin80\], Schönhage \[Sch81\], and Strassen \[Str87\]. An explicit identity computes several products together, possibly with an error that vanishes with a parameter. Combining identifies amplifies the saving, and the resulting independent products give a bound on \(\omega\). Refinements of Strassen’s laser method, starting from the identity of Coppersmith and Winograd \[CW90\], reached \(\omega<2.371339\) \[ADV<sup>+</sup>25\] and \(\omega<2.371177\) \[DEK<sup>+</sup>26\].

OpenAI recently claimed \(\omega\le 9/4\) \[Ope26a\], following a companion bound \(\omega<2.258\) \[Ope26b\], starting from identities for polynomial multiplication. Their theorem is stated for _exact arithmetic_ over the complex numbers, charging unit cost per scalar operation. Their proof uses Strassen’s asymptotic spectrum \[Str88\], an algebraic and topological framework for comparing bilinear maps through numerical invariants. Concavity strengthens inequalities for these invariants; spectral duality then converts them into the exponent bound. Their argument establishes the exponent bound without explicitly constructing the corresponding algorithms.

We give an explicit, constructive algorithm reaching the same bound using integer arithmetic throughout; furthermore, our construction is self-contained. Our starting point is the three-for-one polynomial degeneration of \[Ope26a, Lemma 4.2\]. We generalize it to a (_c_+2)-for-_c_ polynomial packing and nexy use our (_c_+2)-for-_c_ gadget, together with tensoring, to construct a Strassen-style identity: a fixed \(v\times v\) block matrix product can be computed using _r_ products of linear combinations of its blocks, with log_<sub>v</sub>r_ arbitrarily close to 9/4. This replaces the usual _v_<sup>3</sup> block products by _r_, just as Strassen replaces eight by seven. Applying the fixed identity recursively then gives the exponent bound.

**Theorem 1.1.** _For every_ \(\gamma>0\)_, there is an explicit recursive algorithm that, for every positive integer n, multiplies two_ \(n\times n\) _integer matrices with_ \(O(n^{9/4+\gamma})\) _integer arithmetic operations. In particular,_ \(\omega\le 9/4\).

The algorithm remains "galactic": the constants hidden in the \(O(\cdot)\) notation are enormous.

### 1.1 Our techniques

We first introduce the notion of a _polynomial packing_ (PP): a procedure that recovers a collection of polynomial-product coefficients through linear encodings, source polynomial products, and linear decoding. Its efficiency depends on both the number and the dimensions of the source products.

#### Polynomial packing.

We now construct a (_c_+2)-for-_c_ packing modulo \(\varepsilon\), generalizing the three-for-one construction of \[Ope26a, Lemma 4.2\]. Consider univariate polynomials _A,P_<sub>1</sub>_,...,P_<sub>_c_+1</sub> with matrix coefficients, where _A_ has length _a_ and each _P<sub>i</sub>_ has length _b_. Write \[_z<sup>k</sup>_\]_H_ for the coefficient matrix of _z<sup>k</sup>_ in _H_, taking coefficients outside its range to be zero. We want to compute all coefficients of the _c_+1 products _AP_<sub>1</sub>_,...,AP_<sub>_c_+1</sub>, which we call _full products_. Naively, this takes _c_+1 polynomial multiplications. We can trivially reduce the number of polynomial multiplications to _c_ by replacing _P<sub>c</sub>,P_<sub>_c_+1</sub> with _P<sub>c</sub>+z_<sup>_a+b_-1</sup>_P_<sub>_c_+1</sub>: the two products then occupy disjoint coefficient ranges and can be read off separately. But this encoded input has length _a_+2_b_-1, at least the<tbc>


_Proof._ Choose nonnegative integers _p<sub>E</sub>,p<sub>H</sub>,p<sub>D</sub>_ so that the powers of \(\varepsilon\) in the coefficients of the left encoders, right encoders, and decoders of the packing of _T_ have exponents at least -_p<sub>E</sub>,-p<sub>H</sub>,-p<sub>D</sub>_, respectively. Choose _K=p<sub>E</sub>+p<sub>H</sub>+p<sub>D</sub>_+1. Each replacement has decoded error divisible by \(\varepsilon^K\). Billinearity shows that applying the outer encoders and decoders can lower its exponent by at most _p<sub>E</sub>+p<sub>H</sub>+p<sub>D</sub>_, so every added error remains divisible by \(\varepsilon\). The original decoded map is already congruent to _T_ modulo \(\varepsilon\), and the composite encoders and decoders are linear.

We also combine computations on separate coefficient indices. For maps _F,G_ with coefficient arrays _f,g_, their _tensor product_ is the bilinear map defined by \((F\otimes G)(X,Y)_{k,k^\prime}=\sum_{i,j,i^\prime,j^\prime} f_{ijk}g_{i^\prime j^\prime k^\prime} X_{i,i^\prime} Y_{j,j^\prime}\).

**Lemma 2.3** (Combining separate indices)**.** _If F has a packing using_ \(S_1,\dots,S_\alpha\) _and G has a packing using_ \(R_1,\dots,R_\beta\)_, then_ \(F\otimes G\) _has a packing using_ \((S_j\otimes R_k)_{j,k}\)_, obtained by encoding along the two indices and decoding in reverse order. The conclusion holds also modulo the same parameter_ \(\varepsilon\).

_Proof._ Abbreviating each list of sources, the correctness identities are

\(D(S(E(X),H(Y)))=F(X,Y),D'(R(E'(X),H'(Y)))=G(X,Y).\)

Expand the combined computation and group its sums by the unprimed indices. The primed encoding, computation, and decoding form the second identity; substitute it. Applying the first identity to each remaining term gives coefficient \(f_{ijk}g_{i^\prime j^\prime k^\prime}\). This uses only finite sums and linearity of the encoders and decoders. Modulo \(\varepsilon\), make the same substitutions with the complete decoded maps: their polynomial coefficient arrays multiply, and their constant coefficients are _f_ and _g_.

In particular, combining matrix multiplications of dimensions (_p,q,r_) and \((p',q',r')\) gives dimensions \((pp',qq',rr')\): the row, inner, and column indices are respectively paired. Appendix A gives the other operation we use, exchanging the input and output roles of a packing.

## 2.2 The primal and dual gadgets

Our first packing extends the three-for-one gadget of \[Ope26a, Lemma 4.2\]. It computes _c_+1 full products and one middle product from _c_ full products, allowing _t_ additional coefficients in each source right input. For _t_=1, this adds just one coefficient; larger _t_ permits smaller _c_.

Throughout the polynomial constructions, write _s=a+b_-1 and define

\(\mathrm{Full}_{a,b}(A,B)=AB,\mathrm{Mid}_{a,b}(A,Q)=\big([z^{a-1+j}](AQ)\big)_{j=0}^{b-1},\)

where the lengths of _A,B,Q_ are _a,b,s_, respectively. Full returns _s_ coefficients, and Mid returns the _b_ coefficients at exponents _a_-1_,...,s_-1.

**Lemma 2.4** (Primal packing)**.** _For positive integers a,b,c,t with_ \(ct\ge a+2b-1\)_, there is a same-left packing modulo_ \(\varepsilon\) _of_

\(\big((\mathrm{Full}_{a,b}(A,P_i))_{i=1}^{c+1},\mathrm{Mid}_{a,b}(A,Q)\big)\)

_using c copies of_ Full<sub>_a,b+t_</sub>_. Target and source coefficient sizes are_ \(p\times q,q\times r\) _for arbitrary positive integers p,q,r._

_Proof._ We are given _A_ of length _a_, polynomials _P_<sub>1</sub>_,...,P_<sub>_c_+1</sub> of length _b_, and _Q_ of length _s_. We will encode only the right inputs, multiply the encoded polynomials by the unchanged _A_, and recover the requested coefficients from these products.


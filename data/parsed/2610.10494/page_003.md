Second, Wolstenholme’s inequality bounds weighted sums of these parameters. We apply Strassen’s spectral theorem: the largest character value equals asymptotic tensor rank. We state precisely the form of this theorem we use, then show how the rank bound gives a running-time bound for every fixed matrix shape.

#### Relation to the preceding analysis.

The two polynomial splittings in Lemma 2.1 recap the proofs of Lemmas 4.1 and 4.2 of \[9\] in coefficient coordinates. The finite separation adapts Proposition 3.1 of that reference. All three constructions are proved in the appendices. Multinomial counting then gives the required power-sum inequality. The replication construction, rescaling, and coupling of six affine offsets supply the rectangular extension. The weighted bound uses the classical Wolstenholme inequality \[8\]. Strassen’s spectral theorem is a standard input; a modern exposition is \[12\]. We cite it rather than reproduce its proof. We make no priority claim for the standard tools or the finite construction variants. Section 7 substitutes the bounds into known algorithmic tradeoffs.

## 2. Polynomial products and finite constructions

We begin by describing matrix multiplication and convolution as tensors. We then build ways to split polynomial products and separate computations that share variables. These constructions give the inequalities in Section 3. A further construction replicates a convolution; it will let us compare convolutions at different scales in Section 4.

A tensor is a trilinear form in three groups of variables, called its _legs_. A _restriction_ makes linear substitutions independently on the three legs. A _degeneration_ is a limit of such restrictions: the substitutions may depend on \(\varepsilon\neq 0\), and every resulting coefficient converges as \(\varepsilon\rightarrow 0\). Our constructions first change bases and then multiply variables by integer powers of \(\varepsilon\). The resulting coefficient array is a polynomial in \(\varepsilon\) whose constant coefficient is the desired tensor. We write \(T\ge S\) for a restriction and \(T\unknown S\) for a degeneration. Successive constructions can use a single parameter: replace the earlier parameter by a sufficiently large power of the later one, so every earlier error term still has positive total exponent.

The rank(_T_) is the least number of products of three linear forms, one per leg, summing to _T_. The direct sum \(S\oplus T\) uses disjoint variables on all three legs and represents independent computations. The tensor product \(S\otimes T\) pairs their indices, as in a Kronecker product, and represents their composition on blocks. We write _mT_ for _m_ independent copies, and \(T^{\otimes N}\) for _N_ tensor factors. Thus \(\text{rank}(T)xyz\ge T\). All factors used below restrict to _xyz_ by keeping one nonzero term; this is what it means to drop a factor.

The oriented dot products are<tbc>

\(B_X(q)=x\sum_{j=1}^qy_jz_j,\)

<tbc>with _B<sub>Y</sub>(q),B<sub>Z</sub>(q_) obtained by permuting the legs. They have rank _q_, and \(B_i(q)\otimes B_i(q')\) is \(B_i(qq')\) after reindexing. The matrix multiplication tensor factors as

\(\langle A,B,C\rangle=\sum_{u,v,w}x_{uv}y_{vw}z_{wu}\cong B_Y(A)\otimes B_Z(B)\otimes B_X(C).\) (3)

Thus the three dot-product dimensions specify the matrix shape.

For distinct input legs _i,j_, with remaining output leg _k_, the _convolution tensor_ is<tbc>

\(C_{ij}(r,s)=\sum_{h=0}^{r-1}\sum_{\ell=0}^{s-1}x_h^{(i)}x_\ell^{(j)}x_{h+\ell}^{(k)}.\)


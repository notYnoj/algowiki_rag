_Proof._ Combine _h_ copies of the packing on separate matrix indices, using the same parameter \(\varepsilon\) in every copy. Lemma 2.3 gives a packing modulo \(\varepsilon\) for matrix multiplication of side _V=v<sup>h</sup>_ using _r<sup>h</sup>_ scalar products.

By the definition of a packing modulo \(\varepsilon\), the coefficients of the fully decoded map are polynomials with no negative powers, and their constant terms are the coefficients of matrix multiplication. Each coefficient of the combined decoded map is a product of _h_ such polynomials. Its degree is therefore at most _hD_, and its constant term is the product of their constant terms. Thus the constant term of the combined decoded map is precisely matrix multiplication of side _V_ .

Evaluate the encoders and decoders at _hD_+1 distinct nonzero rational values of \(\varepsilon\), for example 1_,...,hD_+1. The encoding and decoding coefficients are Laurent polynomials, so all these specializations are defined and rational. Polynomial interpolation expresses the constant coefficient of the decoded map as a fixed rational linear combination of its values at these points. Each evaluation uses _r<sup>h</sup>_ scalar products, giving an exact rational identity with at most (_hD_+1)_r<sup>h</sup>_ scalar products.

If \(\tau>\mathrm{log}_vr\), then

\(\frac{(hD+1)r^h}{(v^h)^\tau}=(hD+1)\left(\frac{r}{v^\tau}\right)^h\longrightarrow 0.\)

Choose a finite _h_ for which this ratio is less than one. All steps use finite combinations of the given coefficient maps and rational interpolation, so the resulting identity is computable.


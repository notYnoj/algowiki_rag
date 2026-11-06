## Proof of the filtered-scheme stability extension (Remark 4.2).

When coefficients with strong curvature, such as _A<sub>⋆</sub>_ (which behaves like \(\mathrm{cot}(\pi\phi)\)), are evaluated pointwise on a spectral grid, products of fields can generate spurious high-frequency (aliasing) noise that has no counterpart in the continuous solution. For the long-time runs of Section 7.3, we suppress this noise by applying the 2/3-rule filter _F_ after every step. The filter discards the highest third of the resolved wavenumbers in each direction.

Filtering changes the fields that are stored and used in the next step. Therefore, Theorem 4.1, which was proved for the unfiltered scheme, does not apply directly to the scheme that is actually run. We show here that the identity (12) extends to the filtered scheme, with two additional non-negative terms. Consequently, the scheme that produced the results of Section 7.3 is provably stable.

### Properties of the filter.

In Fourier space, _F_ multiplies each mode by 1 (kept) or 0 (discarded), depending only on the wavenumber. Hence _F_ is diagonal in the Fourier basis, which gives three properties:

• _F_<sup>2</sup>=_F_, since multiplying a mode by 0 or 1 twice is the same as doing so once;<tbc>

• _F_<sup>∗</sup>=_F_, since _F_ is a real diagonal operator in an orthonormal basis;<tbc>

• \(\nabla F=F\nabla\), since \(\nabla\) is also diagonal in the Fourier basis, and diagonal operators commute.

It follows that _F(I-F_)=_F-F_<sup>2</sup>=0, and therefore \(\big(\)_Fu,_ (_I-F)u_\(\big)=\(\big(\)_u, F(I-F)u_\(\big)\)=0 for every field _u_. In particular,<tbc>

\(\|u\|^2=\|Fu\|^2+\|(I-F)u\|^2.\) (26)

<tbc>_Effect of the filter on_ \(\Phi\). Let _v_ be a field with _Fv=v_, and let _u_ be arbitrary. We claim that<tbc>

\(\Phi(u,v)-\Phi(Fu,v)=5\|(I-F)u\|^2.\) (27)

<tbc>The first term of \(\Phi\) is handled by (26): \(\|u\|^2-\|Fu\|^2=\|(I-F)u\|^2\). For the second term, write 2_u-v_=(2_Fu-v_)+2(_I-F)u_. Since _Fv=v_, the field 2_Fu-v_ lies in the range of _F_ and is therefore orthogonal to (_I-F)u_. Hence

\(\|2u-v\|^2=\|2Fu-v\|^2+4\|(I-F)u\|^2.\)

Adding the two differences gives \(\|(I-F)u\|^2+4\|(I-F)u\|^2=5\|(I-F)u\|^2\), which proves (27). Thus, filtering can only decrease \(\Phi\), and the decrease is exactly five times the squared norm of the removed part.

### Application to the scheme.

At each step, the stored previous levels are outputs of the filter, so the hypothesis _Fv=v_ holds for them (by induction over the steps, with filtered initial data). We apply (27) with

• \(u=\nabla\phi^{n+1}\) and \(v=\nabla\phi^n\), where \(\phi^n\) is the stored, already filtered field (note that \(\nabla F=F\nabla\));<tbc>

• _u=q_<sup>_n_+1</sup> and _v=q<sup>n</sup>_;<tbc>

• _u=r_<sup>_n_+1</sup> and _v=r<sup>n</sup>_. Here no filtering is applied to the scalar _r_, so this pair contributes nothing.

Replacing the raw fields \(\phi^{n+1},q^{n+1}\) by their filtered versions \(F\phi^{n+1},Fq^{n+1}\) in E<sup>_n_+1</sup> lowers it by

\(\frac{5\gamma}{4}\|(I-F)\nabla\phi^{n+1}\|^2+\frac{5}{4}\|(I-F)q^{n+1}\|^2\ge 0.\)

Therefore (12) holds for the filtered scheme with these two non-negative terms added on the dissipative side. In particular, Corollary 4.1 remains valid: the modified energy of the stored (filtered) fields does not increase, for every \(\Delta t>0\).


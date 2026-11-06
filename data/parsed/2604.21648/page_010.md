<tbc>One goal of theoretical two-grid analysis is to estimate the convergence speed of the method by bounding the norm of the error propagation matrix. If _A_ is HPD, the convergence is typically measured in the _A_-norm, also known as the energy norm. Here, _A_ is in general nonsymmetric and indefinite and therefore we use an arbitrary _B_-norm. A simple approach to estimate such a _B_-norm is to investigate and bound the smoothing steps and the coarse-grid correction individually. By the consistency of the _B_-norm it holds

\(\|E^{\nu_1,\nu_2}\|_B\le\|I-M^{-1}A\|_B^{\nu_1+\nu_2}\|I-\Pi_A\|_B\)

and for \(\|E_+^{\nu_1,\nu_2}\|_B\) analogously. A two-grid method is called convergent if the norm of the corresponding error operator is less than one, that is \(\|E^{\nu_1,\nu_2}\|_B<1\) or \(\|E_+^{\nu_1,\nu_2}\|_B<1\).

By Lemma 2.4 we already know that \(\|I-\Pi_A\|_B\) attains its minimal value one if and only if \(\Pi_A\) is _B_-orthogonal. Therefore, one of our goals is to find restriction and interpolation operators _R_ and _P_ such that \(\Pi_A(P,R)\) is _B_-orthogonal for some HPD _B_.

Besides the _B_-orthogonality of the coarse-grid correction, we require some additional assumption for the smoothing to obtain convergence results. This condition is given by the usual smoothing assumption but now in the _B_-norm.

Definition 3.4. _We say that the smoothing assumption is satisfied if_

\(\|I-M^{-1}A\|_B<1.\)

We can characterize this property with the following theorem which was introduced and partly proven in \[2\].

Theorem 3.5. _Let_ \(\widetilde{M}^{-1}\) _and_ \(\widetilde{M}^{-1}\) _be defined as in_ (3.7) _and_ (3.8)_, respectively. Then the following statements are equivalent:_

(_1)_ \(\|I-M^{-1}A\|_B<1\).<tbc>

(_2)_ \(\widetilde{M}^{-1}\) _is HPD._<tbc>

(_3)_ \(\sigma(\widetilde{M}^{-1}B)\subseteq(0,1]\).<tbc>

(_4)_ \(\widetilde{M}^{-1}\) _is HPD._<tbc>

_(5)_ \(\sigma(\widetilde{M}^{-1}B)\subseteq(0,1]\).

_Proof._ The proof in \[2\] shows that the first two statements are equivalent.<br>
_(1)_ \(\Rightarrow\) _(3):_ Let \(\|I-M^{-1}A\|_B<1\). Then \(\widetilde{M}^{-1}\) is HPD and so is \(B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2}\). By similarity we get \(\sigma(\widetilde{M}^{-1}B)\subseteq(0,\infty)\). Further, it holds

\(\lambda_{max}(I-B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2})=\lambda_{max}((I-B^\frac{1}{2}M^{-1}AB^{-\frac{1}{2}})^H(I-B^\frac{1}{2}M^{-1}AB^{-\frac{1}{2}}))=\lambda_{max}((I-M^{-1}A)^+(I-M^{-1}A))=\|I-M^{-1}A\|_B^2<1.\) (3.12)

But, due to its structure the matrix \(I-B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2}\) is Hermitian positive semi- definite (HPSD) and thus has real nonnegative eigenvalues. Therefore, it holds \(\sigma(I-B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2})\subseteq[0,\infty)\) and hence \(\sigma(\widetilde{M}^{-1}B)=\sigma(B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2})\subseteq(0,1]\).<br>
_(3)_ \(\Rightarrow\) _(1):_ Let \(\sigma(\widetilde{M}^{-1}B)\subseteq(0,1]\). Then \(\sigma(I-B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2})=\sigma(I-\widetilde{M}^{-1}B)\subseteq[0,1)\). With (3.12) we obtain \(\|I-M^{-1}A\|_B^2=\lambda_{max}(I-B^\frac{1}{2}\widetilde{M}^{-1}B^\frac{1}{2})<1\).<br>
_(1)_ \(\Rightarrow\) _(5):_ The proof is analogous to _(1)_ \(\Rightarrow\) _(3)_ and follows by using

\(\lambda_{max}((I-M^{-1}A)^+(I-M^{-1}A))=\lambda_{max}((I-M^{-1}A)(I-M^{-1}A)^+)\)


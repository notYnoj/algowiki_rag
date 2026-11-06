Since T is real-valued, Part (b) of Lemma 3 follows from Part (c) of Lemma 2.

We now show part (_c_) of Lemma 3. Since VT is symmetric by (1.4) (i.e., VTY<sup>-1</sup>=T_<sup>T</sup>_) and (YTY<sup>-1</sup>)<sup>1/2</sup>=YT<sup>1/2</sup>Y<sup>-1</sup> by \[21, Theorem 1.13 (c)\], we can see that (YTY<sup>-1</sup>)<sup>1/2</sup>=YT<sup>1/2</sup>Y<sup>-1</sup>=(T_<sup>T</sup>_)<sup>1/2</sup>=(T<sup>1/2</sup>)_<sup>T</sup>_, where the last equation follows by \[21, Theorem 1.13 (b)\]. Thus, we readily have shown that YT<sup>1/2</sup>=(T<sup>1/2</sup>)_<sup>T</sup>_Y=(YT<sup>1/2</sup>)_<sup>T</sup>_. Part (_c_) is concluded. \(\square\)

The following proposition indicates that an ideal preconditioner for VT is the HPD matrix (T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup>, which can achieve the optimal two-step convergence when MINRES is used due to the fact that the preconditioned matrix has only two distinct eigenvalues \(\pm 1\).

**Proposition 2.** _Let_ \(\mathcal{T}\in\mathbb{R}^{mn\times mn}\) _be defined by (1.2). Then,_ ((T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup>)<sup>-1</sup>YT _has only_ \(\pm 1\) _as eigenvalues._

**Proof:** By Lemma (3) (a), the preconditioner (T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup> is invertible. By Lemma (3) (c), we have YT<sup>1/2</sup>=(T<sup>1/2</sup>)_<sup>T</sup>_Y which yields YT<sup>-1/2</sup>=(T<sup>-1/2</sup>)_<sup>T</sup>_Y. Then, we consider the following preconditioned matrix

\(((\mathcal{T}^{1/2})^T\mathcal{T}^{1/2})^{-1}\mathcal{YT}=\mathcal{T}^{-1/2}(\mathcal{T}^{-1/2})^T\mathcal{YT}=\mathcal{T}^{-1/2}\mathcal{YT}^{-1/2}\mathcal{T}\)<br>
\(=\mathcal{T}^{-1/2}\mathcal{YT}^{-1/2}\mathcal{T}^{1/2}\mathcal{T}^{1/2}\)<br>
\(=\mathcal{T}^{-1/2}\mathcal{YT}^{1/2}.\)

Thus, we have shown that the preconditioned matrix ((T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup>)<sup>-1</sup>YT is similar to Y which is real-valued, symmetric, and orthogonal. Hence, it has only \(\pm 1\) as eigenvalues. \(\square\)

In other words, Proposition 2 provides a guide on designing an effective preconditioner for VT , since in general (T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup> is computationally expensive to implement.

In what follows, we shall show that our proposed preconditioner \(\mathcal{P}_\alpha\) approximates the ideal preconditioner (T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup> in the sense that their difference is a small norm matrix whose magnitude is controlled by the parameter \(\alpha\). Its preconditioning effect becomes apparent since \(\mathcal{P}_\alpha\) gets close to (T<sup>1/2</sup>)_<sup>T</sup>_T<sup>1/2</sup> as \(\alpha\) approaches zero.

Now, we turn our focus on the following lemmas and proposition, which will be used to show our main result.

For a complex number _z_, denote by \(\Re(z)\) and \(\unknown(z)\), the real part and the imaginary part of _z_, respectively.

Similar to Lemma 3, the following lemma on \(\mathcal{C}_\alpha\) is needed.

**Lemma 4.** _Let_ \(\mathcal{C}_\alpha\in\mathbb{R}^{mn\times mn}\) _be defined by (1.5) with_ \(0<\alpha<1\)_. Then,_

**(a)** \(\mathcal{C}_\alpha^{1/2}\) _is a real-valued matrix;_

**(b)** \(\mathcal{YC}_\alpha^{1/2}\) _is symmetric._


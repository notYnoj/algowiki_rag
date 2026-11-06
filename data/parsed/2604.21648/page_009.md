<tbc>For the second eigenvalue problem we define the following matrices

\(\widetilde{M}^{-1}=M^{-1}AB^{-1}+B^{-1}A^HM^{-H}-B^{-1}A^HM^{-H}BM^{-1}AB^{-1},\) (3.7)

\(\widehat{M}^{-1}=M^{-1}AB^{-1}+B^{-1}A^HM^{-H}-M^{-1}AB^{-1}A^HM^{-H}\) (3.8)

which satisfy

\(\widetilde{M}^{-1}B=M^{-1}A+(M^{-1}A)^+-(M^{-1}A)^+M^{-1}A,\) (3.9)

\(\widehat{M}^{-1}B=M^{-1}A+(M^{-1}A)^+-M^{-1}A(M^{-1}A)^+\) (3.10)

and thus

\(I-\widetilde{M}^{-1}B=(I-M^{-1}A)^+(I-M^{-1}A),\)<br>
\(I-\widehat{M}^{-1}B=(I-M^{-1}A)(I-M^{-1}A)^+.\)

Note that \(\widetilde{M}^{-1}\) and \(\widehat{M}^{-1}\) are Hermitian. Then we consider the second eigenvalue problem

(3.11) \(\widehat{M}^{-1}Bz=\mu z.\)

Upon first sight \(\widehat{M}^{-1}\) and \(\widetilde{M}^{-1}\) look complicated but their structure becomes apparent for _B=A_ HPD. Then

\(\widetilde{M}^{-1}=M^{-1}+M^{-H}-M^{-H}AM^{-1}=M^{-H}(M+M^H-A)M^{-1},\)<br>
\(\widehat{M}^{-1}=M^{-1}+M^{-H}-M^{-H}AM^{-1}=M^{-1}(M+M^H-A)M^{-H}\)

and

\(\widetilde{M}=M(M+M^H-A)^{-1}M^H,\)<br>
\(\widehat{M}=M^H(M+M^H-A)^{-1}M.\)

These matrices appear quite often in the AMG analysis of the HPD case, e.g. as symmetrized smoother, see \[38, 36, 23\]. Moreover, they are used to determine optimal restriction and prolongation operators \[4, 38, 12\].

The matrices \(\widetilde{M}^{-1}B\) and \(\widehat{M}^{-1}B\) have the same structure and differ only in the order of the last term. Their properties are summarized in the following result.

Proposition 3.3. _Let_ \(\widetilde{M}^{-1}\) _and_ \(\widehat{M}^{-1}\) _be defined as in_ (3.7) _and_ (3.8)_. Then_ \(\widetilde{M}^{-1}B\) _and_ \(\widehat{M}^{-1}B\) _are B-orthogonal and have real eigenvalues. If M_<sup>-1</sup>_A is additionally B-normal it holds_ \(\widetilde{M}^{-1}=\widehat{M}^{-1}\) _and_ \(\widetilde{M}^{-1}B=\widehat{M}^{-1}B\).

_Proof._ It is obvious that

\((\widetilde{M}^{-1}B)^+=\widetilde{M}^{-1}B\text{and}(\widehat{M}^{-1}B)^+=\widehat{M}^{-1}B,\)

hence \(\widehat{M}^{-1}B\) and \(\widetilde{M}^{-1}B\) are _B_-orthogonal. Then by Proposition 2.10 their eigenvalues are real. If _M_<sup>-1</sup>_A_ is additionally _B_-normal, it commutes with (_M_<sup>-1</sup>_A_)<sup>+</sup> and we have \(\widetilde{M}^{-1}B=\widehat{M}^{-1}B\) and therefore also \(\widetilde{M}^{-1}=\widehat{M}^{-1}\). □

Clearly, if _M_<sup>-1</sup>_A_ is _B_-orthogonal, it also holds \(\widetilde{M}^{-1}=\widehat{M}^{-1}\), but Proposition 3.3 shows that _B_-normality is already sufficient to obtain this equality.


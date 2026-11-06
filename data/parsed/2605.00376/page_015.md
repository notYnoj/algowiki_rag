and

\(\overline{r_{(i-1)2}}=r_{(i-1)2}+Z(r_{(i-1)1}+r_{(i-2)2}-r_{(i-2)1}-r_{(i-1)2}).\) (4.39)

Finally, substituting (4.36) and (4.37) into \(\mathbf{y}_{i-2}^T\), we have:

\(\mathbf{y}_i^T=C\widehat{r_{i1}}\mathbf{y}_{i-1}^T+C\widehat{r_{i2}}\mathbf{y}_{i-2}^T,\) (4.40)

where

\(\widehat{r_{i1}}=r_{i2}-\overline{r_{(i-1)2}}+Z\big(r_{i1}+r_{(i-2)2}-r_{(i-2)1}-r_{i2}\big)\) (4.41)

and

\(\widehat{r_{i2}}=r_{i1}-r_{(i-2)1}+Z(-r_{(i-2)2}-\overline{r_{(i-1)1}}-\overline{r_{(i-1)2}}+Z(r_{i2}+Z(r_{i1}+r_{(i-2)2}-r_{(i-2)1}-r_{i2})+\overline{r_{(i-1)1}}-\overline{r_{(i-1)2}}-r_{i1}+r_{(i-2)1})).\) (4.42)

By ensuring that Equation (4.40) holds for all _i_=4_,...,m_, it follows that the syndrome expressions are valid, that is, the symbol errors indeed occurred at positions _l_<sub>1</sub>_,l_<sub>2</sub>, and _l_<sub>3</sub>. To determine the magnitudes of the errors, we now solve a linear system with three equations involving the variables \(\mathbf{e}_{l_1}^T\), \(\mathbf{e}_{l_2}^T\), and \(\mathbf{e}_{l_3}^T\).

The analysis of this case highlights the main structural aspects of the problem and illustrates how the proposed approach can be extended to handle additional errors, although this extension leads to a significant increase in the algebraic complexity of the involved expressions.

The expressions (4.41) and (4.42) are highly complex to compute when an arbitrary superregular matrix _A_ is used, due to their dependence on multiple indices. Motivated by Corollary 4.1, we present simplified expressions when _A_ is a Vandermonde matrix.

**Corollary 4.2.** _If A is a Vandermonde matrix, then the simplified forms of (4.41) and (4.42) are_

\(\widehat{r_{i1}}=l_3-Z(l_2-l_3)+Z(2l_2-2l_3)\) (4.43)

_and_

\(\widehat{r_{i2}}=3l_2-l_3-Z(l_2-l_3)+Z\big(l_3-l_2-Z(l_2-l_3)+Z(2l_2-2l_3)\big)\) (4.44)

_for i_=4_,...,m, where l_<sub>2</sub> _and l_<sub>3</sub> _are the second and third error positions._

**Proof.** Let _A_ be a Vandermonde matrix. If _i_-2_,i_-1 and _i_ are three consecutive rows and _l<sub>j</sub>_ and _l<sub>k</sub>_ are any two columns of _A_, then, as in the proof of Corollary 4.1, it is shown that

\(l_k=\sigma(i,l_k)+\sigma(i-1,l_k)+Z\big(\sigma(i,l_j)-\sigma(i,l_k)-\sigma(i-1,l_j)+\sigma(i-1,l_k)\big)+Z\big(\sigma(i-1,l_j)-\sigma(i-1,l_k)-\sigma(i-2,l_j)+\sigma(i-2,l_k)\big).\) (4.45)

And, if _i_-3, _i_-2, _i_-1 and _i_ are four consecutive rows and _l<sub>j</sub>_ and _l<sub>k</sub>_ are any two columns of _A_, then it is shown that

\(2l_k=\sigma(i,l_k)+\sigma(i-2,l_k)+Z(\sigma(i,l_j)-\sigma(i,l_k)-\sigma(i-1,l_j)+\sigma(i-1,l_k))+Z\big(\sigma(i-2,l_j)-\sigma(i-2,l_k)-\sigma(i-3,l_j)+\sigma(i-3,l_k)\big),\) (4.46)

since, in a Vandermonde matrix, the differences \(\sigma(i,l_k)-\sigma(i-1,l_k)\) are constant and equal to _l<sub>k</sub>_, and the Zech logarithm terms cancel pairwise when summing over consecutive rows, yielding the stated identities. Using (4.45) and (4.46) in (4.34) and (4.35), we obtain

\(r_{i1}-r_{(i-1)1}=l_2\text{and}r_{i2}-r_{(i-1)2}=l_3,\) (4.47)

and

\(r_{i1}-r_{(i-2)1}=2l_2\text{and}r_{i2}-r_{(i-2)2}=2l_3,\) (4.48)

for _i_=4_,...,m_. Now, using (4.47) and (4.48) in (4.38) and (4.39), then

\(\overline{r_{(i-1)1}}=l_2\text{and}\overline{r_{(i-1)2}}=r_{(i-1)2}+Z(l_2-l_3),\) (4.49)


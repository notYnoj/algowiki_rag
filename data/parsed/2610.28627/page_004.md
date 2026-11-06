<tbc>By distributivity, the same shifted sum now gives

\(\sum_{j=1}^cz^{j-1}AE_j=AP_1-z^cAP_{c+1}+\varepsilon z^bAQ.\)

The coefficients at positions _a_-1_,...,a+b_-2 of \(\varepsilon AQ\), shifted by _z<sup>b</sup>_, lie entirely in the gap. Dividing them by \(\varepsilon\) recovers these coefficients of _AQ_ exactly; we call this output a _middle product_. For the full products, use the same successive decoder as before and reduce modulo \(\varepsilon\): every contribution from _Q_ vanishes. Our so-called _same-left primal packing_ therefore computes

\(\underbrace{(AP_i)_{i=1}^{c+1}}_{c+1\text{full products}}\underbrace{\big([z^k](AQ)\big)_{k=a-1}^{a+b-2}}_{1\text{middle product}}(\text{mod}\varepsilon).\)

Reduction modulo \(\varepsilon\) means taking the constant coefficient of the fully decoded result. The only division by \(\varepsilon\) is applied to the middle output, which is divisible by \(\varepsilon\), so no negative powers remain. Thus _we compute c_+2 _polynomial-product outputs modulo_ \(\varepsilon\) _using c multiplications, with only one extra coefficient in each encoded right polynomial._

To see the gain and its cost, take _a=b=L_ and _c_=3_L_. The encoded polynomials then have length _L_+1=(1+3_/c)L_. In return, _c_ source products provide _c_+1 full outputs and one middle output, giving a packing gain of (_c_+2)_/c_=1+2_/c_. The additional middle window increases the number of outputs from _c_+1 to _c_+2 without increasing the source lengths. The balanced primal/dual construction below converts this improvement into an exponent saving.

We also construct and rely on a _dual_ of the above packing, which reverses the roles: it computes _c_+1 middle products and one full product modulo \(\varepsilon\) using _c_ slightly longer middle-product calls. We obtain it by exchanging and transposing the linear encoding and decoding maps. Transposition preserves the constant coefficient of the decoded map.

## Amplifying the gain: Multivariate Packing.

Running the primal and dual packings side by side gives _c_+2 full and _c_+2 middle outputs from _c_ full and _c_ middle source products. Their counts add, so the gain remains 2(_c_+2)/(2_c_)=(_c_+2)_/c_. To multiply the gain, we move to multivariate polynomials and apply the packings in separate variables. In two variables _x,y_, one primal step in _x_ and one dual step in _y_ give (_c_+2)<sup>2</sup> outputs from _c_<sup>2</sup> source products; continuing in additional variables multiplies the gain further. To see why, start with one common left polynomial _A(x,y_) of length _a_ in each variable and a \((c+2)\times(c+2)\) table of independent right polynomials _B<sub>i,j</sub>(x,y_). We want coefficients of each product _AB<sub>i,j</sub>_. For rows 1_,...,c_+1, we want Full in _x_; for the last row, Mid in _x_. For columns 1_,...,c_+1, we want Mid in _y_; for the last column, Full in _y_. Each _B<sub>i,j</sub>_ has length _b_ in a variable where we want Full and length _a+b_-1 where we want Mid. Figure 2 shows every row and column for _c_=4. For example, each of the (_c_+1)<sup>2</sup> upper-left products requests \([x^ky^\ell](AB_{i,j})\) for \(0\le k<a+b-1\) and \(a-1\le\ell<a+b-1\); its right input has lengths (_b,a+b_-1). Every column supplies the _c_+1 full-range inputs and one middle-range input needed by the primal packing in _x_. Every row supplies the _c_+1 middle-range inputs and one full-range input needed by the dual packing in _y_.

As above, take \(c\ge a+2b-1\). In each column, apply the primal encoder in _x_, viewing the coefficients as polynomials in _y_. This leaves _c_ rows, with the _y_-lengths unchanged. In each resulting row, apply the dual encoder in _y_, viewing the coefficients as polynomials in _x_. We now have a \(c\times c\) table of encoded right polynomials, each of length _b_+1 in _x_ and _a+b_ in _y_. Multiply each by _A_,<tbc>


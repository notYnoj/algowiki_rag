combined length 2_b_ of the two original inputs. The smaller number of polynomial multiplications therefore gives no saving in the total number of input coefficients.

Alternatively, we can use _c_ encoded right polynomials with just one extra coefficient each. For \(c\ge a+b-1\), set<tbc>

\(E_j^{(0)}=P_j-zP_{j+1},1\le j\le c.\)

<tbc>Each \(E_j^{(0)}\) has length _b_+1. After multiplying these polynomials by _A_, take the following telescoping sum:

\(\sum_{j=1}^cz^{j-1}AE_j^{(0)}=(AP_1-zAP_2)+(zAP_2-z^2AP_3)+\cdots+(z^{c-1}AP_c-z^cAP_{c+1})\)<br>
\(=AP_1-z^cAP_{c+1}.\)

This sum is computed by adding coefficients. Writing \(W_j=AE_j^{(0)}\) and _W_ for the displayed sum, we have \([z^k]W=\sum_{j=1}^c[z^{k-j+1}]W_j\). Thus forming _W_ is a linear decoding operation. The intermediate products cancel, so the first _a+b_-1 coefficients give _AP_<sub>1</sub>, and the differences \(AE_j^{(0)}=AP_j-zAP_{j+1}\) then recover the remaining products successively. This still gives no saving in the total number of right-input coefficients: \(c(b+1)\ge(c+1)b\).

But notice the _empty space_ in the combined output: _AP_<sub>1</sub> ends before position _a+b_-1, while _z<sup>c</sup>AP_<sub>_c_+1</sub> starts at position _c_. Taking \(c\ge a+2b-1\) leaves at least _b_ zero coefficient positions between them. We use this space to obtain an additional product output, without making the encoded polynomials any longer.

Introduce a polynomial _Q_ of length _a+b_-1 and write \(Q=\sum_{j=0}^{c-1}q_jz^j\), padding with zeros. Let \(\varepsilon\) be a formal parameter.

Modify the encoding to

\(E_j=P_j-zP_{j+1}+\varepsilon z^bq_{j-1},1\le j\le c.\)

_That is, we add just one coefficient of_ \(\varepsilon Q\) _to each E<sub>j</sub>, at position b. Each P<sub>j</sub> ends at position b_-1_, but the shifted zP_<sub>_j_+1</sub> _already reaches position b: the added coefficient overlaps with its last coefficient._<tbc>

Without Q
AP1
zero coefficients
-c APc+1
With EQ
overlapping
middle of EQ
overlapping
contributions
shifted by zb
contributions
0
a + b - 1
c = a + 2b - 1
coefficient position

Figure 1: The telescoping sum before and after adding \(\varepsilon Q\), shown for _c=a_+2_b_-1. The _b_ highlighted coefficients of \(\varepsilon z^bAQ\) fill the zero gap; its remaining coefficients can overlap the endpoint products.


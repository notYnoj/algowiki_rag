## Encoding procedure.

Since \(ct\ge s+b>s\), we can split the coefficient list of _Q_ into _c_ consecutive blocks of length _t_, padding with zeros:<tbc>

\(Q^{(j)}(z)=\sum_{v=0}^{t-1}[z^{t(j-1)+v}]Qz^v,Q(z)=\sum_{j=1}^cz^{t(j-1)}Q^{(j)}(z).\)

<tbc>For \(1\le j\le c\), set

\(E_j=P_j-z^tP_{j+1}+\varepsilon z^bQ^{(j)}.\)

The first two terms combine adjacent right inputs using a shift of _t_. The last term places one block of \(\varepsilon Q\) in positions _b,...,b+t_-1. All three terms have degree less than _b+t_, so each _E<sub>j</sub>_ is a valid right input to Full<sub>_a,b+t_</sub>.

Compute the _c_ full source products _W<sub>j</sub>=AE<sub>j</sub>_, each of length _s+t_.

## Decoding procedure.

From these products, form the following telescoping sum:

\(W=\sum_{j=1}^cz^{t(j-1)}W_j=\sum_{j=1}^cz^{t(j-1)}AP_j-\sum_{j=1}^cz^{tj}AP_{j+1}+\varepsilon z^bA\sum_{j=1}^cz^{t(j-1)}Q^{(j)}=AP_1+\varepsilon z^bAQ-z^{ct}AP_{c+1}.\text{(3)}\)

In coefficient notation, this means computing

\([z^k]W=\sum_{j=1}^c[z^{k-t(j-1)}]W_j,\)

so forming _W_ is a fixed linear operation on the source outputs. For each \(2\le j\le c\), the term _z_<sup>_t(j_-1)</sup>_AP<sub>j</sub>_ occurs once with each sign and cancels. Only the two endpoint products remain, while the blocks of _Q_ reassemble into _Q_.

## Recover the middle product.

The first endpoint product _AP_<sub>1</sub> has no coefficients at exponents _s_ or above. The last endpoint product _z<sup>ct</sup>AP_<sub>_c_+1</sub> has no coefficients below \(ct\ge s+b\). Thus neither contributes at exponents _s,...,s+b_-1. For \(0\le k<b\), we obtain

\(\varepsilon^{-1}[z^{s+k}]W=[z^{s+k-b}](AQ)=[z^{a-1+k}](AQ).\)

These are exactly the _b_ coefficients of Mid<sub>_a,b_</sub>(_A,Q_). The division by \(\varepsilon\) is exact: every extracted coefficient has a factor \(\varepsilon\), and the resulting output is independent of \(\varepsilon\).

## Recover the full products.

First take the first _s_ coefficients of _W_:

\(Z_1=\sum_{k=0}^{s-1}[z^k]Wz^k.\)


_Proof of Theorem 2.3._ Fix an output ((_h,u),v_). Let _a(i_) be obtained by inserting \(i\in\{1,2\}\) into _u_ at position _h_, and let _b(j_) be obtained by inserting \(j\in\{1,2,3\}\) into _v_ at position _h_. For example, for _k_=3 and _h_=2,<tbc>

\(a(i)=(u_1,i,u_2),b(j)=(v_1,j,v_2).\)

<tbc>In particular, _a(i_)<sub>-_h_</sub>=_u_ and _b(j_)<sub>-_h_</sub>=_v_. Use the six shared products with labels (_a(i),b(j_)), and put<tbc>

\(p_j=U_{(h,u),j},q_j=V_{j,v}(1\le j\le 3).\)

<tbc>Our extended notation gives _p_<sub>3</sub>=0 and _q_<sub>3</sub>=-_q_<sub>1</sub>-_q_<sub>2</sub>, as required. In equation (5), the \(\ell=h\) terms contribute (-1)<sup>_i_-1</sup>_p<sub>j</sub>_ to _A_<sub>_a(i),b(j_)</sub> and **1**<sub>_i_=1</sub>_q<sub>j</sub>_ to _B_<sub>_a(i),b(j_)</sub>. For \(\ell\neq h\), the terms in _A_ are independent of _j_, since only _b<sub>h</sub>_ varies with _j_; call their sum _x<sub>i</sub>_. Likewise, the remaining terms in _B_ are independent of _i_, since only _a<sub>h</sub>_ varies with _i_; call their sum _y<sub>j</sub>_. Thus

\(A_{a(1),b(j)}=x_1+p_j,A_{a(2),b(j)}=x_2-p_j,\)<br>
\(B_{a(1),b(j)}=y_j+q_j,B_{a(2),b(j)}=y_j.\)

Applying Theorem 2.4 gives

\((UV)_{(h,u),v}=\sum_{i=1}^2\sum_{j=1}^3A_{a(i),b(j)}B_{a(i),b(j)}-(x_1+x_2)(y_1+y_2+y_3).\)

The subtracted term is one product of a linear form in _U_ and a linear form in _V_ ; assign it as the private product for this output. All six positive terms belong to the fixed collection of 6_<sup>k</sup>_ shared products.

For the bound on the linear forms, expand each abbreviation _V_<sub>3_,v_</sub>=-_V_<sub>1_,v_</sub>-_V_<sub>2_,v_</sub>. Each shared form and each _x<sub>i</sub>,y<sub>j</sub>_ is then a sum of at most 2_k_ signed input entries. Each private factor combines at most three such forms, giving the bound 6_k_.

Shared products for k = 2
A point (a, b) represents the product A,bBa,b.
(2,3)
h = 1: output (UV) (1,1),2
(2,2)
Fix (a2, b2) = (1,2); vary (a1, b1).
Second coordinate (a2, b2)
h = 2: output (UV) (2,2),1
Fix (a1, b1) = (2,1); vary (a2, b2).
(2,1)
(1,3)
a = (2,1), b = (1,2)
This product is used by both outputs.
(1,2)
(1,1)
Each output sums the six products on its line, then subtracts its private product.
(1,1) (1,2) (1,3) (2,1) (2,2) (2,3)
First coordinate (a1, b1)
In k dimensions: six points per line, and k lines through each point.

Figure 2: Shared products and outputs for _k_=2. Each point is one shared product, and each coordinate line selects the six shared products for one output. The highlighted lines reuse the product at their intersection.


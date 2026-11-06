Since _w_<sub>2_,q_</sub>=2_z<sub>q</sub>/_\[_n(n_-1)\] and \(\sum_qz_q^2=n(n^2-1)/12\),<tbc>

\(\sum_qw_{2,q}^2=\frac{n+1}{3n(n-1)}=a_n.\)

<tbc>For the third order the weight numerator is \(6z_q^2-h/2\). Its squared sum is

\(\sum_q(6z_q^2-h/2)^2=36\sum_qz_q^4-6h\sum_qz_q^2+\frac{nh^2}{4}\)<br>
\(=36\frac{nh(3n^2-7)}{240}-6h\frac{nh}{12}+\frac{nh^2}{4}=\frac{nh(n^2-4)}{5}.\)

Consequently

\(\sum_qw_{3,q}^2=\frac{nh(n^2-4)}{5n^2(n-1)^2(n-2)^2}=\frac{(n+1)(n+2)}{5n(n-1)(n-2)}=b_n.\)

The mixed sum vanishes exactly because _w_<sub>2_,n-q_+1</sub>=-_w_<sub>2_,q_</sub> whereas _w_<sub>3_,n-q_+1</sub>=_w_<sub>3_,q_</sub>. This gives the two same-direction covariance blocks.

For the opposite directions, write _r<sub>X</sub>(i),r<sub>Y</sub>(i_) for the sample ranks of the _i_th pair. The two complete L-comoments are<tbc>

\(\widehat{\lambda}_m^{[XY]}=\sum_{i=1}^nX_iw_{m,r_Y(i)},\widehat{\lambda}_s^{[YX]}=\sum_{j=1}^nY_jw_{s,r_X(j)}.\)

<tbc>Their population means vanish at independence. Expanding the product and separating the two independent marginal samples yields<tbc>

\(\mathbb{E}(\widehat{\lambda}_m^{[XY]}\widehat{\lambda}_s^{[YX]})=\sum_{i=1}^n\sum_{j=1}^n\mathbb{E}(X_iw_{s,r_X(j)})\mathbb{E}(Y_jw_{m,r_Y(i)}).\)

<tbc>Exchangeability and the univariate L-moment rank representation give<tbc>

\(\mathbb{E}(X_iw_{s,r_X(i)})=\frac{\ell_s^X}{n},\mathbb{E}(Y_iw_{m,r_Y(i)})=\frac{\ell_m^Y}{n}.\)

<tbc>For any fixed _i_, the sum over all _j_ of _w<sub>s,r<sub>X</sub>(j_</sub> is zero in every realized sample; multiply by _X<sub>i</sub>_ and take expectation:

\(0=\mathbb{E}(X_i\sum_{j=1}^nw_{s,r_X(j)})\)<br>
\(=\frac{\ell_s^X}{n}+(n-1)\mathbb{E}(X_iw_{s,r_X(j)}),j\neq i.\)

Hence the off-diagonal expectations are<tbc>

\(\mathbb{E}(X_iw_{s,r_X(j)})=-\frac{\ell_s^X}{n(n-1)},\mathbb{E}(Y_jw_{m,r_Y(i)})=-\frac{\ell_m^Y}{n(n-1)},i\neq j.\)


Then \(\widehat{\lambda}_2^{[XY]}=2b_1-b_0\) and \(\widehat{\lambda}_3^{[XY]}=6b_2-6b_1+b_0\), exactly as for the univariate sample L- moments, except that the order statistics of _X_ are replaced by the concomitants _X_<sub>\[_q:n_\]</sub> (Serfling and Xiao, 2007; Chebana and Ouarda, 2007).

For example, let _n_=5 and (_x<sub>i</sub>,y<sub>i</sub>_)=(3,1.3), (8,0.5), (5,2.6), (12,3.4), (6,2.1). Sorting by _y_ gives the concomitants (_X_<sub>\[1:5\]</sub>_,...,X_<sub>\[5:5\]</sub>)=(8,3,6,5,12). Then _b_<sub>0</sub>=34/5=6.8, \(b_1=(0\cdot 8+1\cdot 3+2\cdot 6+3\cdot 5+4\cdot 12)/20=3.9\), and \(b_2=(0\cdot 8+0\cdot 3+2\cdot 6+6\cdot 5+12\cdot 12)/60=3.1\). Hence \(\widehat{\lambda}_2^{[XY]}=2(3.9)-6.8=1\) and \(\widehat{\lambda}_3^{[XY]}=6(3.1)-6(3.9)+6.8=2\). The weights in (2.8) are (_w_<sub>2_,q_</sub>)=(-4,-2,0,2,4)/20 and (_w_<sub>3_,q_</sub>)=(12,-6,-12,-6,12)/60, which give the same values, and so does direct averaging of the kernels over the 10 pairs and the 10 triples.

## B.4 Conditional order-two kernel

Fix (_x,y_) and let \((X',Y')\) be an independent pair. Since _Y_ is continuous,

\(2M_{2,1}^{[XY]}(x,y)=\mathbb{E}((x-X')\mathrm{sgn}(y-Y'))\)<br>
\(=x\mathbb{E}(\mathbf{1}(Y'<y)-\mathbf{1}(Y'>y))-\mathbb{E}(X'\mathbf{1}(Y'<y))+\mathbb{E}(X'\mathbf{1}(Y'>y))\)<br>
\(=x\{2F_Y(y)-1\}+\mu_X-2Q_X(y).\)

Dividing by two yields (3.7). This calculation also verifies that \(\mathbb{E}(M_{2,1}^{[XY]}(Z))=\lambda_2^{[XY]}\).

## B.5 Conditional order-three kernel with two fixed pairs

Fix \((x_\ell,y_\ell)\) and (_x<sub>h</sub>,y<sub>h</sub>_), \(y_\ell<y_h\), and let the third observation be \((X',Y')\). Define \(u_\ell=F_Y(y_\ell)\) and _u<sub>h</sub>=F<sub>Y</sub>(y<sub>h</sub>_). The three possible relative positions of \(Y'\) give

\(Y'<y_\ell:3H_3=X'-2x_\ell+x_h,\)<br>
\(y_\ell<Y'<y_h:3H_3=x_\ell-2X'+x_h,\)<br>
\(Y'>y_h:3H_3=x_\ell-2x_h+X'.\)

The conditional expectation of 3_H_<sub>3</sub> can therefore be written as

\(3M_{3,2}^{[XY]}=u_\ell(-2x_\ell+x_h)+(u_h-u_\ell)(x_\ell+x_h)+(1-u_h)(x_\ell-2x_h)\)<br>
\(+\mathbb{E}(X'\mathbf{1}(Y'<y_\ell))-2\mathbb{E}(X'\mathbf{1}(y_\ell<Y'<y_h))+\mathbb{E}(X'\mathbf{1}(Y'>y_h)).\)

Collect the \(x_\ell\) coefficient: \(-2u_\ell+(u_h-u_\ell)+(1-u_h)=1-3u_\ell\). The _x<sub>h</sub>_ coefficient is \(u_\ell+(u_h-u_\ell)-2(1-u_h)=3u_h-2\). For the terms containing \(X'\), by continuity,

\(Q_X(y_\ell)-2\{Q_X(y_h)-Q_X(y_\ell)\}+\{\mu_X-Q_X(y_h)\}\)<br>
\(=\mu_X-3\{Q_X(y_h)-Q_X(y_\ell)\}.\)

Combining all three coefficients and dividing by three gives exactly (3.8).


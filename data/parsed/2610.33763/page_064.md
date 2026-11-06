From inequality (5.42), we deduce that the series of _f(x,y_) as given by Eq. (5.24) is bounded. Thus, the continuity of _f(x,y_) is established by the WMT.<br>
Now, our goal is to establish the continuity of _u(x,y,t_). By applying Lemma 5.3, Lemma 5.1, and Eq. (5.31), we find that

\(|U_{j,k}(t)|\le\frac{C}{\lambda_{j,k}}\big(K\|\psi^{(iv)}\|_{C^4([0,1]\times[0,1])}+C_0\|g^{(iv)}\|_{C^4([0,1]\times[0,1])}\big),\) (5.43)

where _K=C_<sub>1</sub>(1-_C_<sub>0</sub>) is a positive constant. Based on Eq. (5.43), we deduce that the series of _u(x,y,t_) in Eq. (5.23) is bounded above. Hence, the continuity of _u(x,y,t_) follows by applying the WMT.<br>
Our next task is to demonstrate the continuity of _u<sub>xx</sub>(x,y,t_). To achieve this, we differentiate each term of the series solution provided in Eq. (5.23) w.r.t _x_

\(u_{xx}(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty U_{j,k}(t)X_{xx,j,k}(x,y),\) (5.44)

where<tbc>

\(X_{xx,j,k}(x,y)=-\nu_j^kX_{j,k}(x,y).\)

<tbc>Indeed, we can have<tbc>

\(|X_{j,k}(x,y)|<1,\)

<tbc>which implies

\(\big|X_{xx,j,k}(x,y)\big|\le\nu_j^k.\) (5.45)

Based on Lemma 5.1, Eq. (5.43), and inequality (5.45), we derive the following expression

\(u_{xx}(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty\frac{C}{\mu_k^2\lambda_{j,k}}\big(K\|\psi^{(iv)}\|_{C^4([0,1]\times[0,1])}+C_0\|g^{(iv)}\|_{C^4([0,1]\times[0,1])}\big).\) (5.46)

Eq. (5.46) demonstrates that the series form of _u<sub>xx</sub>(x,y,t_) is bounded above. Consequently, by WMT, _u<sub>xx</sub>(x,y,t_) is continuous.<br>
Next, we establish the continuity of _u<sub>yy</sub>(x,y,t_). By applying term-by-term differentiation w.r.t _y_ on the series solution from Eq. (5.23), we obtain

\(u_{yy}(x,y,t)=-\sum_{j=1}^\infty\sum_{k=1}^\infty\mu_k^2U_{j,k}(t)X_{j,k}(x,y).\) (5.47)

Using Lemma 5.1 and Eq. (5.43), we obtain

\(u_{yy}(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty\frac{C}{\nu_j^k\lambda_{j,k}}\big(K\|\psi^{(iv)}\|_{C^4([0,1]\times[0,1])}+C_0\|g^{(iv)}\|_{C^4([0,1]\times[0,1])}\big).\) (5.48)

Thus, _u<sub>yy</sub>(x,y,t_), as given in Eq. (5.48), is also bounded above, ensuring its continuity by WMT.


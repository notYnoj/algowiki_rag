## 5.3.3 The main results of first-ISP

In this subsection, we outline the existence and the uniqueness of the solution of the first-ISP. To demonstrate the regularity of solutions for both first-ISP and second- ISP, we present the following lemma:

**Lemma 5.3** _[13] Consider_ **Z**_<sub>j,k</sub>(t_) _as defined by Eq. (5.27), which is continuous on_ \([0,\infty)\)_, vanish at t_=0_, positive, and nondecreasing on_ R<sub>+</sub>_. For any t,T\>_0_, the following inequalities_

(_a)_ \(\mathbf{Z}_{j,k}(t)\le\frac{1}{\lambda_{j,k}}\),<tbc>

_(b)_ \(\frac{1}{\mathbf{Z}_{j,k}(t)}\le C_0\lambda_{j,k}\),<tbc>

<tbc>_hold. where C_<sub>0</sub>=_C_<sub>0</sub>(_T)\>_0.

\(\bullet\) From the expression for **W**_<sub>j,k</sub>(t_) in Eq. (5.27), we can written as<tbc>

\(\mathbf{W}_{j,k}(t)=1-\lambda_{j,k}\int_0^t\mathbf{V}_{j,k}(\zeta)d\zeta.\)

<tbc>The form of **V**_<sub>j,k</sub>(t_) here aligns with the expression provided in [13] (Lemma 4.1, Eq. (42)). Given this, the estimate for **V**_<sub>j,k</sub>(t_) can be written as

\(0<c_0\le\lambda_{j,k}\int_0^t\mathbf{V}_{j,k}(\zeta)d\zeta<1,\) (5.40)

based on the inequalities in (5.40), we deduce that

\(\mathbf{W}_{j,k}(t)\le C_1,\) (5.41)

where _c_<sub>0</sub> and _C_<sub>1</sub> are positive constants.

**Theorem 5.2** _Suppose that_ \(\psi(y,x)\) _and g(y,x_) _are given functions in_ \(C^4([0,1]\times[0,1])\) _and meet the conditions given in_ (5.20)_. Then, a regular solution exists for first-ISP associated with the system_ (5.5)-(5.8) _and_ (5.13).

**Proof:** This theorem is proved in two parts.

**Part-I:** To establish the existence of a solution for first-ISP, we need to demonstrate the continuity of the associated series<tbc>

\(f(x,y),u(x,y,t),u_{xx}(x,y,t),u_{yy}(x,y,t),\text{and}_G\mathcal{D}_t^{(\varrho)}u(x,y,t).\)

<tbc>First, we focus on verifying the continuity of _f(x,y_). Using Lemma 5.3, along with estimate (5.41) and Eq. (5.30), we obtain<tbc>

\(|f_{j,k}|\le C_0\lambda_{j,k}(|g_{j,k}|-C_1|\psi_{j,k}|).\)

<tbc>By invoking Lemma 5.1, we deduce

\(|f_{j,k}|\le C_0C\big(\|g^{(iv)}\|_{C^4([0,1]\times[0,1])}-C_1\|\psi^{(iv)}\|_{C^4([0,1]\times[0,1])}\big)\) (5.42)


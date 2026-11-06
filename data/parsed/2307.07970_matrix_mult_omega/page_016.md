Namely, for every \(\varepsilon>0\), there exists an arithmetic circuit of size \(O(n^{\omega+\varepsilon})\) that computes the multiplication of two \(n\times n\) matrices. Since \(\langle q,q,q\rangle^{\otimes n}\equiv\langle q^n,q^n,q^n\rangle\), equivalently \(\omega\) can be written in terms of the asymptotic rank of \(\langle q,q,q\rangle\) as<tbc>

\(\omega=\mathrm{log}_q(\widetilde{R}(\langle q,q,q\rangle)).\)

<tbc>In this paper, we also consider the arithmetic complexity of multiplying rectangular matrices of sizes \(n^a\times n^b\) and \(n^b\times n^c\) where \(a,b,c\in\mathbb{R}_{\ge 0}\). We define the quantity \(\omega(a,b,c)\) similar to \(\omega\) as

\(\omega(a,b,c)=\mathrm{log}_q\big(\widetilde{R}(\langle q^a,q^b,q^c\rangle)\big)\)

where \(q\ge 2\) is a positive integer. This means that for any \(\varepsilon>0\), there exists an arithmetic circuit of size \(O(n^{\omega(a,b,c)+\varepsilon})\) that computes the multiplication of an \(n^a\times n^b\) matrix with an \(n^b\times n^c\) matrix. In this paper, we focus on bounds for the values of the form \(\omega(1,\kappa,1)\) for \(\kappa>0\). We remark that it is known that \(\omega(1,1,\kappa)=\omega(1,\kappa,1)=\omega(\kappa,1,1)\).

## 3.5 Schönhage’s Asymptotic Sum Inequality

By the above definition of \(\omega\), it is clear that if one can bound the asymptotic rank of matrix multiplication tensors, then one would get an upper bound on \(\omega\). In fact, Schönhage showed in \[Sch81\] that one can obtain an upper bound on \(\omega\) if one can bound the asymptotic rank of a direct sum of matrix multiplication tensors. Specifically, we recall Shönhage’s asymptotic sum inequality as follows.

**Theorem 3.1** (Asymptotic Sum Inequality \[Sch81\])**.** _For positive integers r\>m and a<sub>i</sub>,b<sub>i</sub>,c<sub>i</sub> for_ \(i\in[m]\)_, if_<tbc>

\(\widetilde{R}\left(\oplus_{i=1}^m\langle a_i,b_i,c_i\rangle\right)\le r,\)

<tbc>_then_ \(\omega\le 3\tau\) _where_ \(\tau\in[2/3,1]\) _is the solution to the equation_

\(\sum_{i=1}^m(a_i\cdot b_i\cdot c_i)^\tau=r.\)

Analogously, the asymptotic sum inequality can also be used to obtain bounds on the rectangular matrix multiplication as follows.

**Theorem 3.2** (Asymptotic Sum Inequality for \(\omega(a,b,c)\) \[Sch81\])**.** _Let t,q\>_0 _be positive integers and_ \(a,b,c\ge 0\) _, then_

\(t\cdot q^{\omega(a,b,c)}\le\widetilde{R}\left(\oplus_{i=1}^t\langle q^a,q^b,q^c\rangle\right).\)

## 3.6 The Coppersmith-Winograd Tensor

For a nonnegative integer \(q\ge 0\), the Coppersmith-Winograd tensor CW_<sub>q</sub>_ over the variables _X_={_x_<sub>0</sub>_,...,x_<sub>_q_+1</sub>}, _Y_={_y_<sub>0</sub>_,...,y_<sub>_q_+1</sub>}, _Z_={_z_<sub>0</sub>_,...,z_<sub>_q_+1</sub>} is defined as<tbc>

\(\mathrm{CW}_q:=x_0y_0z_{q+1}+x_0y_{q+1}z_0+x_{q+1}y_0z_0+\sum_{i=1}^q(x_0y_iz_i+x_iy_0z_i+x_iy_iz_0).\)


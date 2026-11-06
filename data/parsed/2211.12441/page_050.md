for all _k_=1_,...,a_. Notice that _f(t_)=|sin(_t_)| satisfies all the conditions of the claim, albeit after scaling the period from \(\pi\) to 1.

To prove the general claim, let \(\kappa=kt-\lfloor kt\rfloor\) and \(\lambda=\ell t-\lfloor\ell t\rfloor\), noting that \(\kappa,\lambda\in[0,1]\). By the enclosing property, it is true that \(\kappa/k\ge\lambda/\ell\), since they represent the distance from _t_ to the left endpoints of the _k_ and \(\ell\)-intervals, respectively, and _k_ encloses \(\ell\) at _t_. This can be seen in Fig. 17.

Suppose \(\kappa\le\lambda\). We have

\(f(kt)=f(\kappa)\ge\frac{\kappa}{\lambda}f(\lambda)\ge\frac{k}{\ell}f(\lambda)=\frac{k}{\ell}f(\ell t).\)

The first step follows from the periodicity of _f_, the second from the concavity of _f_ on \[0,1\] and the fact that _f_(0)=0 (the point \((\kappa,f(\kappa))\) is above the line segment connecting \((\lambda,f(\lambda))\) and (0,0)), the third from the aforementioned inequality \(\kappa/k\ge\lambda/\ell\), and the last from the periodicity of _f_ again.

If \(\lambda<\kappa\), we can instead consider the function \(\widetilde{f}(t)=f(1-t)\). Here, \(\widetilde{\kappa}=1-\kappa\) and \(\widetilde{\lambda}=1-\lambda\), and we can use our previous reasoning. This proves the general claim.

## 10 Turing Complexity

This section serves as a supplementary discussion on the time (and space) complexity of algorithms for computing the minimum number of inversions in trees. From the analysis in Section 4.2, computing \(\mathrm{MinInv}(T,\rho)\) involves computing the sum of \(\mathrm{MinRInv}(T_v,\rho)\) independently for each \(v\in T\):<tbc>

\(\mathrm{MinInv}(T,\rho)=\sum_v\mathrm{MinRInv}(T_v,\rho).\)

<tbc>In order to compute \(\mathrm{MinRInv}(T_v,\rho)\) for each _v_, we need to check the orderings \(\sigma\) of the children _u_<sub>1</sub>_,...,u<sub>k</sub>_ of _v_ and determine the minimum number of cross inversions between the corresponding leaf sets _L_<sub>1</sub>_,...,L<sub>k</sub>_ in the order given by \(\sigma\):

\(\mathrm{RInv}(T_v,\rho,\sigma)\doteq\sum_{1\le i<j\le k}\mathrm{XInv}_\rho(L_{\sigma(i)},L_{\sigma(j)}).\)

A natural approach for computing \(\mathrm{MinInv}(T,\rho)\) consists of two phases:

f(kx) k
f(kx) l
t
x
/
K/k

Figure 17: Proof of Claim 74: \(\lambda/\ell\le\kappa/k\)


_Proof._ Let \(\unknown_{F_\theta^\star}\) be the relation on F defined as follows: \(T\unknown_{F_\theta^\star} S\) whenever \(F_\theta^\star(T)\le F_\theta^\star(S)\). Since \(\unknown\) is the smallest preorder on F that is compatible with \(\oplus\) and \(\otimes\) and has properties (D1)-(D4), (R) and (I), also with the legs renumbered, it suffices to show that \(\unknown_{F_\theta^\star}\) is also such a preorder. Indeed, then it contains \(\unknown\), which is the claim.

By definition of \(F_\theta^\star\), the relation \(\unknown_{F_\theta^\star}\) is compatible with direct sums and tensor products. Renumbering the legs of an expression changes \(F_\theta^\star\) into \(F_{\theta^\star}\), where \(\theta'\) is \(\theta\) with its entries renumbered in the same way. So, it suffices to check the properties as stated in Definition 5.3, without the permutations. We do this now. We will write _p_:=_p_<sub>1</sub>.

(D1) This is the upper bound in Proposition 5.8(i).<tbc>

(D2) Let \(w_i=F_\theta^\star(T_i)\) for every \(i\in[m]\). Then by Hölder’s inequality and Proposition 5.8(iv),<tbc>

<tbc>\(t^p\sum_{i=1}^mw_i\le m^{1-p}t^p\big(\sum_{i=1}^mw_i^{1/p}\big)^p\le F_\theta^\star(m,t,m+t-1)\big(\sum_{i=1}^mw_i^{1/p}\big)^p.\)<tbc>

<tbc>The first and last quantities are the values of \(F_\theta^\star\) at the two sides of (D2).<tbc>

(D3) Raising the values at the two sides to the power 1_/p_ gives the inequality of Proposition 5.8(ii) if _z=x+y_-1, and this inequality with the second and third legs renumbered if _y=x+z_-1; a further summand _C_ adds \(F_\theta^\star(C)^{1/p}\) to both sides.<tbc>

(D4) The same as the proof for (D3), but applying Proposition 5.8(iii) instead.<tbc>

(R) The value at _T_<sub>1</sub> is at most the values at \(T_1\oplus T_2\) and at \(T_1\oplus_1T_2\), and the value at \(T_1\oplus_1T_2\) is at most that at \(T_1\oplus T_2\), since \((x^{1/p}+y^{1/p})^p\le x+y\) for all _x,y\>_0 (using that \(p\in[0,1]\)). Moreover, \(F_\theta^\star(x,y,x+y-1)\) is nondecreasing in _y_, also with the second and third legs renumbered, and \(F_\theta^\star(a,b,a+b-1)\le a^{p_2}b^p\), which is the value at \(\mathsf{P}_{a,1,a}\otimes\mathsf{P}_{1,b,b}\) (Proposition 5.8(i) and (iv)).<tbc>

(I) The isomorphisms do not change \(F_\theta^\star\). Indeed, \(F_\theta^\star\) is additive and multiplicative, and \(F_\theta^\star(\langle 1\rangle)=F_\theta^\star(1,1,1)=1\). The formula for partial direct sums is symmetric and associative, and homogeneous of degree one, so it respects the distributivity of \(\otimes\) over \(\oplus_1\). The value at \(\langle n_1,n_2,n_3\rangle\) is multiplicative in (_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>). Finally, the value at the partial direct sum of _r_ copies of _U_ is \(r^pF_\theta^\star(U)\), which is the value at \(U\otimes\mathsf{P}_{1,r,r}\). \(\square\)

_Proof of Theorem 5.4._ Proposition 5.9 tells us that \(F_\theta^\star\) is monotone under \(\unknown\) for every \(\theta\in\Theta\). Then Proposition 5.7, with \(\unknown\) as \(\unknown'\), gives us the result.

**Example 5.10.** The barrier of Proposition 5.7 applies also to preorders \(\unknown'\) extending \(\unknown\), as long as \(F_\theta^\star\) remains monotone. As a basic example, if we add Strassen’s degenerations \(\langle\lceil 3n^2/4\rceil\rangle\unknown\langle n,n,n\rangle[\text{Str87, Theorem 6.6}]\) as one of the generating relations of \(\unknown\), the barrier still applies. Indeed, \(\lceil 3n^2/4\rceil\le n^2\le F_\theta^\star(\langle n,n,n\rangle)\), because \(F_\theta^\star(\langle n,n,n\rangle)=n^{p_1+p_2+p_3}\) and

\(p_1+p_2+p_3-2=\frac{2\theta_1\theta_2\theta_3}{(1-\theta_1)(1-\theta_2)(1-\theta_3)}>0.\)

Similarly, each \(F_\theta^\star\) is also monotone on the polynomial multiplication degenerations of Remark 3.10 and Remark 3.12, so the barrier applies. As another example, which is also clear form the asymptotic spectrum point of view, the barrier remains true if \(\unknown\) is replaced by its asymptotic closure. There an expression \(T\in\mathcal{F}\) is at most \(S\in\mathcal{F}\) if \(T^{\otimes n}\unknown S^{\otimes n}\otimes\langle 2^{o(n)}\rangle\) for every integer \(n\ge 1\). Indeed, then \(F_\theta^\star(T)^n\le F_\theta^\star(S)^n2^{o(n)}\) for every integer \(n\ge 1\), since \(F_\theta^\star\) is multiplicative and \(F_\theta^\star(\langle 2^{o(n)}\rangle)=2^{o(n)}\), so \(F_\theta^\star(T)\le F_\theta^\star(S)\).


Let _Q_ be the expression in the outer brackets. We claim that _Q\<_0, which is sufficient because _B_<sup>_u_-2</sup>_L_<sup>_v_-2</sup>_\>_0. Rewrite<tbc>

<tbc>\(Q=(uL+v\theta_1B)^2-\big(uL^2+v(\theta_1B)^2\big).\)<tbc>

<tbc>Since \(\partial L/\partial B=\theta_1\) and _u+v_=1_/p_<sub>1</sub>_\>_1, then \(\partial Q/\partial B=2\theta_1(u+v-1)(uL+v\theta_1B)>0\), so _Q_ is increasing in _B_. So if we show that _Q_ is equal to 0 at _A=B_, then we are done. At _A=B_ we have _L=A_, so \(Q=A^2\big((u+v\theta_1)^2-(u+v\theta_1^2)\big)\). By (5.6) we get \(u+v\theta_1=1-\theta_2\), and from the definitions we get \(v\theta_1(1-\theta_1)=\theta_2(1-\theta_2)\). We find<tbc>

<tbc>\(u+v\theta_1^2=(u+v\theta_1)-v\theta_1(1-\theta_1)=(1-\theta_2)^2,\)<tbc>

<tbc>which shows \((u+v\theta_1)^2-(u+v\theta_1^2)=0\), and the proof is complete.<tbc>

(iii) Write (_x,y,z_)=(_a,b,a+b_-1). Fix \(a\ge 1\). Let \(\mu:=A^{(1-p_1)/p_1}\), and, for real \(b\ge 1\), let \(h_2(b):=F_\theta^\star(a,b,a+b-1)^{1/p_1}\) and \(h_3(b):=F_\theta^\star(a,a+b-1,b)^{1/p_1}\).<tbc>

<tbc>In (ii) we proved that the function _h_<sub>2</sub> is concave, and the same proof applies for _h_<sub>3</sub> if we exchange the second and third legs. For large _b_ (so that we are in the first case of (5.7) and similarly for _h_<sub>3</sub>), we have \(h_\ell(b)=\mu(b+\theta_\ell(A-1))\). By concavity, it follows that \(h_\ell(b)\le\mu(b+\theta_\ell(A-1))\) for any \(b\ge 1\). Moreover, \(\mu\) lower bounds the slopes at any point, which gives \(h_\ell(b)+\mu t\le h_\ell(b+t)\) for \(t\ge 0\). By (5.5) we also obtain \((\theta_2+\theta_3)(A-1)=a-\theta_1-(\theta_2+\theta_3)=a-1\). By the above three facts, we find that<tbc>

\(2h_2(b)+h_3(b)\le h_2(b)+\mu\big(b+\theta_2(A-1)\big)+\mu\big(b+\theta_3(A-1)\big)\)<br>
\(=h_2(b)+\mu(2b+a-1)\le h_2(3b+a-1),\)

which is the desired result.<tbc>

(iv) Fix \(a\ge 1\). Let _h_:=_h_<sub>2</sub> and \(\mu\) be as in the proof of (iii).<tbc>

<tbc>We prove the first inequality. As before, concavity gives \(h(b)\ge h(1)+\mu(b-1)\) for every real \(b\ge 1\). We find that _h_(1)=_f(a,_1)<sup>1_/p_<sub>1</sub></sup>=_a_<sup>_p_<sub>2</sub>_/p_<sub>1</sub>, because when _b_=1 we have _B_=1 and \(\theta_1B+(1-\theta_1)A=a\). Since \(A\ge a\) and _p_<sub>1</sub>+_p_<sub>2</sub>_\>_1, both \(\mu\) and _h_(1) are at least _a_<sup>(1-_p_<sub>1</sub>)_/p_<sub>1</sub></sup>. It follows that \(h(b)\ge a^{(1-p_1)/p_1}b\), which is the first inequality.<tbc>

<tbc>We prove the second inequality. By concavity, the slopes of _h_ do not exceed \(h'(1)\), where we take the derivative from the right. Hence, \(h(b)\le h(1)+(b-1)h'(1)\). If _a_=1, then \(A=1\le B\) for every \(b\ge 1\), so the first case of (5.7) gives _h(b_)=_b_, so \(h'(1)=1=h(1)\). Let _a\>_1. Then _B_=1_\<A_ at _b_=1, so for _b_ near 1 the second case applies. We have _h=B<sup>u</sup>L<sup>v</sup>_, with _L_, _u_ and _v_ as in the proof of (ii). At _b_=1 we have _B_=1 and _L=a_, and \(B'=1/(1-\theta_2)\) and \(L'=\theta_1/(1-\theta_2)\), so<tbc>

<tbc>\(\frac{h'(1)}{h(1)}=\big(\frac{uB'}{B}+\frac{vL'}{L}\big)(1)=\frac{1}{1-\theta_2}\big(u+\frac{v\theta_1}{a}\big)=\frac{1-p_2+p_2\theta_1/a}{p_1(1-\theta_2)}\le\frac{1-p_2+p_2\theta_1}{p_1(1-\theta_2)}=1,\)<tbc>

<tbc>where we use _a\>_1, and the last equality is (5.6). It follows that \(h(b)\le bh(1)\), that is, \(f(a,b)\le a^{p_2}b^{p_1}\). \(\square\)

## 5.7 Proof of monotonicity of \(F_\theta^\star\) and the operational barrier

We prove \(F_\theta^\star\) is monotone under \(\unknown\).

**Proposition 5.9** (Combinations of the ingredients)**.** _Let_ \(\theta\in\Theta\)_. For all_ \(S,T\in\mathcal{F}\)_, if_ \(T\unknown S\)_, then_ \(F_\theta^\star(T)\le F_\theta^\star(S)\).


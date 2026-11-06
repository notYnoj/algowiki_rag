where {_i,j,k_}={1,2,3}, since _x_<sub>1</sub>+_x_<sub>2</sub>+_x_<sub>3</sub>=2 and \(p_ix_jx_k=\theta_i\). Throughout the remainder of this section we will use _p<sub>i</sub>_ as defined in (5.2), and leave its dependence on \(\theta=(\theta_1,\theta_2,\theta_3)\) implicit. Recall that a triple (_d_<sub>1</sub>_,d_<sub>2</sub>_,d_<sub>3</sub>) of real numbers \(d_1,d_2,d_3\ge 1\) is admissible (Definition 5.1) if its largest entry is the sum of the other two minus 1, that is, if _d_<sub>1</sub>+_d_<sub>2</sub>+_d_<sub>3</sub>=2max(_d_<sub>1</sub>_,d_<sub>2</sub>_,d_<sub>3</sub>)+1.

**Definition 5.5.** Let \(\theta\in\Theta\), and let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be as in (5.2).

(i) For an admissible triple (_d_<sub>1</sub>_,d_<sub>2</sub>_,d_<sub>3</sub>) of real numbers, let \(A_s:=(d_s-\theta_s)/(1-\theta_s)\) for \(s\in[3]\). Let _i_, _j_ and _k_ be indices with {_i,j,k_}={1,2,3} such that \(d_i,d_j\le d_k\) and \(A_i\le A_j\), and define<tbc>

<tbc>\(F_\theta^\star(d_1,d_2,d_3):=A_i^{1-p_i}\big(\theta_jA_i+(1-\theta_j)A_j\big)^{p_i}.\)<tbc>

<tbc>The value does not depend on the choice of the indices: if two entries are largest, then the third is 1, so _i_ is its index, and both choices of _k_ give max(_d_<sub>1</sub>_,d_<sub>2</sub>_,d_<sub>3</sub>)<sup>_p<sub>i</sub>_</sup>; if _A<sub>i</sub>=A<sub>j</sub>_, both choices of _i_ give _A<sub>i</sub>_. On the generators of F, let \(F_\theta^\star(\mathsf{P}_{x,y,z}):=F_\theta^\star(x,y,z)\).<tbc>

(ii) We extend \(F_\theta^\star\) to F as follows. For all \(S,T\in\mathcal{F}\) and every \(\ell\in[3]\) such that the expressions on the left lie in F, let

• \(F_\theta^\star(S\oplus T):=F_\theta^\star(S)+F_\theta^\star(T)\),<tbc>

• \(F_\theta^\star(S\otimes T):=F_\theta^\star(S)F_\theta^\star(T)\), and<tbc>

• \(F_\theta^\star(S\oplus_\ell T):=\big(F_\theta^\star(S)^{1/p_\ell}+F_\theta^\star(T)^{1/p_\ell}\big)^{p_\ell}\).

By construction, the function \(F_\theta^\star\) is additive and multiplicative on F. But we stress that it is defined on formal combinations in F, not on tensors, and we will prove monotonicity of \(F_\theta^\star\) only for the formal preorder \(\unknown\) not for degeneration \(\triangle\).

## 5.5 Choice of \(\theta\) for the \(\omega(a,b,c)\) barrier

To prove Theorem 5.4, we need to choose the parameters \(\theta\in\Theta\) optimally based on _a,b,c_. For the square case, we can take \(\theta_1=\theta_2=\theta_3=1/3\). Then we have _p<sub>i</sub>_=3/4 and _A<sub>s</sub>_=(3_d<sub>s</sub>_-1)/2, so \(F_\theta^\star\) is the function

\(F^\star(x,y,z)=\big(\frac{3m-1}{2}\big)^{1/4}\big(\frac{x+y+z-m}{2}\big)^{3/4},\text{where}m=\mathrm{min}(x,y,z),\) (5.3)

which satisfies \(F^\star(\langle n,n,n\rangle)=n^{9/4}\). The following lemma shows how to choose \(\theta\) to cover the second case of (5.1).

**Lemma 5.6.** _Let_ \(a\ge b\ge c\ge 0\) _be real numbers with c(a+b)\>ab, and let_<tbc>

\(\theta_1:=1-\frac{2ab}{ab+bc+ca},\theta_2:=1-\frac{2bc}{ab+bc+ca},\theta_3:=1-\frac{2ac}{ab+bc+ca}.\)

<tbc>_Then_ \(\theta=(\theta_1,\theta_2,\theta_3)\in\Theta\) _and_

\(\frac{a\theta_2}{(1-\theta_1)(1-\theta_3)}+\frac{b\theta_3}{(1-\theta_1)(1-\theta_2)}+\frac{c\theta_1}{(1-\theta_2)(1-\theta_3)}=\frac{(ab+bc+ca)^2}{4abc}.\)

_Proof._ Let _D_:=_ab+bc+ca_. Since \(c(a+b)>ab\ge 0\) and \(a\ge b\ge c\ge 0\), we have that \(D>2ab\ge 2ac\ge 2bc\). Hence \(\theta_1,\theta_2,\theta_3>0\). Also, \(\theta_1+\theta_2+\theta_3=3-2D/D=1\). Since \(1-\theta_1=2ab/D\), \(1-\theta_2=2bc/D\) and \(1-\theta_3=2ac/D\), the three terms on the left-hand side of the claim are \(D^2\theta_2/(4abc)\), \(D^2\theta_3/(4abc)\) and \(D^2\theta_1/(4abc)\), so their sum is _D_<sup>2</sup>/(4_abc_).


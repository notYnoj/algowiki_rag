(I1) The associativity and commutativity of \(\oplus\) and \(\otimes\), the distributivity of \(\otimes\) over \(\oplus\), and \(T\otimes\langle 1\rangle\cong T\).<tbc>

(I2) Any two orders and bracketings of a partial direct sum \(T_1\oplus_1\cdots\oplus_1T_m\), and the distributivity of \(\otimes\) over \(\oplus_1\): the expression \((T_1\oplus_1\cdots\oplus_1T_m)\otimes(S_1\oplus_1\cdots\oplus_1S_n)\) and the partial direct sum of the _mn_ expressions \(T_i\otimes S_j\).<tbc>

(I3) For all positive integers _n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>_,m_<sub>1</sub>_,m_<sub>2</sub>_,m_<sub>3</sub>, the isomorphism \(\langle n_1,n_2,n_3\rangle\otimes\langle m_1,m_2,m_3\rangle\cong\langle n_1m_1,n_2m_2,n_3m_3\rangle\) (Lemma 2.1(iii)).<tbc>

(I4) The partial direct sum of _r_ copies of _U_ and \(U\otimes\mathsf{P}_{1,r,r}\), for every integer \(r\ge 1\) (Lemma 3.4).

Definition 5.3 collects the combination rules and the ingredients of Section 1.1: the preorder and its compatibility with \(\oplus\) and \(\otimes\) are the rules (C1)-(C3), the renumbering of the legs takes the place of (C4), and (D1)-(D4) are the ingredients. Whenever the triples in (D3) and (D4) are admissible, either _z=x+y_-1 or _y=x+z_-1, so these are the ingredients of Section 1.1 with the shared leg first. The properties (R) and (I) add (standard) restrictions and isomorphisms, and ingredient (D0), \(\mathsf{P}_{1,b,b}\cong\langle 1,1,b\rangle\), follows from (I).

If \(T\unknown S\), then \(T\unknown S\), reading both sides as the tensors that they represent. This will make every relation \(\langle n_1,n_2,n_3\rangle\unknown\langle r\rangle\) give an upper bound on \(\omega_\mathbb{F}\). Indeed, \(\unknown\) is the smallest preorder with the properties of Definition 5.3, and each property still holds with \(\le\) in place of \(\unknown\), by (D0)-(D4).

We now state the barrier.

**Theorem 5.4** (Operational barrier)**.** _Let_ \(n_1,n_2,n_3,r\ge 1\) _be integers with_ \(\langle n_1,n_2,n_3\rangle\unknown\langle r\rangle\).

(i) _Let_ \(a\ge b\ge c\) _be the numbers_ log_n_<sub>1</sub>, log_n_<sub>2</sub> _and_ log_n_<sub>3</sub> _in nonincreasing order. Then_

\(\mathrm{log}r\ge\left\{\begin{array}{ c c }
a+b & \text{\textit{if}}c(a+b)\le ab, \\
\frac{(ab+bc+ca)^2}{4abc} & \text{\textit{if}}c(a+b)>ab.
\end{array}\right.\) (5.1)

(ii) _In particular, if n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=_n, then_ \(n^{9/4}\le r\).

Theorem 5.4 relates to barriers for \(\omega_\mathbb{F}(a,b,c)\) as follows. Every relation \(\langle n_1,n_2,n_3\rangle\unknown\langle r\rangle\) is a degeneration \(\langle n_1,n_2,n_3\rangle\unknown\langle r\rangle\), so \(\phi(\langle n_1,n_2,n_3\rangle)\le r\) for every \(\phi\in\Delta_\mathbb{F}\), and Lemma 4.3(iv) and Lemma 4.4 give \(\omega_\mathbb{F}(\mathrm{log}n_1,\mathrm{log}n_2,\mathrm{log}n_3)\le\mathrm{log}r\). For _n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=_n_\ge 2, this is \(\omega_\mathbb{F}\le\mathrm{log}r/\mathrm{log}n\). By Theorem 5.4, these bounds are at least the bound of Theorem 1.2, and so are their limits, since that bound is continuous and homogeneous in (_a,b,c_). In particular, no such relation, and no limit of such bounds, gives an upper bound on \(\omega_\mathbb{F}\) below 9/4.

## 5.4 Definition of functions \(F_\theta^\star\) on F

Let \(\Theta\) be the set of triples \(\theta=(\theta_1,\theta_2,\theta_3)\) of positive real numbers with \(\theta_1+\theta_2+\theta_3=1\). To prove Theorem 5.4, we will construct, for every \(\theta\in\Theta\), positive functions \(F_\theta^\star\) on F satisfying \(F_\theta^\star(\langle r\rangle)=r\) for every integer \(r\ge 1\) and which are \(\unknown\)-monotone.

The idea behind the construction is to make the inequalities that the degenerations (D0)- (D4) give ( 1) essentially tight. At the matrix multiplication tensors, the functions \(F_\theta^\star\) will have the values \(F_\theta^\star(\mathsf{P}_{1,n,n})=n^{p_1}\), \(F_\theta^\star(\mathsf{P}_{n,1,n})=n^{p_2}\) and \(F_\theta^\star(\mathsf{P}_{n,n,1})=n^{p_3}\), for some exponents _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub>. These cannot be chosen freely: by the proof of Theorem 1.2, the exponents of such functions satisfy the inequality of Proposition 4.14. We want this inequality to be an equality. If we write \(x_i=1-\theta_i\) with \(\theta\in\Theta\), we obtain equality if we take<tbc>

\(p_i:=\frac{\theta_i}{(1-\theta_j)(1-\theta_k)},\) (5.2)


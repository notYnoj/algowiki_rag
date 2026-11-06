We still need to prove that \(F_\theta^\star\) is \(\unknown\)-monotone, but we can already prove the consequences. If we have any preorder \(\unknown'\) on F for which \(F_\theta^\star\) is monotone, we obtain the barrier by evaluating \(F_\theta^\star\) on \(\langle n_1,n_2,n_3\rangle\) for the values of \(\theta\) from Lemma 5.6.

**Proposition 5.7.** _Let_ \(\unknown'\) _be any preorder on_ F_, and let_ \(n_1,n_2,n_3,r\ge 1\) _be integers with_ \(\langle n_1,n_2,n_3\rangle\unknown'\langle r\rangle\).

(i) _If_ \(F_\theta^\star(T)\le F_\theta^\star(S)\) _for all_ \(T,S\in\mathcal{F}\) _with_ \(T\unknown'S\) _and for all_ \(\theta\in\Theta\)_, then_<tbc>

<tbc>\(logr\ge\left\{\begin{array}{ c c }
a+b & \text{\textit{if}}c(a+b)\le ab, \\
\frac{(ab+bc+ca)^2}{4abc} & \text{\textit{if}}c(a+b)>ab,
\end{array}\right.\)<tbc>

<tbc>_where_ \(a\ge b\ge c\) _are the numbers_ log_n_<sub>1</sub>, log_n_<sub>2</sub> _and_ log_n_<sub>3</sub> _in nonincreasing order._<tbc>

(ii) _Suppose n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=_n. If_ \(F_{(\frac{1}{3},\frac{1}{3},\frac{1}{3})}^\star(T)\le F_{(\frac{1}{3},\frac{1}{3},\frac{1}{3})}^\star(S)\) _for all_ \(T,S\in\mathcal{F}\) _with_ \(T\unknown'S\)_, then_ \(r\ge n^{9/4}\).

_Proof._ We compute the values of \(F_\theta^\star\) at \(\langle r\rangle\) and \(\langle n_1,n_2,n_3\rangle\). At the triple (1_,n,n_), Definition 5.5 gives \(F_\theta^\star(1,n,n)=\left(\theta_3+(1-\theta_3)A_3\right)^{p_1}=n^{p_1}\). In the same way, \(F_\theta^\star(n,1,n)=n^{p_2}\) and \(F_\theta^\star(n,n,1)=n^{p_3}\). In particular, \(F_\theta^\star(\langle 1\rangle)=F_\theta^\star(1,1,1)=1\), so \(F_\theta^\star(\langle r\rangle)=r\), and since \(F_\theta^\star\) is multiplicative, \(F_\theta^\star(\langle n_1,n_2,n_3\rangle)=n_1^{p_2}n_2^{p_3}n_3^{p_1}\). So the hypothesis gives, for every \(\theta\) to which it applies (every \(\theta\in\Theta\) in (i), and \(\theta=(\frac{1}{3},\frac{1}{3},\frac{1}{3})\) in (ii)),

\(p_2logn_1+p_3logn_2+p_1logn_3\le logr.\) (5.4)

(i) Renumbering the entries of \(\theta\) renumbers _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> in the same way. Since (5.4) holds for all \(\theta\), it follows that \(ap_2+bp_3+cp_1\le logr\) for all \(\theta\). If _c(a+b)\>ab_, then for the \(\theta\) of Lemma 5.6, \(ap_2+bp_3+cp_1=(ab+bc+ca)^2/(4abc)\), so \((ab+bc+ca)^2/(4abc)\le logr\).

If \(c(a+b)\le ab\), let \(0<\theta_1<1\) and \(\theta_2=\theta_3=(1-\theta_1)/2\). Then \(p_2=p_3=1/(1+\theta_1)\), so \((a+b)/(1+\theta_1)\le logr\), since \(cp_1\ge 0\). Letting \(\theta_1\rightarrow 0\) gives \(a+b\le logr\).

(ii) For \(\theta_1=\theta_2=\theta_3=1/3\), we have _p_<sub>1</sub>=_p_<sub>2</sub>=_p_<sub>3</sub>=3/4, so (5.4) gives \(\frac{9}{4}logn\le logr\), that is, \(n^{9/4}\le r\).

It remains to show monotonicity for the preorder \(\unknown\) as defined in Definition 5.3. We will first prove the basic properties of \(F_\theta^\star\) that we will need for that.

## 5.6 Basic properties of \(F_\theta^\star\)

The following proposition will give the properties of \(F_\theta^\star\) that we will use to prove monotonicity under \(\unknown\). We state it for the tensors P<sub>_x,y,x+y_-1</sub>; since the values of \(F_\theta^\star\) do not change when the legs and the entries of \(\theta\) are renumbered together, it also holds with the legs renumbered. Parts (i)-(iii) correspond to the properties of spectral points in Lemma 4.10, and part (iv) will be used for (D2) and (R).

**Proposition 5.8.** _Let_ \(\theta\in\Theta\)_, and let_ \(p:=p_1=\theta_1(1-\theta_2)^{-1}(1-\theta_3)^{-1}\).

(i) _For all positive integers x, y and z with z=x+y_-1_, we have_ \(min(x,y)\le F_\theta^\star(x,y,z)\le z\)_, and_ \(F_\theta^\star(x,y,x+y-1)\) _is nondecreasing in x and in y._<tbc>

(ii) _For every positive integer x, the function_ \(y\mapsto F_\theta^\star(x,y,x+y-1)^{1/p}\) _on_ \(\mathbb{Z}_{\ge 1}\) _is concave._<tbc>

(iii) _For all positive integers x, y, z with z=x+y_-1_, we have_<tbc>

<tbc>\(2F_\theta^\star(x,y,z)^{1/p}+F_\theta^\star(x,z,y)^{1/p}\le F_\theta^\star(x,2y+z,y+2z)^{1/p}.\)<tbc>


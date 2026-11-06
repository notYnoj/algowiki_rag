<tbc>Proof. We prove that, for any running time _t\>_0, no algorithm _A_ can compute, within _t_ steps, a sequence in which _x_ and _y_ are in the correct relative order with a probability larger than \(1-\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1}\).

First of all, let us focus a deterministic version of algorithm _A_ by fixing a sequence \(\lambda\in\{0,1\}^t\) of random bits that can be used be the algorithm. We call the resulting algorithm \(A_\lambda\), and we let \(p_\lambda\) denote the probability of generating the sequence \(\lambda\) of random bits (i.e., 2<sup>-_t_</sup> if the random bits come from a fair coin).<sup>10</sup> Notice that _A_ might already be a deterministic algorithm, in this case \(A=A_\lambda\) for every \(\lambda\in\{0,1\}^t\).

Consider an instance \(I=\langle\pi,C\rangle\), and let \(\phi_I\) be the permutation of the elements in _S_ returned by \(A_\lambda(I)\), i.e., \(\phi_I(i)=j\) if the element \(i\in S\) is the _j_-th element of the sequence returned by \(A_\lambda\). We define a new instance \(I_{\pi,C}=\langle\pi',C'\rangle\) by "swapping" elements _x_ and _y_ of _I_ along with the results of all their comparisons. More formally we define: \(\pi'(i)=\pi(i)\) for all \(i\in S\backslash\{x,y\}\), \(\pi'(x)=\pi(y)\), and \(\pi'(y)=\pi(x)\); We define the comparison matrix \(C'=(c'_{i,j})_{i,j}\) accordingly, i.e.:

• \(c'_{i,j}=c_{i,j}\) if \(i,j\in S\backslash\{x,y\}\) and _j\>i_,<tbc>

• \(c'_{i,x}=c_{i,y}\) if _i\<x_,<tbc>

• \(c'_{x,j}=c_{y,j}\) if _j\>x_ and \(j\neq y\),<tbc>

• \(c'_{i,y}=c_{i,x}\) if _i\<y_ and \(i\neq x\),<tbc>

• \(c'_{y,j}=c_{x,j}\) if _j\>y_,<tbc>

• \(c'_{x,y}=c_{y,x}\).

<tbc>Letting _R_=(_r<sub>i,j</sub>)<sub>i,j</sub>_ be a random variable over the space of all comparison matrices. Fix a pair _i,j_ with _i\<j_ and observe that \(Pr(r_{i,j}=c'_{i,j})=Pr(r_{i,j}=c_{i,j})\) whenever we are in one of the following cases: (i) \(i\neq x\) and \(j\neq y\), (ii) _i\<x_ and \(j\in\{x,y\}\), or (iii) _j\>y_ and \(i\in\{x,y\}\). In the remaining cases, \(Pr(r_{i,j}=c'_{i,j})=Pr(r_{i,j}=c_{i,j})\cdot\frac{Pr(r_{i,j}=c'_{i,j})}{Pr(r_{i,j}=c_{i,j})}\ge Pr(r_{i,j}=c_{i,j})\cdot\frac{p}{1-p}\). Then, \(Pr(R=C')=Pr(R=C)\cdot\left(\frac{p}{1-p}\right)^{2(y-x)+1}\).

Let \(\widetilde{\pi}\) be a random variable whose value is chosen u.a.r. over all the permutations of _S_. Let Pr(_I_) be the probability that instance \(I=\langle\pi,C\rangle\) is to be solved and notice that \(Pr(I)=Pr(\widetilde{\pi}=\pi)Pr(R=C)\). It follows from the above discussion that \(Pr(I_{\pi,c})\ge Pr(I)\cdot\left(\frac{p}{1-p}\right)^{2(y-x)-1}\).

Let _X<sub>I</sub>_ be an indicator random variable that is 1 if and only if algorithm \(A_\lambda\) on instance _I_ either does not terminate within _t_ steps, or it terminates returning a sequence in which _x_ appears after _y_. Let _U_ be the set of all the possible instances and \(U'\) be the set of the instances \(I\in U\) such that _X<sub>I</sub>_=0 (i.e., _x_ and _y_ appear in the correct order in the output of _A_ on _I_). Notice that there is a bijection between the instances \(I=\langle\pi,C\rangle\) and their corresponding instances \(I_{\pi,C}\) (i.e., our transformation is injective). Moreover, since _I_ and \(I_{\pi,C}\) are indistinguishable by \(A_\lambda\), we have that either (i) \(A_\lambda\) does not terminate within _t_ steps on both instances, or (ii) \(\sigma_I(x)<\sigma_I(y)\Longleftrightarrow\sigma_{I_{\pi,C}}(x)>\sigma_{I_{\pi,C}}(y)\). As a consequence, if _X<sub>I</sub>_=0, then \(X_{I_{\pi,C}}=1\). Now, either \(\sum_{I\in U}X_IPr(I)\ge\frac{1}{2}\) or we must have \(\sum_{I\in U^\prime} Pr(I)\ge\frac{1}{2}\), which implies:

\(\sum_{I\in U}X_IPr(I)\ge\sum_{\langle\pi,C\rangle\in U}X_{I_{\pi,C}}Pr(I_{\pi,C})\ge\sum_{\langle\pi,C\rangle\in U^\prime} X_{I_{\pi,C}}Pr(I_{\pi,C})=\sum_{\langle\pi,C\rangle\in U^\prime} Pr(I_{\pi,C})\)<br>
\(\ge\sum_{I\in U^\prime} Pr(I)\cdot\left(\frac{p}{1-p}\right)^{2(y-x)-1}\ge\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1}.\)

We let _Y_ (resp. \(Y_\lambda\)) be an indicator random variable which is 1 if and only if either the execution of _A_ (resp. \(A_\lambda\)) on a random instance does not terminate within _t_ steps, or it terminates returning a sequence in which _x_ and _y_ appear in the wrong relative order. By the above calculations we know<tbc>

<sup>10</sup>Notice that \(A_\lambda\) can use less than _t_ random bits, but not more (due to the limit on its running time).


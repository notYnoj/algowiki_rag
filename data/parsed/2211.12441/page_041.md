_Proof._

\(\varphi_{X+Y}(t)=\mathbb{E}(e^{it(X+Y)})=\mathbb{E}(e^{itX}e^{itY})=\mathbb{E}(e^{itX})\mathbb{E}(e^{itY})=\varphi_X(t)\varphi_Y(t).\)

Our derivation of the characteristic function \(\varphi_{a,b}\) of _X<sub>a,b</sub>_ is based on a connection between cross inversions and inversions in arrays.

**Fact 57.** _Let A and B be arrays, and let AB be the concatenation of A with B. Then_

\(\mathrm{Inv}(AB)=\mathrm{Inv}(A)+\mathrm{Inv}(B)+\mathrm{XInv}(A,B).\)

_Proof._ Any inversion in _AB_ is either between two elements of _A_, two elements of _B_, or one element of _A_ and one element of _B_. In each case, the inversion is counted in Inv(_A_), Inv(_B_), or XInv(_A,B_), respectively.

Let _X<sub>a</sub>_ be the random variable that counts the number Inv(_A_) of inversions in an array _A_ that is a uniform permutation of \[_a_\], and let \(\varphi_a(t)\) be the characteristic function of _X<sub>a</sub>_.

**Claim 58.** _We have_

\(\varphi_a(t)=\prod_{k=1}^a\left(\frac{e^{it(k-1)}}{k}\cdot\frac{\mathrm{sin}(kt/2)}{\mathrm{sin}(t/2)}\right).\)

_Proof._ Consider the process of placing the elements 1_,...,a_ one by one, each time placing each new element between two elements or on some end of the array, to form an array _A_.

For _k_=1_,...,a_, consider the random variable that counts the number of new inversions formed with _k_ when _k_ is placed. First of all, when _k_ is placed, the number of new inversions is equal to the number of elements to the left of _k_ at the time of placement (only the elements 1_,...,k_-1 have been placed at this point). This means the random variable has a uniform distribution over {0_,...,k_-1}, which we denote by _U_<sub>_k_-1</sub>. Furthermore, this situation applies regardless of the placement of the other elements, so this random variable _U_<sub>_k_-1</sub> is independent from all other previous random variables _U_<sub>_j_-1</sub> with _j\<k_.

Therefore, _X<sub>a</sub>_ can be written as the following sum of independent variables:<tbc>

\(X_a=U_0+\cdots+U_{a-1}.\)

<tbc>We can use Fact 56 to calculate the characteristic function:

\(\varphi_a(t)=\prod_{k=1}^a\mathbb{E}[e^{itU_{k-1}}]=\prod_{k=1}^a\left(\frac{1}{k}\sum_{m=0}^{k-1}e^{itm}\right)=\prod_{k=1}^a\left(\frac{e^{it(k-1)}}{k}\cdot\frac{\mathrm{sin}(kt/2)}{\mathrm{sin}(t/2)}\right)=e^{ia(a-1)/2}\prod_{k=1}^a\left(\frac{1}{k}\cdot\frac{\mathrm{sin}(kt/2)}{\mathrm{sin}(t/2)}\right).\text{(36)}\)

The second-to-last step follows from the geometric sum formula and the identity _e<sup>it</sup>-e_<sup>-_it_</sup>=2sin(_t_), and the last step from the arithmetic sum formula.


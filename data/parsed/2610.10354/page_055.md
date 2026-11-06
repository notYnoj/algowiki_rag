Equation (11) is claimed as in the theorem statement (once we fix the parameter _J_). Equations (10) and (12) involve _A<sub>j</sub>_ rather than _A_; in the following we show that these imply similar statements for _A_.

## Step 3: Relating _H_ to _A_.

To relate _H_ to _A_, we traverse the sets _A=A_<sub>0</sub>_,A_<sub>1</sub>_,...,A<sub>j</sub> backwards_. More precisely, we deduce from \(|A_j\cap(H+x_j)|\ge|A_j|/K_j\) that \(|A_{j-1}\cap(H+x_{j-1})|\ge|A_{j-1}|/K_{j-1}\), for some shifts _x_<sub>_j_-1</sub> and parameters _K_<sub>_j_-1</sub> (we have _x<sub>j</sub>_=0). Indeed, assuming \(|A_j\cap(H+x_j)|\ge|A_j|/K_j\), Property (ii) implies that<tbc>

\(|\{(a_1,a_2)\in A_{j-1}^2:a_1-a_2\in(H+x_j)\}|\ge\Omega_j\big(\frac{|A_{j-1}|^2}{K_j}\big),\)

<tbc>or equivalently,<tbc>

\(\sum_{a\in A_{j-1}}|A_{j-1}\cap(H+x_j+a)|\ge\Omega_j\big(\frac{|A_{j-1}|^2}{K_j}\big).\)

<tbc>In particular, there is some _a_ such that \(|A_{j-1}\cap(H+x_j+a)|\ge\Omega_j(|A_{j-1}|/K_j)\). Choosing _x_<sub>_j_-1</sub>=_x<sub>j</sub>+a_ and _K_<sub>_j_-1</sub>=_O<sub>j</sub>(K<sub>j</sub>_), the claim follows. By induction we learn that

\(|A\cap(H+x_0)|\ge\frac{|A|}{K_0},\) (13)

for some translate _x_<sub>0</sub> and some parameter

\(K_0=O_j(K_j)=O_J(L^{O(1/J)}).\)

Equation (13) is exactly as claimed in the theorem statement, when shifting _H_ by _x_<sub>0</sub>.

## Step 4: Relating _H_ to _B_.

We finally relate _H_ to _B_. Combining Property (i) with Equations (10) and (12) implies that<tbc>

\(|H\cap\mathrm{Sym}(B;\alpha_j)|\ge\frac{|H|}{K_j^2}.\)

<tbc>In particular, by definition of \(\mathrm{Sym}(B;\alpha_j)\) we have<tbc>

\(|\{(b,h)\in B\times H:b+h\in B\}|\ge\frac{\alpha_j}{K_j^2}\cdot|B||H|.\) (14)

<tbc>Let \(\Lambda\subseteq B\) be a random subset, sampled with rate \(p=\mathrm{min}(1,4K_j^2/(\alpha_j|H|))\). Then, with constant probability,

\(|B\cap(H+\Lambda)|\ge\frac{\alpha_j}{4K_j^2}\cdot|B|.\) (15)

To see this, call an element \(b\in B\) _relevant_ if<tbc>

\(r_{B+H}(b)\ge\frac{\alpha_j}{2K_j^2}\cdot|H|.\)


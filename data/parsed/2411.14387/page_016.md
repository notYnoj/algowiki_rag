**Proof.** Let _Y<sub>n</sub>_ be the sequence stated in Theorem 24. First, pad _Y<sub>n</sub>_ so that each key appears _exactly_ |_Y<sub>n</sub>|/n_ times, by adding each key one by one the appropriate number of times, in ascending order. It is easy to see that this maintains the bounds

\(\overline{\text{Alt}}(Y_n)\le O(1)\overline{\text{Funnel}}(Y_n)\ge\Omega(loglogn).\)

Now, let \(C_O,C_\Omega>0\) be constants such that

\(\overline{\text{Alt}}(Y_n)\le C_O\overline{\text{Funnel}}(Y_n)\ge C_\Omega loglogn\)

(we will allow ourselves to make _C<sub>O</sub>_ even larger later on).

Let \(Y_n^{\circ 1}:=Y_n\), and for all power-of-two \(R\ge 1\), let

\(Y_n^{\circ 2R}:=\left(Y_\sqrt{n}^{\circ R}\right)^{\otimes\sqrt{n}}\left(Y_\sqrt{n}^{\circ R},\dots,Y_\sqrt{n}^{\circ R}\right),\)

where "\(X^{\otimes\sqrt{n}}\)" means "_X_ repeated \(\sqrt{n}\) times", and with an abuse of notation we assume that the \(\sqrt{n}\) sequences \(Y_\sqrt{n}^{\circ R},\dots,Y_\sqrt{n}^{\circ R}\) that are being composed each contains a distinct range of keys. We can check that

\(\left|Y_n^{\circ R}\right|=n^{1-1/R}|Y_{n^{1/R}}|\le n^{1-1/R}poly\left(n^{1/R}\right)\le poly(n)\)

as desired. We will show by induction that

\(\overline{\text{Alt}}\big(Y_n^{\circ R}\big)\le C_O(2R-1)\overline{\text{Funnel}}\big(Y_n^{\circ R}\big)\ge C_\Omega\frac{R+1}{2}log\left(\frac{logn}{R}\right).\)

**Base case:** _R_=1.

We verify that indeed

\(\overline{\text{Alt}}(Y_n)\le C_O=C_O(2\cdot 1-1)=C_O(2R-1)\)

and

\(\overline{\text{Funnel}}(Y_n)\ge C_\Omega loglogn=C_\Omega\frac{1+1}{2}log\left(\frac{logn}{1}\right)=C_\Omega\frac{R+1}{2}log\left(\frac{logn}{R}\right).\)

**Inductive case:** \(R\rightarrow 2R\).

Suppose this is true for some \(R\ge 1\), for all _n_. Then for Alt, by Theorem 19 we have

\(\overline{\text{Alt}}\big(Y_n^{\circ 2R}\big)\le\overline{\text{Alt}}\big(Y_\sqrt{n}^{\circ R}\big)+\frac{\sqrt{n}\cdot\overline{\text{Alt}}\big(Y_\sqrt{n}^{\circ R}\big)}{\sqrt{n}}+O(1)\le 2C_O(2R-1)+O(1)=C_O(4R-1)-C_O+O(1)\le C_O(4R-1),\)


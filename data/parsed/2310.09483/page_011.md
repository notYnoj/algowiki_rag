**Algorithm 1** Pivot Phase

1: \(R\leftarrow 0\)

2: \(L\leftarrow 0\)

3: **loop** 8_c_<sub>1</sub>log_N_ times

4: pick a pivot _x<sub>p</sub>_ at random

5: \(Y\leftarrow\{x\in X:x<_cx_p\}\)

6: \(\overline{Y}\leftarrow X\backslash Y\)

7: **if** \(min(|Y|,|\overline{Y}|)\ge\frac{n}{8}\) **then**

8: **return** (_Y,<o>Y</o>_)

9: **else if** \(|Y|<\frac{n}{8}\) **then**

10: \(L\leftarrow L+1\)

11: **else**

12: \(R\leftarrow R+1\)

13: **end if**

14: **end loop**

## 4.1 The Pivot Phase

In this phase, we aim to use a pivot as in quicksort to find the desired partition, in which case we return early. If we do not find such a pivot, the input set has additional structure with high probability, which we will use in the rest of the algorithm.

8_c_<sub>1</sub>log_N_ elements _x<sub>p</sub>_ are randomly chosen and used as pivots. This splits _X_ into two sets _Y_ and <o>_Y_</o> such that \(\overline{Y}\ge_2Y\) by Lemma 3.8. If both of these sets are sufficiently large, then we have found our desired partition, and we return early. Otherwise, if \(|Y|<\frac{n}{8}\) , we say _x<sub>p</sub> goes left_ and if \(|\overline{Y}|<\frac{n}{8}\) , we say _x<sub>p</sub> goes right_. Let _x<sub>L</sub>_ be the _n/_8-th smallest element of _X_ and _x<sub>R</sub>_ the _n/_8-th largest. If _x<sub>p</sub>\>x<sub>L</sub>_+1, then _x<sub>p</sub>_ cannot go left, and symmetrically, if _x<sub>p</sub>\<x<sub>R</sub>_-1, then _x<sub>p</sub>_ cannot go right. Let \(X_L=\{x_p\in X:x_p\le x_L+1\}\) and \(X_R=\{x_p\in X:x_p\ge x_R-1\}\). The elements in \(X\backslash(X_L\cup X_R)\) are thus guaranteed to neither go left or go right. Intuitively, if this set is sufficiently big, we expect to find such a pivot. Otherwise, either _X<sub>L</sub>_ or _X<sub>R</sub>_ must be large. The variables _L_ and _R_ in the code count how many pivots go left and right respectively. Again intuitively, we expect _L\>R_ if _X<sub>R</sub>_ is small and vice versa. These intuitive statements are captured in the following lemmas:

**Lemma 4.1.** _If_ \(|X_L|<\frac{3n}{8}\)_, for any constant r\>_0_, we can choose c_<sub>1</sub> _sufficiently large such that_ \(Pr[L\ge 4c_1logN\) after pivot phase\(]<\frac{1}{N^r}\).

_Proof._ Let _A<sub>i</sub>_ be a random variable that takes value 1 if the _i_th pivot _x<sub>p</sub>_ is in _X<sub>L</sub>_, and 0 otherwise. Note that if _A<sub>i</sub>_ is 0, we cannot increment _L_ in the _i_th iteration, so we have \(L\le A=\sum_iA_i\). Let \(\mu=\mathbb{E}[A]=8c_1logN\frac{|X_L|}{n}\ge c_1logN\). By a Chernoff bound, we have:

\(Pr[L\ge 4c_1logN\text{at line}20]\le Pr[A\ge 4c_1logN]\)<br>
\(=Pr[A\ge(1+\delta)\mu]\)


## 4.3 The Shifting Phase

**Algorithm 3** Shifting Phase

1: Let _P_ be a random permutation of _X_\\_Y_

2: \(i\leftarrow 0\)

3: \(B\leftarrow 4c_3\mathrm{log}N\)

4: **while** \(|Y|<\frac{n}{8}\) **do**

5: \(Z\leftarrow P[i..i+7B)\)

6: Tournament(_Z_)

7: \(Y\leftarrow Y\cup Z[0..B)\)

8: \(i\leftarrow i+7B\)

9: **end while**

10: Let _P_ be a random permutation of _Y_

11: \(i\leftarrow 0\)

12: **while** \(|Y|>\frac{7n}{8}\) **do**

13: \(Z\leftarrow P[i..i+7B)\)

14: \(Z\leftarrow\) Tournament(_Z_)

15: \(Y\leftarrow Y\backslash Z[6B..7B)\)

16: \(i\leftarrow i+7B\)

17: **end while**

18: Let <o>_Y_</o>=_X_\\_Y_

19: **return** (_Y,<o>Y</o>_)

In this phase, if either _Y_ or <o>_Y_</o> is too big, we move some elements to the other set to ensure they both have size \(\ge n/8\). Since the two cases are symmetric, without loss of generality, we assume \(|Y|\le|\overline{Y}|\). We partition <o>_Y_</o> into small subsets, and move the minimum 1/8-th of each subset into _Y_ until \(|Y|\ge n/8\). Since at least 3_n/_8 elements of _X_ are \(\le x_L+1\), at least 1/4-th of the elements in <o>_Y_</o> are \(\le x_L+1\), so even for small subsets we expect the smallest 1/8-th to be all \(\le x_L+1\). Thus, since `Tournament` returns a 2-approximate sorting by Lemma 3.7, we expect the elements we add to _Y_ to be \(\le x_L+3\). These intuitive statements are captured in the following lemmas:

**Lemma 4.7.** _If_ \(|X_L|\ge\frac{3n}{8}\) _and_ \(\mathrm{max}(Y)\le x_L+2\) _after the sample phase, for any constant r\>_0 _we can choose c_<sub>3</sub> _sufficiently large such that after the shifting phase,_ \(\mathrm{Pr}[\mathrm{max}(Y)>x_L+3]<\frac{1}{N^r}\)

_Proof._ Consider some iteration of the loop on line 40. Recall that `Tournament` returns a 2- approximate sorting. Thus, if in each iteration of the loop, _Z_ has at least _B_ elements \(\le x_L+1\), then we are guaranteed to only add elements \(\le x_L+3\) to _Y_ . Since \(|X_L|\ge\frac{3n}{8}\) and \(|Y|<\frac{n}{8}\) , there must be at least \(\frac{n}{4}\) elements \(x\in X\backslash Y\) such that \(x\le x_L+1\). Let _U_ be the set of the \(\frac{n}{4}\) smallest elements of _X_\\_Y_ , breaking ties arbitrarily. Let _A<sub>i</sub>_ be a random variable that takes value 1 if \(Z_i\unknown\in U\) (before sorting), and 0 otherwise. Note that for any subset _S_ of {_A<sub>i</sub>_},

\(\mathrm{Pr}\left[\wedge_{i\in S}A_i\right]=\mathrm{Pr}[A_{S_0}]\mathrm{Pr}[A_{S_1}|A_{S_0}]\dots\mathrm{Pr}\big[A_{S_{|S|}}|A_{S_0},\dots,A_{S_{|S|-1}}\big]\le\frac{3}{4}\frac{\frac{3|X\backslash Y|}{4}-1}{|X\backslash Y|-1}\cdots\frac{\frac{3|X\backslash Y|}{4}-|S|}{|X\backslash Y|-|S|}\le\left(\frac{3}{4}\right)^{|S|}.\)


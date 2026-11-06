Where \(\delta=\frac{n}{2|X_L|}-1>\frac{1}{3}\)

\(\le e^{-\frac{\delta^2\mu}{2+\delta}}\)<br>
\(<e^{-\frac{\mu}{21}}\)<br>
\(\le e^{-logN\frac{c_1}{21}}\)<br>
\(=N^{-\frac{c_1}{21}}\)

Thus, choosing \(c_1\ge 21r\), we get

\(Pr[L\ge 4c_1logN\text{at line}20]<\frac{1}{N^r}.\)

**Corollary 4.2.** _If_ \(|X_R|<\frac{3n}{8}\)_, for any constant r\>_0_, we can choose c_<sub>1</sub> _sufficiently large such that_ \(Pr[R\ge 4c_1logN\) after pivot phase\(]<\frac{1}{N^r}\).

_Proof._ Symmetric.

Throughout the rest of the analysis, we will assume \(L\ge R\). The other case is handled symmetrically.

## 4.2 The Sample Phase

**Algorithm 2** Sample Phase

1: \(Y\leftarrow\emptyset\)

2: **for** \(x_i\in X\) **do**

3: \(C\leftarrow 0\)

4: **loop** 8_c_<sub>2</sub>log_N_ times

5: Choose \(z\in X\) at random

6: **if** _z\<<sub>c</sub>x<sub>i</sub>_ **then**

7: \(C\leftarrow C+1\)

8: **end if**

9: **end loop**

10: **if** _C\<_2_c_<sub>2</sub>log_N_ **then**

11: \(Y\leftarrow Y\cup\{x_i\}\)

12: **end if**

13: **end for**

In this phase, for each element _x<sub>i</sub>_ we estimate its position in the sorted array by comparing it to a small subset of _X_. All elements with estimated position less than \(\frac{n}{4}\) are put in set _Y_ and the remaining elements are put in <o>_Y_</o>. Since \(|X_L|\ge\frac{3n}{8}\) , all elements with positions between \(\frac{n}{8}\) and \(\frac{3n}{8}\) are in \[_x<sub>L</sub>,x<sub>L</sub>_+1\]. Thus, since all elements _\<x<sub>L</sub>_-1 compare less than all of these elements, we intuitively expect them to have estimated position less than \(\frac{n}{4}\) even on a small subset. Similarly, since all elements _\>x<sub>L</sub>_+2 compare greater than all of those elements, we intuitively expect them to have estimated position greater than \(\frac{n}{4}\). These statements are captured in the following lemmas:

**Lemma 4.3.** _If_ \(|X_L|\ge\frac{3n}{8}\)_, for any constant r\>_0 _we can choose c_<sub>2</sub> _sufficiently large such that_<tbc>

\(Pr[\exists x_i<x_L-1:C\ge 2c_2logN]<\frac{1}{N^r}.\)


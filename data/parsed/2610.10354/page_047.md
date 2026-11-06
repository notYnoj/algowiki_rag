**Theorem 1.11** (Bounded Monotone Min-Plus Convolution)**.** _Min-Plus Convolution between an arbitrary sequence and a monotone sequence bounded by_ \[_n_\] _cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

**Proof.** By Lemma 6.3, it suffices to reduce the problem of computing the Min-Plus Convolution between \(A\in[\sqrt{n}]^{[0,n]}\) and \(B\in[\sqrt{n}]^{[0,\sqrt{n}]}\) to bounded-monotone Min-Plus Convolution. By padding, we can assume \(\sqrt{n}\) is an integer for convenience.

We first carefully split _A_ to two halves _A_<sup>odd</sup> and _A_<sup>even</sup>, where

\(A^\mathrm{odd}[i]=\left\{\begin{array}{ c c }
A[i] & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is odd}, \\
\infty & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is even},
\end{array}\right.A^\mathrm{even}[i]=\left\{\begin{array}{ c c }
\infty & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is odd}, \\
A[i] & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is even}.
\end{array}\right.\)

It suffices to separately compute _A_<sup>odd</sup>∗_B_ and _A_<sup>even</sup>∗_B_, and combine the results. As the methods are essentially the same for these two Min-Plus Convolutions, we focus on computing _C_<sup>odd</sup>=_A_<sup>odd</sup>∗_B_.

Create sequences \(A'\in\mathbb{Z}^{[0,n]}\) and \(B'\in\mathbb{Z}^{[0,n]}\), where<tbc>

\(A'[i]=\left\{\begin{array}{ c c }
A[i]+\sqrt{n}\cdot(i\mathrm{mod}\sqrt{n}) & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is odd}, \\
10n & \text{if}\lfloor i/\sqrt{n}\rfloor\text{is even},
\end{array}\right.B'[j]=\left\{\begin{array}{ c c }
B[j]+\sqrt{n}\cdot j & \text{if}j\le\sqrt{n}, \\
10n & \text{otherwise}.
\end{array}\right.\)

<tbc>By definition, all entries of \(A',B'\) are non-negative integers in _O(n_). Moreover, observe that \(B'\) is monotone. Hence, we can use a bounded-monotone Min-Plus Convolution algorithm to compute \(C'=A'*B'\). First, observe that \(C^\mathrm{odd}[k]=\infty\) if and only if \(C'[k]\ge 10n\). Now consider the case where \(C'[k]<10n\). In this case,

\(C'[k]=\mathrm{min}_{0\le j\le\mathrm{min}\{k,\sqrt{n}\}\lfloor(k-j)/\sqrt{n}\rfloor\mathrm{odd}}\left\{A'[k-j]+B'[j]\right\}\)<br>
\(=\mathrm{min}_{0\le j\le\mathrm{min}\{k,\sqrt{n}\}\lfloor(k-j)/\sqrt{n}\rfloor\mathrm{odd}}\left\{A[k-j]+B[j]+((k-j)\mathrm{mod}\sqrt{n}+j)\cdot\sqrt{n}\right\}\)

We can simplify the term \((k-j)\mathrm{mod}\sqrt{n}+j\) via

\((k-j)\mathrm{mod}\sqrt{n}+j=k-j-\lfloor(k-j)/\sqrt{n}\rfloor\cdot\sqrt{n}+j=k-\lfloor(k-j)/\sqrt{n}\rfloor\cdot\sqrt{n}.\)

Because \(0\le j\le\sqrt{n}\), \(\lfloor(k-j)/\sqrt{n}\rfloor\in[\lfloor(k-\sqrt{n})/\sqrt{n}\rfloor,\lfloor k/\sqrt{n}\rfloor]\). Notice that there are exactly two integer values in this range. Combined with the condition that \(\lfloor(k-j)/\sqrt{n}\rfloor\) is odd, there can actually be only one valid value, which can be computed in _O_(1) time. Once \(\lfloor(k-j)/\sqrt{n}\rfloor\) is determined, we can compute \(k-\lfloor(k-j)/\sqrt{n}\rfloor\cdot\sqrt{n}\), and we denote this value by _f_<sub>odd</sub>(_k_). Hence, we can further simplify the expression for \(C'[k]\) as

\(C'[k]=\mathrm{min}_{0\le j\le\mathrm{min}\{k,\sqrt{n}\}\lfloor(k-j)/\sqrt{n}\rfloor\mathrm{odd}}\left\{A[k-j]+B[j]+f_\mathrm{odd}(k)\cdot\sqrt{n}\right\}\)<br>
\(=\left(f_\mathrm{odd}(k)\cdot\sqrt{n}\right)+\mathrm{min}_{0\le j\le\mathrm{min}\{k,\sqrt{n}\}\lfloor(k-j)/\sqrt{n}\rfloor\mathrm{odd}}\left\{A[k-j]+B[j]\right\}\)<br>
\(=\left(f_\mathrm{odd}(k)\cdot\sqrt{n}\right)+C^\mathrm{odd}[k].\)

Hence, we can compute _C_<sup>odd</sup> from \(C'\) in linear time, which completes the proof.


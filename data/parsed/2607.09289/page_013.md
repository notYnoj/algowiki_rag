## 5.1 Overview of the tradeoffs

We first give an overview of the case distinction in  1. For each range of the space-bound parameter \(\alpha\), the table indicates which lemma or theorem is applied for each range of the minimum solution ratio \(\ell'\), together with the bottleneck value of \(\ell'\) in that case. By the time-complexity exponent function of a lemma or theorem, we mean the function \(f(\ell',\alpha)\) such that, under the space bound \(O^*(2^{\alpha n})\), the claimed time complexity is \(O^*(2^{f(\ell^\prime,\alpha)n})\). The space complexity of Lemma 3.9 is bounded by _O_<sup>∗</sup>(3<sup>_n/_4</sup>). Thus, when \(\frac{\mathrm{log}3}{4}<2-\mathrm{log}3\le\alpha\), we have \(O^*(3^{n/4})\le O^*(2^{\alpha n})\), and hence Lemma 3.9 satisfies the space bound \(O^*(2^{\alpha n})\). The other theorems used in  1 explicitly state their time complexities under the space bound \(O^*(2^{\alpha n})\).

Here, \(\alpha_1\) is defined by (7) and satisfies \(0.64737<\alpha_1<0.64738\).

The value \(\alpha_2\) is defined as the value of \(\alpha\in[0.45,1/2]\) for which there exists \(\ell'\in(1/2,0.8)\) such that the three time-complexity exponent functions from Lemma 3.9 and Theorems 5.2 and 5.9 all take the same value at \(\ell'\). Numerically, we have \(0.49211<\alpha_2<0.49212\).

Similarly, \(\alpha_3\) is defined as the value of \(\alpha<1/4\) for which there exists \(\ell'>1/2\) such that the three time-complexity exponent functions from Theorems 5.9, 5.12 and 5.14 all take the same value at \(\ell'\). Numerically, we have \(0.18686<\alpha_3<0.18687\).

Finally, \(\alpha_4\) is defined as the value of \(\alpha<\alpha_3\) for which there exists \(\ell'\) such that the three time-complexity exponent functions from Theorems 4.2, 5.9 and 5.14 all take the same value at \(\ell'\). Numerically, we have \(0.12285<\alpha_4<0.12286\).

For each \(i\in[7]\), the value \(\ell'_i(\alpha)\) in  1 denotes the value of \(\ell'>1/2\) at which the two corresponding time-complexity exponent functions intersect. The corresponding pairs are as follows:

• \(\ell'_1(\alpha)\): Lemma 3.9 and Theorem 5.1, for \(1/2<\alpha\le\alpha_1\).<tbc>

• \(\ell'_2(\alpha)\): Lemma 3.9 and Theorem 5.2, for \(\alpha_2<\alpha\le 1/2\).<tbc>

• \(\ell'_3(\alpha)\): Lemma 3.9 and Theorem 5.9, for \(2-\mathrm{log}3<\alpha\le\alpha_2\).<tbc>

\begin{tabular}{cccc}
Range of \(\alpha\) & \multicolumn{3}{c}{Range of \(\ell'\)} & Worst \(\ell'\) \\
\(1/2<\alpha\le\alpha_1\) & \(\ell'\in(0,1/2]\cup(\ell'_1(\alpha),1]\) & \(\ell'\in(1/2,\ell'_1(\alpha)]\) & \(\ell'_1(\alpha)\) \\
 & Lemma 3.9 & Theorem 5.1 & \\
\(\alpha_2<\alpha\le 1/2\) & \(\ell'\in(0,1/2]\cup(\ell'_2(\alpha),1]\) & \(\ell'\in(1/2,\ell'_2(\alpha)]\) & \(\ell'_2(\alpha)\) \\
 & Lemma 3.9 & Theorem 5.2 & \\
\(2-\mathrm{log}3<\alpha\le\alpha_2\) & \(\ell'\in(0,1/2]\cup(\ell'_3(\alpha),1]\) & \(\ell'\in(1/2,\ell'_3(\alpha)]\) & \(\ell'_3(\alpha)\) \\
 & Lemma 3.9 & Theorem 5.9 & \\
\(\frac{2}{3}(\mathrm{log}3-1)<\alpha\le\) & \multicolumn{3}{c}{\(\ell'\in(0,1]\)} & \multirow{2}{*}{2/3} \\
2-log3 & \multicolumn{3}{c}{Theorem 5.12} & \\
\(\frac{1}{4}<\alpha\le\frac{2}{3}(\mathrm{log}3-1)\) & \(\ell'\in(0,1/2]\cup(\ell'_4(\alpha),1]\) & \(\ell'\in(1/2,\ell'_4(\alpha)]\) & \(\ell'_4(\alpha)\) \\
 & Theorem 5.12 & \multicolumn{2}{c}{Theorem 5.9} \\
\(\alpha_3<\alpha\le 1/4\) & \(\ell'\in(0,1-2\alpha]\) & \(\ell'\in(1-2\alpha,\ell'_5(\alpha)]\) & \(\ell'\in(\ell'_5(\alpha),1]\) & \(\ell'_5(\alpha)\) \\
 & Theorem 4.2 & Theorem 5.9 & Theorem 5.12 & \\
\(\alpha_4<\alpha\le\alpha_3\) & \(\ell'\in(0,1-2\alpha]\) & \(\ell'\in(1-2\alpha,\ell'_6(\alpha)]\) & \(\ell'\in(\ell'_6(\alpha),1]\) & \(\ell'_6(\alpha)\) \\
 & Theorem 4.2 & Theorem 5.9 & Theorem 5.14 & \\
\(0\le\alpha\le\alpha_4\) & \multicolumn{2}{c}{\(\ell'\in(0,\ell'_7(\alpha)]\)} & \multicolumn{2}{c}{\(\ell'\in(\ell'_7(\alpha),1]\)} & \(\ell'_7(\alpha)\) \\
 & Theorem 4.2 & \multicolumn{2}{c}{Theorem 5.14} & \\
\end{tabular}

1: Case distinction by \(\alpha\) and \(\ell'\).


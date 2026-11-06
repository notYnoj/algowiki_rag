\((0,\phi_1,0,\dots,0,\phi_m,0)\) and, subsequently, apply the classic algorithm of Gilbert and Moore \[9\] to construct an alphabetic code _C_ for the distribution \(\nu'=(0,\phi_1,0,\dots,0,\phi_m,0)\). The average length of the constructed code is less than \(H(\nu')+2=H(\phi)+2\). Successively, the authors prune the binary tree representing the alphabetical code _C_ and show that the average length of the new code so obtained satisfies the upper bound (5). The codeword lengths associated with the null probabilities are left unspecified in \[4\], while for non-null probabilities the codeword lengths are equal to \(\lceil-log_2\phi_i\rceil+1\), as it is required in the algorithm by Gilbert and Moore.

Next, we uncover the problematic issue in the analysis claimed in \[4\] by a numeric example. Successively, in Lemma 4 of the Appendix B, we generalize our example to an infinite number of cases.

Let \(\phi=(\phi_1,\phi_2,\phi_3)=\left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)\) and \(\nu'\) be its fully extended distribution \(\left(0,\frac{1}{2},0,\frac{1}{4},0,\frac{1}{4},0\right)\). As said above, the length of the codeword produced by the algorithm of Gilbert and Moore for the symbol of probability \(\phi_1\) is equal to \(\lceil-log_2\phi_1\rceil+1=2\), the length of the codeword produced for the symbol of probability \(\phi_2\) is equal to 3, and the length of the codeword produced for the symbol of probability \(\phi_3\) is equal to 3. However, we will show that there does not exist any alphabetic code for \(\nu'\) with lengths of the codewords

\(L=\langle f_1,\dots,f_7\rangle=\langle x_1,2,x_2,3,x_3,3,x_4\rangle,\) (19)

for _any_ choice of the codewords length \(x_1,x_2,x_3,x_4\in\mathbb{N}_+\) associated to the symbols of null probability.

Let us start with the choice _x_<sub>1</sub>=2 and _x_<sub>2</sub>=_x_<sub>3</sub>=_x_<sub>4</sub>=3. It is immediate to verify that in such a case sum(_L,_7)=1. Therefore, by Theorem 1 there cannot exist an alphabetic code with the chosen lengths. In fact:

\(\begin{array}{ c c }
\text{sum}(L,2)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,1))+2^{-2}=2^{-2} \\
\text{\texttt{sum}}(L,3)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,2))+2^{-2}=2^{-1} \\
\text{\texttt{sum}}(L,4)=\text{\texttt{trunc}}(3,\text{\texttt{sum}}(L,3))+2^{-3}=2^{-1}+2^{-3} \\
\text{\texttt{sum}}(L,5)=\text{\texttt{trunc}}(3,\text{\texttt{sum}}(L,4))+2^{-3}=2^{-1}+2^{-2} \\
\text{\texttt{sum}}(L,6)=\text{\texttt{trunc}}(3,\text{\texttt{sum}}(L,5))+2^{-3}=2^{-1}+2^{-2}+2^{-3} \\
\text{\texttt{sum}}(L,7)=\text{\texttt{trunc}}(3,\text{\texttt{sum}}(L,6))+2^{-3}=2^{-1}+2^{-2}+2^{-2} \\
=1.
\end{array}\)

Similarly, if we increase the lengths _x<sub>i</sub>_, the value of the function `sum` remains the same, since the values of \(\alpha_i=min(f_{i-1},f_i)\) do not change. If we decrease the lengths _x<sub>i</sub>_, considering all possible combinations, we can also verify that the value of `sum` remains greater than or equal to 1. In fact, let us take for example _x_<sub>1</sub>=1, _x_<sub>2</sub>=_x_<sub>3</sub>=2 and _x_<sub>4</sub>=3, we have that:

\(\begin{array}{ c c }
\text{sum}(L,2)=\text{\texttt{trunc}}(1,\text{\texttt{sum}}(L,1))+2^{-1}=2^{-1} \\
\text{\texttt{sum}}(L,3)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,2))+2^{-2}=2^{-1}+2^{-2} \\
\text{\texttt{sum}}(L,4)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,3))+2^{-2}=2^{-1}+2^{-2}+2^{-2} \\
=1 \\
\text{\texttt{sum}}(L,5)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,4))+2^{-2}=2^{-1}+2^{-2}+2^{-2} \\
+2^{-2}=1.25 \\
\text{\texttt{sum}}(L,6)=\text{\texttt{trunc}}(2,\text{\texttt{sum}}(L,5))+2^{-2}=2^{-1}+2^{-2}+2^{-2} \\
+2^{-2}+2^{-2}=1.5 \\
\text{\texttt{sum}}(L,7)=\text{\texttt{trunc}}(3,\text{\texttt{sum}}(L,6))+2^{-3}=2^{-1}+2^{-2}+2^{-2} \\
+2^{-2}+2^{-2}+2^{-3}=1.625.
\end{array}\)

Therefore, by Theorem 1 there cannot exist an alphabetic code with lengths (19).

We now present our new results for alphabetic codes. We will divide our analysis into two cases: The first is about dyadic distributions, the second case is for everything else. We recall that a dyadic distribution \(\phi=(\phi_1,\dots,\phi_m)\) is a probability distribution where each \(\phi_i\) is equal to 2<sup>-_k<sub>i</sub>_</sup>, for suitable integers _k<sub>i</sub>\>_0.

**Theorem 2.** _For any dyadic probability distribution_ \(\phi=(\phi_1,\dots,\phi_m)\) _on the symbols_ \(s_1\prec\cdots\prec s_m\)_, we can construct in linear time an alphabetic code C with_

\(\mathbb{E}[C]\le H(\phi)+1-\phi_1-\phi_m.\) (20)

_Proof._ The idea of the proof is simple and is based on Yeung’s analysis \[29, Thm. 5\]. Yeung proved that, given a probability distribution \(\phi=(\phi_1,\dots,\phi_m)\), there exists an alphabetic code _C_ for \(\phi\) with lengths of the codewords \(L=\langle\ell_1,\dots,\ell_m\rangle\) equal to:

\(\ell_i=\left\{\begin{array}{ c c }
\left\lceil-log_2\phi_i\right\rceil & \text{if either}i=1\text{or}i=m, \\
\left\lceil-log_2\phi_i\right\rceil+1 & \text{otherwise.}
\end{array}\right.\)

S4
S10
S9
S3
S1
S2
S8
S7
S5
S6
S4
S10
S3
S9
S1
S2
S8
S7
S5
S6

Figure 1. The alphabetic trees constructed on the list of lengths \(L=\langle 6,6,5,2,9,8,6,3,2\rangle\). On the left the tree constructed by taking the first \(\ell_i\) bits of the binary expansion of sum(_L,i_), (according to Nakatsu \[25\]), on the right the tree constructed by our algorithm ConstructTree(_L_).


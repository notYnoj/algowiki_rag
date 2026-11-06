Proof. For a proof by contradiction, pick an element \(c:=(i,k,C_{i,k}^\square)\in\mathrm{core}(C)\) violating the claim. Let \((i,j_A,A_{i,j_A}^\square):=a:=f_A(c)\) and \((j_B,k,B_{j_B,k}^\square):=b:=f_B(c)\). We make four symmetric arguments (all illustrated in Figure 1), with the first one presented in more detail.

**1.** Since _c_ is not the minimal core element in \(f_A^{-1}(a)\), we have \(f_A(c')=a\) for some core element \((i',k',C_{i^\prime,k^\prime}^\square):=c'\in\mathrm{core}(C)\) that precedes _c_ in the lexicographical order, denoted \(c'\prec c\). Due to \(f_A(c')=a=(i,j_A,A_{i,j_A}^\square)\), we must have \(i'=i\) and \(j_A<\mathcal{W}_{i+1,k^\prime+1}^{A,B}\). Since \(i'=i\), then \(c'\prec c\) implies \(k'+1\le k\). The monotonicity of the witness matrix (Lemma 3.4) thus yields \(\mathcal{W}_{i+1,k^\prime+1}^{A,B}\le\mathcal{W}_{i+1,k}^{A,B}\). Overall, we conclude that \(j_A<\mathcal{W}_{i+1,k}^{A,B}\).

**2.** Since _c_ is not the maximal core element in \(f_A^{-1}(a)\), we have \(f_A(c')=a\) for some core element \(c'\succ c\). In particular, \(c'=(i,k',C_{i,k^\prime}^\square)\in\mathrm{core}(C)\) for some \(k'>k\). Then, \(\mathcal{W}_{i,k+1}^{A,B}\le\mathcal{W}_{i,k^\prime}^{A,B}\le j_A\) follows from Lemma 3.4 and \(f_A(c')=a\), respectively.

**3.** Since _c_ is not the minimal core element in \(f_B^{-1}(b)\), we have \(f_B(c')=b\) for some core element \(c'\prec c\). In particular, \(c'=(i',k,C_{i^\prime,k}^\square)\in\mathrm{core}(C)\) for some \(i'<i\). Then, \(\mathcal{W}_{i,k+1}^{A,B}\ge\mathcal{W}_{i^\prime+1,k+1}^{A,B}>j_B\) follows from Lemma 3.4 and \(f_B(c')=b\), respectively.

**4.** Since _c_ is not the maximal core element in \(f_B^{-1}(b)\), we have \(f_B(c')=b\) for some core element \(c'\succ c\). In particular, \(c'=(i',k,C_{i^\prime,k}^\square)\in\mathrm{core}(C)\) for some \(i'>i\). Then, \(\mathcal{W}_{i+1,k}^{A,B}\le\mathcal{W}_{i^\prime,k}^{A,B}\le j_B\) follows from Lemma 3.4 and \(f_B(c')=b\), respectively.

Overall, we derive a contradiction: \(j_A<\mathcal{W}_{i+1,k}^{A,B}\le j_B<\mathcal{W}_{i,k+1}^{A,B}\le j_A\). \(\triangleleft\)

As every core element of _C_ is either the first or the last one in some pre-image under _f<sub>A</sub>_ or _f<sub>B</sub>_, we get that \(\delta(C)\le 2\cdot(\delta(A)+\delta(B))\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Example 3.8.** Note that the inequality for the core size from Theorem 1.1 is weaker than the inequality for the core sum from Lemma 3.5. We claim that this weakening is not an artifact of our proof. Consider the following Monge matrices

\(A=\left(\begin{array}{ c c c c }
0 & 4 & 5 & 6 \\
0 & 1 & 2 & 3 \\
0 & 1 & 2 & 0 \\
0 & 1 & 2 & 0
\end{array}\right),B=\left(\begin{array}{ c c c c }
0 & 2 & 4 & 6 \\
0 & 0 & 2 & 4 \\
0 & 0 & 0 & 2 \\
0 & 0 & 0 & 0
\end{array}\right),C=\left(\begin{array}{ c c c c }
0 & 2 & 4 & 6 \\
0 & 1 & 2 & 3 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right).\)

We have \(C=A\otimes B\), \(\delta(A)=2\), \(\delta(B)=3\), and \(6=\delta(C)>\delta(A)+\delta(B)>\mathrm{min}\{\delta(A),\delta(B)\}\).

\(\blacktriangleright\) Remark 3.9. To the best of our knowledge, Theorem 1.1 shows the first bound on the core size of \(A\otimes B\) in terms of the core sizes of _A_ and _B_. Previously, such a bound was only known for unit-Monge matrices \[45\]. In particular, our bound allows simplifying some time complexities of already existing algorithms. For example, \[38, Lemma 18\] shows how to compute the product of two explicitly given Monge matrices _A_ and _B_ in time \(\mathcal{O}(p\mathrm{log}q+q\mathrm{log}r+\delta(A\otimes B)\mathrm{log}q\mathrm{log}r+(\delta(A)+\delta(B))\mathrm{log}^2q)\). Assuming that \(r\in\mathrm{poly}(q)\), Theorem 1.1 tells us that we can drop the third summand in the time complexity.

## 4 Core-Sparse Monge Matrix Min-Plus Multiplication Algorithm

In this section, we present an algorithm that, given the condensed representations of two Monge matrices, computes the condensed representation of their (min,+)-product. Even though the condensed representation itself does not provide efficient random access to the values of the matrix, the following fact justifies our choice of the representation of Monge matrices.


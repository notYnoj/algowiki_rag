Then, indeed, _U_ has |K|_q=r_ columns (and _V_ has |K|_q=r_ rows), and by construction we have that<tbc>

\(R[i,j]=\tilde{C}[i,j]+z\)<br>
\(=\lfloor\tilde{C}[i,j]/q\rfloor\cdot q+((\tilde{C}[i,j]+z)modq)\)<br>
\(=R_1[i,j]\cdot q+(R[i,j]modq)\)<br>
\(=U_1[i,S_1[i,j]]\cdot q+(R[i,j]modq)+V_1[S_1[i,j],j]\cdot q\)<br>
\(=U[i,S[i,j]]+V[S[i,j],j],\)

for all non-\(\perp\) entries. Hence, (_U,V,S_) is a valid rank-_r_ decomposition of _R_.<tbc>

<tbc>_Running Time:_ \(\tilde{O}(n_1n_2+n_1n_3+n_2n_3)\) (negligible).<tbc>

2.4. Solve the _r_-Rank Exact Triangle instance (_A,B,R_), and additionally report a witness _k_ for each output entry (_i,j_) by Lemma 5.2. Update \(C[i,j]\leftarrow min\{C[i,j],A[i,k]+B[k,j]\}\) for each such triple.<tbc>

<tbc>_Running Time:_ \(\tilde{O}(\text{ExactTri}(n_1,n_2,n_3|r))\).

We argue that these steps correctly assign all popular entries _C_\[_i,j_\]. In steps 2.1 and 2.2 we construct a matrix _R_<sub>1</sub> satisfying that (_A_<sub>1</sub>∗_B_<sub>1</sub>)\[_i,j_\]=_R_<sub>1</sub>\[_i,j_\] for all popular pairs (since, as noted before, K contains a pseudo-witness with high probability). Let \(z\in\{0,1,2\}\) be such that \((A*B)[i,j]=\tilde{C}[i,j]+z\). Recalling \(\lfloor(A*B)[i,j]/q\rfloor=(A_1*B_1)[i,j]\), it follows that \(\lfloor(\tilde{C}[i,j]+z)/q\rfloor=R_1[i,j]\). We therefore set \(R[i,j]=\tilde{C}[i,j]+z=(A*B)[i,j]\), and thus (_i,j_) is involved in an exact triangle in the instance (_A,B,R_). It follows that we list a witness _k_ of (_i,j_) and correctly assign _C_\[_i,j_\] in step 2.4.

This completes the algorithm and the correctness proof, and we finally analyze the running time. Summing over the contributions of all steps (analyzed in the boxes), the total time indeed becomes

\(\tilde{O}\big(\text{MinPlus}(n_1,n'_2,n_3|u\le n'_2)\cdot\frac{n_2t}{n'_2}+\text{ExactTri}(n_1,n_2,n_3|r\le u/t)\big),\)

where we have bounded \(p=O(n'_2)\) and \(r=r_1q=\tilde{O}(n'_2/t\cdot u/n'_2)=\tilde{O}(u/t)\). (Moreover, here we have omitted the negligible overhead of \(\tilde{O}(n_1n_2+n_1n_3+n_2n_3)\) for the various bookkeeping steps as this time is necessarily dominated by the ExactTri(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>) call simply to read the input.) Finally, each recursive call reduces _u_ by a constant factor. Thus, the recursion reaches depth at most _O_(log_u_)=_O_(log(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)) and we incur an overhead that is hidden in the \(\tilde{O}\) notation.

**Corollary 5.4.** _Let_ \(0<\alpha\le 1\) _and_ \(\epsilon>0\) _be constants. If_ \(\text{MinPlus}(n,n^\alpha,n|u\le n^\alpha)=O(n^{2+\alpha-\epsilon})\) _then the Strong APSP Hypothesis fails._

**Proof.** Suppose that \(\text{MinPlus}(n,n^\alpha,n|u\le n^\alpha)=O(n^{2+\alpha-\epsilon})\) for some \(\epsilon>0\). Theorem 4.1 states that \(\text{ExactTri}(n,n,n|r\le n^{3-\omega-\epsilon/2})\le O(n^{3-\epsilon/500000})\). Thus, from Lemma 5.3 with _n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=_n_, \(n'_2=n^\alpha\), and \(t=n^{\epsilon/2}\) we get that

\(\text{MinPlus}(n,n,n|u\le n^{3-\omega})\)<br>
\(=\tilde{O}\big(\text{MinPlus}(n,n^\alpha,n|u\le n^\alpha)\cdot n^{1-\alpha+\epsilon/2}+\text{ExactTri}(n,n,n|r\le n^{3-\omega-\epsilon/2})\big)\)<br>
\(=\tilde{O}\big(n^{2+\alpha-\epsilon}\cdot n^{1-\alpha+\epsilon/2}+n^{3-\epsilon/500000}\big)\)<br>
\(=\tilde{O}\big(n^{3-\epsilon/500000}\big).\)

This contradicts the Strong APSP Hypothesis.


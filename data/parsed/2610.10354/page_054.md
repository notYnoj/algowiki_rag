Hence, Lemma 7.2 yields a set \(A_1\subseteq D=Sym(B;\alpha/2)\) that directly satisfies both Properties (i) and (ii).

Now focus on the inductive case, i.e., let \(j\ge 1\), assume that _A<sub>j</sub>_ has already been constructed, and focus on the construction of _A_<sub>_j_+1</sub>. By (i) we have \(A_j\subseteq Sym(B;\alpha_j)\). Apply Lemma 7.3 with \(\alpha_j\) and sets _B,A<sub>j</sub>_, yielding that<tbc>

\(|\{(a_1,a_2)\in A_j^2:a_1-a_2\in Sym(B;\alpha_j^2/2)\}|\ge\frac{\alpha_j^2|A_j|^2}{2}.\)

<tbc>Next, apply Lemma 7.2 with parameter \(\alpha_{j+1}=\alpha_j^2/2\) on the sets \(A_j,Sym(B;\alpha_{j+1})\) to construct a set \(A_{j+1}\subseteq Sym(B;\alpha_{j+1})\) satisfying, for all \(x\in A_{j+1}\),

\(r_{A_j-A_j}(x)=\Omega\left(\frac{\alpha_j}{1+log\frac{1}{\alpha_j}+log(1+\frac{|Sym(B;\alpha_{j+1})|}{|A_j|})}\cdot\frac{|A_j|^2}{|A_{j+1}|}\right)=\Omega_j\left(\frac{|A_j|^2}{|A_{j+1}|}\right).\)

In the last step we used that \(|A_j|=\Omega_j(|A|)\) (by (iii)) and \(|Sym(B;\alpha_{j+1})|\le|B|/\alpha_{j+1}\); taken together these imply that \(log(1+|Sym(B;\alpha_{j+1})|/|A_j|)\) can be hidden in the \(\Omega_j\) notation. Evidently, the set _A_<sub>_j_+1</sub> satisfies both Properties (i) and (ii), completing the construction.

## Step 2: Constructing _H_ by the BSG Theorem.

Take \(0\le j<J\) minimizing |_A_<sub>_j_+1</sub>|/|_A<sub>j</sub>_|. Recall that |_A_<sub>0</sub>|=|_A_| and that \(|A_J|\le|Sym(B;\alpha_J)|\le|B|/\alpha_J=O_J(|B|)\) by Property (i). Thus, writing _L_=1+|_B|/|A_|, we must have<tbc>

\(|A_{j+1}|=O_J\big(L^{1/J}\cdot|A_j|\big).\)

<tbc>Moreover, Property (ii) implies that

\(E(A_j)=\sum_{x\in A_j-A_j}r_{A_j-A_j}(x)^2\)<br>
\(\ge\sum_{x\in A_{j+1}}r_{A_j-A_j}(x)^2\)<br>
\(=\Omega_j\big(\frac{|A_j|^4}{|A_{j+1}|}\big)\)<br>
\(=\Omega_J\big(\frac{|A_j|^3}{L^{1/J}}\big).\)

In this situation, the symmetric BSG theorem (Theorem 2.3) applies, yielding some _K<sub>j</sub>=O<sub>J</sub>(L_<sup>_O_(1_/J_)</sup>) and a set _H_ with

\(|H|\le K_j|A_j|,\) (10)

and

\(|H+H|\le K_j|H|,\) (11)

and

\(|A_j\cap H|\ge\frac{|A_j|}{K_j}.\) (12)


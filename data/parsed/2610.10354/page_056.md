Equation (14) entails that there must be at least \(\alpha_j/2K_j^2\cdot|B|\) relevant elements. But each relevant item is not covered in \(H+\Lambda\) with probability at most \((1-p)^{\frac{\alpha_j}{2K_j^2\cdot|H|}}\) . When _p_=1, this trivially equals 0; otherwise,<tbc>

\((1-p)^{\frac{\alpha_j}{2K_j^2\cdot|H|}}\le exp(-p\cdot\frac{\alpha_j}{2K_j^2}\cdot|H|)\le exp(-2)<\frac{1}{4}.\)

<tbc>By Markov’s inequality, with probability at least 1/2, at least half the relevant elements are covered by \(H+\Lambda\). This proves Equation (15). At the same time, \(\Lambda\) satisfies the following size bound with high probability:

\(|\Lambda|\le O\left(\frac{K_j^2}{\alpha_j}\cdot\frac{|B|}{|H|}\right).\) (16)

### Wrapping Up.

All in all, Equations (11), (13), (15) and (16) are as claimed in Theorem 2.4; it only remains to choose appropriate parameters. All these equations have an overhead of the form _O<sub>J</sub>(L_<sup>_O_(1_/J_)</sup>), i.e.,<tbc>

\(C(J)\cdot\alpha^{-C(J)}\cdot L^{C_0/J}\cdot(logL)^{C(J)},\)

<tbc>for some absolute constant _C_<sub>0</sub> and some constant _C(J_) depending on _J_. Choosing \(J>C_0/\epsilon\), this overhead indeed takes the form

\(K=O_\epsilon(\alpha^{-O_\epsilon(1)}L^\epsilon).\)

The proof of Theorem 2.4 is complete.

## 7.3 Efficient Algorithm

In this section we finally argue that the previous proof can be implemented by an efficient algorithm, running in time \(\widetilde{O}((|A|+|B|)K)\) for some \(K\le O_\epsilon(\alpha^{-O_\epsilon(1)}L^\epsilon)\). To this end, we revisit the four steps from before and comment on their implementations.

### Step 1: Iteratively Smoothing _A_.

In the first step we explicitly compute the sets _A_<sub>1</sub>_,...,A<sub>J</sub>_. This step is already almost completely algorithmic. Each set _A_<sub>_j_+1</sub> is constructed by one call to Lemma 7.2 on input _A<sub>j</sub>_ and \(D=Sym(B;\alpha_{j+1})\); the only problem is that we do not have access to \(Sym(B;\alpha_{j+1})\). Instead, we will compute some superset<tbc>

\(Sym(B;\alpha_{j+1})\subseteq D\subseteq Sym(B;\alpha_{j+1}/2)\)

<tbc>by Lemma 3.3 in time \(\widetilde{O}(|B|/\alpha_{j+1})\). This leaves the correctness unchanged. The running time of Lemma 7.2 can then be bounded by

\(\widetilde{O}\left(|A_j|+\frac{|D|}{\alpha_{j+1}}\right)=\widetilde{O}\left(\frac{|B|}{\alpha_{j+1}^2}\right).\)

The total time of step 1 is dominated by the final iteration, \(\widetilde{O}(|B|/\alpha_J^2)\), which is within the budget.<tbc>


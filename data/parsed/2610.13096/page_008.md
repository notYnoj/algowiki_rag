_Proof._ Let _J=V_\\_I_. By Theorem 2, the bipartite graph consisting of the edges between _I_ and _J_ has a perfect matching. Fix any such matching _M_.

We first prove the forward implication. Let _S_ be any small blocking set and define<tbc>

\(A=S\cap I,B=S\cap J.\)

<tbc>Then \(S=A\cup B\) and \(A\cap B=\varnothing\). Since _S_ is independent, there are no edges between _A_ and _B_. Write

\(N_I(B)=N(B)\cap I.\)

The perfect matching assigns a distinct matched vertex in _J_ to every vertex of _A_, so \(|N(A)|\ge|A|\). None of these matched vertices belongs to _B_, since otherwise _S_ would contain an edge. Similarly, each vertex of _B_ has a distinct matched vertex in _I_, giving \(|N_I(B)|\ge|B|\).

Because \(A\subseteq I\) and _I_ is independent, \(N(A)\subseteq J\). On the other hand, \(N_I(B)\subseteq I\). These two neighborhood sets are therefore disjoint, and both are subsets of _N(S_). Consequently,<tbc>

\(|N(S)|\ge|N(A)|+|N_I(B)|\ge|A|+|B|=|S|.\)

<tbc>Since _S_ is a blocking set, |_N(S_)|=|_S_|, so equality holds throughout this chain. In particular,

\(|N(A)|=|A|,|N_I(B)|=|B|.\)

We now distinguish whether \(S\cap I\) is empty.

**Case 1:** \(S\cap I\neq\varnothing\)**.** Set \(T=A=S\cap I\). Since \(T\subseteq I\), the set _T_ is independent. The equality above gives |_N(T_)|=|_T_|. Furthermore,

\(0<|T|\le|S|<\frac{n}{2}=|I|,\)

so \(\varnothing\neq T\unknown I\). Thus, _T_ is a nonempty proper tight subset of _I_.

**Case 2:** \(S\cap I=\varnothing\)**.** Here \(S=B\subseteq J\), and the equality above gives |_N<sub>I</sub>(S_)|=|_S_|. Since<tbc>

\(N_I(S)\subseteq N(S),|N(S)|=|S|,\)

<tbc>we obtain _N<sub>I</sub>(S_)=_N(S_) and hence \(N(S)\subseteq I\). Let<tbc>

\(C=N(S),T=I\backslash C.\)


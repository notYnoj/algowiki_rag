## A Reduction from SAT to kMin-IP with rank 2<sup>_O_(log<sup>∗</sup>_n_)</sup>

In this section, we reduce SAT to kMin-IP with rank 2<sup>_O_(log<sup>∗</sup>_n_)</sup>. Our reduction proceeds as follows:

\(\includegraphics{}\)

It is well-known that SAT reduces to OV \[Wil05\]. The same proof can be used to give a reduction from SAT to kOV, which we include here for completeness.

**Lemma A.1.** (SAT \(\rightarrow\mathsf{kOV}_{n,O(\mathrm{log}n)}\))_. Suppose there exists an algorithm for_ kOV<sub>_n,O_(log_n_)</sub> _with running time_ \(O(n^{k-\varepsilon})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kSAT _with running time_ \(2^{(1-\delta)n}\cdot\mathrm{poly}(n)\) _for some_ \(\delta>0\)_, thus refuting_ SETH.

_Proof._ For a kSAT formula \(\varphi\) with _n_ variables and _m_ clauses, partition the variables _x_<sub>1</sub>_,...,x<sub>n</sub>_ into _k_ subsets each with _n/k_ variables:<tbc>

\(S_1=\{x_1,\dots,x_\frac{n}{k}\},\dots,S_k=\{x_{n-\frac{n}{k}+1},\dots,x_n\}.\)

<tbc>For each \(1\le i\le k\), let \(A_i=\{\alpha:S_i\rightarrow\{0,1\}\}\). Therefore, |_A<sub>i</sub>_|=2<sup>_n/k_</sup> for all \(1\le i\le k\). For each \(\alpha\in A_i\), construct a vector \(v_\alpha\in\{0,1\}^m\) such that

\(V_\alpha[i]=\left\{\begin{array}{ c c }
0 & \text{if}\alpha\text{satisfies clause}i \\
1 & \text{otherwise.}
\end{array}\right.\)

For each clause, \(\alpha\) gives a partial assignment to it. If that assignment already makes the clause true, then \(v_\alpha[i]=0\). Let \(Y_i=\{v_\alpha:\alpha\in A_i\}\), then |_Y<sub>i</sub>_|=2<sup>_n/k_</sup> for all _i_. Now notice that there exists _y<sub>i,j<sub>i</sub></sub>_ such that 〈_y_<sub>1_,j_<sub>1</sub></sub>_,...,y<sub>k,j<sub>k</sub></sub>_〉=0 if and only if \(\varphi\) is satisfiable.

Therefore running kOV<sub>_n,O_(log_n_)</sub> on _Y_<sub>1</sub>_,...,Y<sub>k</sub>_ will tell us whether \(\varphi\) is satisfiable or not. The running time of this algorithm is \((2^{n/k})^{k-\varepsilon}\cdot\mathrm{poly}(m)=2^{(1-\delta)n}\cdot\mathrm{poly}(n)\).

To give a reduction from kOV<sub>_n,O_(log_n_)</sub> to Z-kOV<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub>, we need the following results.


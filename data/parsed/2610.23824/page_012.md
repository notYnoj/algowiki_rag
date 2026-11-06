**Algorithm 1** COLORING_<sub>k</sub>(n_): An algorithm to color an _n_-vertex graph online.

1: \(\lambda\leftarrow\frac{1}{6kln(3k)lnn+2}\)

2: \(m\sim\text{Binomial}(n,\frac{1}{2})\)

3: Color the first _m_ vertices with COLORING_<sub>k</sub>(m_), if \(m\ge 1\)

4: \(S\leftarrow\) the set of the first _m_ vertices

5: \(A_1\leftarrow S;r\leftarrow 1\)

6: **loop**

7: \(I_r\leftarrow\mathsf{IS}_\lambda(G[A_r])\)

8: **if** \(I_r=\emptyset\) **then**

9: **break**

10: \(A_{r+1}\leftarrow N_{A_r}(I_r)\)

11: \(r\leftarrow r+1\)

12: \(J_1,\dots,J_r\leftarrow\emptyset\)

13: **for** each arrival of the remaining vertices \(v\in V^*\backslash S\) **do**

14: \(i\leftarrow\) the smallest _i_ such that \(N_{I_i}(v)=\emptyset\)

15: \(J_i\leftarrow J_i\cup\{v\}\), and color _v_ using First-Fit on _G_\[_J<sub>i</sub>_\]

**Lemma 15.** \(r\le n+1\).

_Proof._ Since Algorithm 1 ensures that \(I_1,\dots,I_{r-1}\neq\emptyset\) and _A_<sub>_i_+1</sub>=_N<sub>A<sub>i</sub></sub>(I<sub>i</sub>_) contains no vertex of _I<sub>i</sub>_ for each _i_, it follows that \(A_1\unknown\cdots\unknown A_r\). Since \(|A_1|\le n\), we have \(r\le n+1\). □

**Lemma 16.** _Suppose that_ \(\lambda\in(0,1]\)_. For all possible inputs of the first m vertices,_<tbc>

\(Pr[r\le 6kln(3k)lnn+2]\ge 1-\frac{1}{n}.\)

<tbc>_Proof._ Fix an arbitrary realization of _A<sub>i</sub>_. By applying Lemma 12 to _G_\[_A<sub>i</sub>_\], we have

\(\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G[A_i])}[|A_{i+1}|]=\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G[A_i])}[|N_{A_i}(I)|]\)<br>
\(\le\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G[A_i])}[|I\cup N_{A_i}(I)|]\)<br>
\(\le\left(1-\frac{1}{3kln(3k)}\right)|A_i|.\)

Taking expectations over _A<sub>i</sub>_, we obtain \(\mathbb{E}[|A_{i+1}|]\le\left(1-\frac{1}{3kln(3k)}\right)\mathbb{E}[|A_i|]\). Since \(|A_1|\le n\),

\(\mathbb{E}[|A_{i+1}|]\le\left(1-\frac{1}{3kln(3k)}\right)^i\cdot n.\)

Since \((1-\frac{1}{x})^x<\frac{1}{e}\) for all \(x\ge 1\), we have \(\mathbb{E}[|A_{i^*+1}|]\le\frac{1}{n}\) with \(i^*:=\lceil 3kln(3k)\cdot 2lnn\rceil\). Since \(|A_{i^*+1}|\) is a non-negative integer, Markov’s inequality implies that _A_<sub>_i_<sup>∗</sup>+1</sub> is empty with probability at least \(1-\frac{1}{n}\). Moreover, if _A_<sub>_i_<sup>∗</sup>+1</sub> is empty, then _I_<sub>_i_<sup>∗</sup>+1</sub> is also empty, meaning that \(r\le i^*+1\). Therefore, \(r\le 6kln(3k)lnn+2\) with probability at least \(1-\frac{1}{n}\). □


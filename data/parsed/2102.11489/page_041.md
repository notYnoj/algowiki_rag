• \(\mathbf{SP}_{i+1}\Longrightarrow\mathbf{LC}_{i+1}\) (**Theorem 10.1**): from approximate splitter to lossy loose compactor. Simplifying Theorem 10.1 we have:<tbc>

<tbc>Fix some \(\alpha\in(0,1)\). Assuming that for any \(\beta\in(0,1/4]\), \((\alpha,\beta,n,w)\)-approximate splitter can be realized in a circuit with the following cost for some constant _C_sp and function _f(n_):<tbc>

\(\text{\# generalized boolean gates :}C_\mathrm{sp}\cdot n\cdot f(n)\)<br>
\(\text{\# selector gates :}C_\mathrm{sp}\cdot n\)<br>
\(\text{depth :}D_\mathrm{sp}(n)\)

Then there exists a \((1.74\alpha,n,w)\)-lossy loose compactor such that:<tbc>

\(\text{\# generalized boolean gates :}2.07\cdot C_\mathrm{sp}\cdot n\cdot f(f(n))+O_4(n)\)<br>
\(\text{\# selector gates :}2.07\cdot C_\mathrm{sp}\cdot n\)<br>
\(\text{depth :}2.07\cdot D_\mathrm{sp}(n)+O_5(\mathrm{log}f(n))\)

Choose \(C_0:=\widetilde{C}+1\). Our starting point is Theorem 8.1, which gives as a circuit **LC**<sub>0</sub> that realizes (1/log<sup>_C_<sub>0</sub></sup>_n,n,w_)-lossy loose compaction for the constant _C_<sub>0</sub>_\>_1. Using the above two steps, we bootstrap and boost the circuit:

**LC**<sub>0</sub>: By Theorem 8.1, there exists a constant _C\>_1 such that we can solve (1/log<sup>_C_<sub>0</sub></sup>_n,n,w_)-lossy loose compaction with<tbc>

\(\text{generalized boolean gates :}Cn\mathrm{loglog}n\)<br>
\(\text{selector gates :}Cn\)<br>
\(\text{depth :}C\mathrm{loglog}n\)

<tbc>**SP**<sub>1</sub>: By Theorem 9.3, for any \(\beta\in(0,1/4]\), we can construct an \((8/\mathrm{log}^{C_0}n,\beta,n,w)\)-approximate splitter circuit **SP**<sub>1</sub> from **LC**<sub>0</sub>. **SP**<sub>1</sub>’s size is upper bounded by the expressions<sup>8</sup>:<tbc>

\(\text{generalized boolean gates :}2.5Cn\mathrm{log}n+10Cn+O_1(n)\le 5.1Cn\mathrm{log}n\)<br>
\(\text{selector gates :}5Cn+O_2(n)\le 5.1Cn\)<br>
\(\text{depth :}2.4C_0\mathrm{loglog}n\cdot(C\mathrm{loglog}n+O_3(1))\le 2.5C_0\mathrm{loglog}n\cdot(C\mathrm{loglog}n)\)

<tbc>In the above, the inequalities hold as long as _n_ is greater than an appropriately large constant.<tbc>

<tbc>**LC**<sub>1</sub>: Due to Theorem 10.1, we build a \((8\cdot 1.74/\mathrm{log}^{C_0}n,n,w)\) lossy loose compaction circuit **LC**<sub>1</sub> from **SP**<sub>1</sub>. **LC**<sub>1</sub>’s size is upper bounded by the expressions:<tbc>

\(\text{generalized boolean gates :}2.07\cdot 5.1Cn\mathrm{loglog}n+O_4(n)\le 2.1\cdot 5.1Cn\mathrm{loglog}n\)<br>
\(\text{selector gates :}2.07\cdot 5.1Cn\le 2.1\cdot 5.1Cn\)<br>
\(\text{depth :}2.07\cdot(2.5C_0\mathrm{loglog}n)\cdot(C\mathrm{loglog}n)+O_5(\mathrm{loglog}n)\)<br>
\(\le 2.1\cdot(2.5C_0\mathrm{loglog}n)\cdot(C\mathrm{loglog}n)\)

<tbc>**SP**<sub>2</sub>: Due to Theorem 9.3, for any \(\beta\in(0,1/4]\), we can construct a \((8^2\cdot 1.74/\mathrm{log}^{C_0}n,\beta,n,w)\)- approximate splitter circuit **SP**<sub>2</sub> from **LC**<sub>1</sub>. **SP**<sub>2</sub>’s size is upper bounded by the expressions:<tbc>

\(\text{generalized boolean gates :}2.5\cdot 2.1\cdot 5.1Cn\mathrm{loglog}n+10\cdot 2.1\cdot 5.1Cn+O_1(n)\le 2.1\cdot(5.1)^2Cn\mathrm{loglog}n\)<br>
\(\text{selector gates :}5\cdot 2.1\cdot 5.1Cn+O_2(n)\le 2.1\cdot(5.1)^2Cn\)<br>
\(\text{depth :}2.4C_0\mathrm{loglog}n\cdot(2.1\cdot(2.5C_0\mathrm{loglog}n)\cdot(C\mathrm{loglog}n)+O_3(1))\)<br>
\(\le 2.1\cdot(2.5C_0\mathrm{loglog}n)^2\cdot(C\mathrm{loglog}n)\)

<sup>8</sup> When _w\>_loglog_n_, **LC**<sub>0</sub> gives Theorem 11.1. Therefore, the rest of this section assumes \(w\le\mathrm{loglog}n\).


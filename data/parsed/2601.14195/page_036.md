Formally, let _B_ be a (2,2)-e3-sat instance with variables _V_={_V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>n</sub>_} and clauses _C_={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>m</sub>_}. Without loss of generality, we can assume that \(n\ge 3\). We will construct an smi instance \(J=(A,\succ)\) from _B_, where the set of agents _A_ has size

\(|A|=\left\lceil\frac{8}{3}\left(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3}\right)\right\rceil.\) (1)

The set _A_ consists of the disjoint union of agents

\(A_v=\{x_i^r,y_i^r;1\le i\le n\wedge 1\le r\le 4\},\)<br>
\(A_c=\{c_j^s,p_j^s;1\le j\le m\wedge 1\le s\le 3\}\cup\{q_j,z_j;1\le j\le m\},\text{and}\)<br>
\(A_t=\{t_{i,\gamma}^{\beta,k};1\le i\le n\wedge 1\le\gamma\le\gamma_*\wedge 1\le\beta\le 4\wedge 1\le k\le 12\}\)

from the variable, clause, and connector gadgets (where \(\gamma_*=2(\left\lfloor|A|^{1/2}\right\rfloor+1)\). We also have some remaining agents _A<sub>r</sub>_ due to rounding in the floor and ceiling operations. We remark that, although the instance _J_ contains a large number of agents |_A_|, the construction of _J_ remains polynomial in the size of _B_.

The following intuition may help understand the number of agents in Equation 1: every one of the _n_ variable gadgets contributes 8 agents, every one of the _m_ clause gadgets contributes 8 agents, and every variable gadget will be incident to four sets of \(\gamma_*=2(\left\lfloor|A|^{1/2}\right\rfloor+1)\) connector gadgets, each contributing 12 agents. We determined \(\gamma_*\) to achieve the desired inapproximability result in the construction, as will become clear at the end of the proof. We already noted in a previous reduction that _B_ has a lot of structure and that \(m=\frac{4}{3}n\). _A<sub>r</sub>_ acts as a garbage collector for unnecessary agents created due to rounding issues, as will become clear below. Putting this information together, we have

\(|A|=|A_v|+|A_c|+|A_t|+|A_r|\)<br>
\(=8n+8m+4\cdot 12\cdot n\cdot\gamma_*+|A_r|\)<br>
\(=8\left(n+\frac{4}{3}n\right)+48\cdot n\cdot 2\left(\left\lfloor|A|^{1/2}\right\rfloor+1\right)+|A_r|\)<br>
\(=\frac{56}{3}n+96n\left(\left\lfloor|A|^{1/2}\right\rfloor+1\right)+|A_r|\)

Then, as an intermediary step, we solve the equation \(x=\frac{56}{3}n+96n(x^{1/2}+1)\) for _x_, which yields the function \(x(n)=\frac{8}{3}(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3})\). Here, even when \(n\in\mathbb{N}\), _x(n_) might not be an integer value. Hence, we take the ceiling of this function to arrive at the size of _A_ that we specified in Equation 1. Now, we can calculate \(\gamma_*\) explicitly from |_A_|, i.e.,

\(\gamma_*=2\left(\left\lfloor|A|^{1/2}\right\rfloor+1\right)\)<br>
\(=2\left(\left\lfloor\sqrt{\left\lceil\frac{8}{3}\left(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3}\right)\right\rceil}\right\rceil+1\right),\)

and thus

\(|A_t|=48\cdot n\cdot\gamma_*\)<br>
\(=96n\left(\left\lfloor\sqrt{\left\lceil\frac{8}{3}\left(1728n^2+43n+24\sqrt{6}\sqrt{864n^4+43n^3}\right)\right\rceil}\right\rceil+1\right).\)


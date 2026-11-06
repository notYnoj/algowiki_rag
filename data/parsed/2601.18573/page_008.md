Our reduction is similar to that of Biró et al. \[8\] from (2,2)-e3-sat to _k_-BP-AlmostStable- Perfect-smi, but the preference lists of the \(p_j^s\)-agents and our overall analysis differ.

Formally, consider a (2,2)-e3-sat instance _B_ with _n_ variables _V_={_V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>n</sub>_} and _m_ clauses _C_={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>m</sub>_}. Below, we show how to derive an smi instance \(I=(A,\succ)\) from _V_ and _C_. In the construction, _A_ will consist of subsets \(A_v=\{x_i^r,y_i^r;1\le i\le n\wedge 1\le r\le 4\}\) (from the variable gadgets) and \(A_c=\{c_j^s,p_j^s;1\le j\le m\wedge 1\le s\le 3\}\cup\{q_j,z_j;1\le j\le m\}\) (from the clause gadgets). The total number of agents of _I_ is 8(_n+m_).

We will now show how to construct _I_ in full detail. First, for each variable \(V_i\in V\) , we construct a **variable gadget** _G<sub>V<sub>i</sub></sub>_ consisting of the eight agents \(x_i^1,x_i^2,x_i^3,x_i^4,y_i^1,y_i^2,y_i^3,y_i^4\), with the following preference lists:<tbc>

\(x_i^1:y_i^1c(x_i^1)y_i^2y_i^1:x_i^1x_i^4\)<br>
\(x_i^2:y_i^2c(x_i^2)y_i^3y_i^2:x_i^1x_i^2\)<br>
\(x_i^3:y_i^4c(x_i^3)y_i^3y_i^3:x_i^2x_i^3\)<br>
\(x_i^4:y_i^1c(x_i^4)y_i^4y_i^4:x_i^3x_i^4\)

<tbc>where we will specify the \(c(x_i^r)\) entries later. Figure 1 illustrates this construction. Importantly, a _G<sub>V<sub>i</sub></sub>_ gadget admits exactly two perfect matchings: the matchings<tbc>

\(M_{V_i}^1=\{\{x_i^1,y_i^1\},\{x_i^2,y_i^2\},\{x_i^3,y_i^3\},\{x_i^4,y_i^4\}\}\text{and}\)<br>
\(M_{V_i}^2=\{\{x_i^1,y_i^2\},\{x_i^2,y_i^3\},\{x_i^3,y_i^4\},\{x_i^4,y_i^1\}\}.\)

<tbc>Notice that \(bp(M_{V_i}^1)\cap\mathbb{P}_2(A_v)=\{\{x_i^3,y_i^4\}\}\) and \(bp(M_{V_i}^2)\cap\mathbb{P}_2(A_v)=\{\{x_i^1,y_i^1\}\}\), where P<sub>2</sub>(_A<sub>v</sub>_) is the set of unordered pairs of agents in _A<sub>v</sub>_, i.e., we are not considering any blocking pairs that involve \(c(x_i^r)\) agents. Intuitively, \(M_{V_i}^1\) and \(M_{V_i}^2\) correspond to _V<sub>i</sub>_ being true or false, respectively.<tbc>

\(c_j^1:p_j^1x(c_j^1)q_jp_j^1:z_jc_j^1\)<br>
\(c_j^2:p_j^2x(c_j^2)q_jp_j^2:z_jc_j^2\)<br>
\(c_j^3:p_j^3x(c_j^3)q_jp_j^3:z_jc_j^3\)<br>
\(z_j:p_j^1p_j^2p_j^3q_j:c_j^1c_j^2c_j^3\)

<tbc>Now, for each clause \(C_j=(C_j^1\vee C_j^2\vee C_j^3)\in C\), we construct a corresponding **clause gadget** _G<sub>C<sub>j</sub></sub>_. A clause gadget consists of eight agents \(c_j^1,c_j^2,c_j^3,p_j^1,p_j^2,p_j^3,q_j,z_j\), with the following preference lists:

1
1
1
1
1
3
3
2
2
1
1
2
2
3
3
3
3
1
2
3
1
1
4
4
1
1
4
3
2
2
4
4
4

Figure 1: Illustration of the variable gadget construction


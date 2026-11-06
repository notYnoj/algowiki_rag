<tbc>marriage, the optimization of several aggregation functions has been investigated.<br>
\- Utilitarian approach: \(\sum_{i=1}^n\text{\textbf{rk}}(m_i,\mu_\text{\textbf{x}}(m_i))+\sum_{j=1}^n\text{\textbf{rk}}(w_j,\mu_\text{\textbf{x}}(w_j))\), which can be min imized in _O(n_<sup>3</sup>) \[Feder, 1994\]).<br>
\- Egalitarian approach: \(max\{\text{\textbf{rk}}(p,\mu_\text{\textbf{x}}(p)):p\in\mathcal{M}\cup\mathcal{W}\}\), which can also be minimized in _O(n_<sup>2</sup>) \[Gusfield, 1987\].<br>
\- Sex-equal stable marriage: \(|\sum_{i=1}^n\text{\textbf{rk}}(m_i,\mu_\text{\textbf{x}}(m_i))-\sum_{j=1}^n\text{\textbf{rk}}(w_j,\mu_\text{\textbf{x}}(w_j))|\), the min imization of which is NP-hard \[Kato, 1993\].<br>
\- Balanced stable marriage: \(max\{\sum_{i=1}^n\text{\textbf{rk}}(m_i,\mu_\text{\textbf{x}}(m_i)),\sum_{j=1}^n\text{\textbf{rk}}(w_j,\mu_\text{\textbf{x}}(w_j))\}\), the min imization of which is NP-hard \[Manlove, 2013\].

Our contribution differs with previous works on the fair stable marriage problem. Indeed, we optimize a generalized Gini index on disutility values.

Given a matching **x**, the _disutility d(m<sub>i</sub>,_**x**) (also called _dissatisfaction_) of a man _m<sub>i</sub>_ is defined by \(d(\text{\textbf{rk}}(m_i,\mu_\text{\textbf{x}}(m_i)))\), where \(d:\mathbb{N}\rightarrow\mathbb{Q}^+\), is a strictly increasing function called disutility function. The disutility values _d(w<sub>j</sub>,_**x**) are defined similarly for women. Every stable marriage induces therefore a disutility vector:

\(\text{\textbf{d}}(\text{\textbf{x}})=(d(m_1,\text{\textbf{x}}),\dots,d(m_n,\text{\textbf{x}}),d(w_1,\text{\textbf{x}}),\dots,d(w_n,\text{\textbf{x}}))\)

with _N_=2_n_ components. Note that the use of disutility values (often called weights) is a common way to extend the traditional framework where the aggregation function is applied on rank values (see e.g., Teo and Sethuraman \[1998\]; Gusfield and Irving \[1989\]). Using a unique disutility function for all agents guarantees that they all have the same importance in the aggregation operation. Indeed, the disutility values assigned to the ranks do not depend on the agent’s identity. Note that both the egalitarian and the utilitarian variants of the stable marriage problem remain polynomially solvable if one uses disutility values.

**Example 5** _We come back to Example 1. Let d be the disutility function defined by d(i_)=(_i_-1)<sup>2</sup>_, then the disutility values are given by the matrices d<sub>M</sub> and d<sub>W</sub> below where d<sub>M</sub>_\[_i_\]\[_j_\] _(resp. d<sub>W</sub>_\[_j_\]\[_i_\]_) is the disutility of m<sub>i</sub> (resp. w<sub>j</sub>) if he (resp. she) is matched with w<sub>j</sub> (resp. m<sub>i</sub>)._

\(d_M:\left(\begin{array}{ c c c c c c c c c c c c c }
0 & 1 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
1 & 0 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
1 & 4 & 0 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
1 & 4 & 9 & 25 & 36 & 16 & 0 & 49 & 64 & 81 \\
1 & 4 & 9 & 25 & 36 & 0 & 16 & 49 & 64 & 81 \\
1 & 4 & 9 & 0 & 16 & 36 & 25 & 49 & 64 & 81 \\
1 & 4 & 9 & 16 & 0 & 36 & 25 & 49 & 64 & 81 \\
36 & 49 & 64 & 1 & 4 & 9 & 25 & 0 & 81 & 16 \\
36 & 49 & 64 & 1 & 25 & 4 & 9 & 81 & 16 & 0 \\
36 & 49 & 64 & 1 & 4 & 25 & 9 & 16 & 0 & 81
\end{array}\right)d_W:\left(\begin{array}{ c c c c c c c c c c c }
0 & 1 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
0 & 1 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
0 & 1 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 \\
0 & 1 & 4 & 49 & 64 & 36 & 9 & 16 & 25 & 81 \\
0 & 1 & 4 & 49 & 64 & 9 & 36 & 16 & 25 & 81 \\
0 & 1 & 4 & 9 & 36 & 49 & 64 & 16 & 25 & 81 \\
0 & 1 & 4 & 36 & 9 & 49 & 64 & 16 & 25 & 81 \\
16 & 0 & 25 & 36 & 49 & 64 & 9 & 4 & 81 & 1 \\
0 & 1 & 16 & 25 & 36 & 49 & 64 & 81 & 4 & 9 \\
0 & 1 & 4 & 9 & 16 & 25 & 36 & 64 & 81 & 49
\end{array}\right)\)

Let **d**=(_d_<sub>1</sub>_,...,d<sub>N</sub>_) denote a disutility vector. The generalized Gini index \[Weymark, 1981\] is defined as follows:

**Definition 1** _Let_ \(\lambda=(\lambda_1,\dots,\lambda_N)\) _be a vector of weights such that_ \(\lambda_1\ge\dots\ge\lambda_N\)_. The_ \(\mathtt{GGI}_\lambda(\cdot)\) _aggregation function induced by_ \(\lambda\) _is defined by:_

\(\mathtt{GGI}_\lambda(\text{\textbf{d}})=\sum_{i=1}^N\lambda_id_i^\unknown,\)


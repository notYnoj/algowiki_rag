## 3.1 A 3-DSR-ML instance not admitting a stable matching

Subsequently, we present a 3DSR-ML-Sets instance I<sub>instable</sub> with six agents not admitting a stable matching, showing that stable matchings do not have to exist even in the presence of master lists. This somewhat surprising observation will be crucial for our NP-hardness proof in Section 3.2.

The instance I<sub>instable</sub> has six agents _a_, _b_, _c_, _d_, _e_, and _f_. The master list is: \(\{a,b\}\succ\{a,c\}\succ\{a,d\}\succ\{a,f\}\succ\{b,e\}\succ\{c,d\}\succ\{a,e\}\succ\{b,f\}\succ\{c,e\}\succ\{b,d\}\succ\{d,e\}\succ\{b,c\}\succ\{c,f\}\succ\{d,f\}\succ\{e,f\}\).

**Observation 3.1.** _Instance_ I<sub>instable</sub> _does not admit a stable matching._

_Proof._  2 presents for each of the \(\frac{\genfrac(){pt}{2}{6}{3}}{2}=10\) matchings a blocking 3-set.

## 3.2 NP-completeness of 3-DSR-ML

Using the instance I<sub>instable</sub> from Section 3.1, we show NP-completeness of 3DSR-ML-Sets, reducing from the NP-complete problem 1-in-3 Positive 3-Occurrence-SAT \[20\].

The basic idea of the reduction is the following. For each clause _C<sub>j</sub>_, we have two agents _c<sub>j</sub>_ and _d<sub>j</sub>_. For each variable _x<sub>i</sub>_, we have three agents \(x_i^1,x_i^2,\) and \(x_i^3,\) one for each occurrence of the variable. Additionally, there are six agents \(z_i^{k,\ell},\ell\in[6],\) for each literal of a clause. In any stable matching the agents _c<sub>j</sub>_ and _d<sub>j</sub>_ are matched to an agent \(x_i^\ell\) corresponding to a variable occurring in clause _C<sub>j</sub>_. Now consider a variable _x<sub>i</sub>_. If agent \(x_i^k\) (corresponding to the _k_-th occurrence of _x<sub>i</sub>_) is matched to a 2-set {_c<sub>j</sub>,d<sub>j</sub>_} (corresponding to clause _C<sub>j</sub>_) for all \(k\in[3],\) then a stable matching can match \(\{z_i^{k,1},z_i^{k,2},z_i^{k,3}\}\) and \(\{z_i^{k,4},z_i^{k,5},z_i^{k,6}\}\). If agent \(x_i^k\) (corresponding to occurrences of variable _x<sub>i</sub>_) is not matched to a 2-set {_c<sub>j</sub>,d<sub>j</sub>_} (corresponding to clause _C<sub>j</sub>_) for all \(k\in[3],\) then we can match \(\{x_1^i,x_2^i,x_3^i\}\) and then again match \(\{z_i^{k,1},z_i^{k,2},z_i^{k,3}\}\) and \(\{z_i^{k,4},z_i^{k,5},z_i^{k,6}\}\). If, however, agent \(x_i^k\) is matched to a 2-set of the form {_c<sub>j</sub>,d<sub>j</sub>_} for one or two values of _k_, then an agent \(x_i^j\) which is not matched to a 2-set {_c<sub>j</sub>,d<sub>j</sub>_} will together with \(z_i^{k,1},z_i^{k,2},z_i^{k,3},z_i^{k,4},\) and \(z_i^{k,5}\) form a subinstance of six agents which does not admit a stable matching, and, thus, the resulting matching will not be stable.

\begin{tabular}{cc}
Matching & Blocking 3-set \\
{_a,b,c},{d,e,f_} & {_a,d,e_} \\
{_a,b,d},{c,e,f_} & {_a,c,e_} \\
{_a,b,e},{c,d,f_} & {_b,c,d_} \\
{_a,b,f},{c,d,e_} & {_a,c,d_} \\
{_a,c,d},{b,e,f_} & {_a,b,e_} \\
\end{tabular}

\begin{tabular}{cc}
Matching & Blocking 3-set \\
{_a,c,e},{b,d,f_} & {_a,b,e_} \\
{_a,c,f},{b,d,e_} & {_a,b,e_} \\
{_a,d,e},{b,c,f_} & {_a,b,e_} \\
{_a,d,f},{b,c,e_} & {_a,b,e_} \\
{_a,e,f},{b,c,d_} & {_a,c,d_} \\
\end{tabular}

1-in-3 Positive 3-Occurrence-SAT
Input: A boolean formula in conjunctive normal form, where each clause contains exactly three pairwise different variables, and each variable appears exactly three times and only non-negatedly in the formula.
Task: Decide whether there exists a truth assignment satisfying exactly one literal from each clause.

2: A blocking 3-set for each matching in instance I<sub>instable</sub> from Observation 3.1.


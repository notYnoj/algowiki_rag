**Algorithm 2** Translating instances

**Input:** An instance _I_ for MAX SMTI-1TM.

**Output:** An instance \(I'\) for SMI.

1: Let _X_ and _Y_ be the sets of men and women of _I_, respectively.

2: Let \(X':=\{a_i|m_i\in X\}\cup\{b_j|w_j\in Y\}\) be the set of men of \(I'\).

3: Let \(Y':=\{s_j|w_j\in Y\}\cup\{t_j|w_j\in Y\}\) be the set of women of \(I'\).

4: Each _a<sub>i</sub>_’s list is constructed as follows: Consider a tie \((w_{j_1}w_{j_2}\cdots w_{j_k})\) in _m<sub>i</sub>_’s list in _I_. We assume without loss of generality that \(j_1<j_2<\cdots<j_k\). (If not, just arrange the order, which does not change the instance.) Replace each tie \((w_{j_1}w_{j_2}\cdots w_{j_k})\) by a strict order of 2_k_ women \(t_{j_1}t_{j_2}\cdots t_{j_k}s_{j_1}s_{j_2}\cdots s_{j_k}\). A woman who is not included in a tie is considered as a tie of length one.

5: Each _b<sub>j</sub>_’s list is defined as "_b<sub>j</sub>:s<sub>j</sub>t<sub>j</sub>_".

6: For each _j_, let _P(w<sub>j</sub>_) be the list of _w<sub>j</sub>_ in _I_, and _Q(w<sub>j</sub>_) be the list obtained from _P(w<sub>j</sub>_) by replacing each man _m<sub>i</sub>_ by _a<sub>i</sub>_. Then _s<sub>j</sub>_ and _t<sub>j</sub>_’s lists are defined as follows:

\(s_j:Q(w_j)b_j\)<br>
\(t_j:b_jQ(w_j)\)

<tbc>(_b<sub>j</sub>,t<sub>j</sub>_) blocks \(M'\), contradicting the stability of \(M'\) in \(I'\). Hence at most one of _s<sub>j</sub>_ and _t<sub>j</sub>_ can be matched with _a<sub>i</sub>_ for some _i_, which implies that _w<sub>j</sub>_ appears at most once in _M_. Thus _M_ is a matching.

We then show the stability of _M_. Since \(M'\) is the output of MGS, it is stable in \(I'\). Now suppose that _M_ is unstable in _I_ and there is a blocking pair (_m<sub>i</sub>,w<sub>j</sub>_) for _M_. There are four cases:

**Case (i): both** _m<sub>i</sub>_ **and** _w<sub>j</sub>_ **are single.** Since _m<sub>i</sub>_ is single in _M_, Step 3 of Algorithm 1 implies that _a<sub>i</sub>_ is single in \(M'\). Since _w<sub>j</sub>_ is single in _M_, _s<sub>j</sub>_ is not matched in \(M'\) with anyone in _Q(w<sub>j</sub>_), i.e., _s<sub>j</sub>_ is single or matched with _b<sub>j</sub>_. Note that (_a<sub>i</sub>,s<sub>j</sub>_) is a mutually acceptable pair because (_m<sub>i</sub>,w<sub>j</sub>_) is a blocking pair, and \(a_i\succ_{s_j}b_j\) in \(I'\) by construction. Thus (_a<sub>i</sub>,s<sub>j</sub>_) blocks \(M'\), a contradiction.

**Case (ii):** \(w_j\succ_{m_i}M(m_i)\) **and** _w<sub>j</sub>_ **is single.** Let _M(m<sub>i</sub>_)=_w<sub>k</sub>_. Then, by construction of _M_, \(M'(a_i)\) is either _s<sub>k</sub>_ or _t<sub>k</sub>_. By construction of \(I'\), \(w_j\succ_{m_i}w_k\) implies both \(s_j\succ_{a_i}s_k\) and \(s_j\succ_{a_i}t_k\), and in either case we have that \(s_j\succ_{a_i}M'(a_i)\) in \(I'\). Since _w<sub>j</sub>_ is single in _M_, by the same argument as Case (i), _s<sub>j</sub>_ is either single or matched with _b<sub>j</sub>_ in \(M'\). Hence (_a<sub>i</sub>,s<sub>j</sub>_) blocks \(M'\).

**Case (iii):** _m<sub>i</sub>_ **is single and** \(m_i\succ_{w_j}M(w_j)\)**.** Since _m<sub>i</sub>_ is single in _M_, _a<sub>i</sub>_ is single in \(M'\) by the same argument as Case (i). Let _M(w<sub>j</sub>_)=_m<sub>k</sub>_. Then, by construction of _M_, either _s<sub>j</sub>_ or _t<sub>j</sub>_ is matched with _a<sub>k</sub>_, and the other is matched with _b<sub>j</sub>_ since _b<sub>j</sub>_ can never be single as we have seen in an earlier stage of this proof. That is, \(M'(s_j)\) is either _a<sub>k</sub>_ or _b<sub>j</sub>_. Note that \(m_i\succ_{w_j}m_k\) in _P(w<sub>j</sub>_) implies \(a_i\succ_{s_j}a_k\) in _Q(w<sub>j</sub>_), so in either case \(a_i\succ_{s_j}M'(s_j)\) in \(I'\). Therefore (_a<sub>i</sub>,s<sub>j</sub>_) blocks \(M'\).

**Case (iv):** \(w_j\succ_{m_i}M(m_i)\) **and** \(m_i\succ_{w_j}M(w_j)\)**.** By the same argument as Case (ii), we have that \(s_j\succ_{a_i}M'(a_i)\) in \(I'\). By the same argument as Case (iii), we have that \(a_i\succ_{s_j}M'(s_j)\) in \(I'\). Hence (_a<sub>i</sub>,s<sub>j</sub>_) blocks \(M'\).


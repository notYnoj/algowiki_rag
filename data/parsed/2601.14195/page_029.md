## 5.1 Minimax Matchings in General Graphs with Max-Degree 2

We now give an algorithm for Minimax-AlmostStable-sri that solves the problem to optimality in linear time whenever preference lists are of length at most 2. The procedure is given in Algorithm 1 and works as follows: determine whether the instance _I_ admits a stable matching _M<sub>S</sub>_ using Irving’s algorithm \[34\]. If yes, immediately return _M<sub>S</sub>_. If not, compute a maximum- cardinality matching _M<sub>C</sub>_ as follows. Notice that because preference lists are of length at most 2, the acceptability graph of _I_ has maximum degree at most 2, i.e., it consists only of paths and cycles. Thus, to compute _M<sub>C</sub>_, we can simply include every second edge of every path, starting from one of the endpoints, and every second edge of every cycle (such that no included edges have a vertex in common). It is easy to see that this results in a maximum-cardinality matching for graphs with maximum degree at most 2. Next, we perform a rematching procedure on _M<sub>C</sub>_ that ensures that no agent is contained in more than one blocking pair, and return this modified matching.

**Algorithm 1** Exact algorithm for Minimax-AlmostStable-sri with lists of length \(\le 2\)

**Input:** _I_ : an sri instance

**Output:** _M_ : a matching

1: \(M_S\leftarrow\text{Irving}(I)\triangleright\) Compute a stable matching if one exists

2: **if** _M<sub>S</sub>_ exists **then**

3: **return** _M<sub>S</sub>_

4: **end if**

5: \(M_C\leftarrow\text{MaxCard}(I)\triangleright\) Compute a maximum-cardinality matching

6: **while** \(\exists a_i\) such that |_bp<sub>a<sub>i</sub></sub>(M<sub>C</sub>_)|=2 **do** \(\triangleright\) Rematching procedure

7: pick one agent _a<sub>r</sub>_ that is in a blocking pair with _a<sub>i</sub>_

8: \(a_k\leftarrow M_C(a_r)\)

9: \(M_C(a_i)\leftarrow a_r;M_C(a_r)\leftarrow a_i;M_C(a_k)\leftarrow a_k\)

10: **end while**

11: **return** _M<sub>C</sub>_

**Theorem 5.1.** _Let I be an_ sri _instance with n agents. If all preference lists of I are of length at most 2, then_ \(min_{M\in\mathcal{M}}max_{a_i\in A}|bp_{a_i}(M)|\le 1\) _and Algorithm 1 computes an optimal solution to_ Minimax-AlmostStable-sri _in O(n_) _time._

_Proof._ Clearly, if _M<sub>S</sub>_ exists, then \(max_{a_i\in A}|bp_{a_i}(M_S)|\le 0\), so _M<sub>S</sub>_ is optimal. Furthermore, if _M<sub>S</sub>_ does not exist, then \(min_{M\in\mathcal{M}}max_{a_i\in A}|bp_{a_i}(M)|>0\).

Now suppose that \(max_{a_i\in A}|bp_{a_i}(M_C)|>1\), then, because all preference lists are of length at most 2, there exists an agent _a<sub>i</sub>_ who is unmatched in _M<sub>C</sub>_ and who is contained in exactly two blocking pairs, say _bp<sub>a<sub>i</sub></sub>(M<sub>C</sub>_)={{_a<sub>i</sub>,a<sub>r</sub>},{a<sub>i</sub>,a<sub>s</sub>_}} (and suppose that \(a_r\succ_ia_s\)). Clearly, both _a<sub>r</sub>_ and _a<sub>s</sub>_ must be matched in _M<sub>C</sub>_, otherwise _M<sub>C</sub>_ would not be a maximum-cardinality matching as \(M_C\cup\{\{a_i,a_r\}\}\) or \(M_C\cup\{\{a_i,a_s\}\}\) would be a matching of larger size. Also, without loss of generality, let _a<sub>k</sub>_ denote the current partner of _a<sub>r</sub>_ in _M<sub>C</sub>_, then \(a_i\succ_ra_k\), otherwise _a<sub>i</sub>,a<sub>r</sub>_ would not block. Now we update _M<sub>C</sub>_ such that _a<sub>i</sub>_ and _a<sub>r</sub>_ are matched to each other (instead of _a<sub>r</sub>_ to _a<sub>k</sub>_). Due to the bound on the preference list lengths, _a<sub>k</sub>_’s preference list either contains just _a<sub>r</sub>_, or two agents _a<sub>r</sub>_ and _a<sub>l</sub>_ (for some agent _a<sub>l</sub>_). Note, though, that _a<sub>l</sub>_ must be matched in _M<sub>C</sub>_, otherwise \(M'_C=(M_C\backslash\{\{a_r,a_k\}\})\cup\{\{a_i,a_r\},\{a_k,a_l\}\}\) would exceed _M<sub>C</sub>_ in size and thus _M<sub>C</sub>_ would not be a maximum-cardinality matching.

After this rematching procedure completes, the size of _M<sub>C</sub>_ remains the same as previously, but |_bp<sub>a<sub>i</sub></sub>(M<sub>C</sub>_)|=0 (because now _a<sub>i</sub>_ is matched to their first choice _a<sub>r</sub>_). Furthermore, because \(a_i\succ_ra_k\), |_bp<sub>a<sub>r</sub></sub>(M<sub>C</sub>_)|=0. Finally, \(|bp_{a_k}(M_C)|\le 1\) because while _a<sub>k</sub>_ can generally block with at most two agents due to its preference list of length at most two, it cannot block with _a<sub>r</sub>_ because \(a_i\succ_ra_k\). Thus, this rematching procedure strictly decreases the number of agents who<tbc>


**Algorithm 1** Exponential-time algorithm for _k_-Deviator-Max-sri.

**Input:** \(I=(A,\succ):\) an sri instance; _D_: deviator agents; _k_: maximum permitted number of blocking pairs involving deviators

**Output:** _M_: a solution (matching), if one exists

1: \(M_S\leftarrow\mathsf{MV}(I)\triangleright\) Find a max.-card. matching

2: **for** each candidate matching \(M_D\in\mathcal{M}_D\) of _D_ agents **do**

3: **for** each candidate set _B_ of at most _k_ blocking pairs involving _D_ agents **do**

4: **if** \(M_D\cap B=\varnothing\) **then**

5: \(I'\leftarrow I\triangleright\) Make a copy of the instance

6: \(Q\leftarrow\varnothing\)

7: **for** each \(a_i\in D\) **do**

8: **for** each \(a_r\in A\) such that \(a_r\succ_iM_D(a_i)\) and \(\{a_i,a_r\}\notin B\) **do**

9: _Q._add(_a<sub>r</sub>_)

10: remove _a<sub>i</sub>_ and every worse agent from \(\succ'_r\), if such agents exist

11: **end for**

12: **end for**

13: **if** \(\#\{a_i,a_j\}\in M_D\) such that {_a<sub>i</sub>,a<sub>j</sub>_} unacceptable in \(I'\) **then**

14: \(V\leftarrow A\backslash A(M_D)\triangleright\) All agents other than those matched in _M<sub>D</sub>_

15: \(E\leftarrow\) acceptable pairs in \(I'\) whose endpoints belong to _V_

16: define \(w(\{a_r,a_s\})=|A|+|\{a_r,a_s\}\cap Q|\) for all \(\{a_r,a_s\}\in E\)

17: \(M_{mw}\leftarrow\mathsf{HK}(V,E,w)\triangleright\) Find a max.-weight matching

18: **if** every agent in _Q_ is matched in _M<sub>mw</sub>_ and \(|M_D\cup M_{mw}|=|M_S|\) **then**

19: **return** \(M_D\cup M_{mw}\)

20: **end if**

21: **end if**

22: **end if**

23: **end for**

24: **end for**

25: **return** no solution

<tbc>then we reject this configuration (_M<sub>D</sub>,B_) (implicit in line 4). Otherwise, for every agent \(a_i\in D\) and every agent \(a_r\in A\) such that \(a_r\succ_iM_D(a_i)\) and \(\{a_i,a_r\}\notin B\), agent _a<sub>r</sub>_ must end up with a partner better than _a<sub>i</sub>_ (according to \(\succ_r\)). Thus, we truncate \(\succ_r\) in line 10, discarding every agent worse than and including _a<sub>i</sub>_ (if multiple agents in _D_ satisfy this criterion with respect to _a<sub>r</sub>_, we truncate at the best-ranked such agent according to \(\succ_r\)). We must keep track of these agents _a<sub>r</sub>_ to later verify that they do indeed have a partner, and denote the set of all such agents _a<sub>r</sub>_ by _Q_, which is constructed in line 9.

If, after carrying out these truncations, some agent \(a_i\in D\) has a partner in _M<sub>D</sub>_ that is no longer in their preference list (or vice versa), we can reject this configuration (_M<sub>D</sub>,B_) (implicit in line 13). Otherwise, we need to look for a matching of maximum size among the agents not yet matched in _M<sub>D</sub>_ such that every agent in _Q_ is matched. We can do this as follows: we construct a maximum-weight matching instance (_G,w_) (where _G_ is a graph and _w_ is a weight function from the set of edges to the positive integers) consisting of all agents _A_\\_A(M<sub>D</sub>_) (where _A(M<sub>D</sub>_) denotes the set of agents matched in _M<sub>D</sub>_) as vertices and all acceptable pairs among these agents as edges. Furthermore, we construct _w_ as follows: for every acceptable pair of agents _a<sub>r</sub>,a<sub>s</sub>_ present in the instance, we let \(w(\{a_r,a_s\})=n+|\{a_r,a_s\}\cap Q|\), i.e., we assign a weight of _n_ to every edge, plus one extra unit for each endpoint in _Q_. This is done in lines 14-16.

Now, in line 17, we find a maximum-weight matching _M<sub>mw</sub>_ with weight _w(M<sub>mw</sub>_) for the instance (_G,w_) using the algorithm by Huang and Kavitha \[33\]. We claim (and prove this in the theorem below) that _M<sub>mw</sub>_ is a maximum-cardinality matching of (_G,w_) in which every agent<tbc>


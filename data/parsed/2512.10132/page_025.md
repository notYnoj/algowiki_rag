**Algorithm 3** Global Forward DP

**Input:** DP DAG _G_, target vertex _t_

**Output:** Optimal global value _x<sub>t</sub>_

1: \(\triangleright\) Initialize frontier buffer (dictionary: vertex \(\rightarrow\) DP value)

3: \(frontier\leftarrow\emptyset\)

4: \(\triangleright\) Process vertices in topological order

5: **for** \(v\leftarrow 1\) **to** \(T\leftarrow\)

7: **if to** then \(v\in S_\text{src}\) **do**

8: \(x_v\leftarrow a_v\triangleright\) Source initialization

9: **else**

10: \(x_v\leftarrow\) bottom element for \(\oplus\) \(\triangleright\) Compute via global recurrence

11: **for** each \((u,v)\in E\) with \(u\in frontier\leftarrow\)

12: **to** \(\text{\textbf{do}}candidate\leftarrow frontier[u]\otimes w_{u,v}\)

13: \(x_v\leftarrow x_v\oplus candidate\)

16: **end for**

17: **end if**

18: \(\triangleright\) Store in frontier

20: \(frontier[v]\leftarrow x_v\)

21: \(\triangleright\) Garbage collection: remove vertices with no future successors

22: **for** each \(u\in frontier\leftarrow\)

24: **to** \(\text{\textbf{do}}hasFuture\leftarrow\exists w>v:(u,w)\in E\)

25: **if** \(\neg hasFuture\) **then**

26: remove _u_ from _frontier_

27: **end if**

28: **end for**

29: \(\triangleright\) Early termination if target reached

30: **if** _v=t_ **then**

32: **return** _x<sub>t</sub>_

33: **end if**

34: **end for**

35: **return** _frontier_\[_t_\]

36: **Space:** \(O(\omega)\) words

**Time:** \(O(T\cdot\Delta_\text{max})\)


**Algorithm 1** Increasing endpoint scan on (_A,B_)

1: \(d[1..m]\leftarrow 0\); \(e[1..m]\leftarrow\perp\); initialize empty maps _L,P_

2: **for** _i_=1_,...,n_ **do**

3: \((b,q)\leftarrow(0,\perp)\)

4: **for** _j_=1_,...,m_ **do**

5: **if** _A[i_]=_B[j_] **then**

6: \(L(i,j)\leftarrow b+1\); \(P(i,j)\leftarrow q\)

7: **if** _b_+1_\>d[j_] **then**

8: \(d[j]\leftarrow b+1\); \(e[j]\leftarrow(i,j)\)

9: **end if**

10: **else if** _B[j]\<A[i_] and _d[j]\>b_ **then**

11: \((b,q)\leftarrow(d[j],e[j])\)

12: **end if**

13: **end for**

14: **end for**

15: **return** (_L,P_)

## 5. The match-sensitive algorithm

The dense scan touches nonmatching cells. We instead enumerate matches and compute (3)-(4) with dominance queries.

### 5.1. Preprocessing and the range-maximum structure

Assume comparison of two symbols and operations on an index take constant time. Sort the _S_ input occurrences by symbol, form equality groups, and assign ordered value ranks. Within each group, output all pairs consisting of an _A_ occurrence and a _B_ occurrence. This costs _O(S_lg<sub>+</sub>_S+M_) time and _O(S+M_) space. Matches can be stored in lists indexed by their _A_ row. All bounds below are deterministic in this comparison model.

Compress the columns occurring in a match to ranks \(x(v)\in[1..J]\); let _y(v_) be the symbol rank. For _M\>_0, \(J\le M\). Gaps in value ranks are harmless. Both order relations are preserved. A data structure _Q_ supports insertion of a scored match (_x,y,s,v_) and returns the maximum score and one witness in a prefix rectangle \([1..X]\times[1..Y]\). An empty rectangle returns \((0,\perp)\).

For completeness, an implementation with the stated bounds uses a Fenwick tree on the _J_ column ranks. Each outer node stores a sorted list of the value ranks of all points that can update it, and an inner Fenwick tree of maximum-score/witness pairs. These lists are built offline from the match coordinates. Each point appears in _O_(lg<sub>+</sub>_M_) lists; sorting them costs at most \(O(Mlg_+^2M)\) time and their total size is _O(M_lg<sub>+</sub>_M_). Binary search in each list locates an update coordinate or the last query coordinate at most _Y_ . Both operations visit _O_(lg<sub>+</sub>_M_) outer nodes and cost _O_(lg<sub>+</sub>_M_) per node. Only increases to stored maxima are needed. Ties may be resolved arbitrarily.


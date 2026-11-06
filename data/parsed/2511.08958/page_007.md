<tbc>**Algorithm 2** Match-sensitive LCBS

1: Enumerate _V_ in row lists; compute _x(v),y(v_) and _J_

2: **if** \(V=\varnothing\) **then**

3: **return** the empty sequence

4: **end if**

5: Initialize empty dominance structure _Q_ on (_x(v),y(v_))

6: **for** rows _i_ in increasing order **do**

7: **for** matches _v_ in row _i_ **do**

8: \((b,P(v))\leftarrow Q.\text{Query}(x(v)-1,y(v)-1)\); \(I(v)\leftarrow b+1\)

9: **end for**

10: **for** matches _v_ in row _i_ **do**

11: _Q._Update(_x(v),y(v),I(v),v_)

12: **end for**

13: **end for**

14: Release _Q_; initialize empty _Q_ on (_J_+1-_x(v),y(v_))

15: **for** rows _i_ in decreasing order **do**

16: **for** matches _v_ in row _i_ **do**

17: \((b,T(v))\leftarrow Q.\text{Query}(J-x(v),y(v)-1)\); \(D(v)\leftarrow b+1\)

18: **end for**

19: **for** matches _v_ in row _i_ **do**

20: _Q._Update(_J_+1-_x(v),y(v),D(v),v_)

21: **end for**

22: **end for**

23: Choose _p_ maximizing _I(p_)+_D(p_)-1

24: Recover the prefix via _P_, the suffix via _T_, and join once at _p_

## 5.2. Two sweeps

In the forward sweep, process rows in increasing order and query (_x(v_)-1_,y(v_)-1) for each match _v_ in the current row. Add one to the returned maximum to obtain _I(v_). In the backward sweep, process rows in decreasing order and replace the column rank by \(\widehat{x}(v)=J+1-x(v)\). The query \((\widehat{x}(v)-1,y(v)-1)\) obtains the best decreasing successor. The value coordinate is not reversed.

**Theorem 5.1.** Algorithm 2 returns an LCBS in \(O(Slg_+S+Mlg_+^2M)\) time and _O(S+M_lg<sub>+</sub>_M_) auxiliary space.

**Proof:**

At the start of forward row _i_, _Q_ contains exactly the matches of smaller rows, with their correct increasing scores. The strict column and value bounds select precisely the remaining conditions in (3). Querying the whole row before inserting it preserves the invariant. By induction, all _I_ scores and predecessor witnesses are correct. In the backward sweep, stored matches have larger row indices. Mirroring makes a smaller query column equivalent to a larger original column. The unchanged strict<tbc>


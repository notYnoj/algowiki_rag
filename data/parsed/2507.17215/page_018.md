<tbc>**Algorithm 11** : LookUpSegTree(_t,T_)

**Input**: _t_: timestamp, _T_: root of a segment tree

1: sum \(\leftarrow 0\)

2: **if** \(t\in\text{Seg}(T)\) **then**

3: sum \(\leftarrow\) sum + Counter(_T_)

4: **if** \(t\in\text{Seg}(\text{LeftChild}(T))\) **then**

5: LookUpSegTree(_t_,LeftChild(_T_))

6: **else**

7: LookUpSegTree(_t_,RightChild(_T_))

8: **return** sum


We claim that in any local optimum \(\alpha\), it holds that _g<sub>j</sub>_=NAND(_y_<sub>1</sub>_,y_<sub>2</sub>) holds. Suppose that this is not the case.

**Case 1:** \(\alpha(g_j)=1\) and \(\alpha(y_1)=\alpha(y_1)=1\). Then the third clause above, \(\neg g_j\), is violated, and setting _g<sub>j</sub>_ to 0 will satisfy all three clauses above.

**Case 0:** \(\alpha(g_j)=0\) and at least one of _y_<sub>1</sub>_,y_<sub>2</sub> is mapped to 0. Then one of the first two clauses must is violated; flipping _g_ satisfies it; it will violate the third clause, but it is still an improving flip.

So we conclude that under \(\alpha\) every gate is correctly evaluated. Therefore, the value of the _m_ output gate variables under \(\alpha\) give us the correct output of the circuit: _C_(**x**).


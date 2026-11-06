Since 0_\<|C_|=|_S|\<|I_|, we have

\(0<|T|=|I|-|C|<|I|.\)

We claim that _N(T_)=_J_\\_S_.

First, \(T\subseteq I\) and independence of _I_ imply \(N(T)\subseteq J\). If some \(t\in T\) were adjacent to a vertex \(s\in S\), then \(t\in N(S)=C\), contradicting _T=I_\\_C_. Therefore,<tbc>

\(N(T)\subseteq J\backslash S.\)

<tbc>Conversely, the perfect matching matches each vertex of _S_ to a distinct vertex of _C_. Since |_C_|=|_S_|, these matched vertices exhaust _C_. The remaining matching edges therefore match _J_\\_S_ bijectively to _I_\\_C=T_. Hence<tbc>

\(J\backslash S\subseteq N(T).\)

<tbc>Combining the two inclusions yields _N(T_)=_J_\\_S_. It follows that

\(|N(T)|=|J|-|S|,|T|=|I|-|C|=|I|-|S|.\)

Since |_I_|=|_J_|, we have |_N(T_)|=|_T_|. Thus, _T_ is again a nonempty proper tight subset of _I_, proving the forward implication.

For the reverse implication, suppose that \(\emptyset\neq T\unknown I\) and |_T_|=|_N(T_)|. Since \(T\subseteq I\), it is independent, and

\(0<|T|<|I|=\frac{n}{2}.\)

Thus, _T_ itself is a small blocking set.

Theorem 3 shows that, in the case \(\delta=0\) and |_I_|=_n/_2, any graph containing a small blocking set also contains one within _I_. It therefore suffices to detect and construct such a set within _I_.

## 5. Algorithm design and analysis

### 5.1. Constructing a small blocking set within a maximum-cardinality critical independent set

The projection theorem reduces the problem on the entire graph to deciding whether _I_ contains a nonempty proper tight subset. We perform this test using the standard matching-contraction construction.


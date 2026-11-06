\(\mathrm{XInv}_\rho(A,B)+\mathrm{XInv}_\rho(B,A)=|A|\cdot|B|\). Thus,

\(\mathrm{DInv}_\rho(A,B)\doteq\mathrm{XInv}_\rho(A,B)-\mathrm{XInv}_\rho(B,A)\)<br>
\(=(\mathrm{XInv}_\rho(A,B)+\mathrm{XInv}_\rho(B,A))-2\mathrm{XInv}_\rho(B,A)\)<br>
\(=|A|\cdot|B|-2\mathrm{XInv}_\rho(B,A).\) (20)

As \(\mathrm{XInv}_\rho(B,A)\) in an integer, the claim follows.

Fact 50 implies that whenever at least one of the leaf sets _L_<sub>lo</sub> or _L_<sub>hi</sub> is of even cardinality, then (8) fails to hold, and \(\Pi_T\) is sensitive to the underlying \(\tau\) at \(\rho\). Thus, we can guarantee that \(\Pi_T\) satisfies the partition property provided that for any two siblings _u_<sub>1</sub> and _u_<sub>2</sub> in _T_ that are not both leaves, at least one of |L(_T_<sub>_u_<sub>1</sub></sub>)| or |L(_T_<sub>_u_<sub>2</sub></sub>)| is even. We refer to the latter condition as the _product condition_. In trees without nodes of degree 1, the product condition can be expressed alternately in terms of the leaf child sets. We state and prove the result for arbitrary trees as it will help us in the next subsection to generalize the analysis.

**Proposition 51.** _Let T be a tree without nodes of degree 1. The following two conditions are equivalent:_

(_a)_ _For any two siblings u_<sub>1</sub> _and u_<sub>2</sub> _that are not both leaves, at least one of_ |L(_T_<sub>_u_<sub>1</sub></sub>)| _or_ |L(_T_<sub>_u_<sub>2</sub></sub>)| _is even._<tbc>

(_b)_ _At most one leaf child set is odd, and if there exists a node v_<sup>∗</sup> _with an odd leaf child set_ LC(_v_<sup>∗</sup>)_, then all ancestors of v_<sup>∗</sup> _have an empty leaf child set._

_In the case of binary trees, (b) can be simplified to: At most one leaf has a non-leaf sibling._

_Proof._ We establish the two directions of implication separately.

\(\Rightarrow\): We argue the contrapositive. Suppose that at least two of the leaf child sets are odd. Start with the root of _T_ as the node _v_, and iterate the following: If _v_ has a child _u_ such that _T<sub>u</sub>_ contains at least two nodes with an odd leaf child set, replace _v_ by such a child _u_. When the process ends, one of the following situations applies:

\(\circ\) There are two distinct children _u_<sub>1</sub> and _u_<sub>2</sub> of _v_ that are not leaves and each contain a single node with an odd leaf child set. In this case both _T_<sub>_u_<sub>1</sub></sub> and _T_<sub>_u_<sub>2</sub></sub> contain an odd number of leaves, violating (a).<tbc>

\(\circ\) There exists a unique child _u_<sub>1</sub> of _v_ that is not a leaf and contains a single node with an odd leaf child set, and _v_ itself has an odd number of leaf children. In this case, setting _u_<sub>2</sub> to any one leaf child of _v_ (which exists as their number is odd), leads to a violation of (a).

Next, suppose that there exists a unique node _v_<sup>∗</sup> that has an odd leaf child set, and that an ancestor _v_ of _v_<sup>∗</sup> has a leaf child _u_<sub>1</sub>. Setting _u_<sub>2</sub> to the child of _v_ that contains _v_<sup>∗</sup> in its subtree, yields a violation of (a) as _T_<sub>_u_<sub>2</sub></sub> contains an odd number of leaves.

\(\Leftarrow\): If neither _u_<sub>1</sub> nor _u_<sub>2</sub> are leaves, the first condition of (b) guarantees that at most one of _T_<sub>_u_<sub>1</sub></sub> or _T_<sub>_u_<sub>2</sub></sub> contains an odd number of leaves. If _u_<sub>1</sub> is a leaf and _u_<sub>2</sub> is not, then the second condition of (b) implies that _T_<sub>_u_<sub>2</sub></sub> cannot contain a node with an odd leaf child set, and therefore has an even number of leaves.


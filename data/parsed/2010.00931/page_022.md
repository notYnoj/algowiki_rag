**Algorithm 3.** SplayTT (generalized splaying procedure for STTs)

Input: search tree T on S, node x to be splayed until node y is parent of x in T.<br>
procedure splay(x,y)<br>
   while \(x.parent\neq y\) do<br>
   \(p\leftarrow x.parent\)<br>
   if p.parent=y then \(\triangleright\) (ZIG)<br>
   rotate at x<br>
   else<br>
   \(g\leftarrow p.parent\)<br>
   if p separates x and g in S then \(\triangleright\) (ZIG-ZIG)<br>
   rotate at p, then rotate at x<br>
   else if x separates p and g in S then \(\triangleright\) (ZIG-ZAG)<br>
   rotate twice at x

<tbc>_g_ separates _p_ and _x_ cannot arise, as in that case _g,p,x_ would not appear in this order on the search path.)

It is easy to see that the non-separating third case can only arise if the search tree is not Steiner-closed. Therefore, we define and analyse splaying under the restriction that the search tree _T_ is Steiner-closed at all times, including in its initial state. In this way Algorithm 3 is well-defined, and amenable for analysis. A remaining technical challenge is that even if _T_ is Steiner-closed before splaying, the act of splaying may destroy this property. (We show a simple example in Figure 6.)

Let _P=P<sub>x</sub>_ be the node set of the search path of _x_ in a Steiner-closed tree _T_, and let _C_=ch(_P_). The difficulty, intuitively, is that _C_ is not a path as in the BST case, but a tree. Call a node of _C_ of degree more than 2 a _branching node_. We prove an alternative characterization of branching nodes that will be useful later.

**Lemma 13.** _Let T,P be defined as above. A node_ \(p\in P\) _is a branching node of P if and only if_ \(|\delta(T_p)|=2\) _and p has a child q on P with_ \(|\delta(T_q)|=1\).

_Proof._ Let \(p\in P\) be a branching node. Then there are three nodes \(y_1,y_2,y_3\in P\) that are pairwise separated by _p_. W.l.o.g., no node in _P_ separates _p_ from either of the nodes _y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub>. By the search tree property, at most one of _y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub> can be a descendant of _p_. If _y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub> are all ancestors of _p_, then the search path to the parent of _p_ is not Steiner-closed. As such, one of the nodes, say _y_<sub>3</sub>, is a descendant of _p_, and _y_<sub>1</sub>_,y_<sub>2</sub> are ancestors of _p_, which implies \(\delta(T_p)=\{y_1,y_2\}\). (Since _T_ is Steiner-closed and thus a 2-cut tree, \(|\delta(T_p)|=2\).)

Moreover, since _p_ has a descendant _y_<sub>3</sub> on _P_, it also has a child _q_ on _P_, which must be in the same connected component of _S_\\_p_ as _y_<sub>3</sub>. We have \(p\in\delta(T_q)\) and \(\delta(T_q)\backslash\{p\}\subseteq\delta(T_p)=\{y_1,y_2\}\). But since _p_ separates _q_ from both _y_<sub>1</sub> and _y_<sub>2</sub>, we have \(\delta(T_q)=\{p\}\).

For the other direction, suppose _q_ is the child of _p_ and \(|\delta(T_p)|=2\), \(|\delta(T_q)|=1\). Clearly, \(\delta(T_q)=\{p\}\). Say \(\delta(T_p)=\{y_1,y_2\}\). Since \(y_1,y_2\notin\delta(T_q)\), the three nodes _y_<sub>1</sub>_,y_<sub>2</sub>_,q_ must be pairwise separated by _p_. This means that _p_ has degree 3 in ch({_y_<sub>1</sub>_,y_<sub>2</sub>_,q_}), and thus degree at least 3 in ch(_P_).


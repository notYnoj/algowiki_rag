In the second recursive call, A adds to _U_ at most one element \(x'(e)\) with \(e\notin B'_0\). Consequently, \(|U''|\le 1\) and \(\varphi(i+1)-\varphi(i)\le 0\). Additionally, in this recursive call the set _F_ remains unchanged.

Therefore, the potential is never increases and each growth of \(F'\) by a single directed path in _T_ is associated with a decrease of the potential by at least one. Combining this with the fact that \(\varphi(1)-\varphi(t)\le|B'_0|+|U|\), we derive that \(\tilde{F}\backslash F\) is a union of at most \(|B'_0|+|U|\) directed paths in _T_.

For the remaining properties of A, we apply an induction. The base cases (\(U=\emptyset\) and \(v\in U\)) are considered above. The following claim shows the correctness of a single transition.

**Claim 20.** _If_ \(\mathcal{C}_1:=\mathcal{A}(U_1,F\cup F')\) _and_ C<sub>2</sub>:=A(_U_<sub>2</sub>_,F_) _are correct, then so is_ C:=A(_U,F)._

_Proof of Claim 20._ Assume, for a contradiction, that _X=T-S_+Inv(_S_) satisfies C but contains a path from _x_ to _v_ for some \(x\in U\). Since \(\mathcal{C}=\mathcal{C}_1\cup\mathcal{C}_2\), it follows that _X_ satisfies either C<sub>1</sub> or C<sub>2</sub>. Because \(U_1\subseteq U_2\), the inductive hypothesis implies in both cases that _X_ contains no path from any \(u'\in U_1\) to _v_. By the definition of _U_<sub>1</sub>_,U_\\_U_<sub>1</sub> consists of a single element, which is the highest vertex in _U_. Therefore, _x_ must be exactly this vertex.

Since \(v\notin U\), we know that \(x\neq v\). Claim 15 then provides an edge \(e\in B\) such that _e_ is (_x,S_)- active and _X_ contains a path from \(x'(e)\) to _v_. Also, as discussed above, each triple \((\tilde{F},\tilde{R},\tilde{B'})\in\mathcal{C}\) obeys \(\tilde{R}=R_0\), \(\tilde{B'}=B'_0\), and \(F\subseteq\tilde{F}\). Recall that A works only with sets _F_ such that \(F_0\subseteq F\). Thus \(F_0\subseteq\tilde{F}\). By our assumption, _X_ must satisfy some restriction triple from C. Then it also satisfies \((F_0,R_0,B'_0)\). We now distinguish two cases based on whether _e_ belongs to \(B'_0\).

**Case** \(e\in B'_0\)**.** According to Claim 16_,T-R_<sub>0</sub>+_e_ contains a path from _x_ to \(x'(e)\). By construction, \(x'(e)\in U_1\subseteq U_2\). But since _X_ contains a path from \(x'(e)\) to _v_, this contradicts the correctness of either C<sub>1</sub> or C<sub>2</sub>.

**Case** \(e\in B\backslash B'_0\)**.** Recall that _e_ is (_x,S_)-active and _X_ contains a path from \(x'(e)\) to _v_. Claim 18 then tells us that the edge \(e'\in B\backslash B'_0\) with the lowest \(x'(e')\) enjoys the same two properties. By definition, \(x'(e')\in U_2\). Therefore, _X_ cannot satisfy C<sub>2</sub> because there is a path in _X_ from \(x'(e')\) to _v_. Given that \(\mathcal{C}=\mathcal{C}_1\cup\mathcal{C}_2\), _X_ must then satisfy \(\mathcal{C}_1=\mathcal{A}(U_1,F\cup F')\). Together with the structure of restriction triples that A can produce, this implies that for each \((\tilde{F},\tilde{R},\tilde{B})\in\mathcal{C}_1\), it holds that \(F\cup F'\subseteq\tilde{F}\). Hence, \(S\cap F'=\emptyset\) (as _S_ is disjoint from \(\tilde{X}\) of the satisfied triple). Because we have an _x_-active edge from \(B\backslash B'_0\), the set \(F'\) is defined as a subpath of _P_ from \(x'(e')\) to _x_. However, then Claim 17 states that \(e'\) cannot be (_x,S_)-active, which yields a contradiction again.

In both cases, we obtain a contradiction. Therefore, if _X_ satisfies C, it contains no path from any \(x\in U\) to _v_.

We now establish the converse direction. Assume that _X_ satisfies \((F,R_0,B'_0)\) (and therefore also \((F_0,R_0,B'_0)\)) and that _X_ contains no path from any vertex of _U_ to _v_. Let _x_ be the highest vertex in _U_ (as before, \(x\neq v\)). In particular, _X_ does not contain a path from _x_ to _v_. Claim 15 then guarantees that for every edge \(e\in B\), either _e_ is not (_x,S_)-active, or _X_ contains no path from \(x'(e)\) to _v_.

We first examine edges from \(B'_0\). By definition, _U_<sub>1</sub>\\_U_ consists of such \(x'(e)\) that \(e\in B'_0\), _e_ is _x_-active, and _T_<sub>0</sub>-_R_<sub>0</sub>+_e_ contains a path from _x_ to \(x'(e)\). By Claim 16, all such edges _e_ are (_x,S_)-active. This implies that there is no path in _X_ from \(x'(e)\) to _v_. Consequently, _X_ contains no path from any vertex of _U_<sub>1</sub> to _v_. We now consider two cases.

**Case** \(F'\cap S=\emptyset\)**.** Then _X_ satisfies \((F\cup F',R_0,B'_0)\). By inductive hypothesis, _X_ satisfies C<sub>1</sub>, and therefore C as well.


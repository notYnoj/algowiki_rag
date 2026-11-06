Note that the highest vertices in _U_<sub>1</sub> and _U_<sub>2</sub> are strictly lower than _x_. Indeed, by construction, _U_<sub>1</sub>\\_U_ and _U_<sub>2</sub>\\_U_ contain only vertices of the form \(x'(e)\) for _x_-active edges _e_. By the definition of _x_-activeness, this implies that \(x'(e)\) is lower than _x_. Additionally, _U_<sub>1</sub> and _U_<sub>2</sub> do not contain _x_.

Therefore, the computation graph is acyclic. We now prove the correctness of A. Let us start with the structure of a fixed triple \((\tilde{F},\tilde{R},\tilde{B}')\in\mathcal{A}(U,F)\). By construction, we have \(\tilde{R}=R_0\) and \(\tilde{B}'=B'_0\). Moreover, in both recursive calls the set _F_ can only expand. At a leaf, A generates a restriction triple with the given set _F_. Hence, \(F\subseteq\tilde{F}\). We prove the remaining structural property in a separate claim.

**Claim 19.** _For each_ \((\tilde{F},\tilde{R},\tilde{B}')\in\mathcal{A}(U,F)\)_, the set_ \(\tilde{F}\backslash F\) _is a union of at most_ \(|B'_0|+|U|\) _directed paths in T._

_Proof of Claim 19._ For a fixed triple \((\tilde{F},\tilde{R},\tilde{B}')\in\mathcal{A}(U,F)\), consider the branch of the recursion that produced it. Let the sequence of arguments of A along this branch be \((U'_1,F'_1),\dots,(U'_t,F'_t)\), where \((U'_1,F'_1)=(U,F)\) and \(F'_t=\tilde{F}\) (the last equation follows from the form of produced constraint sets in the leaves of A). The structure of recursive calls of A implies that \(F'_i\subseteq F'_{i+1}\) for each _i_. We denote the highest vertex in \(U'_i\) by _x<sub>i</sub>_. As discussed above, _x_<sub>_i_+1</sub> is always lower than _x<sub>i</sub>_. Making a recursive call, A adds to _U_ only the elements of the form \(x'(e)\) for some \(e\in B\). Moreover, if \(x'(e)\in U'_{i+1}\backslash U'_i\), then the edge _e_ is always _x<sub>i</sub>_-active.

For a fixed \(e\in B\), let \(I(e)\subseteq\{1,\dots,t\}\) be a set of indices _i_ with \(x'(e)\in U'_i\). We claim that _I(e_) forms a contiguous subsegment. Assume the contrary. Then there exist indices \(\ell,r\) with \(r>\ell+1\) such that \(\ell,r\in I(e)\), but \(\{\ell+1,\dots,r-1\}\cap I(e)=\emptyset\). Hence, \(x'(e)\in U'_\ell\backslash U'_{\ell+1}\). Recall that in each recursive call, A removes only the highest vertex of the set. Therefore, \(x'(e)=x_\ell\). On the other hand, since \(x'(e)\in U'_r\backslash U'_{r-1}\), the edge _e_ must be (_x_<sub>_r_-1</sub>)-active. By the definition of _x_-activeness, this implies that \(x_\ell=x'(e)\) is lower than _x_<sub>_r_-1</sub>, which leads us to a contradiction because \(\ell<r-1\).

For an edge _e_, let \(\ell(e)\) be the minimum element of _I(e_). If \(I(e)=\emptyset\), we set \(\ell(e)=\infty\). Also, let \(\ell_i\) be the number of \(e\in B'_0\) with \(\ell(e)=i\), and let \(p_i:=\sum_{j\le i}\ell_j\). To bound the growth of \(F'_i\), we define the potential function \(\varphi(i):=|U'_i|+(|B'_0|-p_i)\). Note that \(\varphi(1)=|U|+(|B'_0|-p_1)\le|B'_0|+|U|\). Also, since \(|U'_t|\ge 0\) and \(p_t\le|B'_0|\), we have \(\varphi(t)\ge 0\).

We now analyze how \(\varphi\) changes during a single transition. First, note that<tbc>

\(\varphi(i+1)-\varphi(i)=(|U'_{i+1}|-|U'_i|)+(p_i-p_{i+1})=|U'_{i+1}\backslash U'_i|-|U'_i\backslash U'_{i+1}|-\ell_{i+1}\)

<tbc>Recall that \(U'_{i+1}\backslash U'_i\) consists of elements of the form \(x'(e)\), where \(e\in B\). Consider \(x'(e)\in U'_{i+1}\backslash U'_i\) such that \(e\in B'_0\). Since _I(e_) is a contiguous subsegment, \(i\notin I(e)\), and \(i+1\in I(e)\), we have \(\ell(e)=i+1\). Consequently, we can associate every such \(x'(e)\) with the edge _e_ that increases \(\ell_{i+1}\). Let \(U'':=U'_{i+1}\backslash U'_i\backslash\{x'(e)|e\in B'_0\}\). We obtain that

\(\varphi(i+1)-\varphi(i)\le|U''|-|U'_i\backslash U'_{i+1}|\)

Furthermore, since in each recursive call A removes exactly one element of the set, we have \(|U'_i\backslash U'_{i+1}|=1\), and hence the difference above is at most \(|U''|-1\).

We now distinguish two cases based on the type of transition between \((U'_i,F'_i)\) and \((U'_{i+1},F'_{i+1})\). Recall that A makes two recursive calls. In the first of them (with parameters _U_<sub>1</sub> and \(F\cup F'\)), it adds to _U_ only elements \(x'(e)\) with \(e\in B'_0\). Hence, \(|U''|=0\), and therefore \(\varphi(i+1)-\varphi(i)\le-1\). Moreover, the new set _F_ in this recursive call is obtained by adding one subpath of _P_ (and therefore one directed path in _T_).


<tbc>Plan 6.34.<br>
**Initialise:** _i_=1. (_H<sub>i</sub>,w<sub>i</sub>_), _i_-permissible, where in fact by (_H_<sub>1</sub>_,w_<sub>1</sub>) we mean (_H_<sub>1<sup>∗</sup></sub>_,w_<sup>1<sup>∗</sup></sup>) as alluded to above.

**Step 1:** Find a matching \(M_i^o\) in \((H_i^o,w_i^o)\) via Theorem 6.2 and define \(H_{i.1}:=H_i[V(H_i)\backslash V(M_i^o)]\).

**Step 2:** Obtain a weight function _w_<sub>_i._1</sub> for _H_<sub>_i._1</sub> such that _w_<sub>_i._1</sub>|<sub>_H<sub>i._1</sub>\[_I<sub>t<sub>i</sub><sub>i</sub>_+1</sub>\] is an almost-perfect fractional matching for _H_<sub>_i._1</sub>\[_I_<sub>_t<sub>i</sub><sub>i</sub>_+1</sub>\].

**Step 3:** Run a (random) greedy cover for vertices in _V(H_<sub>_i._1</sub>)\\_I_<sub>_t<sub>i</sub>_+1</sub> to obtain a matching \(M_i^c\). Define _H_<sub>_i_+1</sub>=_H<sub>i</sub>_\[_V(H<sub>i</sub>_)\\_V(M<sub>i</sub>_)\], where \(M_i:=M_i^o\cup M_i^c\).

**Step 4:** Define _w_<sub>_i_+1</sub> in terms of _w<sub>i</sub>_ and _H<sub>i</sub>_ so that _w_<sub>_i_+1</sub> is an almost-perfect fractional matching for _H_<sub>_i_+1</sub>.

**Step 5:** If (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) is not (_i_+1)-permissible, abort. If \(V(H_i)\subseteq I_{n^{10-5}}\) stop. Else, increase _i_ by 1 and go to Step 1.

Similarly to Section 6.2, we show that Plan 6.34 does not abort prematurely, and subsequently that we can successfully reach _L_<sup>∗</sup>. We shall first explain the strategy to obtain (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) from (_H<sub>i</sub>,w<sub>i</sub>_), filling in the details of a single iteration of Plan 6.34 given that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible. We then deduce, by strong induction, the properties of (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) in terms of (_H_<sub>1<sup>∗</sup></sub>_,w_<sub>1<sup>∗</sup></sub>) and hence show via backtracking that (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) is (_i_+1)-permissible, ensuring that the algorithm completes successfully. In the next section we go through one iteration of the Algorithm, filling in details for how we obtain the weight functions _w_<sub>_i._1</sub> and _w_<sub>_i_+1</sub> and observing how (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) ‘looks’ in terms of (_H<sub>i</sub>,w<sub>i</sub>_).

**6.4.1. One iteration of Plan 6.34.** We go through the steps of Plan 6.34 one by one for one iteration, filling in the details of how we intend to get from (_H<sub>i</sub>,w<sub>i</sub>_) to (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>), where we assume throughout this section that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible.

6.4.1.1. _Step 1._ By Theorem 6.28, since (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible, we obtain \(M_i^o\) and define _H_<sub>_i._1</sub> as above.

6.4.1.2. _Step 2._ Below we will define the new weighting \(w_{i.1}(e):E(H_i)\rightarrow\mathbb{R}_{\ge 0}\). First let \(w_{i.0}(e):E(H_i)\rightarrow\mathbb{R}_{\ge 0}\) be given by

\(w_{i.0}(e):=\left\{\begin{array}{ c c }
\frac{w_i(e)}{\overline{\Pi_{u\in e\cap I_{t_{i+1}}}}(1-d_{w_i^o(u))}} & \text{if}e\text{is}i\text{-reachable} \\
w_{1^*}(e) & \text{otherwise.}
\end{array}\right..\)

Proposition 6.35. _For each i-reachable edge_ \(e\in H_i\),

\(w_i(e)\le w_{i.0}(e)\le\frac{1.1w_i(e)log^{4l_3+8}(n)}{c_1^4}.\)

Proof. Note that, since (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible, by Proposition 6.30, for \(u\in I_{t_{i+1}}\) we have that \(1-d_{w_i^o}(u)=\left(1\pm\frac{c_{H_i,v}}{\delta_{H_i,v}}\right)w_i(E_{H_i}(u,I_{t_{i+1}}))\), and by Propo sition 6.31, \(\frac{c_{H_i,v}}{\delta_{H_i,v}}\le\frac{log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}\) . Furthermore, by Proposition 6.26 we have that \(\frac{c_1}{log^{l_3+2}(n)}\le w_i(E_{H_i}(v,I_{t_{i+1}}))\) since \(t_i\le|I_{t_{i+1}}|\), and \(w_i(E_{H_i}(v,I_{t_{i+1}}))\le d_{w_i,H_i}(v)\le\)


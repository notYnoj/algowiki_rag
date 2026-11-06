input :<br>
Instance (P,D) with s distinct x-coordinates<br>
output:<br>
Feasible solution to (P,D) of size at most \(O(logs)\cdot\mathsf{IS}(P,D)\)<br>
\(\mathcal{I}\leftarrow\{\text{interval}[y(p),y(q)]|(p,q)\in D\}\);<br>
\(\mathcal{R}\leftarrow\text{minimum hitting set for}\mathcal{I}\);<br>
return HorizontalDC(P,D,R);

input :<br>
Instance (P,D) with rows R<br>
output:<br>
Feasible solution to (P,D) computed via horizontal divide-and-conquer<br>
\(Q\leftarrow\emptyset\);<br>
\(m\leftarrow\text{median of}\mathcal{R}\);<br>
\(D_m\leftarrow\{(p,q)\in D|y(p)\le m\le y(q)\}\);<br>
foreach \((p,q)\in D_m\) do<br>
\(Q\leftarrow Q\cup\{(x(p),m),(x(q),m)\}\)<br>
\(D_t\leftarrow\{(p,q)\in D|y(p)>m\}\);<br>
\(P_t\leftarrow\{p,q|(p,q)\in D_t\}\);<br>
\(\mathcal{R}_t\leftarrow\{r\in\mathcal{R}|r>m\}\);<br>
\(Q\leftarrow Q\cup\text{HorizontalDC}(P_t,D_t,\mathcal{R}_t)\);<br>
\(D_b\leftarrow\{(p,q)\in D|y(q)<m\}\);<br>
\(P_b\leftarrow\{p,q|(p,q)\in D_b\}\);<br>
\(\mathcal{R}_b\leftarrow\{r\in\mathcal{R}|r<m\}\);<br>
\(Q\leftarrow Q\cup\text{HorizontalDC}(P_b,D_b,\mathcal{R}_b)\);<br>
return Q;

_Proof._ The feasibility of the computed solution follows easily by induction over the number of rows, using the fact that R is a hitting set of I and that in the for loop in Algorithm 2 (Line 5), a feasible solution for _D<sub>m</sub>_ is computed. It is also easy to see that the running time is polynomial in the input size. The set R has size at most _n_, and thus HorizontalDC is called at most _O_(log_n_) times. In each call, at most _s_ points are added, and _s_ is also upper bounded by _n_. Finally, assignments can be done in polynomial time.

**Lemma 11** (Cost)**.** _For any s-thin instance_ (_P,D), algorithm_ HorizontalManhattan _outputs a solution of cost_ \(O(logs)\cdot\mathsf{IS}(P,D)\).

_Proof._ Let _r_=|R| be the number of rows computed in Algorithm 1. There exists a subset \(I\subseteq\mathcal{I}\), also of size _r_, that is an independent set \[13\]. Define \(L=\{\lambda(p,q)|[y(p),y(q)]\in I\}\) to be the set of corresponding left sides of the demands in _I_. In particular, the segments in _L_ are disjoint and |_L_|=_r_. We upper bound the cost of our solution as follows. For each added point, define a _witness interval_, witnessing its cost. The total number of points is then roughly bounded by the number of witness intervals, which we show to be _O_(log_s_)IS(_P,D_).

We enumerate the recursion levels of Algorithm 2 from 1 to \(\lceil logr\rceil\) in a top-down fashion in the recursion tree. In each recursive call, at most _s_ many points are added to _Q_ in line 5-- one for each distinct _x_-coordinate. Hence, during the first \(\lceil logr\rceil-\lceil logs\rceil\) recursion levels at most \(s\cdot 2^{\lceil logr\rceil-\lceil logs\rceil}=O(s\cdot\frac{r}{s})=O(r)\) many points are added to _Q_ in total. We associate each of these points with one unique left side in _L_ in an arbitrary manner. For each of these points, we call<tbc>

**Algorithm 1:** HorizontalManhattan(_P,D_)

**Algorithm 2:** HorizontalDC(_P,D,_R)


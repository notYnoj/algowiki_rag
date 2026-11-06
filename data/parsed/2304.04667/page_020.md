(b) we prioritize assigning _v_ to an optimal _pu_-cut (_S<sub>p,u</sub>,C<sub>p,u</sub>,S<sub>u,p</sub>_) that separates _v_ from _p_ and has a _small cardinality_ \(|S'_{u,p}|\). This ensures that the sets significantly decrease in size with each recursive step and thus upper bounds the total recursion depth by _O_(log_n_).<tbc>

(c) we can only assign two nodes _u,v_ to different sets if we have evidence for doing so in the form of a (likely optimal) vertex-cut _C_ that separates one but not the other from _p_, and thus separates them.<tbc>

<tbc>Satisfying all of the above criteria at the same time requires the following process. We define a reassignment function \(f:V'\rightarrow V'\cup\{\perp\}\) such that for every node \(u\in V'\backslash\{p\}\) with cut (_S<sub>p,u</sub>,C<sub>p,u</sub>,S<sub>u,p</sub>_), we reassign _u_ to _v_, denoted _f(u_)=_v_ with the cut (_S<sub>p,f(u_)</sub>_,C<sub>p,f(u_)</sub>_,S<sub>f(u),p</sub>_) as follows. Denote by \(V_{small},V'_{small}\) two initially identical sets, each containing all nodes _u_ such that \(|S'_{u,p}|\le n'/2\), and denote by \(V_{big},V'_{big}\) two sets, both are initially equal to \(V'\backslash V_{small}\).<tbc>

<tbc>Sort _V<sub>small</sub>_ by Max-Flow(_p,u_), and for all \(u\in V_{small}\) from low Max-Flow(_p,u_) to high and for every node \(v\in S'_{u,p}\cap V'_{small}\), set _f(v_)=_u_ and then remove _v_ from \(V'_{small}\). Furthermore, for every node \(v\in S'_{u,p}\cap V'_{big}\), if Max-Flow(_p,u_)=Max-Flow(_p,v_) then set _f(v_)=_u_ and then remove _v_ from \(V'_{big}\). Finally, set \(f(v)=\perp\) for every node _v_ for which _f_ was not assigned a value (including _p_).<tbc>

<tbc>To get the partition, let _IM(f_) be the image of _f_ (excluding \(\perp\)) and for each \(i\in IM(f)\) let _f_<sup>-1</sup>(_i_) be the set of all nodes _u_ that were reassigned by _f_ to the cut (_S<sub>p,f(i_)</sub>_,C<sub>p,f(i_)</sub>_,S<sub>f(i),p</sub>_). Notice that the nodes in \(V'_{big}\), which include _p_, were not assigned to any set. Thus, we get the partition of \(V'\) into \(V'_{big}\) and each set in \(\{f^{-1}(i)\}_{i\in IM(f)}\). The latter sets may satisfy property (\*\*), but \(V'_{big}\) may not; in particular, (\*\*).3 could be violated because \(V'_{big}\) does not correspond to a minimum cut, and therefore it will be handled separately shortly.<tbc>

5. if |_V<sub>small</sub>|\<n/_4 then _p_ is a failed pivot. In this situation, re-start the expansion operation at step 1 and continue choosing new pivots until \(|V_{small}|\ge n/4\), or until the number of repetitions is more than 4log_n_, in which case output "failure". We show that the latter occurs with low probability.<tbc>

6. for every \(u\in V'\backslash\{p\}\) and \(q\in C_{p,f(u)}\), query directly Max-Flow(_q,u_).<tbc>

7. finally, we recursively compute the expansion operation on each of the sets of the partition, while their sizes are bigger than 1. Let us describe what we store at the recursion node \(t_{V^\prime}\) corresponding to the just-completed expansion operation on \(V'\) with pivot _p_. We store \((|V'|-1)+\alpha(V')\) cuts in \(t_{V^\prime}\), including:<tbc>

(a) for each \(u,v\in V'_H\) we store _C<sub>u,v</sub>_.<tbc>

(b) for each node \(u_{big}\in V'_{big}\backslash\{p\}\) we store the cut (_S<sub>p,u<sub>big</sub></sub>,C<sub>p,u<sub>big</sub></sub>,S<sub>u<sub>big</sub>,p</sub>_).<tbc>

(c) for each node _u_ in one of the other sets of the partition \(\{f^{-1}(i)\}_{i\in IM(f)}\) we store the cut it was reassigned to (_S<sub>p,f(u_)</sub>_,C<sub>p,f(u_)</sub>,S<sub>f(u),p</sub>_).<tbc>

(d) for each \(u\in V'\) and \(q\in C_{p,f(u)}\) we store _C<sub>q,u</sub>_.<tbc>

<tbc>We also keep an array of pointers from each node to its corresponding cuts and also their values, and we call this array _A_. We also store, for each node of \(V'\), the name of the set in the partition that it belongs to, in an array _B_.<tbc>


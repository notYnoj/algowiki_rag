This can be justified since otherwise the minimum _uv_-cut is computed directly in step 6 of the algorithm. Our final assumption is that without loss of generality,

\(\text{Max-Flow}(p,u)\le\text{Max-Flow}(p,v).\) (3.3)

Next, there are a few cases, depending on whether any of _u,v_ is in \(V'_{big}\) or not.

1. First, consider the case when none of _u,v_ are in \(V'_{big}\). There are two sub-cases, depending on whether the values of the two cuts are equal or not.<tbc>

(a) If<tbc>

<tbc>Max-Flow(_p,u)\<_Max-Flow(_p,v),_<tbc>

<tbc>then<tbc>

<tbc>Max-Flow(_u,v_)=Max-Flow(_p,u)._<tbc>

<tbc>Observe that \(v\notin S'_{f(u),p}\) because otherwise, we would have a smaller cut than the minimum cut found for _u_. Together with 3.2 we conclude that \(v\in S'_{p,f(u)}\), and so \(\text{Max-Flow}(u,v)\le\text{Max-Flow}(p,u)\). Furthermore, if it was the case that Max-Flow(_u,v)\<_Max-Flow(_p,u_) then by 3.1 it would be that \(p\in S'_{u,v}\) or \(p\in S'_{v,u}\) which would refute the minimum cut value found for the pairs _p,v_ or _p,u_, respectively. Indeed, (_S_<sub>_p,f(u_)</sub>_,C_<sub>_p,f(u_)</sub>_,S_<sub>_f(u),p_</sub>) is the cut returned.<tbc>

(b) Otherwise,<tbc>

<tbc>Max-Flow(_p,u_)=Max-Flow(_p,v)._<tbc>

<tbc>First, we see that \(v\notin S'_{f(u),p}\). Otherwise, as \(u,v\in V_{small}\) they must have been sent to the same recursion instance, contradicting our assumption on the expansion operation on \(V'\). Like before, it implies that Max-Flow(_u,v_)=Max-Flow(_p,u_), and so for this pivot the algorithm can output (_S_<sub>_p,f(u_)</sub>_,C_<sub>_p,f(u_)</sub>_,S_<sub>_f(u),p_</sub>) as the optimal cut for _u,v_, as required.<tbc>

2. Second, we consider the case when one of the nodes is in \(V'_{big}\) and the other is in \(V'_{small}\), and we separate into three sub-cases according to their Max-Flow value to _p_. More specifically, let \(u_{big}\in V'_{big}\) and \(u\notin V'_{big}\) be nodes where the minimum cut (_S_<sub>_p,u<sub>big</sub>_</sub>_,C_<sub>_p,u<sub>big</sub>_</sub>_,S_<sub>_u<sub>big</sub>,p_</sub>) is the cut corresponding to _u<sub>big</sub>_.<tbc>

(a) If<tbc>

<tbc>Max-Flow(_p,u<sub>big</sub>)\>_Max-Flow(_p,f(u_)),<tbc>

<tbc>then \(u_{big}\notin S'_{f(u),p}\) as otherwise _u<sub>big</sub>_ would have been assigned to _f(u_), as _f(u_) is in _V<sub>small</sub>_. Together with 3.2, we have that \(u_{big}\in S'_{p,f(u)}\). We conclude that (_S_<sub>_p,f(u_)</sub>_,C_<sub>_p,f(u_)</sub>_S_<sub>_f(u),p_</sub>) is a minimum _u<sub>big</sub>v_-cut.<tbc>

(b) If<tbc>

<tbc>Max-Flow(_p,u<sub>big</sub>_)=Max-Flow(_p,f(u_)),<tbc>

<tbc>then it must be that \(u_{big}\notin S'_{f(u),p}\), since otherwise, as \(u_{big}\in V'_{big}\) and when the algo rithm examined _f(u_) it did not set _f(u<sub>big</sub>_):=_f(u_), it must have been the case for a node _x_ that was either _f(u_) or before _f(u_) in the order (i.e. such that \(\text{\textbf{value}}(C_{p,x})\le\text{\textbf{value}}(C_{p,f(u)}))\) that _u<sub>big</sub>_ was tested for the first time, with **value**(_C<sub>p,x</sub>)\>_**value**(_C_<sub>_p,u<sub>big</sub>_</sub>), and so **value**(_C_<sub>_p,f(u_)</sub>)_\>_**value**(_C_<sub>_p,u<sub>big</sub>_</sub>). However, by our assumption it holds that **value**(_C_<sub>_p,f(u_)</sub>)=**value**(_C_<sub>_p,u<sub>big</sub>_</sub>), in contradiction. Together with 3.2 we get \(u_{big}\in S'_{p,f(v)}\), and like before, the returned cut (_S_<sub>_p,f(u_)</sub>_,C_<sub>_p,f(u_)</sub>_,S_<sub>_f(u),p_</sub>) is optimal for _u<sub>big</sub>,u_.<tbc>


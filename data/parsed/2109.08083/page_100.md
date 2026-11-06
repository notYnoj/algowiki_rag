<tbc>Proposition 6.17. _Suppose that G and q_<sup>(1)</sup>_,q_<sup>(2)</sup>_,q_<sup>(3)</sup> _all satisfy the hypotheses of Theorem 6.2 whp. Then_

\(f_v(E_{G[V(G)\backslash V(M)]}(v,S_1,S_2,S_3))=\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{w,G}(u))\)<br>
\(\pm O\left(\Delta^{-\epsilon} max_{u\in\bigcup E_G(v,S_1,S_2,S_3)\backslash\{v\}}d_{w,G}(u)\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\right).\)

Proof. We have that<tbc>

\(f_v(E_{G[V(G)\backslash V(M)]}(v,S_1,S_2,S_3))=f_v(E_G(v,S_1,S_2,S_3))-(q^{(1)}-q^{(2)}+q^{(3)}).\)

<tbc>By Theorem 6.2, we have that<tbc>

\(q^{(l)}\left(\genfrac(){pt}{2}{V(M)}{l}\right)=\left(1\pm\Delta^{-\epsilon}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{l}}q^{(l)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u),\)

<tbc>for every \(l\in[3]\). We claim that

\(\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{w,G}(u))=\) (6.14)

\(f(E_G(v,S_1,S_2,S_3))-\sum_{u\in V(G)}q^{(1)}(u)d_{w,G}(u)\)<br>
\(+\sum_{\{\bar{v}\}\in\genfrac(){pt}{2}{V(G)}{2}}q^{(2)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)-\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{3}}q^{(3)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u).\)

Indeed, consider an edge \(\{v,u,w,x\}\in E_G(v,S_1,S_2,S_3)\). It contributes<tbc>

\(f_v(e)(1-d_{w,G}(u))(1-d_{w,G}(w))(1-d_{w,G}(x))\)

<tbc>to the LHS. To the RHS it contributes

\(f_v(e)\big(1-(d_{w,G}(u)+d_{w,G}(w)+d_{w,G}(x))+(d_{w,G}(u)d_{w,G}(w)\)<br>
\(+d_{w,G}(u)d_{w,G}(x)+d_{w,G}(w)d_{w,G}(x))-d_{w,G}(u)d_{w,G}(w)d_{w,G}(x)\big)\)<br>
\(\equiv f_v(e)(1-d_{w,G}(u))(1-d_{w,G}(w))(1-d_{w,G}(x)).\)

Furthermore, there are no contributions to either the LHS or the RHS other than these. It follows that

\(f(E_{G[V(G)\backslash V(M)]}(v,S_1,S_2,S_3))=\big(f(E_G(v,S_1,S_2,S_3))-\)<br>
\(\sum_{\bar{v}\in V(G)}q^{(1)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)+\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{2}}q^{(2)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)-\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{3}}q^{(3)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\big)\)<br>
\(\pm\Delta^{-\epsilon}\big(\sum_{u\in V(G)}q^{(1)}(u)d_{w,G}(u)+\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{2}}q^{(2)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\)<br>
\(+\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{3}}q^{(3)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\big),\)


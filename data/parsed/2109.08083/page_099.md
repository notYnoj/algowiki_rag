<tbc>It follows that the weight remaining in _V(G_\[_S_\]) once _M_ is removed is

(6.12) \(\sum_{v\in V(G[S])}f(v)-p_S(M)=\sum_{v\in V(G[S])}f(v)(1-d_{w,G}(v))\pm\Delta^{-\epsilon}\sum_{v\in V(G[S])}f(v)d_{w,G}(v),\)

and in particular that the number of vertices remaining in _V(G_\[_S_\]) is

(6.13) \(|V(G[S])|-p_S(M)=\sum_{v\in V(G[S])}(1-d_{w,G}(v))\pm\Delta^{-\epsilon}\sum_{v\in V(G[S])}d_{w,G}(v).\)

## 6.3.1.2. _Degree-type properties._

Let \(G\subseteq\mathcal{T}\) , \(S_1,S_2,S_3\subseteq V(\mathcal{T})\) and \(v\in V(G)\). For a function \(f_v:E(G)\rightarrow\mathbb{R}_{\ge 0}\) such that _f<sub>v</sub>(e_)=0 if \(v\notin e\), we describe \(f_v(E_G(v,S_1,S_2,S_3)):=\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\) in terms of functions on vertices of _G_. In particular taking _f<sub>v</sub>_=1, we’ll describe |_E<sub>G</sub>(v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)| in terms of functions on vertices of _G_. Given \(f_v:E(G)\rightarrow\mathbb{R}_{\ge 0}\), we let \(f_v:\genfrac(){pt}{2}{V(G)}{\le 3}\rightarrow\mathbb{R}_{\ge 0}\) be defined by

\(f_v(\bar{u})=\left\{\begin{array}{ c c }
\sum_{e\supseteq\{v\}\cup\bar{u}}f_v(e) & \text{for}v\notin\bar{u}, \\
0 & \text{otherwise}.
\end{array}\right.\)

Note that when _n_ is odd, or \(G\subseteq\mathcal{T}[I_{t_1}]\) for any _n_, \(\sum_{e\supseteq\{v\}\cup\bar{u}}f_v(e)\) sums over only one edge, since these graphs have maximum pair-degree 1. In the remaining case (when _n_ is even and \(G\unknown\subseteq\mathcal{T}[I_{t_1}]\)), the maximum pair-degree is 2.

Now we define the following function on _V(G_):<tbc>

\(q_{(G,v,S_1,S_2,S_3)}^{(1)}(u):=\left\{\begin{array}{ c c }
f_v(\{u\})\unknown_{\{\{v,u\}\subseteq e\in E_G(v,S_1,S_2,S_3)\}} & \text{for}v\neq u, \\
0 & \text{for}v=u.
\end{array}\right.\)

<tbc>Then for a matching _M_ in _G_, \(q_{(G,v,S_1,S_2,S_3)}^{(1)}(V(M))\) certainly includes the weight for each edge \(e\in E_G(v,S_1,S_2,S_3)\) such that \(v\in e\) and \((e\backslash\{v\})\cap V(M)\neq\emptyset\), but for such an edge {_v,u,w,x_}, if both _u_ and _w_ are in _M_, then the weight on the edge will be counted twice. Hence this function alone does not allow us to count precisely how the degree of a vertex into a particular subgraph of _G_ relates to _M_, and we need to modify for over-counting. Thus we define more generally<tbc>

\(q_{(G,v,S_1,S_2,S_3)}^{(l)}(\bar{u})=\left\{\begin{array}{ c c }
f_v(\bar{u})\unknown_{\{\bar{u}\cup\{v\}\subseteq e\in E_G(v,S_1,S_2,S_3)\}} & \text{for}v\notin\bar{u}, \\
0 & \text{for}v\in\bar{u},
\end{array}\right.\)

<tbc>for \(l\in[3]\). Note that for every \(G\subseteq\mathcal{T}\) , even when _n_ is even, the degree of any set of 3 vertices in _V(G_) is at most one. Then considering<tbc>

\(q_{(G,v,S_1,S_2,S_3)}^{(1)}(V(M))-q_{(G,v,S_1,S_2,S_3)}^{(2)}\left(\genfrac(){pt}{2}{V(M)}{2}\right)+q_{(G,v,S_1,S_2,S_3)}^{(3)}\left(\genfrac(){pt}{2}{V(M)}{3}\right),\)

<tbc>for some \(v\notin V(M)\), the weight of each edge \(e\in E_G(v,S_1,S_2,S_3)\) which intersects _V(M_) in more than one vertex is only counted once by the linear combination of functions. This yields that for \(v\notin V(M)\)

\(f_v(E_{[V(G)\backslash V(M)]}(v,S_1,S_2,S_3))=f_v(E_G(v,S_1,S_2,S_3))-\)<br>
\(\left(q_{(G,v,S_1,S_2,S_3)}^{(1)}(V(M))-q_{(G,v,S_1,S_2,S_3)}^{(2)}\left(\genfrac(){pt}{2}{V(M)}{2}\right)+q_{(G,v,S_1,S_2,S_3)}^{(3)}\left(\genfrac(){pt}{2}{V(M)}{3}\right)\right).\)

From now on, when it is arbitrary or clear from the context, we write _q_<sup>(_l_)</sup> in place of \(q_{(G,v,S_1,S_2,S_3)}^{(l)}\).


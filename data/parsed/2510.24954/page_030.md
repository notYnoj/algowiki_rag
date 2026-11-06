<tbc>(1) \(\Longrightarrow\) (2).

Let \(f:\{0,1\}^n\mapsto\{0,1\}^n\) be a multi-output Boolean function that can be computed by a Boolean OR-circuit with _m_ edges. Let _G_ be the DAG of the Boolean circuit computing _f_, where |_E(G_)|=_m_. Graph _G_ has source nodes \(S\subseteq V(G)\) and sink nodes \(T\subseteq V(G)\), corresponding to input gates and output gates respectively, such that |_S_|=|_T_|=_n_.

Let _H_ be a Steiner reachability shortcut of graph _G_, with \(V(G)\subseteq V(H)\) and \(E(G)\subseteq E(H)\). We may assume without loss of generality that _H_ is a DAG, by contracting all strongly connected components (SCCs) in _H_. This operation will not contract any nodes in _S_ or _T_. Additionally, we can also assume wlog that every source node in _H_ is contained in _S_, and every sink node in _H_ is contained in _T_. Consequently, we can interpret _H_ as an OR-circuit with input gates _S_ and output gates _T_. We claim that circuit _H_ computes function _f_ and satisfies Statement (2).

By Statement (1), |_E(H_)|=_s(m_)+_O(m+n_) and _H_ has depth _d(m_)+_O_(1), as desired. Since _H_ is a Steiner reachability shortcut of _G_, for all \((s,t)\in S\times T\), node _s_ can reach node _t_ in _G_ if and only if node _s_ can reach node _t_ in _H_. Then by Observation B.2, circuit _H_ must compute the same Boolean function as circuit _G_. Then circuit _H_ computes function _f_, as claimed.

(2) \(\Longrightarrow\) (1).

Let _G_ be an _n_-node, _m_-edge directed graph. We may assume wlog that \(m\ge n-1\). Likewise, we may assume wlog that _G_ is a directed acyclic graph, via the following procedure. Contract every SCC in _G_ to obtain a DAG \(G'\). Then a simple argument will show that _G_ has a Steiner reachability shortcut with _s(m_)+_O(m+n_) additional edges and depth _d(m_)+_O_(1) if and only if \(G'\) has one as well.

We will convert DAG _G_ into a circuit _C_ as follows. Let \(v_1,\dots,v_n\in V(G)\) be the nodes of graph _G_. We will define sets of new nodes _S_={_s_<sub>1</sub>_,...,s<sub>n</sub>_} and _T_={_t_<sub>1</sub>_,...,t<sub>n</sub>_}. Nodes _S_ and _T_ will become the input gates and output gates, respectively, of _C_. Let the vertex set of _C_ be \(V(C)=V(G)\cup S\cup T\). We define the edge set _E(C_) of _C_ to be

\(E(C)=E(G)\cup\bigcup_{i\in[1,n]}\{(s_i,v_i),(v_i,t_i)\}.\)

Notice that _C_ is a directed acyclic graph with source nodes _S_ and sink nodes _T_. Consequently, we can interpret _C_ as an OR-circuit with input gates _S_ and output gates _T_. We label node _s<sub>i</sub>_ with binary variable _x<sub>i</sub>_, and we label node _t<sub>i</sub>_ with binary variable _y<sub>i</sub>_, for \(i\in[1,n]\). Let \(f:\{0,1\}^n\mapsto\{0,1\}^n\) denote the Boolean function that circuit _C_ computes.

Let \(m'=|E(C)|=m+2n\). By Statement (2), there exists an OR-circuit \(C'\) with sources _S_ and sinks _T_, such that

• circuit \(C'\) computes function _f_,<tbc>

• circuit \(C'\) has \(s(m')+O(m'+n)=s(m)+O(m+n)\) edges, and<tbc>

• circuit \(C'\) has depth \(d(m')+O(1)=d(m)+O(1)\).

We convert circuit \(C'\) into a Steiner reachability shortcut _H_ of graph _G_ as follows. Let _V(H_) be the disjoint union of \(V(C')\) and the vertex set _V(G_) of _G_. We define the edge set _E(H_) of _H_ to be

\(E(H)=E(C')\bigcup_{i\in[1,n]}\{(v_i,s_i),(t_i,v_i)\}.\)

We claim that graph _H_ is a Steiner reachability shortcut of _G_ and satisfies Statement (1).

We will need the following observation about circuit \(C'\). Fix an \(i\in[1,n]\), and let _x<sub>i</sub>_=1 and _x<sub>j</sub>_=0 for \(j\neq i\). Let _f(x_<sub>1</sub>_,...,x<sub>n</sub>_)=(_y_<sub>1</sub>_,...,y<sub>n</sub>_). Then by Observation B.2, for any \(j\in[1,n]\), we have that _y<sub>j</sub>_=1 if and only if _v<sub>i</sub>_ can reach _v<sub>j</sub>_ in _G_. Since circuit \(C'\) computes function _f_, we<tbc>


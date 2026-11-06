Following Adler et al. \[1\] (and simplified a bit), we define the _rate_ of a network coding solution as follows: Let each source receive a uniform random and independently chosen message _A<sub>i</sub>_ from _A(i_). For each edge _e_, let _A<sub>e</sub>_ denote the random variable giving the message sent on the edge _e_ when executing the network coding solution with the given inputs. The network coding solution achieves rate _r_ if:

• \(H(A_i)\ge rd_i=r\) for all _i_.<tbc>

• For each edge \(e\in E\), we have \(H(A_e)\le c(e)\).

Here \(H(\cdot)\) denotes binary Shannon entropy. The intuition is that the rate is _r_, if the solution can handle upscaling the entropy of all messages by a factor _r_ compared to the demands.

## Multicommodity Flow.

A multicommodity flow problem in an undirected graph _G_=(_V,E_) is specified by a set of _k_ source-sink pairs (_s<sub>i</sub>,t<sub>i</sub>_) of nodes in _G_. We say that _s<sub>i</sub>_ is the source of commodity _i_ and _t<sub>i</sub>_ is the sink of commodity _i_. Each edge \(e\in E\) has an associated capacity \(c(e)\in\mathbb{R}^+\). In addition, there is a demand _d<sub>i</sub>_ between every source-sink pair. For simplicity, we assume _d<sub>i</sub>_=1 for all _i_ as this is sufficient for our needs.

A (fractional) solution to the multicommodity flow problem specifies for each pair of nodes (_u,v_) and commodity _i_, a flow \(f_i(u,v)\in[0,1]\). Intuitively _f<sub>i</sub>(u,v_) specifies how much of commodity _i_ that is to be sent from _u_ to _v_. The flow satisfies _flow conservation_, meaning that:

• For all nodes _u_ that is not a source or sink, we have \(\sum_{w\in V}f_i(u,w)-\sum_{w\in V}f_i(w,u)=0\).<tbc>

• For all sources _s<sub>i</sub>_, we have \(\sum_{w\in V}f_i(s_i,w)-\sum_{w\in V}f_i(w,s_i)=1\).<tbc>

• For all sinks we have \(\sum_{w\in V}f_i(w,t_i)-\sum_{w\in V}f_i(t_i,w)=1\).

The flow also satisfies that for any pair of nodes (_u,v_) and commodity _i_, there is only flow in one direction, i.e. either _f<sub>i</sub>(u,v_)=0 or _f<sub>i</sub>(v,u_)=0. Furthermore, if (_u,v_) is not an edge in _E_, then _f<sub>i</sub>(u,v_)=_f<sub>i</sub>(v,u_)=0. A solution to the multicommodity flow problem achieves a rate of _r_ if:

• For all edges \(e=(u,v)\in E\), we have \(r\cdot\sum_id_i(f_i(u,v)+f_i(v,u))=r\cdot\sum_i(f_i(u,v)+f_i(v,u))\le c(e)\).

Intuitively, the rate is _r_ if we can upscale the demands by a factor _r_ without violating the capacity constraints.

## The Undirected _k_-pairs Conjecture.

Conjecture 1 implies the following for our setting: Given an input to the _k_-pairs communication problem, specified by a directed acyclic graph _G_ with edge capacities and a set of _k_ source-sink pairs with a demand of 1 for every pair, let _r_ be the best achievable network coding rate for _G_. Similarly, let \(G'\) denote the undirected graph resulting from making each directed edge in _G_ undirected (and keeping the capacities, source-sink pairs and a demand of 1 between every pair). Let \(r'\) be the best achievable flow rate in \(G'\). Conjecture 1 implies that \(r\le r'\).

Having defined coding rate and flow rate formally, we also mention that the result of Braverman et al. \[5\] implies that if there exists a graph _G_ where the network coding rate _r_, and the flow rate \(r'\) in the corresponding undirected graph \(G'\), satisfies \(r\ge(1+\varepsilon)r'\) for a constant \(\varepsilon>0\), then there exists an infinite family of graphs {_G_<sup>∗</sup>} for which the corresponding gap is at least (lg|_G_<sup>∗</sup>|)_<sup>c</sup>_ for a constant _c\>_0. So far, all evidence suggest that no such gap exists, as formalized in Conjecture 1.


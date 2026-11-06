Thus, each update reveals the corresponding matrix entry _M_\[_i,j_\]. Since correctly answering all _p_<sup>2</sup> queries uniquely determines _M_ and \(p=\Theta(min\{\sigma,n\})\), any subset sensitivity oracle requires \(\Omega(p^2)=\Omega\left(min\{\sigma^2,n^2\}\right)\) bits of space. □

We next present our lower bound result for colorful spanning trees.

**Theorem 9.2** (Colorful Spanning Trees)**.** _Let_ \(n,\sigma\) _be positive integers with_ \(4\le\sigma\le n(n-1)\)_. There exists an n-vertex edge-colored graph carrying a base spanning tree T_<sup>∗</sup> _and a susceptible set E<sub>Q</sub> of size_ \(\Theta(\sigma)\) _such that any subset sensitivity oracle for colorful spanning tree requires_ \(\Omega(min(\sigma^2,n^2))\) _bits of space under f_=2 _updates._

_Proof._ Set \(p=min(\lfloor\sigma/4\rfloor,\lfloor(n-2)/2\rfloor)\ge 1\), which ensures that \(2p+2\le n\) and \(p+1\le\sigma\). Let \(M\in\{0,1\}^{p\times p}\) be an arbitrary boolean matrix.

We construct an undirected graph _G_=(_V,E_) on exactly _n_ vertices. First, we build the core subgraph on 2_p_+2 vertices defined by \(V_\mathrm{core}=\{s,t\}\cup X\cup Y\), where _X_={_x_<sub>1</sub>_,...,x<sub>p</sub>_} and _Y_={_y_<sub>1</sub>_,...,y<sub>p</sub>_}. The remaining _n_-(2_p_+2) vertices are added as dummy vertices to satisfy the vertex count. The edge set and color assignments for the core graph are defined as follows:

1. For each \(k\in[p]\), add the edge (_s,x<sub>k</sub>_) with color _k_. These _p_ edges have distinct colors 1_,...,p_.<tbc>

2. For each \(k\in[p]\), add the edge (_t,y<sub>k</sub>_) with color _p+k_. These _p_ edges have distinct colors _p_+1_,...,_2_p_.<tbc>

3. Add the edge (_s,t_) with color 2_p_+1.<tbc>

4. For each \((i,j)\in[p]\times[p]\) with _M_\[_i,j_\]=1, add the edge (_x<sub>i</sub>,y<sub>j</sub>_) with color _i_.

To ensure the entire graph is connected, add edges between the _n_-(2_p_+2) dummy vertices and _s_ using _n_-(2_p_+2) new, distinct colors. The total number of colors is exactly _n_-1. Define the susceptible set as \(E_Q=\{t\}\times(X\cup Y)\) (note \(|E_Q|=O(\sigma)\)).

Consider a target pair \((i,j)\in[p]\times[p]\). The _f_=2 update query _U_ consists of:

• Deletion of the edge (_y<sub>j</sub>,t_) of color _p+j_.<tbc>

• Insertion of a new edge (_x<sub>i</sub>,t_) of color _p+j_.

Let _G+U_ be the updated graph. To form a valid colorful spanning tree in _G+U_, exactly one edge from each of the _n_-1 color classes must be selected. We argue below that _G+U_ has a colorful spanning tree if and only if _M_\[_i,j_\]=1.

If _M_\[_i,j_\]=1, then the following is a colorful spanning tree of _G+U_: all edges incident to dummy vertices, edge (_s,t_), edges (_t,y<sub>k</sub>_) for \(k\neq j\), edges (_s,x<sub>r</sub>_) for \(r\neq i\), the inserted edge (_t,x<sub>i</sub>_) of color _p+j_, and edge (_x<sub>i</sub>,y<sub>j</sub>_) of color _i_. It is spanning, acyclic, and uses each color exactly once.

Now let _T_ be a colorful spanning tree of _G+U_. Since _T_ contains one edge per color, it contains all edges incident to dummy vertices, edge (_s,t_), edge (_t,y<sub>k</sub>_) for \(k\neq j\), and the inserted edge (_t,x<sub>i</sub>_) (the unique edge of color _p+j_ after the update). The vertex _y<sub>j</sub>_ is incident only to matrix edges, so _T_ must contain one or more edge of the form (_x<sub>a</sub>,y<sub>j</sub>_), where \(a\in[p]\). Let A be collection of indices \(a\in[p]\) such that (_x<sub>a</sub>,y<sub>j</sub>_) is an edge in _T_. If \(i\in\mathcal{A}\), then we have proved _M_\[_i,j_\]=1. If \(i\notin\mathcal{A}\), then the component of _y<sub>j</sub>_ in _T_ only consists of _y<sub>j</sub>_ together with degree-one vertices from _X_\\{_x<sub>i</sub>_} and cannot contain _t_. Indeed, each \(x_a\in X\) must have exactly one edge of color _a_ incident to it in _T_. This contradicts connectivity of _T_, and proves that a colorful spanning tree cannot exist if _M_\[_i,j_\]=0.


(_i)_ _For every_ \(v\in V(\mathcal{T})\) _we have that_<tbc>

<tbc>\(\frac{n}{3}-2\le E_\mathcal{T}(v,I_{t_0})\le\frac{2n}{3}+2,\)<tbc>

(_ii)_ _for every_ \(v\in I_{t_0}\) _we have that_<tbc>

<tbc>\(E_\mathcal{T}(v,I_{t_1})\ge\frac{n}{30}-2,\)<tbc>

(_iii)_ _when n is odd, for each vertex_ \(v\in(V(\mathcal{T})\backslash I_{t_1})\cap(X\cup Y)\),<tbc>

<tbc>\(|E_\mathcal{T}(v,I_{t_0}\backslash I_{t_{20}})\cap E_{AB}(\mathcal{T})|\ge\frac{n}{40}\)<tbc>

<tbc>_for_ \(AB\in\{OE,EO\}\).<tbc>

_(iv)_ _for each vertex_ \(v\in I_{t_0}\backslash I_{t_1}\)<tbc>

<tbc>\(|E_\mathcal{T}(v,I_{t_1}\backslash I_{t_{20}})\cap E_{AB}(\mathcal{T})|\ge\frac{n}{300}\)<tbc>

<tbc>_for_ \(AB\in\{EE,OO\}\).

Proof. Suppose first that \(v\in X\). For the lower bound of (i) we have that _E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>) consists of all edges that contain _v_ and a vertex from \(I_{t_0}\cap Y\) , of which there are \(\frac{4t_0}{3}+1\) such vertices. Each pair dictates a distinct edge and since \(I_{t_0}\cap(X\pm Y)=X\pm Y\) , each edge is in _E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>). By symmetry we have the same argument for \(v\in Y\) . For \(v\in X+Y\) , _E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>) contains all edges such that _v=u_<sub>1</sub>+_u_<sub>2</sub> mod _n_ where \(u_1,u_2\subseteq[-\frac{2t_0}{3},\frac{2t_0}{3}]\). Now since every vertex _v_ has degree \(n=2t_0\pm 1\) in T , and the maximum pair degree for a pair _u,v_ with \(v\in X+Y\) and \(u\in X\cup Y\) is 1, this excludes at most \(\frac{4t_0}{3}\) of these edges from _E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>) (in the case where each vertex in _V_(T)\\_I_<sub>_t_<sub>0</sub></sub> is in a different edge with _v_). By symmetry we have the same for \(v\in X-Y\) . For the upper bound, every vertex _v_ in \(Y\cup(X+Y)\cup(X-Y)\) shares an edge with every vertex in _X_ in T . Since at least \(\frac{2t_0}{3}\) vertices from _X_ are outside _I_<sub>_t_<sub>0</sub></sub>, at least this many edges (of the _n_ containing _v_ in T ) are not in _E_<sub>T</sub>(_v,I_<sub>_t_<sub>0</sub></sub>). This is similarly true for vertices in _X_, considering the vertices in _Y_\\_I_<sub>_t_<sub>0</sub></sub>. To see (ii), note that \(t_1\approx\frac{4t_0}{5}\) . For a vertex \(v\in I_{t_0}\cap X\) every pairing to a vertex in \([-\frac{2t_0}{15},\frac{2t_0}{15}]\) in _Y_ yields an edge with all other vertices in _I_<sub>_t_<sub>1</sub></sub>. By symmetry the same holds for \(v\in I_{t_0}\cap Y\) . For \(v\in I_{t_0}\cap(X+Y)\), every pair of vertices \((x,y)\in I_{t_1}\times I_{t_1}\) such that the sum is equal to _v_ and the difference is less than \(\frac{4t_0}{5}\) creates a relevant edge for _v_. There are at least \(\frac{t_0}{15}\) such pairings, and by symmetry the same is true for \(v\in I_{t_0}\cap(X-Y)\). To see (iii) and (iv), note that \(t_{20}\le 0.012t_0\). So for a vertex \(v\in X\) it suffices to ensure the choice of vertex in _Y_ has distance at least 0.012_t_<sub>0</sub> from _v_. Furthermore, any choice of vertex in _I_<sub>_t_<sub>0</sub></sub>\\_I_<sub>_t_<sub>1</sub></sub> with the same sign will result in a wrap-around edge. Restricting to when _n_ is odd, this gives at least \(\frac{2t_0}{15}-0.024t_0\ge\frac{t_0}{10}\) such edges. Half of these pairings will wrap around giving odd parity in _X+Y_ and even parity in _X-Y_ , and half will dictate an edge with even parity in _X+Y_ and odd parity in _X-Y_ . By symmetry we get the same when \(v\in Y\) . Finally, the count for (iv) follows similarly, considering now all _n_. In particular, for a vertex in \(X\cap(I_{t_0}\backslash I_{t_1})\) pairing with vertices in \([\frac{t_0}{15},\frac{2t_0}{15}]\) in _Y_ gives a non wrap-around edge with all other vertices in _I_<sub>_t_<sub>1</sub></sub>\\_I_<sub>_t_<sub>20</sub></sub>. The same is true swapping _X_ and _Y_ . For \(v\in(X+Y)\cap(I_{t_0}\backslash I_{t_1})\), if _v_ has positive index, pairing with a vertex in \([\frac{7t_0}{15},\frac{8t_0}{15}]\) gives sufficiently many edges which do not wrap around and have all other vertices contained in _I_<sub>_t_<sub>1</sub></sub>. This gives at least \(\frac{t_0}{15}-2t_{20}\ge 0.04t_0\ge n/150\) edges also avoiding _I_<sub>_t_<sub>20</sub></sub>. Half of the pairings will dictate an edge with vertices in _X+Y_ and _X-Y_ both of odd parity, and half with both of even parity. Similar


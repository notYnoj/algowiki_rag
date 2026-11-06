(_s,t_)-path \(P^*=(s,v_1^1,v_2^2,\dots,v_k^k,v_{k+1}^k,\dots,v_d^k,t)\). Likewise, if there exists an (_s,t_)-path _P_<sup>∗</sup> in _C_<sup>∗</sup>, then there exists an (_s,t_)-path _P_ in _C_. Then by Observation B.2, we conclude that circuit _C_ and circuit _C_<sup>∗</sup> compute the same binary function.

Finally, observe that circuit _C_<sup>∗</sup> has depth _O(d_)=_O_(polylog(_n_)) since every path in _C_<sup>∗</sup> can pass through at most one vertex in each layer _V<sub>i</sub>_ for \(i\in[1,d]\). Likewise, circuit _C_<sup>∗</sup> has size at most \(s_2\le s_1d=\widetilde{O}(s_1)\), since every edge in circuit _C_ is copied at most _d_ times in _C_<sup>∗</sup>.

## C Steiner Shortcut for the Lower Bound of \[VXX24\]

### C.1 Construction of \[VXX24\] Lower Bound

Before presenting our Steiner shortcut for the lower bound construction of \[VXX24\], we first give a sketch of its construction and relevant properties.

The lower bound of \[VXX24\] consists of a graph _G_ and an associated collection of critical paths P. Graph _G_ is parameterized by an integer _r_. Integer _r_ will be chosen to be a power of two.

• **Vertices** _V(G_)**.** Graph _G_ has 2_r_+1 layers, _L_<sub>0</sub>_,...,L_<sub>2_r_</sub>. The vertices of each layer can be written as a collection of points on a three-dimensional grid. Formally, for \(i\in[0,2r]\),<tbc>

<tbc>\(L_i=\{i\}\times[1,4r]\times[1,4r]\times[1,4r^2].\)<tbc>

• **Edges** _E(G_)**.** Before constructing the edge set of _G_, we define a permutation \(\sigma\) of \[0_,r_-1\] as follows. For any \(i\in[0,r-1]\), we define the _i_th element \(\sigma_i\) of \(\sigma\) as the integer whose corresponding lg(_r_)-bit binary representation can be reversed to obtain the lg(_r_)-bit binary representation of _i_. Let _v_<sub>0</sub>_,...,v_<sub>2_r_-1</sub> be a sequence of vectors where<tbc>

<tbc>\(v_i=(1,0,\sigma_{i/2})\)<tbc>

<tbc>for every even \(i\in[0,2r-1]\), and<tbc>

<tbc>\(v_i=(0,1,\sigma_{(i-1)/2})\)<tbc>

<tbc>for every odd \(i\in[0,2r-1]\).<tbc>

<tbc>For every \(i\in[0,2r-1]\) and every point \(x\in[4r]\times[4r]\times[4r^2]\), we add the edge \((i,x)\rightarrow(i+1,x)\) to edge set _E(G_), and we add the edge \((i,x)\rightarrow(i+1,x+v_i)\) to _E(G_) if \((i+1,x+v_i)\in L_{i+1}\) is a valid point in layer _L_<sub>_i_+1</sub>.<sup>9</sup><tbc>

• **Critical Paths** P**.** We define a collection P of paths in graph _G_. Towards this goal, we first define a set of source nodes \(S\subseteq L_0\). Specifically, we choose _S_ to be<tbc>

<tbc>\(S=\{0\}\times[2r]\times[2r]\times[2r^2]\subseteq L_0.\)<tbc>

<tbc>For each node \(s\in S\) and each choice of tuple \((d_1,d_2)\in[r]\times[r]\), we will define a critical path \(P_{d_1,d_2}^s\in\mathcal{P}\) that starts at node \(s\in L_0\) and ends at a node in _L_<sub>2_r_</sub>. Before we can define these critical paths, we will need to define a function \(f_d:[0,r-1]\mapsto[0,r]\) for every \(d\in[r]\). We define _f<sub>d</sub>_ as follows.<tbc>

<tbc>\(f_d(i)=\left\{\begin{array}{ c c }
\sigma_i & \sigma_i<d \\
0 & \text{else}
\end{array}\right.\)<tbc>

<tbc>We are now ready to define our critical paths P. Fix a node \(s\in S\) and a tuple \((d_1,d_2)\in[r]\times[r]\). We iteratively define a path \(P_{d_1,d_2}^s\) starting at _s_ and ending at a node in _L_<sub>2_r_</sub>. We now specify the edge that path \(P_{d_1,d_2}^s\) takes between layers _L<sub>i</sub>_ and _L_<sub>_i_+1</sub>, where \(i\in[0,2r-1]\).<tbc>

<sup>9</sup>The edge set _E(G_) is constructed using permutation \(\sigma\) to ensure Property 3 of Lemma C.1.


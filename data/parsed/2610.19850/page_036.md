## 4.3 Preimage of an _a_-nice PMC

Every _a_-nice PMC \(\Omega\) of _G_ admits an _a_-shutter _D_: either _D_={_a_} or \(a\notin D\). We show that, in both cases, we can produce another PMC very close to \(\Omega\), in terms of adjacency, and which contains _D_. Then, we will prove that such PMC is a preimage of \(\Omega\) for the neighboring function N.

We need a preliminary definition which will be useful for this purpose. We define a subset of \(\Omega\) containing the _shutter-close vertices_: they are vertices which not only undergo a separation due to _D_ but also are adjacent to it.

**Definition 22** (Shutter-close set)**.** _Consider an a-nice PMC_ \(\Omega\) _of G,_ \(S=N(C_G(a,\Omega))\) _and an a-shutter D. A_ shutter-close set _of_ \(\Omega\) _relative to shutter D is an inclusion-wise minimal set_ \(S_D\unknown S\) _satisfying the following properties:_

• _For any pair_ (_v,w_) _of vertices separated by D in_ \(G[\overline{\Omega}\cup\{v,w\}]\)_, at least one among these two vertices belongs to S<sub>D</sub>._<tbc>

• _If_ \(v\in S_D\)_, then v is fully adjacent to D,_ i.e. \(D\subseteq N_G(v)\).<tbc>

S
x
D' = {a}
a
D' 1
y
T
t1
t2
t3
z
D' 2
w
CG(a,S)
CG(T,S)

Figure 11: Another example of graph _G_ (in black) given with an _a_-nice PMC \(\Omega\) (in red). The set _D_<sub>0</sub>={_a_} separates pairs (_x,w_) in graph \(G[\overline{\Omega}\cup\{x,w\}]\). Set \(D_0=D'_0\) is not an _a_-shutter as it separates (_x,w_) but not closely (Case A). We thus fix _u_<sub>1</sub>=_x_ and _v_<sub>1</sub>=_w_ - note that we could have selected _u_<sub>1</sub>=_w_ and _v_<sub>1</sub>=_x_ but in the proof this choice is arbitrary. We compute _D_<sub>1</sub> as the close (_u_<sub>1</sub>_,v_<sub>1</sub>)-separator in \(G[\overline{\Omega}\cup\{u_1,v_1\}]\): this set is made up of the vertices filled with orange. Unfortunately, _D_<sub>1</sub> is not inclusion-wise, as its subset \(D'_1\) (surrounded by an orange area) separates pair (_y,z_). However, \(D'_1\) is an inclusion-wise minimal separator and we pursue with this set. Again, \(D'_1\) is not an _a_-shutter: it separates (_y,z_) closely as _y_ is fully adjacent to \(D'_1\) but _y_ is also adjacent to \(C(a,\Omega\cup D'_1)\). Hence, we fall into Case B. Consequently, we compute the close (_z,y_) separator _D_<sub>2</sub>, made up of the vertices filled with yellow. This time, \(D_2=D'_2\) is an _a_-shutter: it separates only pair (_z,y_), it is fully adjacent to _z_ in the pair, and _z_ is not adjacent to \(C(a,\Omega\cup D'_2)\).


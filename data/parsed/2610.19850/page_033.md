sequences of vertex-sets \((D_i)_{i\ge 0}\), \((D'_i)_{i\ge 0}\), and \((C_i)_{i\ge 1}\) so that at the last iteration \(k\ge 0\), set \(D'_k\) will be our shutter. The number of steps _k_ is linear, _i.e. k\<n_. Set \(D'_i\) is always a subset of _D<sub>i</sub>_, _i.e._ \(D'_i\subseteq D_i\).

_Iteration i_=0. We fix _D_<sub>0</sub>={_a_}. Note that _D_<sub>0</sub> is thus the separator of two vertices \(x,y\in S\), as \(\Omega\) is not a PMC of _G_\\{_a_} (Lemma 13). As it is a singleton, it is naturally inclusion-wise minimal, so we fix \(D'_0=D_0\). If all pairs separated by _D_<sub>0</sub> are separated closely, then _D=D_<sub>0</sub> makes our theorem hold: _D_<sub>0</sub> is an _a_-shutter and _D_<sub>0</sub>={_a_} (see Figure 10 for an example). From now on, we assume that _D_<sub>0</sub> does not satisfy this property: there exists a pair \((u_1,v_1)\in S\times S\) (potentially (_x,y_)) separated by _D_<sub>0</sub> in graph \(G[\overline{\Omega}\cup\{u_1,v_1\}]\) but not closely. More concretely, _a_ is an articulation point for the pair (_u_<sub>1</sub>_,v_<sub>1</sub>) but neither _u_<sub>1</sub> nor _v_<sub>1</sub> are adjacent to _a_. In this case, we show via the induction process that \(\Omega\) admits an _a_-shutter which does not contain _a_. We begin with base case _i_=1.

For any induction step \(i\ge 1\) of our algorithm, we show the following statements:

(a) _D<sub>i</sub>_ is the (_u<sub>i</sub>,v<sub>i</sub>_)-close separator in \(G[\overline{\Omega}\cup\{u_i,v_i\}]\), for some \((u_i,v_i)\in S\times S\);<tbc>

(b) \(D'_i\subseteq D_i\) is an inclusion-wise minimal separator between pairs in \(S\times S\): formally, there is no pair \((u,v)\in S\times S\) admitting some minimal (_u,v_)-separator \(D\unknown D'_i\) in graph \(G[\overline{\Omega}\cup\{u,v\}]\);<tbc>

(c) set _D<sub>i</sub>_ (and thus also \(D'_i\)) does not contain _a_;<tbc>

S
x
Do = {a}
a
y
T
t1
t2
t3
z
w
CG(a,S)
CG(T,S)

Figure 10: An example of graph _G_ (in black) given with an _a_-nice PMC \(\Omega\) (in red) with \(S=N(C_G(a,\Omega))\) and \(T=\Omega\backslash S\). Indeed, \(\Omega\) is not a PMC of _G_\\{_a_} as \((x,z)\notin\mathsf{torso}(G\backslash\{a\},\Omega)\). The connected components of \(G\backslash\Omega\) included into _C<sub>G</sub>(T,S_) are surrounded by blue dashed areas. The set _D_<sub>0</sub>={_a_} separates pair (_x,z_) in graph \(G[\overline{\Omega}\cup\{x,z\}]\), but also pairs (_y,z_) and (_x,w_) in their corresponding induced subgraph. Observe that, for instance, pair (_x,y_) is not separated by _D_<sub>0</sub> as both vertices are adjacent to at least one common blue connected component. The same statement holds for pair (_y,w_) which is directly adjacent. In this example, _D_<sub>0</sub> is an _a_-shutter: all pairs separated by _D_<sub>0</sub> - as mentioned above: (_x,z),(y,z),(x,w_) - are separated closely, as _x_, _y_ (and even _z_) are adjacent to _a_.


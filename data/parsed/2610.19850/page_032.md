<tbc>\(\Omega\) is active with regards to the minimal separator \(S\unknown\Omega\), such that \(S=N(C_G(a,\Omega))\). We fix \(T=\Omega\backslash S\). Note that the singleton {_a_} separates two vertices \(x,y\in S\) in graph \(G[\overline{\Omega}\cup\{x,y\}]\).

Our objective is thus to highlight that \(\Omega\) can be attained from another PMC \(\Omega'\) which either contains _a_ or is a PMC of _G_\\{_a_}, with a number of arcs, polynomial in _n_. This condition will allow us to state that any PMC of _G_ can be attained by PMC-BFS, where the starting set contains all PMCs of _G_ which are not _a_-nice (line 13).

From now on, we fix \(\Omega\) as the notation for the "target PMC" described above, with its bipartition _S,T_ which is function of \(a\in V(G)\): \(S=N(C_G(a,\Omega))\) and \(T=\Omega\backslash S\). Observe that (_S,T_) is a shy decomposition of \(\Omega\) (Definition 19) as, otherwise, {_a_} could not separate _x_ from _y_ (Lemma 13 and Lemma 16). Moreover, \(T\cap C_G(a,\Omega)=\emptyset\).

Our approach consists in computing a _preimage_ of \(\Omega\), _i.e._ a PMC \(\Omega'\neq\Omega\) of _G_ such that the oriented arc \((\Omega',\Omega)\) belongs to the neighborhood function (Definition 20). Then, we will establish key properties of \(\Omega'\) showing that it is in some way going closer to a PMC which is not _a_-nice. To produce the preimage PMC \(\Omega'\), we define the crucial concept of _shutter_.

**Definition 21** (Shutter of a PMC)**.** _Let_ \(a\in V(G)\) _and_ \(\Omega\) _be an a-nice PMC of G (Definition 16), let_ \(S=N(C(a,\Omega))\unknown\Omega\) _and_ \(T=\Omega\backslash S\)_. An a_-shutter<sup>5</sup> \(D\subseteq C(a,\Omega)\) _is a set of vertices satisfying:_

• _D is an inclusion-wise minimal separator of a pair_ \((u,v)\in S\times S\) _in graph_ \(G[\overline{\Omega}\cup\{u,v\}]\)_, meaning that it is not possible to have another pair_ \((u^*,v^*)\in S\times S\) _such that some proper subset of D separates u_<sup>∗</sup> _from v_<sup>∗</sup> _in_ \(G[\overline{\Omega}\cup\{u^*,v^*\}]\).<tbc>

• _For any pair_ (_u,v_) _separated by D in_ \(G[\overline{\Omega}\cup\{u,v\}]\)_, D separates pair_ (_u,v_) _closely (Definition 11) in this graph._<tbc>

• _If D does not contain vertex a,_ i.e. \(a\notin D\)_, then for each pair_ (_u,v_) _separated by D, one among these two vertices u,v is not only fully adjacent to D (condition of the previous bullet) but is also not adjacent to_ \(C_G(a,\Omega\cup D)\), i.e. _the connected component of_ \(G\backslash(\Omega\cup D)\) _containing a._

Let us explain the role played by shutters and their meaning for the PMC \(\Omega\). Looking at the shy decomposition (_S,T_) of the PMC \(\Omega\), our goal is to slightly modify the content of \(\Omega\) in _S_ (for removal) and \(C(a,\Omega)\) (for add-on) to produce another PMC \(\Omega'\). Shutters stand thus as a rather restricted way to add vertices to the PMC \(\Omega\) while removing some of _S_ to obtain a different PMC. Moreover, all vertices of the shutter are adjacent to at least one common vertex in \(\Omega\). This key fact will help us in proving that \((\Omega',\Omega)\in\mathcal{N}\). Finally, we will show how the succession of such arcs in the PMC-graph gives us the whole connectivity.

The following theorem ensures us the existence of an _a_-shutter for \(\Omega\). Moreover, it states that such _a_-shutter _D_ will not contain _a_, except if _D_={_a_}.

**Theorem 8** (Existence of shutters)**.** _Let_ \(\Omega\) _be an a-nice PMC. Then,_ \(\Omega\) _admits at least one a-shutter. Moreover, one of such a-shutter D is either D_={_a_} _or does not contain a._

_Proof._ We propose an algorithmic inductive procedure to build such _a_-shutter _D_. We will show that this algorithm finishes and indeed returns a shutter. More precisely, we produce<tbc>

<sup>5</sup>Let us say briefly a _shutter_ if there is no ambiguity on _a_.


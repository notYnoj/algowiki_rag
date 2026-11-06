For a retained description we write

\(h:=|V(G)\backslash C|.\) (11)

We now show in Proposition 7.2 that every colorable sample _S_ gives rise to at least one retained description, and that each retained description determines at most one sample. There are then only few possible descriptions, and each one is realized by a _q_-tuple with exponentially small probability.

**Proposition 7.2.** _With T and_ \(\alpha\) _as above, let_

\(q:=max\left\{4T,\left\lceil\frac{4}{\alpha}log(16k)\right\rceil\right\}.\) (12)

_For every_ \(\varepsilon\)_-far graph G, a uniformly random q-vertex induced subgraph is non-k-colorable with probability at least_ 2/3_. Consequently,_

\(S_k(\varepsilon)=O\big(\frac{klogk}{\varepsilon}\big).\) (13)

_Proof._ If _n\<q_, we sample all vertices. Since \(\varepsilon n^2>0\), an \(\varepsilon\)-far graph cannot itself be _k_-colorable, so the success probability is one.

**Get a retained description from a** _k_**-colorable** _S_

Assume \(n\ge q\), and equivalently sample a uniformly random ordered tuple _S_=(_x_<sub>1</sub>_,...,x<sub>q</sub>_) of distinct vertices. Suppose _G_\[_S_\] is _k_-colorable and fix a proper coloring \(\varphi:S\rightarrow[k]\). Run the trial coloring process with _A=S_ and choose \(i_t=\varphi(f_t)\). By Lemma 6.1, since \(|S|\ge 4T\ge T\), the run completes _T_ rounds and preserves _S_ in every cap. Lemma 6.2 gives some \(1\le t\le T\) and _C_<sup>∗</sup>=_U(P<sup>t</sup>_) such that

\(S\subseteq C^*,|V(G)\backslash C^*|\ge\alpha tn.\) (14)

The _t_ pivots occupy at most _t_ blocks. Choose a _t_-subset \(W\subseteq[2t]\) containing those blocks, adding arbitrary blocks if necessary. Let _A_<sub>0</sub> be the sample vertices in the blocks indexed by _W_, and put _B_<sub>0</sub>=_S_\\_A_<sub>0</sub>. Write

\(a:=|A_0|,b:=|B_0|=q-a.\)

Then \(\{f_1,\dots,f_t\}\subseteq A_0\subseteq S\). By Lemma 6.3, replaying the first _t_ rounds from _A_<sub>0</sub> with the same color string \(\mathbf{i}=(\varphi(f_1),\dots,\varphi(f_t))\) produces the same cap _C_<sup>∗</sup>. The ordered _u_-part (_u_<sub>1</sub>_,...,u<sub>a</sub>_) corresponding to _S_ is obtained from _A_<sub>0</sub> by listing its vertices in increasing order of their sample positions (their relative position is the same as in the ordered tuple _S_), and _v_<sub>1</sub>_,...,v<sub>b</sub>_ are obtained in the same way from _B_<sub>0</sub>. Once _t_ and _W_ are fixed, the correspondence between the ordered _q_-tuples _S_ and (_u_<sub>1</sub>_,...,u<sub>a</sub>,v_<sub>1</sub>_,...,v<sub>b</sub>_) is a bijection.

Consequently,

\((t,W,(\varphi(f_1),\dots,\varphi(f_t)),u_1,\dots,u_a,v_1,\dots,v_b)\)

is a retained description in the sense of Definition 7.1: the replay from _A_<sub>0</sub> with the color string **i** yields the cap _C_<sup>∗</sup>, and (14) gives both \(S\subseteq C^*\) and \(|V(G)\backslash C^*|\ge\alpha tn\). Hence every colorable sample _S_ admits at least one retained description (there may be multiple possible choices of _t_, _W_, \(\varphi\)).

**Recover** _S_ **from the retained description**

Conversely, the sample _S_ itself is recovered from a retained description as follows: by _W_ and the block partition we know which of the _q_ sample positions belong to the _u_-part and which to the _v_-part, the two tuples are listed in increasing order of their positions, and the vertices of the two tuples are pairwise distinct. Hence a retained description determines at most one ordered sample.

**Counting the number of retained descriptions.**


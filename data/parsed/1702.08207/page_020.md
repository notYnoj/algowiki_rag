_2._ _If the_ (_i_+1)_-st query returns a ‘down’ result, then_ \(M(x,i+1)\ge M(x,i)-(2c+1)\omega\).<tbc>

_3._ _Suppose that between some two steps of the strategy, i_<sub>2</sub>_\>i_<sub>1</sub>_, each of the queries_ (_q_<sub>_i_<sub>1</sub>+1</sub>_,...,q_<sub>_i_<sub>2</sub></sub>) _returns an ‘up’ result, and moreover, the total cost of queries performed was at least_ \(a\omega\)_, for some_ \(a\in\mathbb{N}\):<tbc>

<tbc>\(\sum_{j=i_1+1}^{i_2}w'(q_j)\ge a\omega,\)<tbc>

<tbc>_where q<sub>j</sub>_=Q<sub>A<sub>_S_</sub>_,j_</sub>(_T,x). Then,_ \(M(x,i_2)\ge M(x,i_1)+a\).

Since the value of _M(x,i_) is bounded from above by _L_, we obtain from Lemma 4.11 that the strategy A_<sub>S</sub>_ necessarily terminates when looking for target _x_ with cost at most \(L\omega+(2c+1)\omega d_x\),

\(\mathtt{COST}_{\mathcal{A}_S}(T',x)\le L\omega+(2c+1)\omega d_x.\)

Thus, due to the definition of \(\mathtt{COST}^{(\omega,c)}\) in (3.1) and the monotonicity of of the cost of a strategy with respect to vertex weights, we obtain the following:

**Corollary 4.12.** _For the sequence assignment computed by Algorithm 4.3 it holds_

\(\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T')\le\omega L.\)

To prove Proposition 3.1, it remains to show only the stability of the sequence assignment _S_.

**Lemma 4.13.** _The query sequence assignment S obtained by Algorithm 4.3 is stable._

_Proof._ We perform the proof by induction. Following the definition of stability, assume that _v_ is the root of the remaining subtree at some moment of executing A_<sub>S</sub>_ on \(T'\), and let _u_ be a vertex such that _u_ is a child of _v_ lying on the path from _v_ to the target _x_. We will show that following _S(u_) always results in a subsequence of the sequence of queries performed by following _S(v_).

Let _S_<sup>+</sup>(_v_) be the subsequence of vertices of _S(v_) which lie in _T<sub>u</sub>_, and let _S_<sup>-</sup>(_v_) be the subsequence of all remaining vertices of _S(v_). Note that _x_ belongs to _T<sub>u</sub>_ and hence any query to a node in _S_<sup>-</sup>(_v_) gives an ‘up’ reply.

We now observe the first (leftmost) difference \(v'\) of the sequences _S_<sup>+</sup>(_v_) and _S(u_). Suppose that before such a difference occurs, the common fragment of the sequences contains a query to any vertex _y_ on the path from _u_ to _x_. Then, the root of both trees moves to the same child of _y_, and the process continues identically regardless of the initial root of the tree. Thus, such a vertex _y_ cannot occur prior the difference in sequences _S_<sup>+</sup>(_v_) and _S(u_).

Next, suppose that the first difference between the two sequences consists in the appearance of vertex _v_ in sequence _S_<sup>+</sup>(_v_), i.e., \(v'=v\). Then, the root of the tree moves from _v_ to _u_, and the two processes proceed identically as required. This also implies that _t<sub>v</sub>\>t<sub>u</sub>_.

Finally, we observe that no other first difference between the sequences _S_<sup>+</sup>(_v_) and _S(u_) is possible by the formulation of Algorithm 4.3. In particular, if a triple \((\lfloor t_z\rfloor_\omega,\lceil t_z+w'(z)\rceil_\omega,z)\) is added to _C(u_) in line 9, then the condition in line 8 and _t<sub>v</sub>\>t<sub>u</sub>_ imply that the triple \((\lfloor t_z\rfloor_\omega,\lceil t_z+w'(z)\rceil_\omega,z)\) is added also to the set _C(v_). Similarly, an insertion of a triple \((\lfloor t_z\rfloor_\omega,\lceil t_z+w'(z)\rceil_\omega,z)\) for \(z\in V(T_u)\) into _C(v_) implies that this triple also belongs to _C(u_). Due to the sorting performed in line 10 of Algorithm 4.3, _S_<sup>+</sup>(_v_)=_S(u_).


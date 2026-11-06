**Algorithm 1** Algorithm for vertex-del-sr.

**Input:** A graph _G_=(_V,E_) with strict preferences _\><sub>v</sub>_ on the vertices.

**Output:** A smallest removable set \(S\subseteq V\) and a stable matching _M_ in _G-S_.

1: Set \(S\leftarrow\emptyset\) and \(M\leftarrow\emptyset\).

2: Find a stable partition \(\pi\) using Theorem 2.

3: Let _C_<sub>1</sub>_,...,C<sub>k</sub>_ be the set of odd cycles of \(\pi\) of length \(\ge 3\), and let _C_<sub>_k_+1</sub>_,...,C<sub>l</sub>_ be the set of even cycles of \(\pi\). Let \(\{v_0^i,\dots,v_{j_i}^i\}\) denote the vertices of _C<sub>i</sub>_, where \(\pi(v_{j_i}^i)=v_0^i\), and \(\pi(v_{j+1}^i)=v_{j+1}^i\) otherwise.

4: **for** _i_=1_,...,k_ **do**

5: Set \(S\leftarrow S+v_0^i\) and \(M\leftarrow M\cup\{v_{2j-1}v_{2j}|1\le j\le j_i/2\}\).

6: **end for**

7: **for** _i=k_+1_,...,l_ **do**

8: Set \(M\leftarrow M\cup\{v_{2j-2}v_{2j-1}|1\le j\le j_i/2\}\).

9: **end for**

10: **return** _S_, _M_

\(v\neq\pi(u)\), then \(\pi(v)>_vu,\pi^{-1}(v)>_vu\) or \(\pi(u)>_uv,\pi^{-1}(u)>_uv\) hold as \(\pi\) is a stable partition. As _u_ is matched to one of the vertices \(\pi(u),\pi^{-1}(u)\) and _v_ is matched to one of the vertices \(\pi(v),\pi^{-1}(v)\), _uv_ is not a blocking edge. Therefore we may assume that \(\pi(u)=v\). However, as _u_ and _v_ are not in _S_ and _uv_ is not in _M_, _v_ is matched to \(\pi(v)\) in _M_. By \(\pi(v)>_vu\), _uv_ is not a blocking edge. \(\bullet\)

It remains to show that the size of a removable set cannot be smaller than the number of odd cycles in a stable partition.

**Claim 6.** _The minimum size of a removable set is equal to the number of odd cycles of length at least_ 3 _in any stable partition_ \(\pi\).

_Proof._ Let _S_<sup>∗</sup> be a removable set, and let _M_<sup>∗</sup> be a stable matching in _G-S_<sup>∗</sup>. Since \(\pi\) is a stable partition, every odd cycle of length at least 3 in \(\pi\) must either have a vertex in _S_<sup>∗</sup> or a vertex _u_ matched in _M_<sup>∗</sup> to a partner better than \(\pi^{-1}(u)\). Indeed, if this does not hold for a cycle, then there is a vertex _v_ in the cycle that is unmatched or matched to a worse partner than \(v\pi(v)\) and \(v\pi^{-1}(v)\). But then \(\pi^{-1}(v)v\) blocks, since \(\pi^{-1}(v)\) is not matched to anyone that is better than _v_ by our assumption. We call a vertex \(v\in V\backslash S^*\) _out-dominated_ if it is matched in _M_<sup>∗</sup> to a vertex \(u\neq\pi(v)\) with \(u>_v\pi^{-1}(v)\). A vertex _u_ is an _in-dominator_ if it is the partner in _M_<sup>∗</sup> of an out-dominated vertex _v_. Note that _u_ prefers \(\pi(u)\) and \(\pi^{-1}(u)\) to _v_ because \(\pi\) is a stable partition.

Let _C_={_v_<sub>1</sub>_,...,v<sub>t</sub>_} be an arbitrary cycle of length at least 2 in \(\pi\) such that \(\pi(v_i)=v_{i+1}\), and let _v_<sub>_i_<sub>1</sub></sub>_,...,v<sub>i<sub>z</sub></sub>_ be the in-dominator vertices in _C_. Observe that these vertices are pairwise non-adjacent on the cycle _C_ as an adjacent pair would block _M_<sup>∗</sup>. Also, each of _v_<sub>_i_<sub>1</sub>-1</sub>_,...,v_<sub>_i<sub>z</sub>_-1</sub> must be either in _S_<sup>∗</sup> or out-dominated. Indeed, if for some \(1\le j\le z\) the vertex _v_<sub>_i<sub>j</sub>_-1</sub> is not in _S_<sup>∗</sup> and also not out-dominated, then the edge _v_<sub>_i<sub>j</sub>_-1</sub>_v<sub>i<sub>j</sub></sub>_ blocks as _v<sub>i<sub>j</sub></sub>_ is an in-dominator.

Suppose now that _t_ is odd. We claim that there is at least one vertex in _C_\\{_v_<sub>_i_<sub>1</sub>-1</sub>_,...,v_<sub>_i<sub>z</sub>_-1</sub>} that is either in _S_<sup>∗</sup> or is out-dominated. To see this, consider the paths obtained by removing the vertices {_v_<sub>_i_<sub>1</sub>-1</sub>_,v_<sub>_i_<sub>1</sub></sub>_,...,v_<sub>_i<sub>z</sub>_-1</sub>_,v<sub>i<sub>z</sub></sub>_} from _C_. Since _t_ is odd, one of the paths contains an odd number of vertices; we may assume that this path is _v_<sub>1</sub>_,...,v<sub>p</sub>_ for some odd _p_. If none of these vertices is deleted or out-dominated, then at least one them, say _v<sub>i</sub>_, must be unmatched or matched in _M_<sup>∗</sup> to a vertex worse than \(\pi^{-1}(v_i)\). If \(i\neq 1\), then _v_<sub>_i_-1</sub>_v<sub>i</sub>_ blocks _M_<sup>∗</sup>, a contradiction. If _i_=1, then \(v_t=\pi^{-1}(v_1)\) is an in-dominator as _v_<sub>1</sub> is the first vertex of the path. This implies<tbc>


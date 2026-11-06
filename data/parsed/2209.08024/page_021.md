### Handling many zero-weight vertices.

If almost all vertices have weight zero, then Theorem 5.4 can be improved (in terms of \(\sigma\)) by a preprocessing stage. We briefly sketch the argument.

Let T be the given tree, and _w_ be the given weight function. Let _m_ be the number of vertices with positive weight, and note that \(\sigma_w\ge m\). We first transform T by progressively removing zero-weight leaves, and replacing zero-weight degree-two vertices with an edge. This can be done with a single traversal in O(_n_) time. In the resulting tree \(\mathcal{T}'\), each zero-weight vertex has degree at least three (in particular, each leaf has positive weight). This means that at least half of the vertices in \(\mathcal{T}'\) have positive weight, so \(|V(\mathcal{T}')|\le 2m\). Computing a centroid tree _T_ on \(\mathcal{T}'\) thus requires \(\mathcal{O}(mloglog(\sigma_w+m))=\mathcal{O}(mloglog\sigma_w)\) time with Theorem 1.5 or O(_m_log_m_) with Theorem 5.3. The latter bound is better when \(\sigma_w\ge 2^m\).

It remains to show how to add the removed zero-weight vertices to the centroid tree _T_. Consider a maximal subgraph H of removed vertices. First compute a rooting _T_<sub>H</sub> of H; since all vertices in H have weight zero, _T_<sub>H</sub> is a centroid tree on H. Note that H has up to two neighbors in T , all with positive weight. Let _v_ be the neighbor of H that is farthest from the root in _T_, and attach _T_<sub>H</sub> to _T_ as a child of _v_. It is not hard to see that this requires O(_n_) time in total, and that the resulting search tree is a centroid tree of (T_,w_). Thus, we have

**Theorem 5.5.** _Let_ T _be a tree on n vertices and w be a weight function. We can compute a centroid tree of_ (T_,w_) _in time_ \(\mathcal{O}(n+mloglog\sigma)\) _or_ O(_n+m_log_m), where m is the number of vertices in_ T _with positive weight and_ \(\sigma\) _is the spread of w._

In particular, since \(m\le\sigma\), the running time becomes O(_n_) when \(\sigma\in\mathcal{O}(n/loglogn)\).

## 5.3 Lower bounds on the running time

We start with our generic construction for a lower bound.

**Lemma 5.3.** _Let_ \(k\ge 1\) _and_ \(\ell\ge 1\) _be integers. There is a tree_ \(\mathcal{T}_{k,\ell}\) _on_ \(k\cdot(\ell+1)+1\) _vertices and a class_ \(\mathcal{W}_{k,\ell}\) _of weight functions on_ \(V(\mathcal{T}_{k,\ell})\) _such that_

(_i)_ \(|\mathcal{W}_{k,\ell}|=(\ell!)^k\);<tbc>

_(ii)_ _each_ \(w\in\mathcal{W}_{k,\ell}\) _has spread_ \(\sigma_w\le k\cdot 2^{\ell+1}\);<tbc>

_(iii)_ _for each_ \(w\in\mathcal{W}_{k,\ell}\)_, there is a unique centroid tree T<sub>w</sub> of_ (T_,w), and T<sub>w</sub> has height at least_ \(\ell+1\);<tbc>

_(iv)_ _for each pair of distinct_ \(w,w'\in\mathcal{W}_{k,\ell}\)_, we have_ \(T_w\neq T_{w^\prime}\).

_Proof._ Suppose first that \(k\ge 2\). Let \(\mathcal{T}_{k,\ell}\) consist of a vertex _c_, and _k_ stars of size \(\ell+1\), with centers _v_<sub>1</sub>_,...,v<sub>k</sub>_ adjacent to _c_. The remaining \(\ell\) vertices in the star with center _v<sub>i</sub>_ are denoted \(v_{i,1},\dots,v_{i,\ell}\), for all \(1\le i\le k\). See Figure 8.

Let \(S_\ell\) denote the family of permutations of \(\{1,\dots,\ell\}\). For permutations \(\pi_1,\dots,\pi_k\in S_\ell\), let \(w=w_{\pi_1,\dots,\pi_k}\) denote the weight function defined as \(w(v_{i,j})=2^{\pi_i(j)}\), for all \(1\le i\le k\) and \(1\le j\le\ell\). In words, \(w_{\pi_1,\dots,\pi_k}\) assigns the weights \(2^1,\dots,2^\ell\) to the non-central vertices of the _i_-th star, permuted according to \(\pi_i\), for all _i_. For the remaining vertices, \(w(v_1)=\cdots=w(v_k)=0\), and _w(c_)=1. Let \(\mathcal{W}_{k,\ell}\) be the family of all such weight<tbc>


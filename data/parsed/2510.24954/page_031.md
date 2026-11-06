conclude that for all \((s_i,t_j)\in S\times T\), we have that _s<sub>i</sub>_ can reach _t<sub>j</sub>_ in \(C'\) if and only if _v<sub>i</sub>_ can reach _v<sub>j</sub>_ in graph _G_.

We will first show that graph _H_ preserves the reachability relation of _G_ between vertices in \(V(G)\times V(G)\). Suppose that node _v<sub>i</sub>_ can reach node _v<sub>j</sub>_ in graph _G_. Then since we added edges (_v<sub>i</sub>,s<sub>i</sub>_) and (_t<sub>j</sub>,v<sub>j</sub>_) to graph _H_, the above observation immediately implies that _v<sub>i</sub>_ can reach _v<sub>j</sub>_ in graph _H_.

Now suppose that _v<sub>i</sub>_ can reach _v<sub>j</sub>_ in graph _H_; we claim that _v<sub>i</sub>_ can reach _v<sub>j</sub>_ in graph _G_ as well. Let _P_ be a \(v_i\rightsquigarrow v_j\) path in graph _H_. We can write path _P_ as a concatenation of paths

\(P=P_1\circ\cdots\circ P_k,\)

where, for each \(\ell\in[1,k]\), subpath \(P_\ell\) is internally vertex-disjoint from _V(G_). For each \(\ell\in[1,k]\), let subpath \(P_\ell\) be an \(x_\ell\rightsquigarrow x_{\ell+1}\) path, where \(x_\ell,x_{\ell+1}\in V(G)\), _x_<sub>1</sub>=_v<sub>i</sub>_, and _x_<sub>_k_+1</sub>=_v<sub>j</sub>_. Notice that since path \(P_\ell\) is internally vertex-disjoint from _V(G_), path \(P_\ell\) is a path in circuit \(C'\) as well, for all \(\ell\in[1,k]\). Then by our earlier observation about circuit \(C'\), we must have that \(x_\ell\) can reach \(x_{\ell+1}\) in _G_. We have shown that \(x_\ell\) can reach \(x_{\ell+1}\) in _G_ for all \(\ell\in[1,k]\), so by the transitivity of the reachability relation, we must have that _x_<sub>1</sub>=_v<sub>i</sub>_ can reach _x_<sub>_k_+1</sub>=_v<sub>j</sub>_ in _G_. We have shown that _H_ preserves the reachability relation of _G_ between vertices in \(V(G)\times V(G)\).

Finally, we quickly observe that \(|E(H)|=|E(C')|+2n=s(m)+O(m+n)\), and _H_ has diameter _d(m_)+_O_(1), as claimed in Statement (2).

With Lemma B.3 in hand, we can now prove that our conjecture for low-depth Steiner shortcuts (Conjecture 2) is equivalent to the conjecture for low-depth OR-circuits (Conjecture 3).

**Theorem B.1.** _Conjecture 2 is equivalent to Conjecture 3._

_Proof._ First, notice that if a Boolean OR-circuit has depth _d_, then it also has diameter _d_. Therefore, by Lemma B.3, if Conjecture 3 is true, then every directed graph on _n_ nodes and _m_ edges admits a Steiner reachability shortcut with \(\widetilde{O}(m)\) additional edges and diameter polylog(_n_), so Conjecture 2 is true as well.

What remains is to prove that Conjecture 2 implies Conjecture 3. If Conjecture 2 is true, then by Lemma B.3 every Boolean function \(f:\{0,1\}^n\mapsto\{0,1\}^n\) that can be computed by a Boolean OR-circuit _C_ with size _s_<sub>1</sub> can also be computed by an OR-circuit with size \(s_2=\widetilde{O}(s_1)\) and diameter _d=O_(polylog(_n_)). We will now convert circuit _C_ into a circuit _C_<sup>∗</sup> with _depth O(d_) by a simple layering operation. Let _S_ denote the set of input gates of _C_, let _T_ denote the output gates of _C_, and let _V_ denote the set of OR gates in _C_. We will make _d_ copies of set _V_ , which we denote _V_<sub>1</sub>_,...,V<sub>d</sub>_. Sets _V_<sub>1</sub>_,...,V<sub>d</sub>_ will be the new OR gates in our new OR-circuit _C_<sup>∗</sup>. For each \(v\in V\) , we let \(v_i\in V_i\) denote the copy of _v_ in _V<sub>i</sub>_. We define the edge set of circuit _C_<sup>∗</sup> as follows:

• For each edge \((x,y)\in S\times V\) in circuit _C_, add edge \((x,y_1)\in S\times V_1\) to _C_<sup>∗</sup>.<tbc>

• For each edge \((x,y)\in V\times T\) in circuit _C_, add edge \((x_d,y)\in V_d\times T\) to _C_<sup>∗</sup>.<tbc>

• For each edge \((x,y)\in S\times T\) in circuit _C_, add edge \((x,y)\in S\times T\) to _C_<sup>∗</sup>.<tbc>

• For each edge \((x,y)\in V\times V\) , add edge \((x_i,y_{i+1})\in V_i\times V_{i+1}\) to _C_<sup>∗</sup> for every \(i\in[1,d-1]\).<tbc>

• For each \(v\in V\) and each \(i\in[1,d-1]\), add the edge \((v_i,v_{i+1})\in V_i\times V_{i+1}\) to _C_<sup>∗</sup>.

This completes the definition of the new circuit _C_<sup>∗</sup>.

We now quickly verify that circuit _C_<sup>∗</sup> computes the same function as _C_. Notice that an input gate \(s\in S\) can reach an output gate \(t\in T\) in circuit _C_ if and only if there is an (_s,t_)-path _P_=(_s,v_<sup>1</sup>_,v_<sup>2</sup>_,...,v<sup>k</sup>,t_) in _C_ of length at most _d_. If _P_ exists in _C_, then circuit _C_<sup>∗</sup> must contain the<tbc>


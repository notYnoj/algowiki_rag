**Remark 9.** It also follows from Theorem 7 that the weighted version of vertex-del-sr is NP-complete too. This can be seen from the fact that if we let the vertices of _T_ have weight 0 and other vertices have weight 1, then there is a removable set of weight 0 if and only if there is a removable set \(S\subseteq T\).

Finally, we investigate vertex-min-del-sqm. The only difference now is that each vertex _v_ has a nonnegative integer capacity _q(v_), and the aim is to achieve the existence of a stable _q_-matching by removing a minimum number of vertices. Note that if the aim was to decrease the vertex capacities by a minimum total amount, then the problem would be polynomial-time solvable. Indeed, it could be reduced to vertex-del-sr by making _q(v_) copies of each vertex. However, if we look for a minimal size removable set \(S\subseteq V\) , then the problem becomes NP-hard.

**Theorem 10.** vertex-del-sqm _is NP complete even if the capacities are at most_ 3.

_Proof._ The problem is clearly in NP. To show hardness, we reduce from com-smti, see the definition in Section 2.

Consider an instance (_G_=(_A,B;E),\>_) of com-smti, where _A_={_a_<sub>1</sub>_,...,a<sub>n</sub>_}, _B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_}, and ties are restricted to a subset \(b_1,\dots,b_\ell\), each of which have two neighbors. We create an instance of vertex-del-sqm as follows, see Figure 1c for an example. For each \(a_i\in A\), we add three agents \(a'_i\), _x<sub>i</sub>_ and \(x'_i\) with \(q(a'_i)=q(x_i)=q(x'_i)=1\). For each \(i\in[\ell]\), we add a gadget _G<sub>i</sub>_ with eight agents \(b'_i\), \(b''_i\), \(s_i^1\), \(s_i^2\), \(s_i^3\) and \(z_i^1\), \(z_i^2\), \(z_i^3\). Among these agents, \(q(b'_i)=q(b''_i)=q(s_i^1)=q(z_i^1)=3\) and \(q(s_i^2)=q(s_i^3)=q(z_i^2)=q(z_i^3)=1\). Finally, for \(i=\ell+1,\dots,n\), we add an agent \(b'_i\) with \(q(b'_i)=1\). For \(i\in[\ell]\), let \(a'_{i_1}\) and \(a'_{i_2}\) denote the two neighbors of _b<sub>i</sub>_ where _i_<sub>1</sub>_\<i_<sub>2</sub>.

a1
a2
a3
3
2
1
3
1
1
3
1
1
1
2
1
2
b1
b2
b3

x1
x2
x2
x3
x3
2
1
2
1
2
1
2
1
2
1
2
1
a'
a'
a'
a'
5
5
4
5
3
3
3
3
1
1
1
2
2
1
2
2
3
b'
b'
b2
b3
2
1
y1

x1
x2
x2
x3
x3
2
1
2
1
2
1
2
1
2
1
2
1
a'
a'
a'
5
4
5
3
3
3
3
1
1
2
1
2
b'
b'
b2
b3
3
3
2
2
b2
b3
4
3
4
3
S1
z1
2
1
2
1
2
2
2
1
2
1
S2
S1
z2
z3

(a) An instance of com-smti with ties at _b_<sub>1</sub>. Thick edges form a perfect weakly stable matching _M_.

(b) The corresponding vertex-subset-del-sr instance with \(T=\{b'_1,b''_1,y_1,b'_2\}\). Thick edges form a stable matching \(M'\) after deleting _y_<sub>1</sub> and \(b''_1\).

(c) The corresponding vertex-del-sqm instance with capacity 3 for vertices \(b'_1\), \(b''_1\), \(s_1^1\) and \(z_1^1\), and 1 otherwise. Thick edges form a stable _q_-matching \(M'\) after deleting \(b''_1\).

Figure 1: Illustrations of Theorems 7 and 10. Higher values correspond to higher preferences.


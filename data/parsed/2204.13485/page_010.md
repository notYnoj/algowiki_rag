The preference lists of the vertices \(a'_i\) for \(i\in[n]\) and \(b'_i\) for \(i=\ell+1,\dots,n\) are inherited from the original instance. We further extend the preferences as follows:

• we add \(x_i>x'_i\) to the end of each \(a'_i\)’s preference lists,<tbc>

• _x<sub>i</sub>_ has preference \(x'_i>a'_i\) and \(x'_i\) has preference \(a'_i>x_i\),<tbc>

• for \(i\in[\ell]\), the agents have the following preferences:

\(\begin{array}{ c c c }
b'_i:s_i^1>z_i^1>a'_{i_1} & s_i^1:b'_i>b''_i>s_i^2>s_i^3 & z_i^1:b'_i>b''_i>z_i^2>z_i^3 \\
b''_i:s_i^1>z_i^1>a'_{i_2} & s_i^2:s_i^3>s_i^1 & z_i^2:z_i^3>z_i^1 \\
s_i^3:s_i^1>s_i^2 & z_i^3:z_i^1>z_i^2.
\end{array}\)

Let \((G'=(V',E'),>',q)\) denote the obtained instance of vertex-del-sqm and set \(k=\ell\). We claim that there is a perfect weakly stable matching _M_ in (_G,\>_) if and only if there is a removable set \(S\subseteq V'\) with \(|S|\le k\) in \((G',>',q)\). We start with an important observation.

**Claim 11.** _The gadget G<sub>i</sub> has no stable q-matching for_ \(i\in[\ell]\)_. Furthermore, if_ \(v\in V(G_i)\) _is a vertex such that G<sub>i</sub>-v admits a stable q-matching, then_ \(v\in\{b'_i,b''_i\}\).

_Proof._ Let _G<sub>i</sub>_ be one of the gadgets. To see that _G<sub>i</sub>_ does not admit a stable _q_-matching, observe that since \(q(b'_i)=q(b''_i)=q(s_i^1)=q(z_i^1)=3\), all of them can get their two best partners, so the edges \(b'_is_i^1\), \(b'_iz_i^1\), \(b''_is_i^1\) and \(b''_iz_i^1\) must be contained in any stable _q_-matching. But then \(s_i^1\) has only one remaining capacity for \(s_i^2\) and \(s_i^3\). Thus there exists no stable _q_-matching as one of \(s_i^3s_i^1\), \(s_i^1s_i^2\) and \(s_i^2s_i^3\) blocks.

Suppose now that \(v\in V(G_i)\) is such that _G<sub>i</sub>-v_ admits a stable _q_-matching. If \(v\in\{s_i^1,s_i^2,s_i^3\}\), then, since \(z_i^1\) is the best remaining choice for both \(b'_i\) and \(b''_i\), and \(b'_i\) and \(b''_i\) are the best two choices for \(z_i^1\), the edges \(b'_iz_i^1\) and \(b''_iz_i^1\) are contained in any stable _q_-matching. But then \(z_i^1\) has only one remaining capacity for \(z_i^2\) and \(z_i^3\), thus there exists no stable _q_-matching.

The case when \(v\in\{z_i^1,z_i^2,z_i^3\}\) can be proved analogously. \(\bullet\)

Suppose there is a perfect weakly stable matching _M_. We create a _q_-matching \(M'\) in \(G'\) by adding \(a'_ib'_j\) or \(a'_ib''_j\) for each \(a_ib_j\in M\) and \(x_ix'_i\) for \(i\in[n]\). Then, for every \(i\in[\ell]\), we delete the copy of _b<sub>i</sub>_ not matched to \(A'=\{a'_i|i\in[n]\}\). Then, if \(b'_i\) got deleted, we add the edges of \(N'_i=\{b''_is_i^1,b''_iz_i^1,s_i^1s_i^2,s_i^1s_i^3,z_i^1z_i^2,z_i^1z_i^3\}\) to \(M'\) and otherwise we add \(N''_i=\{b'_is_i^1,b'_iz_i^1,s_i^1s_i^2,s_i^1s_i^3,z_i^1z_i^2,z_i^1z_i^3\}\). The number of deleted vertices is then exactly _k_. Suppose there is a blocking edge to \(M'\). It cannot contain _x<sub>i</sub>_ or \(x'_i\), since each _a<sub>i</sub>_ is with a better partner. If there is a blocking edge of type \(a'_ib'_j\), then \(j>\ell\), since \(b'_j\) (or \(b''_j\)) is matched with all of its partners if \(j\le\ell\). But by the definition of \(>'\), this means that _a<sub>i</sub>b<sub>j</sub>_ is blocking _M_, contradiction. Finally, the edges \(s_j^2s_j^3\) and \(z_j^2z_j^3\) also do not block \(M'\), because \(s_j^3\) and \(z_j^3\) are matched with their best partner in \(M'\) for each \(j\le\ell\).

Now assume that there is a set \(S\subseteq V'\) with \(|S|\le k\) such that there is a stable _q_-matching \(M'\) in \(G'-S\). Each \(a'_i\) must be matched to some \(b'_j\) or \(b''_j\), since otherwise there would be no stable matching because of the cycle \(\{a'_i,x_i,x'_i\}\). Also, for any \(j\in[\ell]\), at most one of \(b'_j\) and \(b''_j\) can be matched to some \(a'_i\), since by claim 11 one of them has to be deleted, otherwise there would be a gadget _G<sub>i</sub>_ where at least two vertices are deleted (it is also clear that deleting vertices outside _V(G<sub>i</sub>_) cannot create a stable _q_-matching in _G<sub>i</sub>_), contradicting \(|S|\le k\). Therefore, \(M'\) induces a perfect matching _M_ in the original instance. If there is an edge blocking _M_, then the copy of the same edge is blocking \(M'\), contradiction.


**Correctness.** If the algorithm terminates in Step (ii), correctness follows directly from Theorem 4.7. If this is not the case, correctness follows from this claim.

\(\square\) Claim 4.9. **G** _is AT-free if and only if_ **T** _is triangle-free._

Proof. To prove the forward direction, suppose **T** contains a triangle with vertices {_A,B,C_}. We claim that their representatives _r<sub>A</sub>,r<sub>B</sub>,r<sub>C</sub>_ form an AT in **G**. Since {_A,B_}, {_B,C_}, and {_C,A_} are edges in **T**, it follows by construction that {_r<sub>A</sub>,r<sub>B</sub>_}, {_r<sub>B</sub>,r<sub>C</sub>_}, and {_r<sub>C</sub>,r<sub>A</sub>_} are non-edges in **G**. Furthermore, since {_A,B_} and {_C,A_} are edges in **T**, we must have _C<sub>r<sub>A</sub></sub>(r<sub>B</sub>)=C<sub>r<sub>A</sub></sub>(r<sub>C</sub>)=A_. This implies the existence of an _r<sub>B</sub>-r<sub>C</sub>_ path in **G** that avoids the neighborhood _N[r<sub>A</sub>_]. By symmetry, there exist _r<sub>A</sub>-r<sub>C</sub>_ and _r<sub>A</sub>-r<sub>B</sub>_ paths that avoid _N[r<sub>B</sub>_] and _N[r<sub>C</sub>_], respectively.

Conversely, assume that {_a,b,c_} is an AT in **G**. Let _A_:=_C<sub>a</sub>(b_)=_C<sub>a</sub>(c_), _B_:=_C<sub>b</sub>(a_)=_C<sub>b</sub>(c_), and _C_:=_C<sub>c</sub>(a_)=_C<sub>c</sub>(b_). Note that if {_r<sub>A</sub>,r<sub>B</sub>,r<sub>C</sub>_}={_a,b,c_}, then _r<sub>A</sub>,r<sub>B</sub>,r<sub>C</sub>_ is an AT: the previously established argument for the forward direction applies conversely to show that _A,B,C_ forms a triangle in **T**.

Thus, it suffices to show that _r<sub>A</sub>,b,c_ remains an AT in **G**. Note that _r<sub>A</sub>_ must be distinct from _b,c_, since _b,c_ are vertices in **G**_<sub>r<sub>A</sub></sub>_. If we can demonstrate that the property of being an AT is preserved when replacing _a_ with the corresponding representative _r<sub>A</sub>_, then by symmetry, replacing _b_ with _r<sub>B</sub>_ ensures that _r<sub>A</sub>,r<sub>B</sub>,c_ is an AT. Applying this logic once more implies that _r<sub>A</sub>,r<sub>B</sub>,r<sub>C</sub>_ is an AT, and thus we get the existence of the triangle _A,B,C_ in **T**.

Assume \(r_A\neq a\), as the case _r<sub>A</sub>=a_ is trivial. Since \(A\in C_a\) and \(A\in C_{r_A}\), we observe that \(N(r_A)\cap A=\emptyset\); otherwise, _A_ could not be a connected component in **G**_<sub>r<sub>A</sub></sub>_. Because \(b,c\in A\), this immediately implies that _r<sub>A</sub>_ is non-adjacent to both _b_ and _c_.

Furthermore, since _A_ is a component in **G**\\_N[r<sub>A</sub>_], there exists a _b-c_ path that avoids _N[r<sub>A</sub>_]. To prove that {_r<sub>A</sub>,b,c_} is an AT, it remains to show that there exists a _b-r<sub>A</sub>_ path avoiding _N[c_] and, by symmetry, a _c-r<sub>A</sub>_ path avoiding _N[b_]. As _a,b,c_ is an AT, there already exists a _b-a_ path \(\pi\) that avoids _N[c_]. Let \(a'\) be the neighbor of _a_ on \(\pi\). Without loss of generality, we can assume \(a'\in N(a)\cap N(A)\). We now consider two cases for the construction of the _b-r<sub>A</sub>_ path:

\(\includegraphics{}\text{If}r_A\in N(a)\text{, we concatenate}\pi\text{with the edge}\{a,r_A\}\text{. Since}r_A\notin N(c)\text{, this path avoids}N[c]\text{.}\includegraphics{}\text{If}r_A\notin N(a)\text{, we note that}r_A\notin A\text{(otherwise}A\text{would not be a component in}\mathbf{G}\backslash N[r_A]\text{). By Proposition 4.3 applied to}a,r_A\text{, and any}v\in A\text{, it follows that every vertex}v\in N(a)\cap N(A)\text{must also be a neighbor of}r_A\text{. In particular,}a'\in N(r_A)\text{. We can therefore construct a valid path by concatenating the}b-a'\text{subpath of}\pi\text{(which avoids}N[c]\text{) with the edge}\{a',r_A\}\text{.}\square\)

**Runtime.** Step (i) and Step (iii) take time \(\tilde{\mathcal{O}}(n^\omega)\). On the other hand, Step (ii) only takes time \(\tilde{\mathcal{O}}(n^2)\).

## 4.3 Listing Dominating Pairs in Matrix Multiplication Time

\(\blacktriangleright\) **Main Theorem 3.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm for listing all dominating pairs._

**Proof.** Let **G**=(_V,E_) be an undirected graph.

We begin by observing that we may assume each **G**_<sub>v</sub>_ contains at least one node. Indeed, if this were not the case, then _N[v_]=_V_ . In such an instance, _v_ can be removed from **G** because it is already known that _v_ is adjacent to every vertex (and path) in **G**. Moreover, in this case we know that _u,v_ constitutes a dominating pair for all \(u\in V\backslash\{v\}\).

Now, for each pair of distinct nodes \(u,v\in V\) , we must determine whether _u,v_ constitutes a dominating pair. To this end, we observe that _u,v_ is a dominating pair if and only if for each node \(w\notin N[u]\cup N[v]\), we have \(C_w(u)\neq C_w(v)\). This condition follows because \(C_w(u)\neq C_w(v)\) indicates that there is no _u-v_ path that avoids the neighborhood of _w_. Conversely, for any node \(w\in N[u]\cup N[v]\), every _u-v_ path trivially intersects the closed neighborhood of _w_, as either _u_ or _v_ lies in _N[w_]; and for any node \(w\notin N[u]\cup N[v]\), if we have \(C_w(u)\neq C_w(v)\), then any _u-v_ path must intersect _N(w_).


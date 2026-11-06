## C Complete Hardness Proofs

### C.1 List enforcement for flipping

We prove Theorem 4 in full detail. Let (_G,q,L_) be an instance of List Coloring, and let _C_ be a vertex cover of _G_ of size _k_. The empty graph is a trivial yes-instance and can be handled separately. We delete colors that occur in no list and relabel the remaining palette. If some vertex has an empty list, we return a fixed no-instance. Thus, _q_ is at most the explicit list-encoding length. Put _n_=|_V(G_)| and _b=n_. Construct _H_ from a copy of _G_. Give every original vertex initial color 1. For every original vertex _v_ and every color \(c\in[q]\backslash L(v)\), add _b_+1 pendent vertices adjacent only to _v_, all initially colored _c_. This is a polynomial construction with the same palette.

If \(\psi\) is a proper list coloring of _G_, flip each original vertex whose initial color differs from \(\psi(v)\) and leave all pendent vertices unchanged. At most _n=b_ flips are used. Edges inside the copy of _G_ are proper because \(\psi\) is proper. If a pendent vertex at _v_ has color _c_, then \(c\notin L(v)\) and hence \(\psi(v)\neq c\), so its edge is proper as well.

Conversely, suppose a proper coloring of _H_ is reachable with at most _b_ flips. If an original vertex _v_ ends with a forbidden color _c_, each of its _b_+1 pendent vertices initially colored _c_ must end with another color. This already requires more than _b_ flips. Thus every original vertex receives a color from its list, and restriction to _G_ is a proper list coloring.

It remains to bound the parameters. The graph _G-C_ is independent. After deleting _C_ from _H_, every original vertex outside _C_ is the center of a star of pendent vertices, while pendent vertices whose center belongs to _C_ become isolated. Hence _H-C_ is a forest and \(\text{fvs}(H)\le k\).

u 1
u 5
w 1
w 5
w 1
u
v
w
u
w
b 5
x
x
x
x
5
List Coloring Coloring Discovery

**Fig.4.** The list-enforcement gadget, illustrated for _b_=4. For every \(c\in[q]\backslash L(v)\), the vertex _v_ receives _b_+1 pendent vertices initially colored _c_. Dotted segments abbreviate omitted vertices.


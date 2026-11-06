Hence, for any \(v\notin\{z_1,z_2\}\) we have that \(\kappa(f',v)\le\kappa(f,v)\), and for \(v\in\{z_1,z_2\}\) we have that \(\kappa(f',v)<\kappa(f,v)\), a contradiction.

By a very similar proof, one can show how to decrease the crossing weight when there exist two support paths that share a terminal and cross once at another node. A consequence of this lemma is that by taking a minimum cost flow, which subject to that also minimizes the crossing weight, we may assume flow paths cross at most once. We thus obtain Theorem 3.3 as a corollary.

## A.3 Nested Supports Lemma

This subsection is dedicated to a proof of Theorem 3.6.

For a face _F_ and support path \(P\in\mathrm{supp}(x^F)\), we let _C(P_) be the embedded cycle obtained by taking the demand _h_ that _P_ routes and embedding it within the open interior of the face _F_ to join the ends of _P_. Note that the embeddings of different demand edges within a face _F_ may cross each other (but of course, for different faces the demands do not cross, and moreover no demand edge crosses any supply edge).

Finally, some more terminology and notation. Recall that for a (simple) cycle _C_, we use Int(_C_) and int(_C_) for the closed and open interior respectively of the region bounded by _C_. Additionally, when we say an object is contained within a face _F_, we are not referring to the boundary of _F_, but the region of the plane that corresponds to _F_.

**Lemma A.2** (Face Uncrossing Lemma)**.** _Let_ (_G,H,u,d_) _be a facial multiflow instance that is feasible, and let_ \((H_F:F\in\mathcal{F})\) _be a facial decomposition. There exists a feasible flow x such that the following holds: for every pair of distinct faces_ \(F_1,F_2\in\mathcal{F}\) _and any_ \(P_1\in\mathrm{supp}(x^{F_1})\) _and_ \(P_2\in\mathrm{supp}(x^{F_2})\)_, the paths P_<sub>1</sub> _and P_<sub>2</sub> _do not cross, and (more strongly) the cycles C(P_<sub>1</sub>) _and C(P_<sub>2</sub>) _do not cross._

_Proof._ Augment the instance by adding leaves as follows: for every face _F_ and demand \(h=(s,t)\in H_F\), add leaves (_s<sub>h</sub>,s),(t<sub>h</sub>,t_) of capacity equal to _d(h_) and embed the leaves into the face _F_, and move the demand _h_ from (_s,t_) to (_s<sub>h</sub>,t<sub>h</sub>_). We keep the same facial decomposition and still embed the demand edge (_s<sub>h</sub>,t<sub>h</sub>_) within the face _F_ (accepting that demand edges within _F_ may cross). It suffices to prove that, for this augmented instance, there exists a feasible flow _x_ such that for distinct faces \(F_1,F_2\in\mathcal{F}\) and paths \(P_1\in\mathrm{supp}(x^{F_1}),P_2\in\mathrm{supp}(x^{F_2})\), the cycles _C(P_<sub>1</sub>) and _C(P_<sub>2</sub>) do not cross (since by contracting the added leaves, we obtain the desired flow for the original instance).

Let _x_ be a feasible flow for the augmented instance such that any pair of support paths crosses at most once, which exists by Theorem 3.3. Let _F_<sub>1</sub>_,F_<sub>2</sub> be distinct faces, and let \(P_1\in\mathrm{supp}(x^{F_1}),P_2\in\mathrm{supp}(x^{F_2})\). Suppose for the sake of contradiction that _C(P_<sub>1</sub>) and _C(P_<sub>2</sub>) cross. Cycles that cross must cross at least twice. However, since _C(P_<sub>1</sub>)_,C(P_<sub>2</sub>) do not share their leaf edges or demand edges, these crossings must happen on subpaths of the paths _P_<sub>1</sub>_,P_<sub>2</sub>. But then this contradicts that _P_<sub>1</sub>_,P_<sub>2</sub> cross at most once.

_Proof of Theorem 3.6._ We again augment the instance by adding leaves, as in the proof of Theorem A.2. Let _x_ be a flow as resulting from Theorem A.2. First, we can assume without loss of generality that for each face _F_, \(E(F)\subseteq\mathrm{supp}(x^F)\) (and in particular, _F_ is a face of _G_\[supp(_x<sup>F</sup>_)\]). If this is not the case for some face _F_, we can add new demands parallel to each edge of _E(F_) of demand weight \(\epsilon>0\), and increasing the capacity of each edge in _E(F_) by \(\epsilon\), and extend _x_ by routing along these single-edge paths. This does not introduce any new crossings. Now, it suffices to show the nested supports property holds for _x_.

By using parallelizations, we may assume all paths are edge-disjoint. Consider two distinct faces _F_<sub>1</sub>_,F_<sub>2</sub>. To simplify the notation, for _i_=1,2 let _x<sup>i</sup>=x<sup>F<sub>i</sub></sup>_ and let \(G_i=G[\mathrm{supp}(x^i)]=G[\mathrm{supp}(x^i)\cup E(F_i)]\). For _i_=1,2, we will use the notation <o>_i_</o> to mean the number in {1,2}\\{_i_}. First, we prove that for each \(i\in\{1,2\}\), _G<sub>i</sub>_ is contained in a single face of \(G_\overline{i}\). We will deal with the stellated supports at the end.

Observe that for \(i\in\{1,2\}\) and any \(P\in\mathrm{supp}(x^i)\), the other face \(F_\overline{i}\) is contained in either Ext(_C(P_)) or Int(_C(P_)).

**Claim A.3.** _Let_ \(i\in\{1,2\}\).


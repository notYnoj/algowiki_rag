• _If the face F<sub>i</sub> is contained in_ Int(_C(P_)) _for_ \(P\in\mathrm{supp}(x^\overline{i})\)_, then every path_ \(Q\in\mathrm{supp}(x^i)\) _is contained in_ Int(_C(P_))_, and hence G<sub>i</sub> is contained in_ Int(_C(P_)).<tbc>

• _If the face F<sub>i</sub> is contained in_ Ext(_C(P_)) _for_ \(P\in\mathrm{supp}(x^\overline{i})\)_, then every path_ \(Q\in\mathrm{supp}(x^i)\) _is contained in_ Ext(_C(P_))_, and hence G<sub>i</sub> is contained in_ Ext(_C(P_)).

_Proof._ Suppose that _F<sub>i</sub>_ is contained in Int(_C(P_)) for \(P\in\mathrm{supp}(x^\overline{i})\). The cycle _C(Q_) has an edge (namely, its demand edge) that lies in int(_C(P_)). If it leaves Int(_C(P_)), it must cross the cycle _C(P_), which means it must cross the path _P_. This contradicts the earlier claim. The case for Ext(_C(P_)) is similar.

We say _F<sub>i</sub>_ is _universally exterior_ if _F<sub>i</sub>_ is contained in Ext(_C(P_)) for all \(P\in\mathrm{supp}(x^\overline{i})\). Note that if _F<sub>i</sub>_ is universally exterior, then by Theorem A.3, _G<sub>i</sub>_ is contained in Ext(_C(P_)) for all \(P\in\mathrm{supp}(x^\overline{i})\).

**Claim A.4.** _Either F_<sub>1</sub> _is universally exterior or F_<sub>2</sub> _is universally exterior._

_Proof._ There are two cases.

Case 1: there exists \(P_1\in\mathrm{supp}(x^1)\) such that _F_<sub>2</sub> is contained in Int(_C(P_<sub>1</sub>)). Now, consider \(P_2\in\mathrm{supp}(x^2)\). Then by Theorem A.3, we have that _P_<sub>2</sub> is contained in Int(_C(P_<sub>1</sub>)), and consequently _P_<sub>1</sub> is contained in Ext(_C(P_<sub>2</sub>)). Furthermore, this implies that _F_<sub>1</sub> is contained in Ext(_C(P_<sub>2</sub>)), since if _F_<sub>1</sub> were contained in Int(_C(P_<sub>2</sub>)), then Theorem A.3 would imply that _P_<sub>1</sub> is contained in Int(_C(P_<sub>2</sub>)). Hence _F_<sub>1</sub> is universally exterior.

Case 2: there does not exist \(P_1\in\mathrm{supp}(x^1)\) such that _F_<sub>2</sub> is contained in Int(_C(P_<sub>1</sub>)). Then _F_<sub>2</sub> is contained in Ext(_C(P_<sub>1</sub>)) for all \(P_1\in\mathrm{supp}(x^{H_{F_1}})\), and _F_<sub>2</sub> is universally exterior.

**Claim A.5.** _If F<sub>i</sub> is universally exterior, then the other support graph_ \(G_\overline{i}\) _is entirely contained within a single face of G<sub>i</sub> (note that this face is possibly bounded or unbounded)._

_Proof._ Let \(F_i^*\) be the face of _G<sub>i</sub>_ that contains \(F_\overline{i}\). We will show that for all \(P\in\mathrm{supp}(x^\overline{i})\), the cycle _C(P_) is contained in \(F_i^*\), which proves the claim.

Let _h_ be the (embedded) demand edge routed by _P_. Certainly the demand _h_ is contained in the interior of \(F_i^*\) since it is embedded in the interior of \(F_\overline{i}\). Now, if _C(P_) ever leaves \(F_i^*\), then there exists a node _v_ that is incident with four distinct edges that alternate in clockwise order between _C(P_) and supp(_x<sup>i</sup>_). Say listed in clockwise order these are _e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>_,e_<sub>4</sub>, where \(e_1,e_3\in C(P)\) and \(e_2,e_4\in\mathrm{supp}(x^i)\). However, since _C(P_) is a simple cycle, then at least one of _e_<sub>2</sub>_,e_<sub>4</sub> must enter int(_C(P_)), which contradicts that _F<sub>i</sub>_ is universally exterior.

Now, suppose without loss of generality that _F_<sub>1</sub> is universally exterior, and thus _G_<sub>2</sub> is contained in a single face \(F_1^*\) of _G_<sub>1</sub>. If _F_<sub>2</sub> is also universally exterior, then we are done. So suppose not. Then there exists \(P_1\in\mathrm{supp}(x^1)\) such that _F_<sub>2</sub> is contained in Int(_C(P_<sub>1</sub>)), and hence by Theorem A.3 we have that _G_<sub>2</sub> is contained in Int(_C(P_<sub>1</sub>)). Therefore the face \(F_1^*\) of _G_<sub>1</sub> that contains _G_<sub>2</sub> must be a bounded face. It then follows that _G_<sub>1</sub> must be contained within the unbounded face of _G_<sub>2</sub>.

Thus we have proven that for each _i_, _G<sub>i</sub>_ is contained in a single face of \(G_\overline{i}\). For each _i_, let _S<sub>i</sub>_ be the star graph added to _G<sub>i</sub>_ to obtain _G_\[_x,F<sub>i</sub>_\] (so that _G_\[_x,F<sub>i</sub>_\]=_G<sub>i</sub>+S<sub>i</sub>_.

Now fix an \(i\in\{1,2\}\). Let \(F_i^*\) be the face of _G<sub>i</sub>_ that contains \(G_\overline{i}\). First, observe that \(G[x,F_\overline{i}]=G_\overline{i}+S_\overline{i}\) is still contained in that same face of _G<sub>i</sub>_, since the star \(S_\overline{i}\) is added into the open interior of \(F_\overline{i}\) and its embedding is completely disjoint from \(G_\overline{i}\).

So \(G[x,F_\overline{i}]\) is contained in a single face \(F_i^*\) of _G<sub>i</sub>_. The only way that \(G[x,F_\overline{i}]\) is not contained in a single face of _G<sub>i</sub>+S<sub>i</sub>=G_\[_x,F<sub>i</sub>_\] is if adding the star _S<sub>i</sub>_ divides \(F_i^*\) into multiple faces. However, for this to happen we would need that \(F_i^*=F_i\) (recall that _F<sub>i</sub>_ is a face of _G<sub>i</sub>_, since we assumed that \(E(F_i)\subseteq\mathrm{supp}(x^{F_i})\)). However, it cannot be the case that \(F_i^*=F_i\), since the leaves added to \(F_\overline{i}\) are not contained in _F<sub>i</sub>_ but are in \(G_\overline{i}\).

Thus \(G[x,F_\overline{i}]\) is contained in a single face of _G_\[_x,F<sub>i</sub>_\]. By a symmetric argument we have that _G_\[_x,F<sub>i</sub>_\] is contained in a single face of \(G[x,F_\overline{i}]\) This concludes the proof.


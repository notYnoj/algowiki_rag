• \(T=\Omega\backslash S\) _is included into a connected component C of G_\\_S full for S: N<sub>G</sub>(C_)=_S,_<tbc>

• _S is_ \(\Omega\)_-shy with regard to C._

_Proof._ We recall that for any PMC \(\Omega\), given a minimal separator \(S\unknown\Omega\), the set \(\Omega\backslash S\) is included into one single full component of _S_ (Lemma 10). We proceed by proving the following claim.

_Claim:_ Given a PMC \(\Omega\), one of its minimal separator \(S\unknown\Omega\) and _C_ the full component of _S_ containing \(T=\Omega\backslash S\), at least one of the two possibilities holds:

• either there is no connected component _B_ of _G_\[_C_\\_T_\] such that \(S\subseteq N_G(B)\),<tbc>

• or there is another minimal separator \(S'\unknown\Omega\) such that \(S\unknown S'\).

We start by proving this claim. Assume that the first item is not satisfied: there is a connected component _B_ of _G_\[_C_\\_T_\] full for _S_. Hence, \(S\subseteq N(B)\unknown\Omega\).

At least one vertex \(u\in T\) is adjacent to _B_ as \(B\subseteq C\) and _C_ is a connected component of _G_\\_S_. Otherwise, _B_ would be a full component for _S_ different from _C_. Formally, \(B\subseteq R_G^+(u,\Omega)\) or more concisely \(u\in N(B)\). Meanwhile, _B_ obviously cannot see all the vertices of \(\Omega\) as it would contradict that \(\Omega\) is a PMC (and thus a shy set). It follows that there exists a vertex \(v\in T\) which is not adjacent to _B_: \(B\cap R_G^+(v,\Omega)=\emptyset\).

We fix \(S'=N_G(B)\). Remember that \(S'\) is a minimal separator of _G_, according to Lemma 9, because _B_ is a connected component of \(G\backslash\Omega\). As stated above, \(S\unknown N(B)\) and also \(u\in N(B)\). Finally, \(S\unknown S'\) and \(S'\unknown\Omega\). Figure 7 illustrates this reasoning with an example.

We conclude about the statement of the lemma. The claim above provides us with a procedure to build the larger minimal separator with the required property. Start with an arbitrary minimal separator \(S\unknown\Omega\). By the claim, we know that either _S_ admits no full<tbc>

S
B
T
u
S'
v
C

S'
B
T'
u
v
C'

(a) An example of graph _G_ with a PMC \(\Omega=S\cup T\) surrounded by red lines. The connected component _B_ of _G_\[_C_\\_T_\] is full for _S_, hence _S_ is not \(\Omega\)-shy with regards to _C_. Separator \(S'=N(B)\) - surrounded by yellow lines - is also a minimal separator of _G_, included into \(\Omega\), satisfying \(S\unknown S'\).

(b) The new decomposition \((S',T')\) with separator \(S'\) and \(T'=\Omega\backslash S'\). Here, \(C'\) represents the (unique) connected component of \(G\backslash S'\) containing \(T'\), observe that \(B\cap C'=\emptyset\). No component of \(G[C'\backslash T']\) is full for \(S'\), so \(S'\) is \(\Omega\)-shy with regard to \(C'\).

Figure 7: Illustration of the proof: how _S_ can be extended if it does not satisfy Lemma 15.


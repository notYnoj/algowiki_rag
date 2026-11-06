fixing \(S'_D=\Omega'\cap S_D\), we have \(\Omega'=D\cup(\Omega\backslash S_D)\cup S'_D\).

Let us show now that \((\Omega',\Omega)\in\mathcal{N}\). The arguments are very similar to the ones used in Theorem 9. We guess \(u^*\in D\), and we add _N<sub>G</sub>(u_<sup>∗</sup>) to \(\Omega'\): \(X^*=\Omega'\cup N_G(u^*)\). Note the following key fact: \(\Omega\backslash\Omega'\) is included into _N<sub>G</sub>(u_<sup>∗</sup>) as \(\Omega\backslash\Omega'\subseteq S_D\) and by definition, vertices of _S<sub>D</sub>_ are adjacent to every vertex of _D_. In brief, \(\Omega\unknown X^*\). We guess some _b_<sup>∗</sup> which belongs to \(T\subseteq\Omega\cap\Omega'\). As \(u^*\in C_G(a,S)\) and \(b^*\in C_G(T,S)\), _S_ is a minimal (_b_<sup>∗</sup>_,u_<sup>∗</sup>)-separator. More precisely, set _S_ is the _X_<sup>∗</sup>-close (_b_<sup>∗</sup>_,u_<sup>∗</sup>)-separator in _G_: as \(\Omega\) is a PMC of _G_, there is a path from _b_<sup>∗</sup> to each \(s\in S\) whose internal vertices belong to <o>_X_</o><sup>∗</sup>. So _S_<sup>∗</sup>=_S_. Finally, we only keep vertices of \(X^*\cap(S^*\cup C_G(b^*,S^*))=\Omega\).

An example of preimage \(\Omega'\), highlighted by Theorem 10, is shown in Figure 13 on the same setting than in Figure 11.

## 4.3.3 Conclusions on PMC neighborhood

Finally, we present a statement summarizing our contributions in subsection 4.3: any _a_-nice PMC admits a preimage which is "closer" to some PMC which is not _a_-nice.

**Theorem 11** (Preimage of an _a_-nice PMC)**.** _Let_ \(\Omega\) _be an a-nice PMC of G. There exists a PMC_ \(\Omega'\neq\Omega\)_, satisfying_ \((\Omega',\Omega)\in\mathcal{N}\)_, such that_ \(\Omega'\) _either contains a or otherwise_ \(C_G(a,\Omega')\unknown C_G(a,\Omega)\).

_Proof._ From Theorem 8, \(\Omega\) admits an _a_-shutter _D_. Either _D_={_a_}: in this case, from Theorem 9, there is a PMC \(\Omega'=\Omega_a\) which contains _a_ and such that \((\Omega',\Omega)\in\mathcal{N}\). Otherwise, \(a\notin D\): from Theorem 10, there exists a PMC \(\Omega'\) such that \((\Omega',\Omega)\in\mathcal{N}\) and moreover, \(C_G(a,S')\unknown C_G(a,S)\), reusing the notation from Theorem 10. In both PMCs, _S_ (resp. \(S'\)) is the neighborhood of the connected component of \(G\backslash\Omega\) (resp. \(G\backslash\Omega'\)) containing _a_. Hence, \(C_G(a,S)=C_G(a,\Omega)\) and \(C_G(a,S')=C_G(a,\Omega')\). This completes the proof.

The direct consequence of this result is a connectivity result on PMC neighborhood N which allows us to conclude that PMC-BFS will find all _a_-nice PMCs.

**Corollary 3.** _Let_ \(\Omega\) _be an a-nice PMC of G. There exists a sequence of PMCs_ \(\Omega^{(r)},\dots,\Omega^{(2)},\Omega^{(1)}\) _with_ \(r\ge 2\)_, such that:_

• \(\Omega^{(1)}=\Omega\),<tbc>

• \(\Omega^{(r)}\) _is not a-nice,_<tbc>

• _for each_ \(2\le i\le r\), \((\Omega^{(i)},\Omega^{(i-1)})\in\mathcal{N}\).

_Proof._ According to Theorem 11, the PMC \(\Omega\) admits a preimage \(\Omega'\) which either contains _a_ or satisfies \(C_G(a,\Omega')\unknown C_G(a,\Omega)\). If \(\Omega'\) is not _a_-nice (in particular if it contains _a_), then we highlight the (short) sequence \(\Omega',\Omega\). Otherwise, if \(\Omega'\) is still _a_-nice, then its set \(C_G(a,\Omega')\) is reduced compared to \(C_G(a,\Omega)\). In this case, we apply again Theorem 11 on PMC \(\Omega'\) and iteratively on all PMCs produced which are _a_-nice. The fact is that set \(C_G(a,\Omega)\) decreases by at least one vertex at each step. Hence, this process is finite and since _a_ always belongs to \(C_G(a,\Omega)\), we will for sure obtain at some moment \(r\ge 2\), a PMC \(\Omega^{(r)}\) which is not _a_-nice.


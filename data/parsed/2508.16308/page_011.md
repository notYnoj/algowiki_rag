_Proof._ The graphs _G_<sub>1</sub> and _G_<sub>2</sub> are properly _k_-colorable by Lemma 4. As \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)are created by applying the same transformation on _G_<sub>1</sub> and _G_<sub>2</sub> respectively as in Section 6, the graphs \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)are _k_-partially _k_-colorable by Lemma 3, properly _k_-colorable, and \(\Delta_{E(G_1^{\{\ell,k\}})}=\Delta_{E(G_2^{\{\ell,k\}})}=k\) by Observation 1.

**Fact 1.** _For arbitrary k-partial k-colorings_ \(\chi_1\) _and_ \(\chi_2\) _of_ \(G_1^{\{\ell,k\}}\) _and_ \(G_2^{\{\ell,k\}}\)_respectively, the following hold:_

1. \(\forall i\in[k],\chi_1((i,1))=\chi_1((i,\ell))\) _in_ \(G_1^{\{\ell,k\}}\),<tbc>

_2._ \(\exists j\in[k],\chi_2((j,1))\neq\chi_2((j,\ell))\) _in_ \(G_2^{\{\ell,k\}}\).

_Proof._ Let \(\chi'_1\) and \(\chi'_2\) be _k_-colorings of _G_<sub>1</sub> and _G_<sub>2</sub> respectively which are defined as follows:

\(\forall i\in[k],j\in[\ell]:\chi'_1((i,j))=\chi_1((i,j)),\)<br>
\(\forall i\in[k],j\in[\ell]:\chi'_2((i,j))=\chi_2((i,j)).\)

By the same arguments as in the proof of Lemma 2, every pair of adjacent vertices is colored properly in _G_<sub>1</sub> and _G_<sub>2</sub> and therefore, \(\chi'_1\) and \(\chi'_2\) are proper colorings of _G_<sub>1</sub> and _G_<sub>2</sub>, respectively. By Lemma 5, for each \(i\in[k]\), \(\chi'_1((i,1))=\chi'_1((i,\ell))\) in _G_<sub>1</sub> and therefore, \(\chi_1((i,1))=\chi_1((i,\ell))\) in \(G_1^{\{\ell,k\}}\) as well and hence item 1 holds. By the same argument and the fact that \(\tau_{\ell/2}\neq\unknown\), there exists \(j\in[k]\) such that \(\chi'_2((j,1))\neq\chi'_2((j,\ell))\) in _G_<sub>2</sub> and therefore, \(\chi_2((j,1))\neq\chi_2((j,\ell))\) in \(G_2^{\{\ell,k\}}\) and item 2 holds.

**Fact 2.** _For each_ \(i\in[k]\)_, the vertex_ (_i,_1) _has the same_ \(3\big(\frac{\ell}{2}-1\big)\)_-neighborhood in_ \(G_1^{\{\ell,k\}}\) _and_ \(G_2^{\{\ell,k\}}\)_. The same holds true for the vertex_ \((i,\ell)\)_. More precisely, the following holds:_

\(N_{G_1^{\{\ell,k\}}}^{3(\ell/2-1)}[(i,1)]=N_{G_2^{\{\ell,k\}}}^{3(\ell/2-1)}[(i,1)],\)<br>
\(N_{G_1^{\{\ell,k\}}}^{3(\ell/2-1)}[(i,\ell)]=N_{G_2^{\{\ell,k\}}}^{3(\ell/2-1)}[(i,\ell)].\)

_Proof._ By the construction of the graphs _G_<sub>1</sub> and _G_<sub>2</sub>, we have that the graphs induced on \((V_1\cup\dots\cup V_{\ell/2})\) by _G_<sub>1</sub> and _G_<sub>2</sub> are same. This is also true for the set \((V_{\ell/2+1}\cup\dots V_\ell)\). More precisely, the following holds:

\(G_1[V_1\cup\dots\cup V_{\ell/2}]=G_2[V_1\cup\dots\cup V_{\ell/2}],\)<br>
\(G_1[V_{\ell/2+1}\cup\dots\cup V_\ell]=G_2[V_{\ell/2+1}\cup\dots\cup V_\ell].\)

The graphs _G_<sub>1</sub> and _G_<sub>2</sub> only differ in the anti-matching between \(V_{\ell/2}\) and \(V_{\ell/2+1}\). Therefore, for each \(i\in[k]\), the vertex (_i,_1) has the same \(\big(\ell/2-1\big)\)-neighborhood in _G_<sub>1</sub> and _G_<sub>2</sub>. The same holds true for the vertex \((i,\ell)\), i.e.

\(N_{G_1^{\ell/2-1}}[(i,1)]=N_{G_2^{\ell/2-1}}[(i,1)],\)<br>
\(N_{G_1^{\ell/2-1}}^{\ell/2-1}[(i,\ell)]=N_{G_2^{\ell/2-1}}^{\ell/2-1}[(i,\ell)].\)

By the construction of \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\), as each edge {_u,v_} is replaced consistently with the _k_-edge gadget _e_<sub>{_u,v_}</sub>, and the distance between _u_ and _v_ in _e_<sub>{_u,v_}</sub> is 3, the vertex (_i,_1) (as well as \((i,\ell)\)) has the same \(3(\ell/2-1)\)-neighborhood in \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\).


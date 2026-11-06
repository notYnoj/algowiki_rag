<tbc>means that there are two possibilities: either _U_ has no full component, and, it is a PMC, or _U_ admits a full component which is a native one. In brief, _U_ is a brightening (Definition 17).

_Complexity time._ At each iteration of the while-loop, we need to update the collection of conflict pairs for the current set _U<sub>i</sub>_. This operation amounts to determine graph torso(_G,U<sub>i</sub>_), which can be done in _O(m_+|_U<sub>i</sub>_|<sup>2</sup>)=_O(n_<sup>2</sup>). Consequently, as the total number of iterations is at most linear in _n_, the time complexity of conflict-greedy is in _O(n_<sup>3</sup>).

Let us come back to the example given in Figure 5a. As stated above, we could show that even if _X_ is a shy set, none of its proper subset is a PMC. Consequently, set conflict- greedy(_X_) will not be a PMC and will admit only native full components. Indeed, the single conflict pair for _X_ is (_a,b_). Assume w.l.o.g. that the vertex selected in line 5 is _u=a_. Then we remove _b_ from the current set: \(U=X\backslash\{b\}=S\cup\{a\}\). Now, set _U_ has no conflict pair since it admits a full component. Observe by the way that it has a unique full component \(\{a'\}\). This component is indeed native: \(\{a'\}\) was already a connected component of _G_\\_X_. As an example, the connected component \(\{b,b'\}\) of _G_\\_U_ - which is not full - was not a connected component of _G_\\_X_: it is non-native.

On the contrary, in Figure 5b, the set _X_ is a PMC superset, as \(S\cup\{a\}\) is a PMC. However, conflict-greedy can fail in finding a PMC subset of _X_. Indeed, consider the case where the selected vertex is _u=b_ (in conflict with _a_). The obtained set after an iteration is \(U=S\cup\{b\}\) which admits a (native) full component. Nevertheless, note that if we had selected _u=a_, then we would have obtained \(U=S\cup\{a\}\).

Both remarks on the examples of Figure 5 ensure us that the algorithm conflict-greedy is definitely not a good candidate for identifying a PMC which is the subset of some given shy set _X_. However, this subroutine will be necessary in the remainder for establishing the main contributions of this paper.

## 3.2 Shy separators

As stated in the previous subsection, the algorithm conflict-greedy is not sufficient to show that PMC Superset can be solved in polynomial time. We introduce a concept which is essential to achieve this goal: _shy separators_.

**Definition 18** (Shy separators)**.** _Consider a graph G with a set_ \(X\subseteq V(G)\) _and_ \(S\unknown X\) _a minimal separator of G. Let C be a full component for S in G_\\_S._

_We say that S is an X_-shy separator _with regard to C if, for any connected component_ \(B\subseteq C\) _of graph G_\\_X, then_ \(N_G(B)\cap S\neq S\).

This definition is based upon some vertex set _X_ (which represents a possible PMC superset in our context), a minimal separator _S_ of _G_ included into _X_, and a full component for _S_. For some _X_, a separator \(S\unknown X\) can be _X_-shy with regard to a full component _C_<sub>1</sub> whereas it is not for another full component _C_<sub>2</sub>. As a specific example, assume \(X=S\cup C\): in this case, _S_ is naturally _X_-shy with regards to _C_ as graph _G_\\_X_ does not contain any connected component included into _C_, since \(C\unknown X\).

We will see that, for some vertex set _X_, being a PMC superset is directly related to the presence of some _X_-shy separator. First, we establish a link between PMCs and shy separators.

**Lemma 15.** _For any_ \(PMC\Omega\)_, there is a minimal separator_ \(S\unknown\Omega\) _of G such that:_


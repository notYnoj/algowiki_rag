3. The PMCs of _G_ can also be written as \(S\cup\{a\}\), where _S_ is a minimal separator of _G_: we check whether such sets are PMCs.<tbc>

4. There can be PMCs of _G_ which are not recognized in the three first cases, but they can be expressed as \(S\cup(T\backslash\{a\})\), where _S_ and _T_ are two minimal separators of _G_. Originally, these PMCs were expressed as \(S\cup(C\cap T)\) in \[6\], where _C_ is a full component for _S_. But Korhonen \[21\] recently improved this characterization.

In fact, the collection of PMCs found in the fourth step contains all _a_-nice PMCs. Furthermore, the authors showed that the three first steps of BT-enum compute all the PMCs which are either PMCs of _G_\\{_a_} (step 1) or containing _a_ (steps 2 and 3). In the remainder, our own enumeration algorithm PMC-Traversal will utterly modify this fourth step to reduce the enumeration running time.

The following series of lemmas proves why BT-enum enumerates all PMCs of _G_. These results will also be used for our contribution. Lemma 12 justifies that steps 2 and 3 are sufficient to enumerate the PMCs which contain _a_. Lemma 13 proves that the fourth step enumerates _a_-nice PMCs, as announced.

**Lemma 11** (\[6\])**.** _Let_ \(\Omega'\) _be a PMC of G_\\{_a}, for any_ \(a\in V(G)\)_. Then either_ \(\Omega'\cup\{a\}\) _or_ \(\Omega'\) _is a PMC of G. It follows that_ \(|\Pi_G|\ge|\Pi_{G\backslash\{a\}}|\).

**Lemma 12** (\[6\])**.** _Let_ \(\Omega\) _be a PMC of G such that_ \(a\in\Omega\)_. Then_ \(\Omega'=\Omega\backslash\{a\}\) _is either a PMC of G_\\{_a_} _or a minimal separator of G._

**Lemma 13** (\[6\], Theorem 2 of \[22\])**.** _Let_ \(\Omega\) _be a PMC of G such that_ \(a\notin\Omega\)_. Let_ \(S=N(C_G(a,\Omega))\) _be the minimal separator of_ \(\Omega\) _neighbor of_ \(C_G(a,\Omega)\).

_If_ \(\Omega\) _is an a-nice PMC, then there is a minimal separator T of G such that_ \(\Omega=S\cup T\backslash\{a\}\) _with_ \(a\in T\)_. Moreover, singleton_ {_a_} _is a_ (_x,y)-separator in_ \(G[\overline{\Omega}\cup\{x,y\}]\)_, for some_ \(x,y\in S\).

In summary, BT-enum proceeds as follows: it determines recursively the list of PMCs of some subgraph _G_\\{_a_} of the input graph _G_, then it executes the four cases provided above and return the list of sets considered which were confirmed as PMCs. The base case of the recursion is the enumeration of PMCs in the single-vertex graph, which is trivial. The output-quadratic running time of BT-enum comes from the fourth case, which consists in enumerating all pairs of minimal separators of _G_. The first three cases cost a time linear in the number of PMCs, in particular the third one which uses the polynomial-delay enumeration of minimal separators (Lemma 1) and exploits the inequality \(|\Delta_G|\le n|\Pi_G|\). This gives eventually a total running time of \(O(n^2m|\Delta_G|^2)\). As recalled above, our best known lower bound for the number of PMCs is \(|\Pi_G|\ge\frac{|\Delta_G|}{n}\) . Thus BT-enum guarantees output-quadratic time \(O(n^3m|\Pi_G|^2)\).

## 2.4 PMC enumeration and extension

A common technique to obtain polynomial-delay enumeration algorithms is called _Flashlight Search_ \[26\]. In this context, consider that we are tackling some enumeration problems where the objective is to list all inclusion-wise maximal sets of elements satisfying a certain property. Considering an arbitrary ordering _e_<sub>1</sub>_,e_<sub>2</sub>_,...,e<sub>n</sub>_ of the elements that could belong to solutions, this method consists in creating a binary tree whose paths from root to the leaves provide us<tbc>


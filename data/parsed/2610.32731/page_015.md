<tbc>produces the _k_-th largest element of _G_, and that OPT(_T,k_+1)=OPT(_G,k_), so the running time is O(_k_+OPT(_G,k_)). Thus, theorem 19 extends to forests.

We now describe the algorithm, starting with a _heaapification_ subroutine \[KKZZ18\]. Let _F_ be a forest consistent with a linear order _L_, and let _U_ be a set of nodes in _F_ with a common parent _p_. The procedure Heapify(_F,U_) modifies _F_ as follows: First, detach each \(u\in U\) from its parent _p_. Then, build a _heap_ on _U_. That is, build any binary tree _B_ with _V(B_)=_U_, such that the given ordering _L_ is consistent with _B_. Finally, make the root _r_ of _B_ a child of _p_, and return _r_.

**Lemma 20.** Heapify(_F,U_) _takes_ O(|_U_|) _time and yields a forest_ \(F'\) _such that L is consistent with_ \(F'\)_, and_ \(\mathcal{L}(F')\subseteq\mathcal{L}(F)\)_, that is, every ordering_ \(L'\) _of_ \(V(F)=V(F')\) _that is consistent with_ \(F'\) _is also consistent with F._

_Proof._ It is well-known that Heapify can be implemented in linear time with a bottom-up construction. Observe \(F'\) differs from _F_ by adding the edges in _B_ and removing the edges between each \(u\in U\backslash\{\text{root}(B)\}\) and _p_. Since _L_ is consistent with _B_ and _F_, clearly _L_ is also consistent with \(F'\). On the other hand, it is easy to see that if some _u_ is an ancestor of some _v_ in _F_, then the same is true in \(F'\). That implies \(\mathcal{L}(F')\subseteq\mathcal{L}(F)\).

We call our algorithm WSHTreeSelect (see algorithm 1 for pseudocode). It is quite close to the algorithm `Soft-Select-Heapify` of Kaplan, Kozma, Zamir, and Zwick \[KKZZ18\], only that we use a _weighted_ soft heap, and some details need to be adjusted. The weight of each node is precisely its degree in _T_ plus 1. We maintain a WSH _Q_ and a set _S_ of all elements ever inserted into _Q_. Initially, insert the root of _T_ into _Q_.

Then, repeat the following _k_-1 times. Find the minimum node in _Q_. Due to corruption, this node may have a parent that is still in _Q_. Since we know that the parent must be smaller, we can take the parent instead. Perform this replacement as long as possible. Then, remove the chosen node _x_ from _Q_. Let _C_ be the set of newly corrupted elements, including _x_ if it has not been corrupted before. For each \(v\in C\), perform Heapify on its (original) children, and then insert each of its (current) children into _Q_.

We will prove that afterwards, all of the _k_ smallest nodes must be contained in _S_, and \(|S|\le\mathcal{O}(k+\text{OPT}(G,k))\). Thus, we can simply call a linear-time selection algorithm such as median-of-medians \[BFP<sup>+</sup>73\] on _S,k_ to find the _k_-th smallest element.

The parent replacement of lines 8 to 9 in algorithm 1, which is not present in the aforementioned `Soft-Select-Heapify` \[KKZZ18\], is necessary to ensure the following.

**Lemma 21.** _Let D be the set of elements deleted from Q so far at any point during a run of_ WSHTreeSelect_. Then D is a prefix of T_<sub>0</sub>.

_Proof._ We proceed by induction. In the first step, the root is deleted, which trivially forms a prefix of _T_<sub>0</sub>. Now suppose \(D\neq\emptyset\) is the set of element deleted so far, and we next delete a (non-root) node _x_. It suffices to show that the parent _p_ of _x_ is contained in _D_ (then \(D\cup\{x\}\) is a prefix, as desired).

Suppose \(p\notin D\). Then _x_ must have been inserted into _Q_ when _p_ was corrupted. But then _p_ is contained in _Q_, so _x_ will not actually be deleted in the current iteration (due to line 9). This contradiction proves our claim, and thus the lemma.


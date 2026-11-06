It remains to analyze the running time. The call to Lemma 4.3 takes time \(O(n^{2-\delta})\) for some constant \(\delta=\delta(\rho,\epsilon)>0\). We can also charge the scan through T to that running time. By Lemma 4.3, each constructed subinstance \((A',B',C')\) admits an \((K=O(n^\epsilon),N=O(n^{2-2\rho}))\)-container _H_ of \(A'\cup B'\cup C'\). It follows that<tbc>

\(|A'+B'|\le|H+H|\le K|H|\le O(n^{2-2\rho+\epsilon}).\)

<tbc>Similarly, by an application of the Plünnecke-Ruzsa inequality (Lemma 2.1),

\(|B'-C'|\le|H-H|\le K^2|H|\le O(n^{2-2\rho+2\epsilon}).\)

Therefore, the \(O(n^\epsilon)\) calls to Lemma 4.4 run in total time \(O(n^{2-2\rho+3\epsilon})\). The claimed running time follows, picking any constant \(0<\epsilon<2\rho/3\).

## 4.1 Low-Doubling Containment for One Set

The proof of Lemma 4.3 involves two steps: (1) to reduce from any low-rank instance to subinstances where only one of the three sets admits a low-doubling container, and (2) to extend that one low- doubling container to all three sets. We start with step (1):

**Lemma 4.5** (Low-Doubling Containment for One Set)**.** _For every_ \(\epsilon>0\) _and_ \(0<\rho\le 1/2\) _there is some_ \(\delta=\delta(\rho,\epsilon)>0\) _such that the following holds. There is a randomized algorithm that, given a 3SUM instance_ (_A,B,C_) _and a set X of size_ \(|X|\le n^{1-\rho}\) _such that_ \(C\subseteq X+X\)_, computes_

• \(O(n^\epsilon)\) _subinstances_ \((A'\subseteq A,B,C)\) _with_ \(O(n^\epsilon)\)_-doubling_ \(O(n^{2-2\rho})\)_-containers of_ \(A'\)_, and_<tbc>

• _a set of 3SUM solutions_ \(\mathcal{T}\subseteq A\times B\times C\),

_so that each solution is either part of exactly one subinstance or part of_ T _. The algorithm runs in time_ \(O(n^{2-\delta})\).

The proof of Lemma 4.5 requires some setup. We start with the following simple lemma that allows to trade off the size of the container with its doubling.

**Lemma 4.6.** _Let_ \(\epsilon,\gamma>0\) _and_ \(0<\rho\le 1/2\)_. There is a deterministic algorithm to reduce any 3SUM instance_ (_A,B,C_) _provided with a_ \((O(n^\epsilon),O(n^{2-2\rho+\gamma}))\)_-container of A to_ \(O(n^\gamma)\) _subinstances_ \((A'\subseteq A,B,C)\) _provided with a_ \((O(n^{\epsilon+\gamma}),O(n^{2-2\rho}))\)_-container of_ \(A'\)_. It runs in linear time_ \(O(n^{1+\gamma})\).

**Proof.** Let _H_ denote the _K_-doubling container of _A_ with \(K=O(n^\epsilon)\). Arbitrarily partition _H_ into \(t=O(n^\gamma)\) pieces _H_<sub>1</sub>_,...,H<sub>t</sub>_ of size at most \(\lceil|H|/t\rceil=O(n^{2-2\rho})\), and let _A_<sub>1</sub>_,...,A<sub>t</sub>_ denote the subsets \(A_i=A\cap H_i\). Then the 3SUM instance (_A,B,C_) is equivalent to the instances (_A_<sub>1</sub>_,B,C),...,(A<sub>t</sub>,B,C_) (in the sense that their solutions stand in one-to-one correspondence). Moreover, each _A<sub>i</sub>_ is contained in _H<sub>i</sub>_, and as

\(|H_i+H_i|\le|H+H|\le K|H|\le O(Kt)|H_i|=O(n^{\epsilon+\gamma})|H_i|,\)

_H<sub>i</sub>_ is a \((O(n^{\epsilon+\gamma}),O(n^{2-2\rho}))\)-container of _A<sub>i</sub>_.

The more interesting ingredient to Lemma 4.5 is the following lemma. Intuitively, it states that certain structure can be _amplified_. Namely, any 3SUM instance (_A,B,C_) where _C_ is a subset of (_k_+1)-popular sums can be replaced by a subinstance that is a subset of (_k_+2)-popular sums. Curiously, the amplified structure does not show up in _C_, but in _B_.


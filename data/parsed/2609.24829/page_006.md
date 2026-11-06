Let \(t_e:=t_e^E\) where _E_ is the edge set of the graph. _Light_ edges have small values of _t<sub>e</sub>_ while _heavy_ edges have large values of _t<sub>e</sub>_ (where small and large are defined as necessary in a subsequent algorithm). We also have \(\Delta_e(G)=\Delta_e=max_et_e\).

### 2.2 Related results

As we discussed in the introduction, all previous results require a lower bound estimate on the number of triangles in the entire stream. It is precisely this requirement that we eliminate.

In the multi-pass edge-streaming model, where the algorithm may scan the input more than once, Cor mode and Jowhari \[CJ14\] proved that any constant-pass algorithm for arbitrary graphs requires \(\Theta\left(\frac{m}{\sqrt{T}}\right)\) space, and they gave a two-pass algorithm achieving this bound. Building on this result, Kolountza kis et al. \[KMPT12\] presented a three-pass algorithm that uses \(O\left(m^{1/2}+\frac{m^{3/2}}{T}\right)\) space, while Bera and Chakrabarti \[BC17\] later showed how to attain \(O\left(\frac{m^{3/2}}{T}\right)\) space in just four passes.

In the adjacency-list streaming model, where the neighbors of each vertex arrive in a contiguous block (so each edge is observed twice), McGregor, et al. \[MVV16\] gave a one-pass algorithm using \(O\left(\frac{m}{\sqrt{T}}\right)\) space. More recently, Kallaugher, et al. \[KMPV19\] designed a two-pass algorithm requiring \(O\left(\frac{m}{T^{2/3}}\right)\) space, and they proved matching lower bounds (under standard communication-complexity conjectures) for both one- and two-pass algorithms in this model.

Finally, the query model considers the number of edge- or vertex-queries rather than space usage. Although this setting is quite different, it faces the same challenge of "heavy" vertices or edges. Eden, et al. \[ELRS17\] initiated the study of triangle counting under query complexity bounds, and their techniques were extended by Eden et al. \[ERS18\] to count general cliques and by Assadi et al. \[AKK19\] to count all constant-size subgraphs.

## 3 Warmup

### 3.1 Verified Triangle Counting

In many of the algorithms found in the literature, the assumption that the input parameter \(\tau\) is a lower bound poses two complications: The first is the assumption of _knowledge_ of such a lower bound \(\tau\). The second is the _inability to verify_ that \(\tau\) is indeed a lower bound. That is, the algorithms will necessarily output some estimate, where in reality \(\tau\) is not even a lower bound on _T_ - so the estimate need not be accurate. This raises the need for a _verified_ triangle counting algorithm: An algorithm that not only produces an estimate, but declares when the input parameter doesn’t satisfy the assumptions placed on it. We modify a previous algorithm to provide such an algorithm and prove the following theorem:

**Theorem 3.1.** _There exists a single-pass algorithm_ A _which takes one pass over a randomly ordered stream and parameter_ \(\tau\) _such that a) the algorithm uses_ \(s(m,\tau)=\widetilde{O}(\varepsilon^{-2}\delta^{-1}(m/\sqrt{\tau}+T/\sqrt{\tau}))\) _space in expectation, and b) with probability at least_ \(1-\delta-1/\mathrm{poly}(n)\):

• _If_ \(T\ge\tau\)_, the output is a_ \((1\pm\varepsilon)\)_-approximation of T._<tbc>

• _If_ \(T<\tau\)_, the output is a_ \((1\pm\varepsilon)\)_-approximation of T or `FAIL`._

_Note that the algorithm has no a priori information about T._

**Remark 3.2.** _To fix terminology, we say that an execution of_ A _is_ successful _if it outputs a correct estimate or `FAIL`. That is 3.1 means_ \(\mathrm{Pr}\left[\mathcal{A}\text{\textit{is successful}}\right]\ge 1-\delta-1/\mathrm{poly}(n)\).


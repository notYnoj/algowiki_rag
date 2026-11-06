• _outputs a set_ C _of at most_ 2<sup>44log<sup>2</sup>(_k_)</sup> _cycle separators each partitioned into heavy, light, and discarded vertices such that for each_ \(C\in\mathcal{C}\), (_C,_1) _is measured for k and 1 and for each_ \(P\subseteq V\) _with_ \(|P|\le k\)_, at least one_ \(C\in\mathcal{C}\) _is_ max(3/4_,q)-balanced for w,_ \(P\cap C_\mathrm{di}=\emptyset\)_, and_

\(|P\cap C_\mathrm{li}|\le\frac{11|P|\mathrm{log}(k)}{2\sqrt{k}}.\)

_Analysis of Running time._ The algorithm by Nederlof iteratively replaces one cycle separator by 4. The total number of cycle separators considered is in O(2<sup>44log<sup>2</sup>(_k_)</sup>) and for each cycle separator, he applies a menger-type algorithm by Fomin, Lokshtanov, Marx, Pilipczuk, Pilipczuk, and Saurabh \[FLM<sup>+</sup>22\]. Based on the outcome, only some vertices are added to either the heavy, light, or discarded vertices. The time needed for the latter is dominated by the menger-type algorithm, so it only remains to analyze this algorithm. This algorithm first computes in O(_n+m_) time an auxiliary graph _H_ whose number of vertices and edges is linear in the number of vertices and edges in the original graph. Since the input graph is planar, this takes O(_n_) time and _H_ also has O(_n_) edges (but is not necessarily planar). It then computes a minimum-cost flow in _H_, partitions the flow into walks, shortcuts these walks to paths if necessary, computes a solution to the dual LP of the minimum-cost flow problem, and partition the vertices based on the solution for the dual. Using recent improvements for almost-linear time algorithms for flows and their duals \[CKL<sup>+</sup>25\], we can compute an optimal integral solution to the minimum-cost flow problem and its dual LP in O(_m_<sup>1+_o_(1)</sup>)=O(_n_<sup>1+_o_(1)</sup>) time. All other steps can be performed in O(_kn_log_n_) time, so overall, the algorithm takes 2<sup>O(log<sup>2</sup>(_k_))</sup>_n_<sup>1+_o_(1)</sup> time.

Finally, we summarize a couple of simple inequalities that we will use repeatedly.

**Lemma 7.** _If_ \(d\ge 16\)_, then_ \(\mathrm{log}^2(d)\le d\)_. If_ \(d\ge 54\)_, then_ \(\lfloor d-3\sqrt{d}\rfloor\ge\frac{4d}{7}\) _. If_ \(d\ge 54\)_, then_ \(\sqrt{D-3\sqrt{D}}+1-\sqrt{D}\le-1/10\).

_Proof._ Since the first statement is trivial, we will focus on the second and third. To this end, observe that \(\lfloor d-3\sqrt{d}\rfloor\ge d-3\sqrt{d}-1\). As both sides of the inequality are positive for any \(d\ge 11\), we can square both sides and only show \(d-3\sqrt{d}-1\ge\frac{4d}{7}\) . Note that

\(d-3\sqrt{d}-1\ge(4/7)d\)<br>
\(\Leftrightarrow(3/7)d\ge 3\sqrt{d}+1\)<br>
\(\Leftrightarrow\sqrt{d}\ge 7+7/(3\sqrt{d}),\)

\(7/(3\sqrt{d})\le 1/3\) for all \(d\ge 49\), and \(7+1/3\le\sqrt{54}\).

Note that the third inequality is equivalent to \(\sqrt{D}-11/10\ge\sqrt{D-3\sqrt{D}}\). Since both sides are positive for any \(d\ge 54\) (as \(\sqrt{D}-11/10\ge\sqrt{54}-2>5\) and \(\sqrt{D-3\sqrt{D}}\ge\sqrt{54-3\sqrt{54}}>5\)), we can square both sides and only show \((\sqrt{D}-11/10)^2\ge D-3\sqrt{D}\). This holds as

\((\sqrt{D}-11/10)^2=D-\frac{22}{10}\sqrt{D}+\frac{121}{100}\ge D-\frac{30}{10}\sqrt{D}+0=D-3\sqrt{D}.\)

## 3 The Framework

In this section, we show our main result, Theorem 3. It describes a general algorithmic framework for solving request variants on planar graphs in subexponential parameterized time. The framework can handle non-bidimensional weighted problems and does not require the solution to consist of a<tbc>


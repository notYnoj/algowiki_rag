_Proof._ To obtain the longest common subsequence of _x_ and _y_, one applies at most \(\delta m\) deletions. By counting, at most \(\sqrt{\delta}\frac{|x|}{w'}\) intervals of \(\mathcal{I}_{w^\prime}\) receive more than \(\sqrt{\delta}w'\) deletions, and the remaining intervals satisfy the desired inequality.

We now can establish (3) in this case.

**Lemma 5.7.** _If at least_ \(\gamma m_x\) _many_ \(\gamma w\)_-intervals are_ \(\gamma\)_-imbalanced, and_ \(\mathsf{LCS}(x,y)\ge(1-\delta)|x|\)_, then_ (3) _holds._

_Proof._ Let \(I_1<\cdots<I_{m_x/\gamma}\) be the intervals of \(\mathcal{I}_{\gamma w}\). For all \(i=1,\dots,m_x/\gamma\), let \(J_i:=\text{round}_{\theta w}(J_{I_i}^\tau)\), so that _J<sub>i</sub>_ are pairwise disjoint. Let _K<sub>imbal</sub>_ be the indices _i_ such that _I<sub>i</sub>_ is \(\gamma\)-imbalanced. By assumption \(|K_{imbal}|\ge\gamma m_x\). Let _K<sub>good</sub>_ be the indices _i_ such that \(\mathsf{LCS}(I_i,J_{I_i}^\tau)\ge(1-\sqrt{\delta})|I_i|\). By Lemma 5.6 with \(w'=\gamma w\), \(|K_{good}|\ge(1-\sqrt{\delta})\frac{m_x}{\gamma}\) .

Observe that under these assumptions, CoveringAlgorithm certifies many rectangles using the trivial algorithm. For \(i\in K_{good}\), we have \(\mathsf{Trivial}(I_i,J_i)\ge\frac{1}{2}(1-\sqrt{\delta})|I_i|-2\theta w\ge(\frac{1}{2}-\sqrt{\delta})|I_i|\). Thus, we certify \((I_i\times J'_i,(\frac{1}{2}-\sqrt{\delta})|I_i|)\) for some subinterval \(J'_i\subset J_i\), defined as the shortest \(\theta w\)-aligned interval with end\(J'_i=\text{end}J_i\) and \(\mathsf{Trivial}(I_i,J'_i)\ge\frac{1}{2}(1-\sqrt{\delta})|I_i|\).

For \(i\in K_{good}\cap K_{imbal}\), we have \(\mathsf{Trivial}(I_i,J_i)\ge\mathsf{Trivial}(I_i,J_{I_i}^\tau)-2\theta w\ge(\frac{1}{2}+\gamma-\sqrt{\delta})|I_i|-2\theta w>(\frac{1}{2}+\frac{\gamma}{2})\gamma w\). Thus, we certify \((I_i\times J'_i,(\frac{1}{2}+\frac{\gamma}{2})|I_i|)\) for some subinterval \(J'_i\subset J_i\), defined as the shortest \(\theta w\)-aligned interval with end\(J'_i=\text{end}J_i\) and \(\mathsf{Trivial}(I_i,J'_i)\ge(\frac{1}{2}+\frac{\gamma}{2})|I_i|\).

Thus CoveringAlgorithm obtains an ordered collection of certified rectangles \((I_i\times J'_i,\kappa_i)\) over \(i\in K_{good}\) with \(\kappa_i\ge(\frac{1}{2}-\sqrt{\delta})|I_i|\) for all \(i\in K_{good}\) and \(\kappa_i\ge(\frac{1}{2}-\sqrt{\delta}+\frac{\gamma}{2})|I_i|\) for all \(i\in K_{good}\cap K_{imbal}\). Thus,

\(\mathsf{FullLCSAAlgorithm}(x,y)\ge\sum_{i\in K_{good}}\kappa_i\)<br>
\(\ge\left(\frac{1}{2}-\sqrt{\delta}\right)(\gamma w)\cdot|K_{good}|+\frac{\gamma}{2}(\gamma w)\cdot|K_{good}\cap K_{imbal}|\)<br>
\(\ge\left(\frac{1+\delta}{2}\right)\mathsf{LCS}(x,y),\)

as desired. In the last inequality, we used (i) \(|K_{good}|\ge(1-\sqrt{\delta})\frac{m_x}{\gamma}\) , (ii) \(|K_{good}\cap K_{imbal}|\ge\gamma m_x-\frac{\sqrt{\delta}m_x}{\gamma}\) , (iii) \(\gamma\gg\delta\), and (iv) \(m_xw=|x|\ge\mathsf{LCS}(x,y)\).

## Subcase 3: Many nearly-square intervals.

This case applies when the equal-length input algorithm \[RS20\] correctly certifies many rectangles. Recall that an interval \(I\in\mathcal{I}_w\) is _nearly-square_ if \(|J_I^\tau|\le(1+\beta)|I|\). For convenience, we call _I oblong_ if it is not nearly-square.

**Lemma 5.8.** _If at least_ \(\beta^2m_x\) _intervals_ \(I\in\mathcal{I}_w\) _are nearly-square, then_ (3) _holds._

_Proof._ Let \(I_1<I_2<\cdots<I_{m_x}\) be the intervals of I_<sub>w</sub>_. For all _i_=1_,...,m<sub>x</sub>_, let \(J_i:=\text{round}_{\theta w}(J_{I_i}^\tau)\), so that the _J<sub>i</sub>_ are pairwise disjoint. Let _K<sub>short</sub>_ be the set of indices _i_ such that _I<sub>i</sub>_ is nearly-square. By assumption, \(|K_{short}|\ge\beta^2m_x\). Let _K<sub>good</sub>_ be the set of indices _i_ such that \(\mathsf{LCS}(I_i,J_{I_i}^\tau)\ge(1-\sqrt{\delta})|I_i|\). By Lemma 5.6, \(|K_{good}|\ge(1-\sqrt{\delta})m_x\).

Just as in the proof of Lemma 5.8, we track the rectangles that are certified by CoveringAlgorithm. For \(i\in K_{good}\), we have \(\mathsf{Trivial}(I_i,J_i)\ge(\frac{1}{2}-\sqrt{\delta})|I_i|\), so we certify \((I_i\times J'_i,(\frac{1}{2}-\sqrt{\delta})|I_i|)\) for some subinterval \(J'_i\subset J_i\). For \(i\in K_{good}\cap K_{short}\), we have \((1+\alpha)w\ge(1+\beta)w\ge|J_{I_i}^\tau|\ge|J_i|\) since _I<sub>i</sub>_ is nearly-square, and \(|J_i|\ge\mathsf{LCS}(I_i,J_i)\ge\mathsf{LCS}(I_i,J_{I_i}^\tau)-2\theta w\ge(1-\sqrt{\delta}-2\theta)w\ge(1-\alpha)w\). Hence, EqLCS(_I<sub>i</sub>,J<sub>i</sub>_) is called at Line 14 and has value at least \((\frac{1}{2}+\alpha)\mathsf{LCS}(I_i,J_i)\ge(\frac{1}{2}+\alpha)(1-\sqrt{\delta}-2\theta)w>\frac{1+\alpha}{2}w\) by Theorem 2.2.


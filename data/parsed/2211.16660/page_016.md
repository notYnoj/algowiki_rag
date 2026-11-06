We thus have an ordered collection of certified rectangles \((I_i\times J'_i,\kappa_i)\) over \(i\in K_{good}\) with \(\kappa_i\ge(\frac{1}{2}-\sqrt{\delta})w\) for all \(i\in K_{good}\) and \(\kappa_i\ge(\frac{1}{2}-\sqrt{\delta}+\frac{\alpha}{2})w\) for \(i\in K_{good}\cap K_{short}\). Thus,

\(\mathsf{FullLCSAAlgorithm}(x,y)\ge\sum_{i\in K_{good}}\kappa_i\)<br>
\(\ge\left(\frac{1}{2}-\sqrt{\delta}\right)w\cdot|K_{good}|+\frac{\alpha}{2}w\cdot|K_{good}\cap K_{short}|\)<br>
\(\ge\left(\frac{1+\delta}{2}\right)\mathsf{LCS}(x,y),\)

as desired. In the last inequality, we used (i) \(|K_{good}|\ge(1-\sqrt{\delta})m_x\), (ii) \(|K_{good}\cap K_{short}|\ge\beta^2m_x-\sqrt{\delta}m_x\), (iii) \(\alpha\gg\beta\gg\delta\), and (iv) \(m_xw=|x|\ge\mathsf{LCS}(x,y)\).

### Wrapping up the bad case.

We now can prove the following lemma.

**Lemma 5.9.** _If_ (_x,y_) _is bad, then_ (3) _holds._

_Proof._ If (_x,y_) is bad, then either item 1, 2, or 3 of Definition 5.1 is violated. If 1 is violated, (3) holds by Lemma 5.5. If 2 is violated, there are at least \(\gamma m_x\) intervals _I_ with a \(\gamma\)-imbalanced \(\gamma w\)-subinterval, so there are at least \(\gamma m_x\) many \(\gamma\)-imbalanced \(\gamma w\)-intervals, so by Lemma 5.7, (3) holds. If 3 is violated, (3) holds by Lemma 5.8.

## 5.5 Proof of (3) for good inputs

Let

\(m'_x:=(1-2\beta^2)m_x.\)

The following lemma establishes the natural structural property for good inputs.

**Lemma 5.10.** _If_ (_x,y_) _is good, then there exist an ordered sequence of rectangles_ \(I_1\times J_1<\cdots<I_{m_\unknown^\prime}\times J_{m_\unknown^\prime}\) _such that for all i, (i)_ \(I_i\in\mathcal{I}_w\)_, (ii) every_ \(\gamma w\)_-subinterval of I<sub>i</sub> is_ \(\gamma\)_-balanced, (iii)_ \(|J_i|\ge(1+0.9\beta)w\)_, and (iv)_ \(\mathsf{IsQType}_w(y_{J_i},\mathsf{GetPType}_w(x_{I_i}))\) _returns true._

_Proof._ Among the _m<sub>x</sub>_ intervals \(I\in\mathcal{I}_w\), all but at most \(\sqrt{\delta}m_x\) intervals satisfy \(\mathsf{LCS}(I,J_I^\tau)>(1-\sqrt{\delta})|I|\) by Lemma 5.6, at most \(\gamma m_x\) have a \(\gamma\)-imbalanced \(\gamma w\)-subinterval since (_x,y_) is good, and at most \(\beta^2m_x\) are nearly-square since (_x,y_) is good. Thus, at least \((1-2\beta^2)m_x=m'_x\) intervals are (i) satisfying \(\mathsf{LCS}(I,J_I^\tau)>(1-\sqrt{\delta})|I|\), (ii) \(\gamma\)-balanced in all \(\gamma w\)-subintervals, and (iii) oblong. Let \(I_1<\cdots<I_{m_\unknown^\prime}\) be \(m'_x\) of these intervals. Let \(J_i:=\mathsf{round}_{\theta w}(J_{I_i}^\tau)\), so these _J<sub>i</sub>_ are pairwise disjoint. For all such _i_, we have

\(|J_i|\ge|J_{I_i}^\tau|-2\theta w\ge(1+\beta-2\theta)w\ge(1+0.9\beta)w\)

and

\(\mathsf{LCS}(I_i,J_i)\ge\mathsf{LCS}(I_i,J_{I_i}^\tau)-2\theta w\ge(1-\sqrt{\delta}-2\theta)w\ge(1-\alpha)w.\)

For all _t_ such that _x<sub>I<sub>i</sub></sub>_ has property _P<sub>t</sub>_, we have _y<sub>J<sub>i</sub></sub>_ has property _Q<sub>t</sub>_ by Lemma 4.1 (Item 2). Thus, \(\mathsf{IsQType}_w(y_{J_i},t)\) returns true for _t_=GetPType_<sub>w</sub>(x<sub>I<sub>i</sub></sub>_). We have found our ordered sequence of rectangles \(I_1\times J_1<\cdots<I_{m_\unknown^\prime}\times J_{m_\unknown^\prime}\).

We now can prove the main result for this section.

**Lemma 5.11.** _If_ (_x,y_) _is good, then_ (3) _holds._


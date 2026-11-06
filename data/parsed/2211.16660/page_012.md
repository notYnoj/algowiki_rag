• \(\delta\) is the overall LCS approximation advantage: we obtain a \((\frac{1+\delta}{2})\)-approximation. We assume \(\text{LCS}(x,y)\ge(1-\delta)|x|\), or else Trivial gives a \((\frac{1+\delta}{2})\)-approximation.<tbc>

• \(\theta\) is the discretization parameter for _J_-intervals: we round all _J_-intervals so that they are \(\theta w\) aligned. \(\theta\) is small enough so that the effect of this rounding is negligible. We take \(\theta\), the _J_-interval discretization, to be smaller than \(\gamma\), the _I_-interval discretization, so that the gain from matching "Trivial rectangles" is larger than the loss due to discretization.<tbc>

Input: x,y such that \(1(x)=0(x)\le min(1(y),0(y))\)<br>
Output: A set R of certified rectangles \((I\times J,\kappa)\) where I is \(\gamma w\)-aligned, J is \(\theta w\)-aligned, and<br>
\(\text{LCS}(I,J)\ge\kappa\).<br>
// Trivial rectangles<br>
\(\mathcal{R}\leftarrow\{([0,|x|]\times[0,|y|],\text{Trivial}([0,|x|],[0,|y|]))\}\)<br>
for all \(\gamma w\)-aligned intervals I do<br>
   for j=0,...,m<sub>y</sub>/\(\theta\) do<br>
   \(J\leftarrow\) the smallest \(\theta w\)-aligned interval s.t. end\(J=\theta wj\) and \(\text{Trivial}(I,J)\ge(\frac{1}{2}-\sqrt{\delta})|I|\)<br>
   if J exists then<br>
   \(\mathcal{R}\leftarrow\mathcal{R}\cup(I\times J,\text{Trivial}(I,J))\)<br>
   \(J\leftarrow\) the smallest \(\theta w\)-aligned interval s.t. end\(J=\theta wj\) and \(\text{Trivial}(I,J)\ge(\frac{1}{2}+\frac{\gamma}{2})|I|\)<br>
   if J exists then<br>
   \(\mathcal{R}\leftarrow\mathcal{R}\cup(I\times J,\text{Trivial}(I,J))\)<br>
   for \(\theta w\)-aligned intervals J with |J|=|I| do<br>
   \(\mathcal{R}\leftarrow\mathcal{R}\cup(I\times J,\text{Trivial}(I,J))\)<br>
// Nearly-square rectangles<br>
   for intervals \(I\in\mathcal{I}_w\) do<br>
   for \(\theta w\)-aligned intervals J with \(|J|\in[(1-\alpha)w,(1+\alpha)w]\) do<br>
   \(\mathcal{R}\leftarrow\mathcal{R}\cup(I\times J,\text{EqLCS}(I,J))\)<br>
// Algorithmic structure lemma rectangles<br>
   for i=1,...,m<sub>x</sub> do<br>
   \(I\leftarrow[(i-1)w,iw]\)<br>
   \(t\leftarrow\) GetPType<sub>w</sub>(x<sub>I</sub>)<br>
   \(I'\leftarrow\) Getl<sub>w</sub>(x<sub>I</sub>,t)<br>
   for \(j=1,\dots,m_y/\theta\) do<br>
   \(J\leftarrow\) smallest interval such that end\(J=\theta wj\), \(|J|\ge(1+0.9\beta)w\), and IsQType<sub>w</sub>(y<sub>J</sub>,t)<br>
   if J exists then<br>
   \(\mathcal{R}\leftarrow\mathcal{R}\cup(I'\times J,\frac{|I'|}{2}+\alpha w)\)<br>
return R.

## 5.2 Runtime

We now analyze the runtime. We re-emphasize, as we did in the proof sketch, that we need to be careful about factors _m<sub>y</sub>_ in our runtime, but not powers of _m<sub>x</sub>_: _m<sub>x</sub>_ is only log_n_, but _m<sub>y</sub>_ is roughly |_y|/|x_|, which can be a positive power of |_y_|.

**Algorithm 1:** CoveringAlgorithm


Input: x,y such that \(1(x)=0(x)\le min(1(y),0(y))\)<br>
Output: A (\(\frac{1+\delta}{2}\))-approximation of LCS<br>
\(\mathcal{R}\leftarrow\text{CoveringAlgorithm}(x,y)\)<br>
// DP\[i\]\[j\] lower bounds \(LCS([0,\gamma w],[0,\theta wj])\)<br>
\(\text{DP}\leftarrow[0,m_x/\gamma]\times[0,m_y/\theta]\) array, initialized to 0<br>
for \(i=1,\dots,m_x/\gamma\) do<br>
   for \(j=1,\dots,m_y/\theta\) do<br>
   \(\text{DP}[i][j]\leftarrow max(\text{DP}[i-1][j],\text{DP}[i][j-1])\)<br>
   for \((I\times J,\kappa)\in\mathcal{R}\) with end\(I=(\gamma w)i,\text{end}J=(\theta w)j\), do<br>
\(\text{DP}[i][j]\leftarrow max(\text{DP}[i][j],\text{DP}[(\text{start}I)/(\gamma w)][(\text{start}J)/(\theta w)]+\kappa)\)<br>
return \(\text{DP}[m_x/\gamma][m_y/\theta]\).

We first run a _O_(|_y_|)-time preprocessing of prefix-sums that allows us to query zero-counts and one- counts in any interval in either _x_ or _y_ in _O_(1) time. We also preprocess string _y_ so that we can test every property _Q<sub>t</sub>_ efficiently on substrings of _y_; for each _t_ this takes _O_(|_y_|log|_y_|) preprocessing time, for a total preprocessing time that is _O_(|_y_|log<sup>2</sup>|_y_|).

The runtime of CoveringAlgorithm is dominated by calls to Trivial,EqLCS,GetPType_<sub>w</sub>_,IsQType_<sub>w</sub>_, and Getl_<sub>w</sub>_. Note that in Lines 4 and 7, _J_ can be computed by a binary search over a search space of size \(m_y/\theta\), and thus can be found in \(log(m_y/\theta)\) calls to Trivial, which each take _O_(1) time with preprocessing. Thus, the first nested loop takes \(O(m_x^2m_ylogm_y)\le\tilde{O}(|y|/|x|)\) time.

The second nested loop has _O(m<sub>x</sub>m<sub>y</sub>_) calls to EqLCS, each of which runs in \(O(|x|^{1+\frac{\varepsilon}{2}})\) time, and thus takes \(O(n^{1+\varepsilon})\) time.

For the third nested loop, the number of calls to GetPType_<sub>w</sub>_ and Getl_<sub>w</sub>_ is _m<sub>x</sub>_, and each run in time _O(w_log_w_), so the runtime is at most \(\tilde{O}(|x|)\). Because the property _Q<sub>t</sub>_ is hereditary, we can compute _J_ in Line 20 by binary search with \(log(m_y/\theta)\le O(log|y|)\) calls to IsQType_<sub>w</sub>_, which runs in time _O(w_) (the binary search crucially saves us a factor of roughly |_y|/|x_| in the runtime). The number of binary searches is _O(m<sub>x</sub>m<sub>y</sub>_), so in total the runtime of this step is \(O(m_xm_y\cdot log(m_y)\cdot w)\le O(|y|log^2|y|)\).

There are _O(m<sub>x</sub>m<sub>y</sub>_) rectangles, and the dynamic programming has _O(m<sub>x</sub>m<sub>y</sub>_) states. The runtime of the dynamic programming is thus \(O(m_xm_y)\le\tilde{O}(|y|/|x|)\), so the total runtime is thus \(O(|y|^{1+\varepsilon})\).

## 5.3 Correctness proof, high level overview

We need to show two things about our output, FullLCSAAlgorithm(_x,y_).

\(\text{LCS}(x,y)\ge\text{FullLCSAAlgorithm}(x,y)\) (2)

\(\frac{1+\delta}{2}\text{LCS}(x,y)\le\text{FullLCSAAlgorithm}(x,y)\) (3)

Equation (2) is the easier, which we prove at the end of this section. Equation (3) is the harder direction. We prove it in two cases, based on the following definition.

**Definition 5.1.** We say a pair of binary strings (_x,y_) is _good_ if

1. \(\text{LCS}(x,y)\ge(1-\delta)|x|\),<tbc>

2. For at least \((1-\gamma)m_x\) intervals \(I\in\mathcal{I}_w\), every \(I'\in\mathcal{I}_{\gamma w}(I)\) is \(\gamma\)-balanced, and<tbc>

3. At least \(1-\beta^2\) of \(I\in\mathcal{I}_w\) satisfy \(|J_I^\tau|\ge(1+\beta)|I|\).<tbc>

**Algorithm 2:** FullLCSAAlgorithm


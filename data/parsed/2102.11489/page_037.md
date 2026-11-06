_m_blue+_m/_64 _is satisfied at the beginning of some call_ **Swap**_<sup>n</sup>_(**X**)_, then if and when the function makes a recursive call to_ **Swap**_<sup>n</sup>_(**Y**)_, the same condition is satisfied by the array_ **Y**.

_Proof._ If the execution does not trigger the base case, since _n_ is greater than a sufficiently large constant, _m_ must be greater than a sufficiently large constant too.

Suppose the inequality is satisfied at the beginning of the recursive call. Then, after Step (b), at most _m/_256 elements are `blue`, and at least _m/_64 elements are `red`. After Step (d), due to the property of the near-sorter, **Y**red has at least \((1-\epsilon')\cdot(m/64)\) `red` elements. As long as _m_ is greater than some appropriate constant, in the next recursive call to **Swap**_<sup>n</sup>_(**Y**) in Step (e), \(m':=|\mathbf{Y}|\le\frac{m}{1.9}+\frac{m}{32}\). Let \(m'_\mathrm{red}\) and \(m'_\mathrm{blue}\) be the number of `red` and `blue` elements in **Y** respectively. We have that \(m'_\mathrm{blue}\le m/256\) and \(m'_\mathrm{red}\ge(1-\epsilon')\cdot(m/64)\). Therefore,

\(\frac{m'_\mathrm{red}-m'_\mathrm{blue}}{m'}\ge\frac{(1-\epsilon')\cdot(m/64)-m/256}{\frac{m}{1.9}+\frac{m}{32}}>1/64\)

**Fact 9.6.** _Assume that n is greater than a sufficiently large constant. The remaining number of colored elements at the end of the algorithm is at most_ \(8\alpha n+n_\mathrm{red}-n_\mathrm{blue}\).

_Proof._ The number of `blue` elements remaining is equal to the total number of `blue` elements lost during all executions of Step (c), plus the size of the base case \(\alpha n\). Let _c_:=1/(1/1.9+1/32). The total number of elements lost during all executions of Step (c) is upper bounded by \(\alpha n+\alpha n/c+\alpha n/c^2+\dots\le 3\alpha n\). Therefore, the total number of `blue` elements remaining is upper bounded by \(4\alpha n\). This means that the total number of colored elements remaining is at most \(8\alpha n+n_\mathrm{red}-n_\mathrm{blue}\).

Clearly, Step 1 of the algorithm takes only _n_ number of generalized boolean gates. We now discuss how to implement Step 2 as a circuit.

**Implementing Step 2 in circuit.** This step is accomplished through recursive calls to **Swap** on arrays of length \(n':=n,n/c,n/c^2,\dots\), where _c_:=1/(1/1.9+1/32). The recursion stops when \(n'<\alpha n\). For each length \(n'\), we consume an approximate swapper, a loose compactor, an \(\epsilon'\)-near- sorter, and the reverse-routing circuitry of the loose compactor and the \(\epsilon'\)-near-sorter. Thus for each problem size \(n'=n,n/c,n/c^2,\dots\), we need

• \(S_\mathrm{sw}(n')\) number of (_w_+1)-selector gates and \(B_\mathrm{sw}(n')\) number of generalized boolean gates corresponding to Step (b);<tbc>

• \(2S_\mathrm{lc}(n')\) number of (_w_+2)-selector gates (one for the forward direction and one for the reverse direction) and \(B_\mathrm{lc}(n')\) generalized boolean gates corresponding to Step (c);<tbc>

• \(O(n')\) number of generalized boolean gates and \(O(n')\) number of (_w_+2)-selector gates due to Step (d) and its reverse routing; and<tbc>

• \(O(n')\) generalized boolean gates and \(O(n')\) number of _w_-selector gates due to Step (g).

Note that each (_w_+1)-selector gate can be realized with one _w_-selector gate that operates on the _w_-bit payload and one generalized boolean gate that computes on the extra metadata bit; further, during the reverse routing, the metadata generalized boolean gate can also be used to save whether each output is a filler. Thus each problem size \(n'\) can be implemented with \(S_\mathrm{sw}(n')+2S_\mathrm{lc}(n')+O(n')\) number of (_w_+1)-selector gates and \(B_\mathrm{sw}(n')+B_\mathrm{lc}(n')+2S_\mathrm{lc}(n')+O(n')\) generalized boolean gates. Replacing each (_w_+1)-selector gate with a _w_-selector gate and a generalized boolean gate, we have<tbc>


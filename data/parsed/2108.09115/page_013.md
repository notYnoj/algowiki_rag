inequality. Fortunately, each dense window can only contributes to one level of the entire recursion and thus the overall approximation factor remains bounded.

When we compute the edit distance between pairs of windows, we do it exactly using our algorithm from Section 3. This algorithm is very efficient when the windows are close, but its running time may be as slow as quadratic in the window size when the distance is large. We remark that three recent approximate edit distance algorithms \[And19, BR19, KS19\] also use the basic divide-and-conquer framework, yet manage to obtain comparable or faster running times without preprocessing. Those algorithms compute window-window distances by recursively applying an approximate edit distance algorithm; while this improves efficiency, the approximation factor explodes exponentially in the depth of the recursion.

## 5.2 Decomposition into Variable Sized Windows

### Parameters Settings.

We divide the strings _A,B_ into _windows_, equivalently contiguous substrings. We use _d_ and _t_ to denote the window width and the number of windows of _A_ respectively. Fix _d=n_<sup>1/4</sup> and \(t=\frac{n}{d}=n^{3/4}\) throughout the presentation.

Let \(\epsilon>0\) be an arbitrarily small constant (or slightly sub-constant), such that we would like to obtain a \((7+O(\epsilon))\)-approximation in \(O(n^{3/2+O(\epsilon)})\)-time. The windows in _B_ will vary in width. Moreover, they can be overlapping where the amount of overlap will be controlled by a parameter \(\tau\) which is the relative ED threshold between a pair of windows. We will vary \(\tau\) geometrically, and for each value of \(\tau\), we will compute a set of windows \(\mathcal{B}^\tau\). Let \(t_\tau\) denote the number of windows of \(\mathcal{B}^\tau\). We will have \(t_\tau=O(\frac{n}{\epsilon\tau d})\).

### Choice of Windows.

The choice of windows play a crucial role in our overall algorithm design. For the string _A_, partition _A_ into disjoint _windows_ of width _d_ denoted by A.

\(\mathcal{A}=\{A[1,d],A[d+1,2d],\dots,A[n-d+1,n]\}\)

We now compute the windows of _B_. Let us take \(\tau=\{0,\frac{1}{d},\frac{(1+\epsilon)}{d},\frac{(1+\epsilon)^2}{d},\dots,1\}\). For each value of \(\tau\), we compute a set of windows \(\mathcal{B}^\tau\). Finally, we set \(\mathcal{B}=\cup_\tau\mathcal{B}^\tau\) to denote all computed windows of _B_.

For \(\tau=0\), take \(h_\tau=d\), and \(l_\tau=d\). For \(\tau=\frac{1}{d}\), take \(h_\tau=d+1,l_\tau=d-1\). In general, for \(\tau=\frac{(1+\epsilon)^j}{d}\) , \(j\ge 1\), take \(h_\tau=\lfloor d+(1+\epsilon)^{j-1}\rfloor\) and \(l_\tau=\lfloor d-(1+\epsilon)^{j-1}\rfloor\).

Set \(\gamma_\tau=max(1,\lfloor\epsilon\tau d\rfloor)\). Define

\(\mathcal{H}^\tau:=\{B[1,h_\tau),B[\gamma_\tau+1,\gamma_\tau+h_\tau),B[2\gamma_\tau+1,2\gamma_\tau+h_\tau],\dots\}\)<br>
\(\mathsf{L}^\tau:=\{B[1,l_\tau),B[\gamma_\tau+1,\gamma_\tau+l_\tau),B[2\gamma_\tau+1,2\gamma_\tau+l_\tau],\dots\}\)

Finally, \(\mathcal{B}\tau=\mathcal{H}^\tau\cup\mathsf{L}^\tau\), that is \(\mathcal{B}\tau\) consists of intervals of length \(h_\tau\) and \(l_\tau\) starting at every \(\gamma_\tau\) grid points.

For window \(a\in\mathcal{A}\) (similarly for windows in B), let _s(a_) denote the starting index of _a_ (e.g., _s(A_\[1_,d_\])=1) and let _e(a_) denote index the the last index of _a_ (_e(A_\[1_,d_\])=_d_). This completes the description of the windows.

Note that overall we create \(t=\frac{n}{d}\) windows of _A_ and \(t_\tau=O(\frac{n}{\gamma_\tau})\).


Algorithm 2.2. The Feasible Triplet Algorithm

Once Algorithm 2.2 has terminated, values _r_ and \(\epsilon\) can be used to calculate a lower bound on \(\gamma_{\sigma,d}\) according to (2.6).

### 2.1.1 The Binary Case

The algorithm and related definitions can be greatly simplified (see Algorithm 2.3) when working only with pairs of strings with an alphabet of size two (that is, \(d=2,\sigma=2\)). Let _a_ and _b_ be strings of length \(\ell\), and let _s_ have value 1 if _a_ and _b_ start with the same character and have value 0 otherwise. If we let _F_<sub>0</sub> and _F_<sub>1</sub> be sub-functions that simplify _F<sub>z</sub>_ to the binary case, then, at coordinate (_a,b_), _F_ reduces to

\(F(\mathbf{v}_\mathbf{1},\mathbf{v}_\mathbf{2})[a,b]=\mathbf{s}+max\big(F_0(\mathbf{v}_\mathbf{1},\mathbf{v}_\mathbf{2},a,b),F_1(\mathbf{v}_\mathbf{1},\mathbf{v}_\mathbf{2},a,b)\big).\) (2.7)

Algorithm 2.3. The Binary Feasible Triplet Algorithm

We now define _F_<sub>1</sub> and _F_<sub>0</sub>. Note that _F_<sub>0</sub> has the same definition as _F_<sub>1</sub>, but swaps 0 and 1 when evaluating _h(a_) and _h(b_):


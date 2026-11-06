**Definition 4.4.** A window respecting alignment is a function \(f:\mathcal{W}_1\rightarrow\mathcal{W}_1\times\mathcal{W}_2\times\cdots\times\mathcal{W}_k\) with the following properties:

• For all \(W\in\mathcal{W}_1\), _f(W_)<sub>1</sub>=_W_.<tbc>

• For any \(j<j'\) and any _i_, \(\mathsf{e}(f(W_{1,j})_i)<\mathsf{s}(f(W_{1,j^\prime})_i)\).

Let _r<sub>i</sub>(f_) denote the number of characters in _X<sub>i</sub>_ that are not contained in _f(W)<sub>i</sub>_ for any \(W\in\mathcal{W}_1\). The cost of a window-respecting alignment is defined as follows:

\(\delta_E(f):=\sum_{j\in[J]}\delta_E(f(W_{1,j}))+\sum_ir_i(f).\)

Let F be the set of all window-respecting alignments. The following lemma shows that window- respecting alignments approximate normal alignments:

**Lemma 4.5.**

\(\delta_E(X_1,X_2,\dots X_k)\le min_{f\in\mathcal{F}}\delta_E(f)\le(1+13\epsilon k)\delta_E(X_1,X_2,\dots X_k).\)

_Proof._ The first inequality follows because for any _f_, there is an alignment that for all _j_ exactly aligns _W_<sub>1_,j_</sub> with the windows in _f(W<sub>i,j</sub>_) at cost at most \(\delta_E(f(W_{i,j}))\), and uses \(\sum_ir_i(f)\) deletions to handle the remaining characters in each string.

Next, we show that there exists \(f\in\mathcal{F}\) such that \(\delta_E(f)\le(1+\epsilon k)\delta_E(X_1,X_2,\dots X_k)\). Let us take the substrings _X<sub>i,j</sub>_ given by Lemma 4.3. Note that _W_<sub>1_,j_</sub>=_X_<sub>1_,j_</sub>.

If \(|X_{i,j}|\le\epsilon\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3(\sigma-1)\), let _W<sub>i,j</sub>_ be the empty window "starting" at index \(\mathsf{e}(W_{i,j-1})+1\), or if _j_=1, at index 1. Then we have \(|X_{i,j}|-|W_{i,j}|\le\epsilon\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3(\sigma-1)\).

Otherwise, let _W<sub>i,j</sub>_ be the longest window \(W_{i,\Delta,p}\) that is a substring of _X<sub>i,j</sub>_. Note that |_X<sub>i,j</sub>_| and |_W_<sub>1_,j_</sub>| differ by at most \(\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})\) and \(|W_{i,j}|\le 2\tau/\epsilon^2\) for all _i,j_. If \(\epsilon\) is a sufficiently small constant, this implies there is a choice of _W<sub>i,j</sub>_ such that \(|X_{i,j}|-|W_{i,j}|\le\epsilon\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3(\sigma-1)\). We can identify _W<sub>i,j</sub>_ as follows: Take _X<sub>i,j</sub>_ and delete at most \(\sigma-1\) characters from the beginning until it starts at \(p\sigma+1\) for some integer _p_ to get \(\tilde{X}_{i,j}\). We have \(|X_{i,j}|-|\tilde{X}_{i,j}|\le\sigma-1\), and so \(|\tilde{X}_{i,j}|\) and |_W_<sub>1_,j_</sub>| differ by at most \(\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+(\sigma-1)\) characters. Choose \(\Delta\) such that \(\frac{1}{1+\epsilon}(\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+(\sigma-1))\le\Delta\le\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+(\sigma-1)\). \(W_{i,\Delta,p}\) is a prefix of \(\tilde{X}_{i,j}\) containing all but at most the last \(\epsilon(\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+(\sigma-1))+(\sigma-1)\) characters of \(\tilde{X}_{i,j}\). In turn, if \(\epsilon\) is sufficiently small we have \(|X_{i,j}|-|W_{i,j}|\le\epsilon\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3(\sigma-1)\).

In turn, by triangle inequality and since \(\sigma-1\le\epsilon kD\tau/|X_1|\):

\(\delta_E(W_{1,j},W_{2,j}\dots W_{k,j})\le(1+\epsilon k)\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3\epsilon kD\tau/|X_1|.\)

We now choose _f(W_<sub>1_,j_</sub>)=(_W_<sub>1_,j_</sub>_,W_<sub>2_,j_</sub>_...W<sub>k,j</sub>_). We also have that the number of characters _f_ does not align within _X_<sub>2_,j_</sub>_,X_<sub>3_,j_</sub>_...X<sub>k,j</sub>_ is at most \(\epsilon k\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+3\epsilon kD\tau/|X_1|\).

Putting it all together and using Lemma 4.3 we get:

\(\delta_E(f):=\sum_{j\in[J]}\delta_E(f(W_{1,j}))+\sum_ir_i(f)\)<br>
\(\le(1+\epsilon k)\sum_j\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+\frac{|X_1|}{\tau}\cdot\frac{3\epsilon kD\tau}{|X_1|}\)<br>
\(+\epsilon k\sum_j\delta_E(W_{1,j},X_{2,j}\dots X_{k,j})+\frac{|X_1|}{\tau}\cdot\frac{3\epsilon kD\tau}{|X_1|}+\sum_i(|X_i|-\sum_{j\in[J]}|X_{i,j}|)\)<br>
\(\le(1+2\epsilon k)\sum_j\delta_E(X_{1,j},X_{2,j},\dots X_{k,j})+6\epsilon k\delta_E(X_1,X_2,\dots,X_k)+\sum_i(|X_i|-\sum_{j\in[J]}|X_{i,j}|)\)<br>
\(\le(1+13\epsilon k)\delta_E(X_1,X_2,\dots X_k).\)

## 4.2 An Efficient Algorithm for Window-Respecting Alignments

Our algorithm, denoted _k_-ED-Alg, is as follows:


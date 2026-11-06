## 13:14 Tight Energy Lower Bounds for Distributed Graph Algorithms

We use \(N=\frac{n(n-1)(n-2)}{6}\) to denote the maximum possible number of triangles in any _n_-node graph. Define _w_ to be a node chosen uniformly at random (note that _w_ itself is a random variable), and let _T<sub>w</sub>_ denote the set of triangles output by _w_.

In the proof of Theorem 4.1 in [34], they show that, if _w_ is not a randomly chosen node, but instead the node that outputs the maximum number of triangles, then

\(\mathbf{I}[E:T_w]\ge\frac{\sqrt{2}}{3}\left(\frac{N}{16n}\right)^{2/3}\cdot\mathbf{Pr}\left[|T_w|\ge\frac{N}{16n}\right].\) (10)

We now argue that an asymptotically-equivalent bound also holds for a _randomly_ chosen _w_, under the assumption that each triangle needs to be output by at least one of its constituting nodes. Since there are \(\frac{N}{8}\) triangles in expectation, [34] show that there are at least \(\frac{N}{16}\) triangles with probability at least \(\frac{1}{15}\) by the (reverse) Markov’s inequality. Condition on this event. Observing that each node is in at most _O(n_<sup>2</sup>)=_O(N/n_) triangles, implies that a constant fraction of the nodes must output at least \(\Omega(N/n)\) each. Since _w_ is chosen uniformly at random, it follows that \(|T_w|\ge\Omega\big(\frac{N}{n}\big)\) happens with constant probability, and thus (10) tells us that

\(\mathbf{I}[E:T_w]=\Omega\big(\big(\frac{N}{n}\big)^{2/3}\big).\) (11)

Let _S<sub>w</sub>_ denote the initial state of _w_, which includes the knowledge of its incident edges and let \(\Pi_w\) be the transcript of the messages received by _w_. We aim to apply Lemma 1 with _U_={_w_}, and thus we need to derive a suitable lower bound on \(\mathbf{I}[E:\Pi_w|S_w]\).

Observe that _T<sub>w</sub>_ is a function of \(\Pi_w\), _S<sub>w</sub>_, and the private randomness of _w_. By the data-processing inequality (see Fact 2.6) we obtain that

\(\mathbf{I}[E:\Pi_w|S_w]\ge\mathbf{I}[E:T_w|S_w]\)<br> \(\text{(by (3))}=\mathbf{H}[E|S_w]-\mathbf{H}[E|S_w,T_w]\)<br> \(\text{(since}w\text{has}\le n-1\text{incident edges)}\ge\mathbf{H}[E]-(n-1)-\mathbf{H}[E|S_w,T_w]\)<br> \(\text{(by Fact 2.1)}\ge\mathbf{H}[E]-(n-1)-\mathbf{H}[E|T_w]\)<br> \(\text{(by (3))}=\mathbf{I}[E:T_w]-(n-1)\)<br> \(\text{(by (11))}=\Omega\big(n^{4/3}\big)\) (12)

To complete the proof of the worst-case energy complexity bound, we instantiate Lemma 1(ii) with _V<sub>A</sub>=U_={_w_}, \(V_B=\partial U=V(G)\backslash\{w\}\), _d<sub>U</sub>=n_-1, _Z=E_, and \(L=\Theta\big(n^{4/3}\big)\). Note that there is no dependency between the algorithm’s output and the choice of the cut (_V<sub>A</sub>,V<sub>B</sub>_), as the latter only depends on the randomly chosen node _w_. This shows that node _w_ has a worst-case energy complexity of \(\Omega\big(n^{1/3}/logn\big)\).

Next, we prove the node-averaged bound of \(\Omega(n/logn)\) for local triangle listing. Let P(_T<sub>v</sub>_) denote the set of edges that are part of the triangles output by node _v_. From Lemma 4.3 of [34], it follows that **I**[_E:T<sub>v</sub>_]=**E**[|P(_T<sub>v</sub>_)|], for any _v_. Since _v_ needs to output all its triangles, (11) can be strengthened to yield \(\mathbf{I}[E:T_v]=\Omega\big(n^2\big)\) (as argued in Proposition 4.4 of [34]), and this holds for any node _v_. Analogously to (12), we obtain \(\mathbf{I}[E:\Pi_v|S_v]=\Omega\big(n^2\big)\). Before we can instantiate Lemma 1(i) with _V<sub>A</sub>=U_={_v_}, _Z=E_, \(V_B=\partial U=V(G)\backslash\{v\}\), _d<sub>U</sub>=n_-1, and \(L=\Theta\big(n^2\big)\), we need to verify that \(|\text{supp}(Z)|\le 2^{c\cdot L}=2^{c\cdot\Theta\big(n^2\big)}\), which indeed holds for a suitable constant _c_. This shows that _v_ requires \(\Omega(n/logn)\) awake rounds in expectation. Since the above holds for any _v_, the claimed bound on the node-averaged energy complexity follows. \(\blacktriangleleft\)


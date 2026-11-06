Then, we have<tbc>

\(\big|\mathrm{supp}\big(\mathrm{weights}\big(\{i^*+1,\dots,r_j\}\backslash A\big)\big)\big|\)<br>
\(\ge|\mathrm{supp}(\{w_{i^*+1},\dots,w_{r_j}\})|-|\mathrm{supp}(\mathrm{weights}(A))|\)<br>
\(>(2C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j-1)-C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^j\text{(by Eq. (25))}\)<br>
\(>C\sqrt{w_\mathrm{max}\mathrm{log}w_\mathrm{max}}\cdot 2^{j-1}.\)

Then by Eq. (24) we have<tbc>

<tbc>\(\big|\mathrm{supp}\big(\mathrm{weights}\big(\{i^*+1,\dots,r_j\}\backslash A\big)\big)\big|\cdot W(A\cap I_{\mathcal{W}_{>j}})\ge 2C^2w_\mathrm{max}^2\sqrt{\mathrm{log}w_\mathrm{max}},\)<tbc>

<tbc>and we can apply Lemma 3.1 to weights \(\big(\{i^*+1,\dots,r_j\}\backslash A\big)\) and \(\mathrm{weights}(A\cap I_{\mathcal{W}_{>j}})\) to obtain non-empty \(A'\subseteq A\cap I_{\mathcal{W}_{>j}},B'\subseteq\{i^*+1,\dots,r_j\}\backslash A\) with the same total weight \(W(A')=W(B')\). By definition of \(\mathcal{W}_{\le j}\) we know \(\mathrm{min}_{i\in A^\prime} i>r_j\ge\mathrm{max}_{i\in B^\prime} i\). Hence, \(((A\backslash A')\cup B',B)\) achieves strictly higher profit than (_A,B_), contradicting the optimality of (_A,B_).

We have reached contradiction in both cases, so Eq. (24) cannot hold. This finishes the proof of the claimed properties of the partitioning \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\).

Finally we briefly describe how this partitioning can be computed without actually sorting the _n_ items in _O(n_log_n_) time. First recall that the break point element _i_<sup>∗</sup> of the greedy solution can be found in deterministic _O(n_) time using linear-time median finding algorithms as in \[PRW21\]. Then, for all \(w\in\mathcal{W}\), we can find the item in \(\{i\in[n]:w_i=w\), _p<sub>i</sub>/w<sub>i</sub>\<p_<sub>_i_<sup>∗</sup></sub>_/w_<sub>_i_<sup>∗</sup></sub>} with the highest efficiency, as well as the item in \(\{i\in[n]:w_i=w\), _p<sub>i</sub>/w<sub>i</sub>\>p_<sub>_i_<sup>∗</sup></sub>_/w_<sub>_i_<sup>∗</sup></sub>} with the lowest efficiency, in _O(n+w_<sub>max</sub>) total time. We then sort these 2|W| items by their efficiencies in _O(w_<sub>max</sub>log_w_<sub>max</sub>) time. Using this information, we can easily compute the weights of the boundary items \(\ell_j,r_j\) defined above, and then we can obtain the partitioning.

## B.3 Proof of Lemma 3.6

Here we show how a slightly weaker version of Lemma 3.6 with one extra log(2_r_) factor can be derived from the additive combinatorial result of Bringmann and Wellnitz \[BW21\] (which built on works of Sárközy \[Sár89, Sár94\] and Galil and Margalit \[GM91\]). In the end we will briefly explain how to remove this logarithmic factor by opening the black box of \[BW21\].

**Lemma B.1** (Weaker version of Lemma 3.6)**.** _There is a constant C such that the following holds. Suppose two multisets A,B supported on_ \[_N_\] _satisfy_

\(|\mathrm{supp}_r(A)|\ge C\sqrt{N/r}\cdot\sqrt{\mathrm{log}(2N)}\mathrm{log}(2r)\) (26)

_for some_ \(r\ge 1\)_, and_

\(\Sigma(B)\ge\Sigma(A)-N.\) (27)

_Then,_ \(\mathcal{S}^*(A)\cap\mathcal{S}^*(B)\neq\varnothing\).

To prove Lemma B.1, we need the following lemma by Bringmann and Wellnitz \[BW21\]. For a multiset _X_, denote the maximum multiplicity of _X_ by \(\mu_X:=\mathrm{max}_x\mu_X(x)\).


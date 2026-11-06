_Proof._ We set \(\gamma=1/10\). The overall running time is

\(O(k|S|\mathsf{w}_\mathsf{max}^2+k^2|S|^2\mathsf{w}_\mathsf{max})\)<br>
\(=O(k\cdot k^\gamma logk\cdot\mathsf{w}_\mathsf{max}^2+k^2\cdot k^{2\gamma} log^2k\cdot\mathsf{w}_\mathsf{max})\)<br>
\(=O(k^{1.1}logk\cdot\mathsf{w}_\mathsf{max}^2+k^{2.2}log^2k\cdot\mathsf{w}_\mathsf{max})\)

where the first step follows from \(|S|=O(k^\gamma logk)\), the second step follows from \(\gamma=0.1\).

The guarantee of table \(\widehat{\mathsf{O}}_{\lambda^2}\) follows from properties of graph \(\mathsf{NG}_\lambda\) (Algorithm 1 provides the first property of table in Theorem statement, Lemma 3.4 provides the second property of table in Theorem statement).

## 3.2 Sparsification for arbitrary \(\lambda\) (Step 1 of Theorem 2.1)

One shortcoming of Lemma 3.4 is that the number of remaining edges is only truly subquadratic if \(\lambda\) is constant. As we discuss in Section 3.1, the overall running time of the algorithm depends on the number of edges in the remaining graph; and in order for the running time to be truly subquadratic, we need to reduce the number of edges to truly subquadratic. In this section, we show how one can obtain this bound even when \(\lambda\) is sub-constant. However, instead of losing a factor \(\lambda^2\) in the approximation, our technique loses a factor of \(\Omega(\lambda^3)\).

From here on, we assume that all of the windows are of the same length and we show at the end of the section that this is almost without loss of generality. We begin by giving a definition:

**Definition 3.14** (lcs_<sub>w<sub>a</sub></sub>(w<sub>i</sub>,w<sub>j</sub>_))**.** For two windows _w<sub>i</sub>_ and _w<sub>j</sub>_, and a window _w<sub>a</sub>_, define lcs_<sub>w<sub>a</sub></sub>(w<sub>i</sub>,w<sub>j</sub>_) as the length of the LCS of opt_<sub>i,a</sub>_ and _w<sub>j</sub>_, where opt_<sub>i,a</sub>_ denotes a fixed LCS of _w<sub>i</sub>_ and _w<sub>a</sub>_.

Notice that unlike lcs, this new definition is not symmetric. That is, the size of lcs_<sub>w<sub>a</sub></sub>(w<sub>i</sub>,w<sub>j</sub>_) may be different from the size of lcs_<sub>w<sub>a</sub></sub>(w<sub>j</sub>,w<sub>i</sub>_). Throughout this section and Section 3.2.1, opt_<sub>i,a</sub>_ refers to a fixed (e.g., lexicographically smallest) longest common subsequence of _w<sub>i</sub>_ and _w<sub>a</sub>_. We moreover assume that opt_<sub>i,a</sub>_ and opt_<sub>a,i</sub>_ refer to the same matching.

Similar to lcs, we also normalize the size of lcs_<sub>s</sub>_ by the geometric mean of the lengths of the two windows. Our assumption from here on, until the statement of Theorem 3.21 is that all the windows are of the same length which implies that

\(||\mathsf{lcs}_{w_a}(w_i,w_j)||=\mathsf{lcs}_{w_a}(w_i,w_j)/\sqrt{|w_i||w_j|}=\mathsf{lcs}_{w_a}(w_i,w_j)/|w_i|=\mathsf{lcs}_{w_a}(w_i,w_j)/|w_j|.\)

We bring a reduction in Theorem 3.21 to make our solution work for windows of arbitrary length. In what follows, we first give an algorithm for detecting _close pairs_ (a notion that we introduce later in the section) of windows, and then prove that the number of remaining pairs whose normalized lcs is at least \(\lambda\) is truly subquadratic.

Our algorithm is based on a data structure which we call \(\mathsf{lcs-cmp}(w_a,S,\widetilde{\lambda})\). The reader can think of \(\widetilde{\lambda}=\lambda^2/2\). Let us fix a threshold \(\widetilde{\lambda}\) and a window _w<sub>a</sub>_. \(\mathsf{lcs-cmp}(w_a,S,\widetilde{\lambda})\) receives a set _S_ of windows as input and preprocesses the windows in time \(\widetilde{O}(|w_a|^2|S|)\). Next, \(\mathsf{lcs-cmp}(w_a,S,\widetilde{\lambda})\) would be able to answer each query of the following form in almost linear time (_O_(wmax)):

Given two windows \(w_i,w_j\in S\), either certify that \(||\mathsf{lcs}_{w_a}(w_i,w_j)||<\widetilde{\lambda}\) or find a solution for ||lcs_<sub>w<sub>a</sub></sub>(w<sub>i</sub>,w<sub>j</sub>_)|| of size at least \(\widetilde{\lambda}^2/4\).

We first show in Section 3.2.1, how lcs-cmp gives us a sparsification in truly subquadratic time and then discuss the algorithm for lcs-cmp in Section 3.2.2.


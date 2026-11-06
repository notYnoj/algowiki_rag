This implies that there exists a vertex _b_ whose degree in \(\mathsf{NF}_\lambda\) is more than<tbc>

\(\frac{|V(\mathsf{NF}_\lambda)|}{r}-1=\frac{|V(\mathsf{NF}_\lambda)|}{2/\lambda}-1\ge k^{1-\gamma}-1,\)

<tbc>where the inequality follows by Eq. (9). Thus, the degree of _b_ is at least \(k^{1-\gamma}\). For each vertex _c_ of \(\mathsf{NF}_\lambda\) which is adjacent to _b_ we have

\(||\mathsf{LCS}_{w_c}(w_a,w_b)||=||\mathsf{LCS}_{w_a}(w_c,w_b)||\ge\lambda^2/2.\)

Since the degree of _b_ in \(\mathsf{NF}_\lambda\) is at least \(k^{1-\gamma}\), this means that pair (_w<sub>a</sub>,w<sub>b</sub>_) is a close pair and the edge (_w<sub>a</sub>,w<sub>b</sub>_) should not have existed between the vertices in \(\mathsf{NG}_\lambda\) in the first place.

Now, we are ready to bring our main theorem of this section. In Theorem 3.21 we assume that the windows may have different length but the total number of distinct window sizes is bounded by W<sub>layers</sub>.

**Theorem 3.21** (Sparsification for arbitrary \(\lambda\) (Step 1 of Theorem 2.1))**.** _Given k windows_ \(w_1,\cdots,w_k\)_. Let_ W<sub>layers</sub> _denote the number of different sizes for windows. For any_ \(\lambda\in(0,1)\) _and_ \(\gamma\in(0,1)\)_, there is a randomized algorithm (Algorithm 2) that runs in time_<tbc>

\(O(\mathsf{w}_\mathsf{layers}^2(k^{1+\gamma}\mathsf{w}_\mathsf{max}^2\mathrm{log}^2k+k^{2+\gamma}\mathsf{w}_\mathsf{max}\mathrm{log}k))\)

<tbc>_and outputs a table_ \(\widehat{\mathsf{O}}_{\lambda^3}\in\{0,1\}^{k\times k}\) _such that_<tbc>

\(\mathsf{lcs}(w_i,w_j)/\mathrm{max}\{|w_i|,|w_j|\}\ge\lambda^4/16,\text{\textit{if}}\widehat{\mathsf{O}}_{\lambda^3}[i][j]=1\)

<tbc>_and_

\(\left|\left\{(i,j)|\mathsf{lcs}(w_i,w_j)/\mathrm{max}\{|w_i|,|w_j|\}\ge\lambda,\text{and}\widehat{\mathsf{O}}_{\lambda^3}[i][j]=0\right\}\right|=O(k^{2-\gamma}\mathsf{w}_\mathsf{layers}^2/\lambda).\)

_The algorithm has success probability_ 1-1_/k_<sup>3</sup>.

_Proof._ We run the algorithm explained above \(\mathsf{w}_\mathsf{layers}+\genfrac(){pt}{2}{\mathsf{w}_\mathsf{layers}}{2}\) times. Each of the first W<sub>layers</sub> runs considers one set of windows with equal sizes. Each of the next \(\genfrac(){pt}{2}{\mathsf{w}_\mathsf{layers}}{2}\) runs on one pair of window sizes. For such runs, we pad the smaller windows by dummy characters to make sure all windows have equal lengths. Our estimation for each pair of windows is obtained in one of the runs (which focuses on those particular lengths). Thus, both the runtime and the number of false-negatives of our algorithm are multiplied by a factor of \(O(\mathsf{w}_\mathsf{layers}^2)\).

The running time of each round of Algorithm 2 is

\(=O(\mathsf{lcs-cmp}.\mathsf{Initial}\mathrm{time}+|S|^2\cdot(\mathsf{lcs-cmp}.\mathsf{Query}\mathrm{time}))\)<br>
\(=O(|S|\mathsf{w}_\mathsf{max}^2\mathrm{log}k+|S|^2\mathsf{w}_\mathsf{max})\)<br>
\(=O(k\mathsf{w}_\mathsf{max}^2\mathrm{log}k+k^2\mathsf{w}_\mathsf{max})\)

Since the algorithm repeats the sampling procedure \(O(k^\gamma\mathrm{log}k)\) rounds, thus the overall running time is

\(O(k^\gamma\mathrm{log}k)\cdot O(k\mathsf{w}_\mathsf{max}^2\mathrm{log}k+k^2\mathsf{w}_\mathsf{max})=O(k^{1+\gamma}\mathsf{w}_\mathsf{max}^2\mathrm{log}^2k+k^{2+\gamma}\mathsf{w}_\mathsf{max}\mathrm{log}k).\)


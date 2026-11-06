crossing remains allowed. Therefore, the expectation of \(|\mathrm{Cr}_\sigma^F|\) is at least \(|\mathrm{Cr}_\sigma|/4-\sum_{i=1}^N\mathsf{WB}(X_i)=|\mathsf{WB}_\sigma(X)|/4-\sum_{i=1}^N\mathsf{WB}(X_i)=|\mathsf{WB}(X)|/4-\sum_{i=1}^N\mathsf{WB}(X_i)\). □

From the above claim, there is a choice of the bits _b_<sub>1</sub>_,...,b<sub>N</sub>_, such that, if we define the set _F_ of forbidden points with respect to these bits as before, then \(|\mathrm{Cr}_\sigma^F|\ge\mathsf{WB}(X)/4-\sum_{i=1}^N\mathsf{WB}(X_i)\). From now on we assume that the values of the bits _b_<sub>1</sub>_,...,b<sub>N</sub>_ are fixed, and that the resulting set _F_ of forbidden points satisfies that \(|\mathrm{Cr}_\sigma^F|\ge\mathsf{WB}(X)/4-\sum_{i=1}^N\mathsf{WB}(X_i)\).

## Transforming \(\sigma\) into \(\sigma'\).

We now show how to transform the original permutation \(\sigma\) of L into a new permutation \(\sigma'\) of L, which we will later transform into a permutation \(\tilde{\sigma}\) of \(\tilde{\mathcal{L}}\). We perform _N_ iterations. The input to the _i_th iteration is a permutation \(\sigma_i\) of L and a subset \(F_i\subseteq F\) of forbidden points. The output of the iteration is a new permutation \(\sigma_{i+1}\) of L, and a set \(F_{i+1}\subseteq F_i\) of forbidden points. The final permutation is \(\sigma'=\sigma_{N+1}\), and the final set _F_<sub>_N_+1</sub> of forbidden points will be empty. The input to the first iteration is \(\sigma_1=\sigma\) and _F_<sub>1</sub>=_F_. We now fix some \(1\le i\le N\), and show how to execute the _i_th iteration. Intuitively, in the _i_th iteration, we consolidate the lines of L_<sub>i</sub>_. Recall that we have denoted by \(L_i^*,L_i^{**}\in\mathcal{L}_i\) the first and the last lines of L_<sub>i</sub>_, respectively, in the permutation \(\sigma\). We only move the lines of L_<sub>i</sub>_ in iteration _i_, so this ensures that, in permutation \(\sigma_i\), the first line of L_<sub>i</sub>_ that appears in the permutation is \(L_i^*\), and the last line is \(L_i^{**}\).

We now describe the _i_th iteration. Recall that we are given as input a permutation \(\sigma_i\) of the lines of L, and a subset \(F_i\subseteq F\) of forbidden points. We consider the block B_<sub>i</sub>_ and the corresponding bit _b<sub>i</sub>_.

Assume first that _b<sub>i</sub>_=0; recall that in this case, all points of _X_ that lie on the columns of B_<sub>i</sub>_ to the left of \(L_i^*\) are forbidden (see Figure 2). We start by switching the locations of \(L_i^*\) and \(L_i^1\) in the permutation \(\sigma_i\) (recall that \(L_i^1\) is the leftmost line in L_<sub>i</sub>_). Therefore, \(L_i^1\) becomes the first line of L_<sub>i</sub>_ in the resulting permutation. Next, we consider the location of line \(L_i^{**}\) in \(\sigma_i\), and we place the lines \(L_i^{q_i+1},L_i^2,L_i^3,\dots,L_i^{q_i}\) in that location, in this order. This defines the new permutation \(\sigma_{i+1}\).

Assume now that _b<sub>i</sub>_=1; recall that in this case, all points of _X_ that lie on the columns of B_<sub>i</sub>_ to the right of \(L_i^*\) are forbidden (see Figure 2). We start by switching the locations of \(L_i^*\) and \(L_i^{q_i+1}\) in the permutation \(\sigma_i\) (recall that \(L_i^{q_i+1}\) is the rightmost line in L_<sub>i</sub>_). Therefore, \(L_i^{q_i+1}\) becomes the first line of L_<sub>i</sub>_ in the resulting permutation. Next, we consider the location of line \(L_i^{**}\) in \(\sigma_i\), and we place the lines \(L_i^1,L_i^2,L_i^3,\dots,L_i^{q_i}\) in that location, in this order. This defines the new permutation \(\sigma_{i+1}\).

Lastly, we discard from _F<sub>i</sub>_ all points that lie on the columns of B_<sub>i</sub>_, obtaining the new set _F_<sub>_i_+1</sub> of forbidden points.

Once every block B_<sub>i</sub>_ is processed, we obtain a final permutation \(\sigma_{N+1}\) that we denote by \(\sigma'\), and the final set \(F_{N+1}=\emptyset\) of forbidden lines. The following lemma is central to our analysis. It shows that the Wilber bound does not decrease by much after every iteration. The Wilber bound is defined with respect to the appropriate sets of forbidden points.

**Lemma 3.8** _For all_ \(1\le i\le N\), \(\mathsf{WB}_{\sigma_{i+1}}^{F_{i+1}}(X)\ge\mathsf{WB}_{\sigma_i}^{F_i}(X)-\mathsf{WB}(X_i)-O(|X_i|)\).

Assume first that the lemma is correct. Recall that we have ensured that \(\mathsf{WB}_{\sigma_1}^{F_1}(X)=\mathsf{WB}_\sigma^F(X)\ge\mathsf{WB}(X)/4-\sum_{i=1}^N\mathsf{WB}(X_i)\). Since \(F_{N+1}=\emptyset\), this will ensure that:<tbc>

\(\mathsf{WB}_{\sigma^\prime}(X)\ge\mathsf{WB}_\sigma^F(X)-\sum_i\mathsf{WB}(X_i)-O(|X|)\ge\mathsf{WB}(X)/4-2\sum_i\mathsf{WB}(X_i)-O(|X|).\)


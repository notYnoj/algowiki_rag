**Lemma 5.1** (follows from \[CDG<sup>+</sup>18\])**.** _After running Algorithm 7,_ \(\mathsf{LCS}(\widehat{M})\ge\mathsf{LCS}(M')-2n\epsilon_\mathsf{nbs}\) _holds with probability at least_ 1-1_/n_<sup>4</sup>.

_Proof._ It follows from the definition that the error can only come from the underestimated pairs of windows; for all other pairs, the corresponding entries of matrix \(\widehat{M}\) are at least as large as the respective entries of \(M'\). We prove below that the error from underestimated pairs is bounded.

To this end, fix an optimal window-compatible solution with respect to \(M'\) and let

\((x_1,y_1),(x_2,y_2),\dots\)

be the first indices of the underestimated pairs of windows that contribute to this optimal solution. Let the pairs be sorted by their index. That is _x_<sub>1</sub>_\<x_<sub>2</sub>_\<x_<sub>3</sub>_\<..._ and _y_<sub>1</sub>_\<y_<sub>2</sub>_\<y_<sub>3</sub>_\<..._ hold. The proof is based on the following intuitive argument: with high probability, all but very few pairs of underestimated windows that contribute to the optimal window-compatible solution of \(M'\) are detected in Algorithm 7 and thus their values are corrected.

To see this, consider one pair (_x<sub>i</sub>,y<sub>i</sub>_). This means that there is a window \(w\in W_A\) and a window \(w'\in W_B\) such that the starting index of _w_ is equal to _x<sub>i</sub>_ and the starting index of \(w'\) is equal to _y<sub>i</sub>_. Moreover, the value of the pair \((w,w')\) is underestimated in _M_. Let _X_ be the set of all (_x<sub>j</sub>,y<sub>j</sub>_)’s in (_x_<sub>1</sub>_,y_<sub>1</sub>),(_x_<sub>2</sub>_,y_<sub>2</sub>)_,..._ such that \(|x_j-x_i|\le\mathcal{W}\) and \(|y_j-y_i|\le\mathcal{W}\). Notice that each elements of _X_ in addition to being an underestimated pair of windows also contributes to the optimal window- compatible solution of \(M'\). If \(|X|\ge\epsilon_\mathsf{nbs}k^{\eta/2}\), then with high probability the _A_-side window of one of these underestimated pairs will be sampled in Algorithm 7 and therefore after detecting the underestimated pair, we compute the LCS of (_x<sub>i</sub>,y<sub>i</sub>_) from scratch. If \(|X|<\epsilon_\mathsf{nbs}k^{\eta/2}\) then at least one of the following two constraints should hold:

• The number of _x<sub>j</sub>_’s in (_x_<sub>1</sub>_,y_<sub>1</sub>),(_x_<sub>2</sub>_,y_<sub>2</sub>)_,..._ such that \(x_i-\mathcal{W}\le x_j\le x_i\) is smaller than \(\epsilon_\mathsf{nbs}k^{\eta/2}\).<tbc>

• The number of _y<sub>j</sub>_’s in (_x_<sub>1</sub>_,y_<sub>1</sub>),(_x_<sub>2</sub>_,y_<sub>2</sub>)_,..._ such that \(y_i-\mathcal{W}\le y_j\le y_i\) is smaller than \(\epsilon_\mathsf{nbs}k^{\eta/2}\).

Keep in mind that in the constrains above, each (_x<sub>j</sub>,y<sub>j</sub>_) is an underestimated pair which contributes to the optimal solution of \(M'\). If the former holds, we call _x<sub>i</sub> lonely_. Similarly, if the latter holds, we call _y<sub>i</sub>_ lonely. A simple argument implies that the number of lonely _x<sub>i</sub>_’s (and similarly the number of lonely _y<sub>i</sub>_’s) is bounded by \((\epsilon_\mathsf{nbs}k^{\eta/2})n/\mathcal{W}\): Divide the string into blocks of size W. In each block, at most \(\epsilon_\mathsf{nbs}k^{\eta/2}x_j\)’s are lonely. Thus, the total number of lonely _x<sub>j</sub>_’s is bounded by \((\epsilon_\mathsf{nbs}k^{\eta/2})n/\mathcal{W}\). A similar argument also holds for the number of lonely _y<sub>j</sub>_’s.

Therefore, the size of |_X_| may be smaller than \(\epsilon_\mathsf{nbs}k^{\eta/2}\) for at most \(2(\epsilon_\mathsf{nbs}k^{\eta/2})n/\mathcal{W}\) underes timated pairs in (_x_<sub>1</sub>_,y_<sub>1</sub>),(_x_<sub>2</sub>_,y_<sub>2</sub>)_,..._. This implies that with high probability, the error of \(\widehat{M}\) in comparison to \(M'\) is bounded by

\(2\mathsf{w}_\mathsf{max}(\epsilon_\mathsf{nbs}k^{\eta/2})n/\mathcal{W}=2\mathsf{w}_\mathsf{max}(\epsilon_\mathsf{nbs}k^{\eta/2})n/(k^{\eta/2}\mathsf{w}_\mathsf{max})\)<br>
\(=2n\epsilon_\mathsf{nbs}\)

**Theorem 5.2** (nearby searching for \(\Omega(\lambda^3)\) approximation)**.** _Given that the number of underestimated pairs in Step 1 is bounded by_ \(k^{2-\eta}\)_, for an arbitrary small constant_ \(\epsilon>0\)_, Step 2 takes time_ \(\widetilde{O}(\mathsf{w}_\mathsf{max}^2k^{2-\eta/2}/\lambda^6)\) _and has approximation factor_ \(1-\epsilon\) _with probability at least_ 1-1_/n_<sup>3</sup>.

_Proof._ To make sure the multiplicative factor in the approximation remains \(1-\epsilon\), we set \(\epsilon_\mathsf{nbs}=\Theta(\lambda^4)\). Thus, the runtime of the algorithm would be as follows: In the sampling process, we<tbc>


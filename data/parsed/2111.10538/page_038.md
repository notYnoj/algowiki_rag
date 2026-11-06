• _The total number of windows is equal to_ \(k=|W_A|+|W_B|=\widetilde{O}(n/d)\).<tbc>

• _The maximum size of the windows is equal to_ \(\mathsf{w}_\mathsf{max}=\Theta(d/\lambda)\).<tbc>

• _The minimum size of the windows is equal to_ \(\mathsf{w}_\mathsf{min}=\Theta(d)\).<tbc>

• _The ratio of the maximum window size over the minimum window size is bounded by_ \(\mathsf{w}_\mathsf{gap}=\mathsf{w}_\mathsf{max}/\mathsf{w}_\mathsf{min}=\Theta(1/\lambda)\).<tbc>

• _The number of different layers which is equal to the number of different window sizes is equal to_ \(\mathsf{w}_\mathsf{layers}=O(\mathrm{log}(1/\lambda))\).

_Proof._ We derive the number of windows (the rest of the parameters follow immediately from the construction). In each layer of _W<sub>B</sub>_, the number of windows is<tbc>

\(|W_B^i|=O(t_i\cdot(d_i/d))=O(n/d).\)

<tbc>Therefore the total number of windows is

\(|W_B|=O(fn/d)=\widetilde{O}(n/d).\)

## 4.2.1 Up-to-constant-factor-optimality of window-compatible common subsequence

We present another structural lemma for window-compatible common subsequences. It is similar to Lemma 4.7, but loses a constant factor in length of common subsequence.

**Lemma 4.7** (Window-compatible structural lemma (arbitrary \(\lambda\)))**.**

_For any two strings X,Y of length n, it is possible to map them into A,B in one of the following ways:_

• _A=X,B=Y_<tbc>

• _A=Y,B=X_<tbc>

• _A_=reverse(_X),B_=reverse(_Y), or_<tbc>

• _A_=reverse(_Y),B_=reverse(_X),_

_such that the following holds: If_ \(||\mathsf{lcs}(A,B)||\ge\lambda\)_, there exists a window-compatible common subsequence of A,B of length at least_ \(\Omega(\lambda n)-2\epsilon_0n\) _for the window sets constructed in Definition 4.5._

_Proof._ Fix any LCS of _X,Y_, and suppose we first try _A=X,B=Y_ . For each _j_, let _A<sub>j</sub>_ be the _j_-th window of _A_, and let \(\widetilde{B}_j\) be the minimal substring of _B_ containing all characters common to _A<sub>j</sub>_ and the LCS.

We will analyze a few different cases of \(\widetilde{B}_j\); the trickiest case is when \(\widetilde{B}_j\) and \(\widetilde{B}_{j+1}\) are both contained in the same \(W_B^0\)-window of length _d_. Denote this window by \(\widehat{B}_{j,j+1}\). We claim that in this case the opposite cannot also be true: The minimal substring of _A_ containing all characters common to \(\widehat{B}_{j,j+1}\) and the LCS is not contained in any _W<sub>A</sub>_-window -- this is because it intersects both _A<sub>j</sub>_ and _A_<sub>_j_+1</sub>. We will throw out all such _j_’s; wlog their contribution is at most half of the LCS (otherwise we can consider the reverse assignment _A=Y,B=X_).


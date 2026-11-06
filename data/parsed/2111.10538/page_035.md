• _The total number of windows is equal to_ \(k=|W_A|+|W_B|=O((1/\lambda)^3n/d)\).<tbc>

• _The maximum size of the windows is equal to_ \(\mathsf{w}_\mathsf{max}=\Theta(d/\lambda)\).<tbc>

• _The minimum size of the windows is equal to_ \(\mathsf{w}_\mathsf{min}=\Theta(d\lambda)\).<tbc>

• _The ratio of the maximum window size over the minimum window size is bounded by_ \(\mathsf{w}_\mathsf{gap}=\mathsf{w}_\mathsf{max}/\mathsf{w}_\mathsf{min}=\Theta(1/\lambda^2)\).<tbc>

• _The number of different layers which is equal to the number of different window sizes is equal to_ \(\mathsf{w}_\mathsf{layers}=O((1/\lambda)log(1/\lambda))\)

_Proof._ We derive the number of windows (the rest of the parameters follow immediately from the construction). In each layer of _W<sub>B</sub>_, the number of windows is<tbc>

\(|W_B^i|=O(t_id_i/g_i)=O(n/(d_i\epsilon_0)).\)

<tbc>Thus the total number of windows is given by

\(|W_B|=\sum_{i=-f}^f|W_B^i|=O\left(n/\epsilon_0\sum_{i=-f}^f1/d_i\right)\text{(Def. 4.2)}=O\big(n/(d\epsilon_0)\underbrace{\sum_{i=-f}^f1/(1+\epsilon_0)^i}_{=O(1/\epsilon_0^2)}\big)=O(n/(d\epsilon_0^3))\text{(Geometric sequence).}\)

## 4.1.1 Near-optimality of window-compatible common subsequence

We present a<br>
structural lemma for window-compatible common subsequences. This essentially, shows that the problem of computing LCS between the two strings reduces to the problem of computing the LCS’s between the windows.

**Lemma 4.4** (Window-compatible structural lemma (constant \(\lambda\)))**.**

_For any two strings A,B of length n: If_ \(||\mathsf{lcs}(A,B)||\ge\lambda\)_, there exists a window-compatible common subsequence of A,B of length at least_ \(\lambda n-8\epsilon_0n\) _for the window sets constructed in Definition 4.2._

_Proof._ Fix a LCS of _A,B._

Let _A<sub>j</sub>_ be the _j_-th window of _A_, and let \(\widetilde{B}_j\) be the minimal substring of _B_ containing all characters common to _A<sub>j</sub>_ and the LCS. We consider three cases:

**Case 1:** \(|\widetilde{B}_j|\in[\epsilon_0d,d/\epsilon_0]\)**:** In this case we can keep this pair.


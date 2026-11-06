• \(r\le 6k\mathrm{ln}(3k)\mathrm{ln}n+2\), and<tbc>

• at least one of _G_<sup>∗</sup>\[_J_<sub>1</sub>\]_,...,G_<sup>∗</sup>\[_J<sub>r</sub>_\] has maximum degree more than \(10k\mathrm{ln}n\cdot(6k\mathrm{ln}(3k)\mathrm{ln}n+2)\)

is at most \(\frac{n+1}{n^2}\le\frac{2}{n}\) by the union bound and the fact that \(r\le n+1\) (Lemma 15). Excluding the case _r\>_6_k_ln(3_k_)ln_n_+2, which happens with probability at most \(\frac{1}{n}\) (Lemma 16), Lemma 22 follows. □

## 5.3 The Grand Finale

Finally, we analyze the total number of colors used in Algorithm 1.

**Lemma 23.** _In Algorithm 1, the number of colors used for V_<sup>∗</sup>\\_S is O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>3</sup>_n_) _in expectation._

_Proof._ If the maximum degrees in _G_\[_J_<sub>1</sub>\]_,...,G_\[_J<sub>r</sub>_\] are at most \(\Delta\), then First-Fit uses at most \(\Delta+1\) colors, resulting in at most \(r(\Delta+1)\) colors for the entire _V_<sup>∗</sup>\\_S_. Therefore, by Lemma 16, Lemma 22, and the union bound, we use at most \(O(k\mathrm{log}k\mathrm{log}n)\cdot O(k^2\mathrm{log}k\mathrm{log}^2n)=O(k^3\mathrm{log}^2k\mathrm{log}^3n)\) colors with probability at least \(1-\frac{4}{n}\). In the remaining case, which occurs with probability at most \(\frac{4}{n}\), we may use up to _n_ colors, but this is negligible. □

**Lemma 24.** _The number of calls to_ \(\mathsf{COLORING}_k(\cdot)\) _in Algorithm 1 is at most_ 2log<sub>2</sub>_n_+1 _with probability at least_ \(1-\frac{1}{n}\).

_Proof._ By Lemma 13, each vertex \(v\in V^*\) is put into _S_, i.e., colored in the recursion, with probability \(\frac{1}{2}\). Hence, each vertex \(v\in V^*\) goes down for at least 2log<sub>2</sub>_n_ recursions with probability at most \(2^{-2\mathrm{log}_2n}=\frac{1}{n^2}\). If this does not happen for any \(v\in V^*\), then the recursion depth in Algorithm 1 is at most 2log<sub>2</sub>_n_. By the union bound, this occurs with probability at least \(1-\frac{1}{n^2}\cdot|V^*|=1-\frac{1}{n}\). □

We are now ready to prove our main theorem, which shows that Algorithm 1 uses at most _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors in expectation.

**Theorem 1** (restated)**.** _In the random-order model, when both n and k are known in advance, there exists a randomized online algorithm that colors any k-colorable n-vertex graph using O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) _colors in expectation._

_Proof._ For each call to \(\mathsf{COLORING}_k(\cdot)\), we use _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>3</sup>_n_) colors in expectation, due to Lemma 23. Note that we can assume random arrivals in each call to \(\mathsf{COLORING}_k(m)\), because _m_ does not depend on the graph structure (i.e., it depends only on random choices), and the probability of this event does not change by shuffling the order of the first _m_ vertices, due to the random-order assumption in the original graph _G_<sup>∗</sup>.

Hence, across the shallowest \(\lfloor 2\mathrm{log}_2n+1\rfloor\) calls to \(\mathsf{COLORING}_k(\cdot)\) (or all calls if there are fewer), we use _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors in expectation. If there are more than 2log<sub>2</sub>_n_+1 calls, at most _n_ colors may be used, but this probability is at most \(\frac{1}{n}\) (Lemma 24), so this is negligible. □


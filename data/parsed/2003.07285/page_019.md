**Data**: _s_ and <o>_s_</o>.

**Result**: An approximate solution for LCS.

**1** lcs<sub>1</sub> = the solution returned by Algorithm 3;

**2** lcs<sub>2</sub> = the solution returned by Algorithm 4;

**3** return argmax{|lcs<sub>1</sub>|,|lcs<sub>2</sub>|}

Observation 8.1. _Let X_={_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x_<sub>|_X_|</sub>} _be a set of numbers with the property that_ \(\sum_ix_i=S\) _and_ max_<sub>i</sub>x<sub>i</sub>=M. then, at least S/M of the numbers in X have value at least S/|X|._

## 8.1 Algorithm 3: Block to Block Algorithm

We start by analyzing Algorithm 3. Algorithm 3 divides _s_ and <o>_s_</o> into \(\sqrt{n}\) blocks of size \(\sqrt{n}\). Denote by _b<sub>i</sub>_ and <o>_b_</o><sub>i</sub>, the _i_’th block of _s_ and <o>_s_</o>, respectively. Algorithm 3 constructs a \(\sqrt{n}\times\sqrt{n}\) table _T_ as follows: for every _i_ and _j_, Algorithm 3 chooses a random position in _b<sub>i</sub>_. Let _c_ be the symbol in the randomly selected position. We set<tbc>

\(T[i][j]=min\{\mathsf{fr}_c(b_i),\mathsf{fr}_c(\overline{b_j})\}.\)

<tbc>For brevity, denote by _c<sub>i,j</sub>_ the symbol selected for blocks _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub>. Obviously, we can fill table _T_ in time _O(n_). Using _T_, Algorithm 5 finds the longest common subsequence of _s_ and <o>_s_</o> with the following two constraints:

• No two characters in the same block of _s_ are matched to the characters in different blocks of <o>_s_</o> and vice versa.<tbc>

• If a block _b<sub>i</sub>_ is matched to a block <o>_b_</o><sub>j</sub>, then all the matched symbols of _b<sub>i</sub>_ and <o>_b_</o><sub>j</sub> are _c<sub>i,j</sub>_.

Denote by \(\widetilde{\mathsf{lcs}}(s,\overline{s})\), the longest common subsequence of _s_ and <o>_s_</o> with the constraints described above. We can use dynamic programming to find \(\widetilde{\mathsf{lcs}}(s,\overline{s})\) as follows. Let _D_ be a \(\sqrt{n}\times\sqrt{n}\) table where _D_\[_i_\]\[_j_\] stores the length of the longest restricted common subsequence of the strings corresponding to the first _i_ blocks of _s_ and the first _j_ blocks of <o>_s_</o>. Then, _D_\[_i_\]\[_j_\] can be computed via the following recursive formula:

\(D[i][j]=\left\{\begin{array}{ c c }
0 & i\text{or}j=0 \\
max\left\{\begin{array}{ c }
D[i][j-1], \\
D[i-1][j], \\
T[i][j]+D[i-1][j-1]
\end{array}\right\} & i,j>0
\end{array}\right.\) (8.6)

The total running time of Algorithm 3 is _O(n_). We now determine the conditions under which Algorithm 3 returns an \(O(n^{1/2-\zeta})\) approximation solution for a fixed \(\zeta\). For this, we first in Lemma 8.2 show that there exists a set of \(\Omega(n^{1/2-2\delta})\) pairs of blocks, where each block pair contributes \(\Omega(n^{1/2-\delta})\) characters to lcs(_s,<o>s</o>_).

Lemma 8.2. _There exist two sequences i_<sub>1</sub>_\<i_<sub>2</sub>_\<...\<i<sub>l</sub> and j_<sub>1</sub>_\<j_<sub>2</sub>_\<...\<j<sub>l</sub> of indices such that_ \(l\ge n^{1/2-2\delta}/8\)_, and for every k,_ \(|\mathsf{lcs}(b_{i_k},\overline{b_{j_k}})|\ge n^{1/2-\delta}/2\).

**Algorithm 6:** block-to-block + random shifting Algorithm


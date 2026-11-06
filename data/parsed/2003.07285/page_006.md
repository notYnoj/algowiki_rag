The first two algorithms that we perform on the input instances are Algorithms 1 and 2. Algorithm 1 is a modification of Algorithm 0 which is \(\overline{o}(\sqrt{n})\) approximation when the solution size is small. Here we skip the details and just mention that after applying Algorithm 1, the solution size in the nontrivial instances is lower bounded by \(\overline{\Omega}(n)\).

Observation 4.2. _After running Algorithm 1 we have_ \(|\mathsf{lcs}(s,\overline{s})|=\overline{\Omega}(n)\) _for all the nontrivial instances._

Next, we discuss Algorithm 2 in Section 7 and show that after running Algorithm 2, the number of symbols in the nontrivial instances is bounded <o>_O_</o>(_n_<sup>1/2</sup>).

Observation 4.3. _After running Algorithm 2, we have m_=<o>_O_</o>(_n_<sup>1/2</sup>) _for any nontrivial instance._

The more technically involved part of the analysis is dedicated to Algorithms 3, and 4 which we discuss in Section 4.1.

## 4.1 Decomposition into Blocks & Permutations

The last step of our algorithm is technically more involved as we perform two separate algorithms and argue that the better of the two algorithms has an approximation factor of \(\overline{o}(\sqrt{n})\) on the nontrivial instances. So far, we have shown that in the nontrivial instances we have \(m=\overline{O}(\sqrt{n})\) and \(|\mathsf{lcs}(s,\overline{s})|=\overline{\Omega}(n)\). Therefore, we assume that the rest of the cases are excluded from the nontrivial instances.

We divide both _s_ and <o>_s_</o> into blocks of size \(\sqrt{n}\). Denote by _b<sub>i</sub>_ and \(\overline{b_i}\), the _i_’th block of _s_ and <o>_s_</o>, respectively. We perform Algorithms 3 and 4 simultaneously on _s_ and <o>_s_</o> and argue that one of them performs well on each nontrivial instance. We first bring the pseudocodes of Algorithms 3 and 4 and then present the intuition behind each algorithm.

Data: s and <o>_s_</o>.<br>
Result: An approximate solution for LCS.<br>
Divide s and <o>_s_</o> into \(\sqrt{n}\) blocks as explained; \(\triangleright b_i\): i’th block of s and <o>_b_</o><sub>j</sub>: j’th block of <o>_s_</o><br>
Compute fr<sub>c</sub>(b<sub>i</sub>) and fr<sub>c</sub>(<o>_b_</o><sub>i</sub>) for every symbol \(c\in\Sigma\) and \(i\in[\sqrt{n}]\);<br>
\(T,D\leftarrow\) two \(\sqrt{n}\times\sqrt{n}\) tables;<br>
for \(i\leftarrow 1\) to \(\sqrt{n}\) do<br>
   for \(j\leftarrow 1\) to \(\sqrt{n}\) do<br>
   \(c\leftarrow\) a random character of block b<sub>i</sub>;<br>
   \(T[i][j]\leftarrow\mathrm{min}\{\mathsf{fr}_c(b_i),\mathsf{fr}_c(\overline{b_j})\}\);<br>
   for \(i\leftarrow 1\) to \(\sqrt{n}\) do<br>
   for \(j\leftarrow 1\) to \(\sqrt{n}\) do<br>
   \(D[i][j]\leftarrow\mathrm{max}\{D[i][j-1],D[i-1][j],D[i-1][j-1]+T[i][j]\}\);<br>
Return(max<sub>i,j</sub>D[i][j])

As mentioned earlier, we decompose the strings into \(\sqrt{n}\) blocks of equal size in both the algorithms. In Algorithm 3, we estimate the LCS of each pair of blocks from _s_ and <o>_s_</o> by a very simple sampling argument and then run a dynamic program to construct a solution that incorporates all blocks. In Algorithm 4 however, we first turn each block into a _semi-permutation_. That is, we<tbc>

**Algorithm 3:** block to block


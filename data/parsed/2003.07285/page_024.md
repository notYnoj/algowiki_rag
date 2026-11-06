Data: U<br>
Result: \(U'\): a set of complete permutations.<br>
\(\mathsf{mask}(s)=\emptyset\);<br>
B: a set of \(\mathrm{log}n/\alpha\) blocks of s that belong to \(\widetilde{U}_2\), selected uniformly at random;<br>
for each \(b\in B\) do<br>
  \(\tilde{b}=\mathrm{maximal}\) substring of b only consisted of the characters in \(\widetilde{\Sigma}\backslash\mathsf{mask}(s)\) ;<br>
  \(\mathsf{mask}(s)\leftarrow\mathsf{mask}(s)+\tilde{b}\); \(\triangleright\tilde{b}\) is appended to the end of mask(s)<br>
if mask(s) is not a permutation of \(\widetilde{\Sigma}\) then<br>
Add<br>
the<br>
characters<br>
in<br>
\(\widetilde{\Sigma}\backslash\mathsf{mask}(s)\)<br>
with<br>
an<br>
arbitrary<br>
order<br>
to<br>
the<br>
end<br>
of<br>
mask<br>
(s)<br>
for each \(b_i\in U\) do<br>
   \(b'_i=b_i\) ;<br>
   b=maximal substring of mask(s) only consisted of the characters in \(\widetilde{\Sigma}\backslash\tilde{b}'_i\) ;<br>
   \(b'_i=b'_i+b\) ;<br>
return \(U'=\{b'_1,b'_2,\dots,b'_{|U|}\}\)

Lemma 8.4. _Let_ \(\beta\) _be the expected length of the longest common subsequence of two random blocks of U and <o>U</o> and_ \(b'_i,\overline{b'_j}\) _be two random blocks of_ \(U'\) _and_ \(\overline{U'}\)_. Then, the expected size of_ \(\mathsf{lcs}(b'_i,\overline{b'_j})\) _is_ \(O(\beta\mathrm{log}n/\alpha)\).

**Proof.** First, note that mask(s) is consisted of two parts: the part that is appended to mask(s) with respect to the random blocks of \(\widetilde{U}_2\), and the part that includes the symbols which are added to mask(s) in an arbitrary order. We denote these two parts by _w_ and _a_, respectively (and <o>_w_</o>,<o>_a_</o> for mask(<o>_s_</o>)). Recall that the probability that each symbol appears in each random block is \(\alpha\). Considering this, we claim that the expected size of _a_ is _O_(1). Let _p<sub>c</sub>_ be the probability that after appending the extra symbols in \(\mathrm{log}n/\alpha\) randomly selected blocks, \(b'_i\) does not contain symbol _c_. By definition, _c_ appears in each of the randomly selected blocks with probability at least \(\alpha\). Hence, after \(\mathrm{log}n/\alpha\) steps, we have

\(p_c\le(1-\alpha)^{\mathrm{log}n/\alpha}\simeq e^{-\mathrm{log}n}\le 1/n.\)

On the other hand, we know that the number of the characters in \(\Sigma\) is _O(n_) which concludes that the expected number of the characters in _a_ is \(O(n\cdot p_c)=O(1)\). The same argument also implies <o>_a_</o>=_O_(1). Furthermore, each of _w_ and <o>_w_</o> is a concatenation of the characters in \(\mathrm{log}n/\alpha\) random blocks.

Now, consider two blocks \(b'_i\) and \(\overline{b'_j}\) selected uniformly at random from \(U'\) and \(\overline{U'}\). Note that we can argue that each of \(b'_i\) and \(\overline{b'_j}\) is a concatenation of the characters in at most \(\mathrm{log}n/\alpha\) random blocks plus a string of size _O_(1). With an argument similar to the one used in the proof of Lemma 8.2, we can imply that the number of different block pairs that contribute to \(\mathsf{lcs}(b'_i,\overline{b'_j})\) is \(O(\mathrm{log}n/\alpha)\). Furthermore, we assume that the expected size of the longest common subsequence of two random blocks of _U_ and <o>_U_</o> is \(\beta\), which concludes that the expected size of the longest common subsequence of \(b'_i\) and \(\overline{b'_j}\) is \(O(\beta\mathrm{log}n/\alpha)\).

**Algorithm 7:** semi-permutation to complete-permutation


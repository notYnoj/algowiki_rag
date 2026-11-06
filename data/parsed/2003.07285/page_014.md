<tbc>Let _R_:=|{(_i,j_)|_s<sub>i</sub>_=<o>_s_</o><sub>j</sub>}| be the number of matching pairs in _s_ and <o>_s_</o>. This step is based on an exact algorithm by Apostolico and Guerra \[22\] to solve LCS in time \(\widetilde{O}(n+R)\). The main idea behind the algorithm of Apostolico and Guerra \[22\] is to construct an array _M_ of size _R_, where each element of _M_ is a pair of indices (_a,b_) that corresponds to a matching pair of _s<sub>a</sub>_ and <o>_s_</o><sub>b</sub> (_s<sub>a</sub>_=<o>_s_</o><sub>b</sub>). The construction of _M_ also requires the pairs to be sorted, that is, pair (_a,b_) comes before pair \((a',b')\) if and only if either \(a<a'\) or \(a=a'\) and \(b<b'\).

It follows from the construction of _M_ that finding lcs(_s,_<o>_s_</o>) is equivalent to finding the longest subsequence of _M_ that is increasing in terms of both the first and the second element of each pair. Apostolico and Guerra \[22\] show that such an increasing subsequence can be found in time \(\widetilde{O}(n+R)\) using a classic data structure. Here, we slightly modify the method of \[22\] to present a randomized \(\widetilde{O}(n+R/\alpha)\) algorithm with an approximation factor of \(\alpha\). The overall idea is to sample each element of _M_ with a rate of \(1/\alpha\) and solve the problem for the sampled set. Notice that since we wish to keep the running time \(\widetilde{O}(n+R/\alpha)\), we do not afford to generate array _M_ before sampling the elements since the size of _M_ may be more than \(\widetilde{O}(n+R/\alpha)\). However, we explain later in the section that the sampled array can be constructed in time \(O(n+R/\alpha)\) and thus an \(\alpha\) approximation of LCS can be obtained in time \(\widetilde{O}(n+R/\alpha)\).

Data: s and <o>_s_</o>. R: number of matching pairs of s and \(s'\)<br>
Result: An \(\alpha\)-approximate solution for LCS.<br>
M<sup>∗</sup>= empty array ;<br>
\(j\leftarrow 0\) ;<br>
P= a geometric probability distribution on \(\{1,2,\dots,\infty\}\) with \(P(Y=k)=(1-\alpha)^{k-1}\alpha\) ;<br>
\(z\leftarrow 0\);<br>
while j\<R do<br>
   Sample x from P; \(\triangleright x\): distance to the index of the next element<br>
\(j\leftarrow j+x\) ;<br>
   if \(j\le R\) then<br>
   \(p\leftarrow j\)’th element of M; \(\triangleright M\) is the set of matching pairs<br>
   \(\triangleright\) We dont have access to M directly, but M\[j\] can be found in time \(\widetilde{O}(1)\)<br>
   M<sup>∗</sup>\[z\]=p;<br>
   \(z\leftarrow z+1\);<br>
Find the longest subsequence of M<sup>∗</sup> which is increasing in terms of both the elements.

Using the above algorithm, we modify the input to guarantee \(m=O(n^{1/2+\eta})\) for some \(\eta\ge 0\). For a given threshold \(\tau\), define a symbol _c_ in string _t_ to be low frequency, if \(\mathsf{fr}_c(t)\le\tau\) and high frequency otherwise. For a string _t_, we define _t_<sub>L</sub> and _t_<sub>H</sub> to be subsequences of _t_ subject to only low and only high frequency symbols, respectively. For instance, if _t_=aabccd and \(\tau=1\) we have _t_<sub>L</sub>=bd and _t_<sub>H</sub>=aacc.

It follows from the definition that for any threshold \(\tau\) we have

\(|\mathsf{lcs}(s_\mathsf{L},\overline{s_\mathsf{L}})|+|\mathsf{lcs}(s_\mathsf{L},\overline{s_\mathsf{H}})|+\)<br>
\(|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{L}})|+|\mathsf{lcs}(s_\mathsf{H},\overline{s_\mathsf{H}})|\ge|\mathsf{lcs}(s,\overline{s})|\)

**Algorithm 5:** sampled array


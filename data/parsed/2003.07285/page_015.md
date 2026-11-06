which in turn implies

\(max\left\{\begin{array}{ c }
|\text{lcs}(s_\text{L},\overline{s_\text{L}})|, \\
|\text{lcs}(s_\text{L},\overline{s_\text{H}})|, \\
|\text{lcs}(s_\text{H},\overline{s_\text{L}})|, \\
|\text{lcs}(s_\text{H},\overline{s_\text{H}})|
\end{array}\right\}\ge|\text{lcs}(s,\overline{s})|/4.\)

Hence, by solving LCS for all four combinations and returning the best solution, one can provide a 4-approximation solution to lcs(_s,<o>s</o>_). Indeed this argument also carries over to any approximate solution, that is, approximating the subproblems within a factor of \(\alpha\) implies a \(4\alpha\) approximate solution for lcs(_s,<o>s</o>_). We show that except the subproblem (_s_H,<o>s</o>H) the number of matching pairs (_R_) for the rest of the subproblems is bounded and thus a desirable solution for such instances can be obtained using Algorithm 5. Hence, the only nontrivial instance is the case of (_s_H,<o>s</o>H). Therefore, if the solution of Algorithm 2 is not desirable, it only suffices to find an approximate solution for lcs(_s_H,<o>s</o>H). Moreover, since each symbol appears at least \(\tau\) times in any of _s_H and <o>s</o>H, the number of symbols of _s_H and <o>s</o>H is bounded by \(n/\tau\).

Algorithm 2 has no assumption on the input and outputs three strings \(t,s'\) and \(\overline{s'}\), where \(s'\) and \(\overline{s'}\) are subsequences of _s_ and <o>s</o>. For a fixed \(0<\eta<1/2\), Algorithm 2 guarantees that either _t_ is an \(O(n^{1/2-\eta})\) approximation solution, or \(|\text{lcs}(s',\overline{s'})|\ge|\text{lcs}(s,\overline{s})|/4\) and \(|\Sigma'|=O(n^{1/2+\eta})\), where \(\Sigma'\) is the set of symbols appeared in \(s'\) and \(\overline{s'}\).

As mentioned earlier, the basic idea behind Algorithm 2 is to decompose each of _s_ and <o>s</o> into two substrings based on the frequency of the symbols and solve the subproblems corresponding to the four combinations. For this purpose, we define the concept of low and high frequency symbols. Let \(\tau=n^{1/2-\eta}\) be a threshold and define a symbol _c_ to have a low frequency in string _t_, if \(\text{fr}_c(t)\le\tau\). Otherwise, _c_ has a high frequency. In addition, let _t_L and _t_H be the substrings of _t_ restricted to the symbols with low and high frequencies, respectively. Since _s_L and _s_H cover _s_ and <o>s</o>L and <o>s</o>H cover <o>s</o>, we have

\(|\text{lcs}(s_\text{L},\overline{s_\text{L}})|+|\text{lcs}(s_\text{L},\overline{s_\text{H}})|+\)<br>
\(|\text{lcs}(s_\text{H},\overline{s_\text{L}})|+|\text{lcs}(s_\text{H},\overline{s_\text{H}})|\ge|\text{lcs}(s,\overline{s})|.\) (7.4)

Inputs: s and <o>s</o>.
Outputs: ,s', , where ,s' is a subsequence of s and ' is a subsequence of <o>s</o>.
Guarantee: Either t is an (n1/2- ) approximation of lcs(s, , or
• |lcs(s', , /
• | = O(n1/2+ ).

**Algorithm 2:** low, high frequency algorithm

**Data**: _s_ and <o>s</o>.

**Result**: An approximate solution for LCS.

**1** \(\tau\leftarrow n^{1/2-\eta}\) ;

**2** Construct _s_L,_s_H,<o>s</o>L,<o>s</o>H ;

**3** Approximate lcs(_s_L,<o>s</o>L), lcs(_s_L,<o>s</o>H), and lcs(_s_H,<o>s</o>L) using Algorithm 5 and return the best;


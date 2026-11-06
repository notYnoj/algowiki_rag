**Lemma 4.7.** _Let_ \(\ell\) _be a power of two, and_ \(w>\varepsilon^{-2}\ell\)_. If a string x of length w is_ \(\ell\)_-fine, then there exists an interval I with_ \(\mathsf{LCS}(x_I,y_\ell)\ge\frac{|I|}{2}+\varepsilon^3|x|\)_. Furthermore, given x and_ \(\ell\)_, we can determine the interval I and the common subsequence of x<sub>I</sub> and_ \(y_\ell\) _in time O(w_log_w)._

_Proof._ The number of \(\ell^+\)-flags in _x_ is at least \(\varepsilon w\). By pigeonhole, there exists some interval \(I'=[a,b]\) of length \(4\varepsilon^2w\) containing at least \(2\varepsilon^3w\) many \(\ell^+\)-flags (the lost factor of two accounts for \(2\varepsilon^2w\) possibly not evenly dividing _w_). Furthermore, since _x_ is not coarse, we may assume that each such \(\ell^+\)-flag is an \(\ell'\)-flag for some \(\ell'\in[\ell,\varepsilon^2w)\). Thus, the interval \(I=[a,b+11\varepsilon^2w]\) has length \(4\varepsilon^2w+11\varepsilon^2w\le 20\varepsilon^2w\) and \(x':=x_I\) has at least \(2\varepsilon^3w\) many \(\ell^+\)-flags (we cannot simply take \(x'=x_{I^\prime}\), as bits at the right end of _I_ may be flags in _x_ but not in \(x_{I^\prime}\)). Furthermore, \(x'\) is \(\varepsilon^2\)-balanced since it has length at least \(\varepsilon^2w\) and is a substring of _x_, which is not coarse. We can find interval \(I'\), and thus _I_ and \(x'\), in time _O(w_log_w_), because (with preprocessing of the string’s prefix sums) we can test whether a bit is an \(\ell^+\)-flag in log_w_ time, so counting the flags in an interval can be done in _O(w_log_w_) time, and there are a constant number of intervals to check.

Now we claim \(\mathsf{LCS}(x',y_\ell)\ge\frac{|x'|}{2}+\varepsilon^3|x|\). Construct a common subsequence \(x''\) of \(x'\) and \(y'\) as follows: Initialize a counter _i_=1. While \(i\le 1(x')\),

1. Append a one to \(x''\),<tbc>

2. If the _i_th one of \(x'\) is an \(\ell'\)-flag for some \(\ell'\ge\ell\), append \(1+[10(\ell'-1)]\) zeros to \(x''\) and \(i\leftarrow i+\ell'\).<tbc>

3. Otherwise \(i\leftarrow i+1\).<tbc>

<tbc>We claim the subsequence \(x''\) has the following properties.

• \(x''\) is a subsequence of \(x'\).<tbc>

• \(x''\) is a subsequence of \(y_\ell\).<tbc>

• \(x''\) has length at least \(\frac{|x'|}{2}+\varepsilon^3|x|\).

To see the first property, take the subsequence of \(x'\) where the one added to \(x''\) when the counter is _i_ is matched to the _i_-th one of \(x'\), and the zeros added when the counter is _i_ are the zeros between the _i_-th and \((i+\ell')\)-th one of \(x'\), of which there are at least \(1+[10(\ell'-1)]\) because _i_ is an \(\ell'\)-flag in \(x'\).

To see the second property, first note that \([10(\ell'-1)]+1\ge\ell'\) for all positive integers \(\ell'\), so all runs of zeros in \(x''\) have length at least \(\ell\). Write \(x''=1^{a_1}0^{a_2}1^{a_3}0^{a_4}\cdots 1^{a_{2k+1}}\), where all \(a_{2i}\ge\ell\) and \(a_{2i-1}\ge 1\) for all positive integers _i_ (except possibly _a_<sub>2_k_+1</sub>, which may be 0). Notice that 1_<sup>a<sub>i</sub></sup>_ and 0_<sup>a<sub>i</sub></sup>_ are each subsequences of \((0^\ell 1^\ell)^{r_i}\), where \(r_i:=\lceil a_i/\ell\rceil\le\frac{a_i}{\ell}+1\). Thus, \(x''\) is a subsequence of \((0^\ell 1^\ell)^r\) for \(r:=r_1+\cdots+r_{2k+1}\). Thus, we have

\(r\le r_1+\cdots+r_{2k+1}\le\frac{a_1+\cdots+a_{2k+1}}{\ell}+(2k+1)<\frac{4(a_1+\cdots+a_{2k+1})}{\ell}\le\frac{80\varepsilon^2w}{\ell}<\frac{\varepsilon w}{5\ell},\)

proving that \(x''\) is a subsequence of \(y_\ell\). In the third inequality above, we used \(a_2+a_4+\cdots+a_{2k}\ge k\ell\), so \(2k+1\le 3k<\frac{3(a_1+\cdots+a_{2k+1})}{\ell}\) . In the fourth inequality, we used \(a_1+\cdots+a_{2k+1}=|x''|\le|x'|\le 20\varepsilon^2w\).

To see the third property, notice that \(|x''|-i\) only changes when a run of zeros is added to \(x''\). If this run is added for an \(\ell'\)-flag at _i_ in \(x'\), then difference \(|x''|-i\) increases by \(1+[9(\ell'-1)]\ge\ell'\), while the total number of flags skipped over is at most \(\ell'\). By induction on _i_, after every while-loop iteration, we have

\(|x''|-i\ge\#\{\ell^+\text{-flags in}[i]\}.\)

so the total length of \(x''\) at the end is at least

\(1(x')+\#\{\ell^+\text{-flags in}x'\}\ge\left(\frac{1}{2}-\varepsilon^2\right)|x'|+2\varepsilon^3w\ge\frac{|x'|}{2}+\varepsilon^3|x|,\)

as desired. The first inequality above follows from the fact that \(x'\) is \(\varepsilon^2\)-balanced, and the second from \(|x'|\le 20\varepsilon^2w\).


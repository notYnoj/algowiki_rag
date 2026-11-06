If \(\text{level}(s)\leftarrow\ell\) is triggered through updateScores, then before the last if statement in extendPaths, we have \(\text{level}(s)=\ell-1\ge\ell_0\) and _v_ is added to \(\hat{L}(s,\ell)\). On the other hand, if \(\text{level}(s)\leftarrow\ell\) is triggered through increaseLevel, at the first step of increaseLevel, we have \(\text{level}(s)=\ell-1\ge\ell_0\) so _v_ is added to \(\hat{L}(s,\ell)\).

In any future iterations, the equality holds as we only update \(\hat{L}(s,\text{level}(s)+1)\) when level(_s_) increases.

Thus, we have established that \(\widehat{\text{d}}(s,v)=\text{dist}(s,v)\) for all \(\text{dist}(s,v)\le\text{level}(s)\) at the end of each iteration of the while loop. Again, we must argue that the while loop does not terminate until all distances are computed.

**Lemma 5.14.** _If there exists_ \(\widehat{\text{d}}(s,v)>\text{dist}(s,v)\) _at the end of an iteration, then the while loop will not terminate._

_Proof._ Suppose the while loop terminates while there is some wrong distance: i.e. _v_ with \(\widehat{\text{d}}(s,v)>\text{dist}(s,v)\) at the end of the iteration. We claim \(s\in S\), ensuring the while loop does not terminate. It suffices to argue \(v\unknown\in\bigcup_{r=0}^{\text{level}(s)}\hat{L}(s,r)\). By Lemma 5.13, we have \(\widehat{\text{d}}(s,v)>\text{dist}(s,v)>\text{level}(s)\), implying that \(v\unknown\in\bigcup_{r\le\text{level}(s)}\hat{L}(s,r)\) since \(\hat{L}(s,r)\) only contains vertices _w_ with \(\widehat{\text{d}}(s,w)\le r\), as desired.

Finally, we argue that either the condition to run increaseLevel or the condition to run extendPaths is satisfied in each iteration.

**Lemma 5.15.** _If all s have_ \(\mathcal{A}(s,b)\neq\emptyset\) _for some b, there exists_ \(V_i^{(b)}\) _with_ \(\text{score}(i,b)>\frac{|S|\left|N\left(V_i^{(b)}\right)\right|}{2\phi n\mathrm{log}B}\) .

_Proof._ Following a similar argument to Lemma 5.4, we bound the sum of scores from below.

\(\sum_{i,b}\text{score}(i,b)=\sum_{i,b}\left|\left\{s\in S\text{s.t.}\mathcal{A}(s,b)\cap V_i^{(b)}\neq\emptyset\right\}\right|=\sum_s\left|\left\{V_i^{(b)}\text{s.t.}\mathcal{A}(s,b)\cap V_i^{(b)}\neq\emptyset\right\}\right|\ge|S|\)

If all \(\text{score}(i,b)\le\frac{|S|\left|N\left(V_i^{(b)}\right)\right|}{2\phi n\mathrm{log}B}\) , then we obtain a contradiction via

\(\sum_{i,b}\text{score}(i,b)\le\sum_b\sum_i\frac{|S|\left|N\left(V_i^{(b)}\right)\right|}{2\phi n\mathrm{log}B}\le(1+\mathrm{log}B)\frac{|S|}{2\mathrm{log}B}<|S|.\)

We have thus established that our algorithm (if it terminates) outputs exact distances between _S_<sub>in</sub> and _V_ . As before, it remains to show that the algorithm terminates, which we prove below.

## Running Time.

We now bound the running time, thus proving that our algorithm terminates and produces the correct output. First, the initialization phase takes \(O\left(n^{2+o(1)}\mathrm{log}B+|S_\mathrm{in}|Bn\right)=Bn^{2+o(1)}\) time.

We separately bound the time required by the while loop of the computation phase. First, we bound the total time required by all iterations where increaseLevel is invoked. We defer the proof to the end of this section.

**Lemma 5.16.** _The total time used by all calls to increaseLevel is_ \(\tilde{O}\left(|S_\mathrm{in}|nB\right)=\tilde{O}\left(Bn^2\right)\).

Next, we bound the total time required by all iterations where extendPaths is invoked. As in Theorem 5.1, we bound the time required by all iterations where a fixed cluster \(V_i^{(b)}\) is chosen. Let _T(i,b_) denote the iterations where \(V_i^{(b)}\) is the chosen cluster. We again bound the number of iterations where \(s\in S'\) in _T(i,b_) and the size of _T(i,b_), analogously to Lemma 5.5 and Lemma 5.6.

**Lemma 5.17.** _For any_ \(s\in S_\mathrm{in}\) _and_ \(V_i^{(b)}\), \(s\in S'\) _for at most_ 3_d distinct_ \(t\in T(i,b)\).


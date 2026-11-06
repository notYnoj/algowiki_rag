results in a "regular path" (Definition 6.2), see Fig. 6 for an example of such a rounding) to be:

\(M\cdot(\mathrm{Curv}(p)\text{on active scales})\lesssim M\cdot\mathrm{Curv}(p)\cdot(\mathrm{fraction of active scales})\)<br>
\(\lesssim M\cdot\varepsilon n\sqrt{|S|}\cdot\frac{|\widetilde{S}|}{|S|}\)<br>
\(=o(\varepsilon n).\)

These ideas suffice for obtaining an additive _o(n_)-approximation for ED and LCS<sup>11</sup>.

## 2.4 Multiplicative Approximations

To obtain multiplicative \((1\pm o(1))\)-factor approximations for both ED and LCS, we need to introduce a few additional ideas. Here also the differences between ED and LCS become more important.

### Challenge 1 (LCS): vertical difference could be much larger than weight of the path

For ED, we use the fact that the vertical difference |_p(l_)-_p(r_)| is at most the length of the \(\langle l,p(l)\rangle-\langle r,p(r)\rangle\) path to get a bound on the curvature of _p_ inside the interval (_l,r_]. For LCS, the vertical difference is no longer bounded by the weight of the path so locally the curvature could generally be much higher than the contribution to LCS.

Intuitively, we can simply discard intervals with very high curvature compared to low contribution to the LCS. To bound the total error incurred by discarding such intervals, we introduce a scaled variant of the tree total deviation (Section 4.2). We use it to show that indeed most of the contribution to LCS comes from segments of the path where the ratio between curvature and weight is bounded, so we can safely discard the remaining segments.

### Challenge 2 (ED+LCS): uneven contribution from sub-paths

For a fixed candidate path, if we simply split it into _M_ parts with equal widths, sample a random subset of _M/_2 parts, and let our estimate be twice the answer in the sample, one would hope that the estimate would concentrate around the true sum. However, this concentration may not hold when the sub-paths on different parts have very different weights; e.g., in the extreme case, the sub-path in one of the _M_ parts has a much higher weight than the rest combined, and the estimate would fluctuate greatly based on whether this part is in the sample or not.

Fortunately, if we apply the total tree deviation result on the "weight distribution" of the path, we can also see that on average, the sub-paths should not differ too much in lengths. It turns out that it suffices to obtain an estimate that satisfies the following desiderata:

• The estimate is "(nearly) sound", i.e., it does not underestimate the answer for ED (by less than (1-_o_(1))), and does not overtimate the answer for LCS (by more than (1+_o_(1))).<tbc>

• As long as the sub-paths do not differ too much in lengths, the estimate is also "(nearly) complete" , i.e., it does not overestimate the answer for ED (by more than (1+_o_(1))), and does not underestimate the answer for LCS (by less than (1-_o_(1))).<tbc>

• The estimate also has "back-up" worst-case error guarantee, i.e., even if the sub-paths lengths vary greatly, we incur an additive error of at most _O_(1) times the length of the path.<tbc>

<sup>11</sup>We introduced part of our ideas for ED exclusively, but for additive _o(n_)-approximation, these two problems are equivalent since LCS is (mostly) a complementary version of ED.


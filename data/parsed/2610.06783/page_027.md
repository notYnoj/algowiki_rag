<tbc>large power of _D_. Together with the cost of the encodings (Section 2.4.4), this is why Theorem 5 assumes \(N\ge D^{18}\).

From now on, we fix _L_=19_m_, so that _N_<sub>0</sub>=3<sup>18_m_</sup> and \(K=\genfrac(){pt}{2}{19m}{m}\). Recall that _D_=4_<sup>m</sup>_, so \(2^m=\sqrt{D}\) and 2<sup>-_m/_9</sup>=_D_<sup>-1/18</sup>.

**Lemma 11.** _For every set U of output strings whose inner sets have exactly m elements,_

\(|\text{Leaves}(U)|\le\sum_{d=0}^mmin\{|U|\alpha_d,\beta_d\},\)

_and if L_=19_m, then_ \(|\text{Leaves}(U)|\le 2^{-m/9}\big(2^m|U|+2M\big)\).

_Proof._ We bound the number of leaves of order _d_ in Leaves(_U_) in two ways: by \(|U|\alpha_d\), charging each output string of _U_ for its leaves of order _d_, and by \(\beta_d\), the number of all leaves of order _d_. Since every leaf of Leaves(_U_) has an order \(0\le d\le m\), summing the smaller of the two over _d_ gives the first inequality. (Summed on their own, \(|U|\alpha_d\) gives \(|U|\cdot 10^m\), the cost of computing each output string of _U_ by itself, and \(\beta_d\) gives less than 2_M_ by (5), the cost of computing all _M_ output strings.) Neither \(|U|\alpha_d\) nor \(\beta_d\) depends on which output strings are in _U_.

For the second inequality, let _L_=19_m_. We use \(|U|\alpha_d\) for the orders \(d\le m/9\) and \(\beta_d\) for the orders _d\>m/_9 (Figure 7). The orders _d\>m/_9 contribute at most \(\sum_{d>m/9}\beta_d\le M\sum_{d>m/9}2^{-d}<2\cdot 2^{-m/9}M\) by (5). The orders \(d\le m/9\) contribute at most \(|U|\sum_{d\le m/9}\genfrac(){pt}{2}{m}{d}9^d\), and since \(9^d=72^d8^{-d}\le 72^{m/9}8^{-d}\) for \(d\le m/9\),

\(\sum_{d\le m/9}\genfrac(){pt}{2}{m}{d}9^d\le 72^{m/9}\sum_{d=0}^m\genfrac(){pt}{2}{m}{d}8^{-d}=72^{m/9}\genfrac(){pt}{2}{9}{8}^m=\big(72\cdot\genfrac(){pt}{2}{9}{8}^9\big)^{m/9}<256^{m/9}=2^m\cdot 2^{-m/9},\)

since \(72\cdot(9/8)^9<208\). Adding the two parts gives the second inequality.

\(\includegraphics{}\text{Figure 6: The leaves contributing to one output string, drawn for}L=6\text{,}m=2\text{, and the output string}w=z_{13}z_0z_{21}z_{33}z_0z_{12}\text{of Figure 4. A leaf is written as the string of terms it chose, level by level. A leaf of order}d\text{is the private leaf with}P_0\text{replaced by one of the nine terms}P_{ij}\text{(shown as a generic}P_{ij}\text{in the shaded cells) at exactly}d\text{levels. Leaves of higher order are more numerous per output string, but each is shared by more output strings: a leaf that chose}P_0\text{at}m-d\text{levels contributes to one output string for each set}Q\text{of size}m\text{containing those levels,}\genfrac(){pt}{2}{L-m+d}{d}\text{of them. At}L=19m\text{this makes them fewer in all, by (5).}\)


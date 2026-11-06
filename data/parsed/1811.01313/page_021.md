and _Y_ is small. This is of course requires that the joint distribution of (_Z,Y_) is far from a product distribution. If we use _T_ denote the expected Hamming distance between _Z_ and _Y_ , then it must be the case that \(\mathbb{E}[K]\le T\) since _X_ and _Z_ have the same distribution and _K_ gives the distance to the nearest vector in F (not just to the random vector _Z_).

We now argue that _T_ is small for the right joint distribution on _Z_ and _Y_ . Our choice of joint distribution and our proof is inspired by the \(\sqrt{IC}\) protocol compression algorithm for non-product distributions given in the seminal work of Barak et al. \[4\].

Pick uniform random numbers \(\kappa_1,\dots,\kappa_{nw}\) between 0 and 1. For each _i_, we let the _i_’th bit of _Z_, denoted _Z<sub>i</sub>_ equal 1 if \(\kappa_i\le 1/2\) and 0 otherwise. Thus _Z_ is uniform random in {0,1}_<sup>nw</sup>_. For _Y_ , we choose each bit _Y<sub>i</sub>_ one at a time. Assume we have already chosen values _y_<sub>1</sub>_,...,y_<sub>_i_-1</sub> for the preceeding bits and let _D_ be uniform random in F. We choose _Y<sub>i</sub>_ to be 1 if \(\kappa_i\le\mathrm{Pr}[D_i=1|D_{i-1}=y_{i-1},\dots,D_1=y_1]\) and 0 otherwise. Hence _Y_ is uniform random in F. Thus, if we have already chosen values _y_<sub>1</sub>_,...,y_<sub>_i_-1</sub>, then the probability that _Z<sub>i</sub>_ and _Y<sub>i</sub>_ are distinct is |1/2-Pr\[_Y<sub>i</sub>_=1|_Y_<sub>_i_-1</sub>=_y_<sub>_i_-1</sub>_,...,Y_<sub>1</sub>=_y_<sub>1</sub>\]|. For ease of notation, use _Y<sub>\<i</sub>_ to denote _Y_<sub>_i_-1</sub>_,...,Y_<sub>1</sub> and _y<sub>\<i</sub>_ to denote _y_<sub>_i_-1</sub>_,...,y_<sub>1</sub>, i.e. we have \(\mathrm{Pr}[Z_i\neq Y_i|Y_{<i}=y_{<i}]=|1/2-\mathrm{Pr}[Y_i=1|Y_{<i}=y_{<i}]|\).

Let _U_ denote the uniform distribution on 1 bit and let _P_ denote the distribution of _Y<sub>i</sub>_ conditioned on _Y<sub>\<i</sub>=y<sub>\<i</sub>_. The probability that \(Z_i\neq Y_i\) is thus equal to \(\|U-P\|_1\). Using Pinsker’s inequality, this means that<tbc>

\(D_{KL}(U||P)\ge 2\|U-P\|_1^2=2\left(\mathrm{Pr}[Z_i\neq Y_i|Y_{<i}=y_{<i}]\right)^2.\)

<tbc>But the KL-divergence from the uniform random distribution over a bit simply equals 1-_H(Y<sub>i</sub>|Y<sub>\<i</sub>=y<sub>\<i</sub>_), that is:<tbc>

\(1-H(Y_i|Y_{<i}=y_{<i})\ge 2\left(\mathrm{Pr}[Z_i\neq Y_i|Y_{<i}=y_{<i}]\right)^2\)

<tbc>We can now bound E\[_K_\] as follows:

\(\mathbb{E}[K]=\sum_{i=1}^{nw}\sum_{y_{<i}}\mathrm{Pr}[Y_{<i}=y_{<i}]\cdot\mathrm{Pr}[Z_i\neq Y_i|Y_{<i}=y_{<i}]\)<br>
\(\le\sum_{i=1}^{nw}\sum_{y_{<i}}\mathrm{Pr}[Y_{<i}=y_{<i}]\cdot\sqrt{(1-H(Y_i|Y_{<i}=y_{<i}))/2}\)

Using Cauchy-Schwartz, we further conclude that:

\(\mathbb{E}[K]\le\sum_{i=1}^{nw}\sum_{y_{<i}}\sqrt{\mathrm{Pr}[Y_{<i}=y_{<i}]}\cdot\sqrt{\mathrm{Pr}[Y_{<i}=y_{<i}](1-H(Y_i|Y_{<i}=y_{<i}))/2}\)<br>
\(\le\sqrt{\left(\sum_{i=1}^{nw}\sum_{y_{<i}}\mathrm{Pr}[Y_{<i}=y_{<i}]\right)\cdot\left(\sum_{i=1}^{nw}\sum_{y_{<i}}\mathrm{Pr}[Y_{<i}=y_{<i}](1-H(Y_i|Y_{<i}=y_{<i}))/2\right)}\)<br>
\(=\sqrt{\left(nw\right)\cdot\left(\sum_{i=1}^{nw}\sum_{y_{<i}}\mathrm{Pr}[Y_{<i}=y_{<i}](1-H(Y_i|Y_{<i}=y_{<i}))/2\right)}\)<br>
\(=\sqrt{(nw)\cdot\left((nw-H(Y))/2\right)}\)

But _Y_ was uniform random in F, i.e. \(H(Y)=\mathrm{lg}|\mathcal{F}|\ge nw-r\) so we get:<tbc>

\(\mathbb{E}[K]=O(\sqrt{nwr}).\)


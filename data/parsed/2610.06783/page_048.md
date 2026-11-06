the original _D_ was larger than 4<sup>_m_-1</sup>, the assumption \(N\ge D^{18}\) now reads \(N\ge 4^{18(m-1)}\). Let _L_:=21_m_ and \(t:=\lceil m/9\rceil\). We will apply Theorem 30 with these parameters, and we will verify its condition \(N\ge\sqrt{K}N_0\) below, in the step on the encodings.

_Boxes._ We have \(\rho=9m/(L-m+1)=9m/(20m+1)<9/20\), so \(1/(1-\rho)<2\), and since \(t\ge m/9\), also \(\rho^t\le(9/20)^{m/9}=D^{-\gamma}\), where \(\gamma:=\mathrm{ln}(20/9)/(9\mathrm{ln}4)=0.0640\dots\). Hence the first term of (8) is \(O(m^2N^2/D^\gamma)\).

_Queries._ A query reads \(\sum_{d\le t}\alpha_d\) numbers, and we bound this sum as in the proof of Lemma 11. Since \(9^d=72^d8^{-d}\le 72^t8^{-d}\) for \(d\le t\), and _t\<m/_9+1,

\(\sum_{d=0}^t\genfrac(){pt}{2}{m}{d}9^d\le 72^t\sum_{d=0}^m\genfrac(){pt}{2}{m}{d}8^{-d}=72^t\genfrac(){pt}{2}{9}{8}^m<72\cdot\left(72\cdot\left(\frac{9}{8}\right)^9\right)^{m/9}=72D^q,\)

where \(q:=\mathrm{ln}(72\cdot(9/8)^9)/(9\mathrm{ln}4)=0.4277\dots\). Hence a query takes _O(LD<sup>q</sup>_)=_O(mD<sup>q</sup>_) time.

_Encodings._ It remains to show that the last term of (8) is at most \(N^2/D^\gamma\), and that \(N\ge\sqrt{K}N_0\). Both follow from<tbc>

\(\frac{D^\gamma\cdot 10^L}{\sqrt{K}N_0}\le N,\) (10)

<tbc>the first by rearranging, and the second because \(10^L\ge M=KN_0^2\) and \(D^\gamma\ge 1\). As in Section 2.4.4, we compare _m_-th powers by comparing their bases. We have \(D^\gamma=(20/9)^{m/9}\), 10_<sup>L</sup>_=10<sup>21_m_</sup>, and _N_<sub>0</sub>=3<sup>20_m_</sup>, and the standard bound \(\genfrac(){pt}{2}{n}{k}\ge\frac{1}{n+1}\cdot\frac{n^n}{k^k(n-k)^{n-k}}\) gives \(K=\genfrac(){pt}{2}{21m}{m}\ge\frac{1}{21m+1}\left(21^{21}/20^{20}\right)^m\). Hence the left-hand side of (10) is at most \(\sqrt{21m+1}\cdot\Lambda^m\), where

\(\Lambda:=\frac{10^{21}\cdot(20/9)^{1/9}}{(21^{21}/20^{20})^{1/2}\cdot 3^{20}}=4.198\dots\cdot 10^{10}.\)

We now use the assumption \(N\ge D^{18}\). Its base \(4^{18}=6.871\dots\cdot 10^{10}\) is larger than \(\Lambda\) by a factor of more than 1.63. Since \(N\ge 4^{18(m-1)}\), the inequality (10) therefore holds whenever \(1.63^m\ge 4^{18}\sqrt{21m+1}\), which is the case for all \(m\ge 60\). (For _m\<_60, _D_ is bounded by a constant, and the corollary holds trivially.)

_Conclusion._ For \(m\ge 60\), Theorem 30 thus applies. The preprocessing takes \(O(m^2N^2/D^\gamma)\) time and space, and a query takes _O(mD<sup>q</sup>_) time. Since _m=O_(log_D_) and the exponents \(\gamma-0.063\) and 0.437-_q_ are positive, we have \(m^2=O(D^{\gamma-0.063})\) and _m=O(D_<sup>0.437-_q_</sup>), which gives the bounds _O(N_<sup>2</sup>_/D_<sup>0.063</sup>) and _O(D_<sup>0.437</sup>) of the corollary. The bound for a set _W_ follows by asking |_W_| queries.

## Other choices of the parameters.

The numbers 21 and \(\frac{1}{9}\) did not play a special role in this proof, and the same calculation works with \(L=\lceil cm\rceil\) and \(t=\lceil\theta m\rceil\) for any constants _c\>_10 and \(0<\theta<0.9\). This gives Corollary 31 below, which we use for the left half of  2, with the _c_ of the row and the \(\theta\) that gives the _q_ of the column (\(\theta=\frac{1}{9}\) for _q_=0.43). To state it, let \(\mathrm{H}(x):=-x\mathrm{ln}x-(1-x)\mathrm{ln}(1-x)\) be the entropy function (with natural logarithms), let \(\Lambda:=10^ce^{-\frac{1}{2}c\mathrm{H}(1/c)}3^{-(c-1)}4^\gamma\) be the general form of the base \(\Lambda\) above, and let<tbc>

\(R_c(\gamma):=\frac{\mathrm{ln}4}{\mathrm{ln}\Lambda}=\frac{\mathrm{ln}4}{c\mathrm{ln}10-\frac{1}{2}c\mathrm{H}(1/c)-(c-1)\mathrm{ln}3+\gamma\mathrm{ln}4}.\) (11)


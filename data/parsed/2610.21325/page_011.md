<tbc>nates **z**(**x**):=**V**(**x**-**c**) of each database vector as an integer code \(\mathbf{w}_\mathbf{x}\in\{-127,\dots,127\}^m\) with one scale \(s_\mathbf{x}:=\|\mathbf{z}(\mathbf{x})\|_\infty/127\) per vector, so that **z**(**x**)=_s_**<sub>x</sub>**(**w**<sub>x</sub>+**d**<sub>x</sub>) with \(\|\mathbf{d}_\mathbf{x}\|_\infty\le 1/2\). The residual coordinate \(\rho(\mathbf{x})\) stays in fp32, because it is often the largest coordinate and would otherwise coarsen the scale of all others. A query is encoded in the same way. Splitting \(\langle\mathbf{z}(\mathbf{q}),\mathbf{z}(\mathbf{x})\rangle\) into the product of the codes and the rounding terms and applying the Cauchy- Schwarz inequality to the rounding terms, as in Eq. (10), gives<tbc>

\(\langle\mathbf{z}(\mathbf{q}),\mathbf{z}(\mathbf{x})\rangle\le s_\mathbf{q}s_\mathbf{x}\beta(\mathbf{q},\mathbf{x}),\text{where}\beta(\mathbf{q},\mathbf{x}):=\langle\mathbf{w}_\mathbf{q},\mathbf{w}_\mathbf{x}\rangle+\|\mathbf{d}_\mathbf{q}\|\|\mathbf{w}_\mathbf{x}\|+\|\mathbf{d}_\mathbf{x}\|(\|\mathbf{w}_\mathbf{q}\|+\|\mathbf{d}_\mathbf{q}\|).\text{(18)}\)

<tbc>Since \(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle=\langle\mathbf{z}(\mathbf{q}),\mathbf{z}(\mathbf{x})\rangle+\rho(\mathbf{q})\rho(\mathbf{x})\), Eq. (8) and Eq. (18) bound \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2\) from below by \(B(\mathbf{q},\mathbf{x}):=a(\mathbf{q})+a(\mathbf{x})-2(s_\mathbf{q}s_\mathbf{x}\beta(\mathbf{q},\mathbf{x})+\rho(\mathbf{q})\rho(\mathbf{x}))\). The integer retina evaluates _B_ in fp32 and keeps **x** if and only if the computed value \(\widehat{B}(\mathbf{q},\mathbf{x})\) satisfies

\(\widehat{B}(\mathbf{q},\mathbf{x})\le U^2(1+10^{-4})+\omega(\mathbf{q}),\text{where}\omega(\mathbf{q}):=64u\big(\sqrt{a(\mathbf{q})}+\sqrt{M_a}\big)^2,\text{(19)}\)

where _u_=2<sup>-24</sup> and _M<sub>a</sub>_ denotes the database maximum of _a_(**x**).

**Proposition 6** (No false dismissal with integer codes)**.** _Assume_ 127<sup>2</sup>_m\<_2<sup>24</sup>_. If_ \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le U\)_, the integer retina keeps_ **x**.

_Proof._ We bound the exact value, then the product of the codes, and finally the rounding of the remaining arithmetic in three steps.

Step 1 bounds the exact value. By Eq. (18) and the premise, \(B(\mathbf{q},\mathbf{x})\le\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2\le U^2\).

Step 2 concerns the product of the codes. The integer tensor cores return \(\langle\mathbf{w}_\mathbf{q},\mathbf{w}_\mathbf{x}\rangle\) exactly. Because the magnitude of this product is at most 127<sup>2</sup>_m\<_2<sup>24</sup>, the conversion of the product to fp32 is exact as well.

Step 3 bounds the rounding of the remaining arithmetic. The other scalars are stored in fp32 and combined by fp32 multiplications and additions, so that each of the four summands _a_(**q**), _a_(**x**), \(2s_\mathbf{q}s_\mathbf{x}\beta\), and \(2\rho(\mathbf{q})\rho(\mathbf{x})\) of _B_ passes through at most 16 roundings. Hence \(|\widehat{B}-B|\le\gamma_{16}S\), where \(\gamma_{16}:=16u/(1-16u)\) and _S_ is the sum of the magnitudes of the four summands. Since \(s_\mathbf{q}\|\mathbf{w}_\mathbf{q}\|\le\|\mathbf{z}(\mathbf{q})\|+s_\mathbf{q}\|\mathbf{d}_\mathbf{q}\|\) and \(\|\mathbf{d}_\mathbf{q}\|\le\sqrt{m}/2\), the scale satisfies \(s_\mathbf{q}(\|\mathbf{w}_\mathbf{q}\|+\|\mathbf{d}_\mathbf{q}\|)\le(1+\sqrt{m}/127)\|\mathbf{z}(\mathbf{q})\|\), and likewise for **x**. Because \(|\beta|\le(\|\mathbf{w}_\mathbf{q}\|+\|\mathbf{d}_\mathbf{q}\|)(\|\mathbf{w}_\mathbf{x}\|+\|\mathbf{d}_\mathbf{x}\|)\), the third summand is therefore at most \(2(1+\sqrt{m}/127)^2\sqrt{a(\mathbf{q})a(\mathbf{x})}\), where the factor \((1+\sqrt{m}/127)^2\) stays below 1.6 under the assumption. The fourth summand is at most \(2\sqrt{a(\mathbf{q})a(\mathbf{x})}\), so that \(S\le a(\mathbf{q})+a(\mathbf{x})+5.2\sqrt{a(\mathbf{q})a(\mathbf{x})}\le 2.6\big(\sqrt{a(\mathbf{q})}+\)<tbc>

\(\sqrt{a(\mathbf{x})}\big)^2\)

<tbc>. Consequently, \(|\widehat{B}-B|\le 42u\big(\sqrt{a(\mathbf{q})}+\sqrt{a(\mathbf{x})}\big)^2\le\omega(\mathbf{q})\). Combined with Step 1, this bound gives \(\widehat{B}\le U^2+\omega(\mathbf{q})\), so that the test of Eq. (19) keeps **x**.

The integer retina runs as one Triton \[64\] kernel, which multiplies the codes on the integer tensor cores and evaluates Eq. (19) on the accumulated products. Each database vector occupies its _m_ codes, padded as the half-precision retina vectors, and five fp32 scalars, namely _a_(**x**), _s_**<sub>x</sub>**, \(\|\mathbf{d}_\mathbf{x}\|\), \(\|\mathbf{w}_\mathbf{x}\|\), and \(\rho(\mathbf{x})\). At the same width, the integer retina therefore needs about half of the 2(_m_+5) bytes of the half- precision retina. As in the half-precision pass, the threshold _U_ comes from the exact distances of the anchors, and the fovea verifies every survivor in fp64.

Figure 8 compares the two retinas on BIGANN-10M and DINOv2 with an anchor stride of 16 and 16 anchors, which is the configuration of the fastest DINOv2 run. Every query of every run is exact. In addition, the validation of one million pairs per run at their own lower bound finds no violation. At the same width, the integer retina halves the device memory at the cost of more survivors, which rise from 327 to 452 per query on DINOv2 at _m_=635 and from 178 to 641 on BIGANN-10M at _m_=123. At the same memory, the integer retina keeps far fewer survivors. On BIGANN- 10M, for example, 148 bytes per vector at _m_=123 keep 641 survivors per query, whereas the half-precision retina keeps 2,507 at _m_=59 with 132 bytes. On DINOv2, the half-precision retina with 644 bytes per vector at _m_=315 overflows the survivor list, whereas the integer retina with 660 bytes per vector at _m_=635 is exact at 53.5k queries per second, which is \(2.7\times\) the throughput of the fastest cuVS search.

The integer retina is still slower than the half-precision retina at the same width, with 53.5k against 152k queries per second on DINOv2 at _m_=635. Its kernel is neither persistent nor tuned, whereas the integer tensor cores of the H100 offer twice the fp16 rate per coordinate. The integer retina therefore suits datasets that would otherwise exceed device memory, since it stores about twice as many vectors<tbc>

(a) BIGANN-10M
(b) DINOv2
fp16
104
Xoverflow
int8
105
83k
17k
labels: exact QPS
104
103
24k
94k
25k
103
103k
53k
152k
141k
102
102
100
200
400
500
1000
2000
Bytes per vector
Bytes per vector

Figure 8: Survivors of the fp16 and int8 retinas.


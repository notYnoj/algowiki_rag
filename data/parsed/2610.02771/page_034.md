We next establish the variance and range bounds needed for Bernstein’s inequality. Conditional on _W<sub>k</sub>=w_,<tbc>

\(\mathbb{E}[Z_{k,s}^2|W_k=w]=2A_s\int_{I_s}max\{\sigma,t\}\mathbf{1}\{|w|\ge t\}dt.\)

<tbc>Hence, writing _v<sub>k,s</sub>_:=Var(_Z<sub>k,s</sub>_), we have<tbc>

\(\sum_{s=0}^j\frac{v_{k,s}}{A_s}\le\sum_{s=0}^j\frac{\mathbb{E}[Z_{k,s}^2]}{A_s}\le 2\mathbb{E}\left[\int_0^{L_j}max\{\sigma,t\}\mathbf{1}\{|W_k|\ge t\}dt\right].\)

<tbc>For any \(x\ge 0\),<tbc>

\(\int_0^{L_j}max\{\sigma,t\}\mathbf{1}\{x\ge t\}dt\le\int_0^xmax\{\sigma,t\}dt\le\sigma x+\frac{x^2}{2}.\)

<tbc>Since \(\mathbb{E}[W_k^2]\le 2\sigma^2\), this gives

\(\sum_{s=0}^j\frac{v_{k,s}}{A_s}\le C\sigma^2\)

for a universal constant _C\>_0.

Also,<tbc>

\(|Z_{k,s}|\le\frac{2}{q_s(T)}=2A_smax\{\sigma,T\}\le 2A_sL_s.\)

<tbc>Because \(A_s\ge log2\) for every _s_, the centered variables satisfy

\(|Z_{k,s}-\mathbb{E}Z_{k,s}|\le CA_sL_s\)

for another universal constant _C\>_0.

Now fix a phase _j_. Suppose each slab \(s\le j\) has been topped up to _m<sub>s,j</sub>_ samples. Define

\(\overline{Z_{k,s}}=\frac{1}{m_{s,j}}\sum_{i=1}^{m_{s,j}}Z_{k,s,i}.\)

The centered error of the reusable clipped estimator is

\(\sum_{s=0}^j\left(\overline{Z_{k,s}}-\mathbb{E}Z_{k,s}\right).\)

Its Bernstein variance proxy is<tbc>

\(V_{k,j}:=\sum_{s=0}^j\frac{v_{k,s}}{m_{s,j}},\)

<tbc>and its maximum summand range is<tbc>

\(B_{k,j}:=max_{s\le j}\frac{CA_sL_s}{m_{s,j}}.\)

<tbc>By the choice of _m<sub>s,j</sub>_,<tbc>

\(V_{k,j}\le\frac{\rho_j^2}{C_0\sigma^2\Gamma_j}\sum_{s=0}^j\frac{v_{k,s}}{A_s}\le\frac{C\rho_j^2}{C_0\Gamma_j},\)

<tbc>and

\(B_{k,j}\le max_{s\le j}\frac{CA_sL_s}{C_0A_s\sigma^2\Gamma_j/\rho_j^2}\le\frac{CL_j\rho_j^2}{C_0\sigma^2\Gamma_j}=\frac{32C\rho_j}{C_0\Gamma_j},\)

where the last equality uses \(L_j=32\sigma^2/\rho_j\).

Bernstein’s inequality therefore gives, for a universal constant _c\>_0,

\(Pr\left(\left|\sum_{s=0}^j\left(\overline{Z_{k,s}}-\mathbb{E}Z_{k,s}\right)\right|>2\sqrt{V_{k,j}\Gamma_j}+B_{k,j}\Gamma_j\right)\le e^{-c\Gamma_j}.\)


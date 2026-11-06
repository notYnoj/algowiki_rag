For every fixed \(A\ge 1\) and every \(s\le TL_\delta+AR+2\), there exists a constant _C_<sub>1</sub>=_C_<sub>1</sub>(_T,K_) such that<tbc>

\(\widetilde{H}_s(\eta)\le C_1(1+logA)M.\)

<tbc>Indeed, \(R\le L_\delta+M+1\), and therefore \(log(es)\le C_T+logA+log(L_\delta+M+2)\). Since \(log(L_\delta+M+2)\le C_K+log(1+L_\delta)+log(1+M)\) and \(M=log(K/\eta)+log(1+L_\delta)\), the displayed bound follows after using \(M\ge m_0\). Consequently, for the value _A=A_<sub>inv</sub> and the associated _s_,

\(\widetilde{H}_s(\eta)\le C_1(1+logA_\mathrm{inv})M.\) (F.1)

Moreover, because \(s\ge A_\mathrm{inv}M\),

\(\frac{\widetilde{H}_s(\eta)}{s}\le\frac{C_1(1+logA_\mathrm{inv})}{A_\mathrm{inv}}.\) (F.2)

Define<tbc>

\(F(L):=\frac{L+s}{T}-a\sqrt{(\overline{c}L+s)\widetilde{H}_{\overline{c}L+s}(\eta)}-b\widetilde{H}_{\overline{c}L+s}(\eta)-d-c(\overline{c}L+s,\delta).\)

<tbc>For \(t\ge 1\),<tbc>

\(\frac{d}{dt}\widetilde{H}_t(\eta)=\frac{1}{t},\)

<tbc>and<tbc>

\(\frac{d}{dt}\sqrt{t\widetilde{H}_t(\eta)}=\frac{\widetilde{H}_t(\eta)+1}{2\sqrt{t\widetilde{H}_t(\eta)}}\le\sqrt{\frac{\widetilde{H}_t(\eta)}{t}},\)

<tbc>because \(\widetilde{H}_t(\eta)\ge 1\). Also<tbc>

\(\frac{d}{dt}c(t,\delta)=\frac{1}{1+t/2}\le\frac{2}{t}.\)

<tbc>Hence<tbc>

\(F'(L)\ge\frac{1}{T}-a\overline{c}\sqrt{\frac{\widetilde{H}_{\overline{c}L+s}(\eta)}{\overline{c}L+s}}-(b+2)\frac{\overline{c}}{\overline{c}L+s}.\)

<tbc>The map \(t\mapsto\widetilde{H}_t(\eta)/t\) is decreasing for \(t\ge 1\) because \(\widetilde{H}_t(\eta)\ge 1\). Using (F.2), we can choose _A_<sub>inv</sub> large enough that

\(a\overline{c}\sqrt{\frac{\widetilde{H}_s(\eta)}{s}}+(b+2)\frac{\overline{c}}{s}\le\frac{1}{2T}\)

uniformly in \(\delta\) and \(\eta\). For such a choice, \(F'(L)\ge 1/(2T)>0\) for all \(L\ge 0\).

It remains to make _F_(0)_\>_0. Since<tbc>

\(c(s,\delta)\le L_\delta+2\widetilde{H}_s(\eta)+C_2(K),\)

<tbc>one has<tbc>

\(F(0)\ge\frac{s}{T}-L_\delta-a\sqrt{s\widetilde{H}_s(\eta)}-(b+2)\widetilde{H}_s(\eta)-d-C_2(K).\)

<tbc>The definition of _s_ gives<tbc>

\(\frac{s}{T}-L_\delta\ge\frac{A_\mathrm{inv}}{T}R.\)

<tbc>Using (F.1) and \(s\le TL_\delta+A_\mathrm{inv}R+2\), we get<tbc>

\(s\widetilde{H}_s(\eta)\le C_3(1+logA_\mathrm{inv})M\left(TL_\delta+A_\mathrm{inv}R+2\right).\)

<tbc>Since \(L_\delta M\le R^2\), \(RM\le R^2\), and \(M\le R^2\), this implies<tbc>

\(\sqrt{s\widetilde{H}_s(\eta)}\le C_4\sqrt{A_\mathrm{inv}(1+logA_\mathrm{inv})}R.\)

<tbc>Also, (F.1) gives \(\widetilde{H}_s(\eta)\le C_5(1+logA_\mathrm{inv})R\). Therefore<tbc>

\(F(0)\ge\left[\frac{A_\mathrm{inv}}{T}-aC_4\sqrt{A_\mathrm{inv}(1+logA_\mathrm{inv})}-(b+2)C_5(1+logA_\mathrm{inv})-d-C_2(K)}\right]R.\)


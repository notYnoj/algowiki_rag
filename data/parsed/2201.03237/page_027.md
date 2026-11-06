point set \(\{Q:Q\in R_d\cap\delta(B,Q)<r\}\) as and the corresponding region as _Reg_<sub>3</sub>. We set up a cartesian coordinate system _x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>d</sub>_ in _d_ dimensional space with point _B_ as origin and specify that the positive direction of axis _x_<sub>1</sub> is same as \(\overrightarrow{AC}\). The probability to achieve monotonic search is the ratio of the volume of _Reg_<sub>1</sub> to _Reg_<sub>3</sub>, which can be represented as<tbc>

\(Prob=\frac{Volume(Reg_1)}{Volume(Reg_3)}\)

<tbc>Because \(PS_2\in PS_1\), there is<tbc>

\(Prob=\frac{Volume(Reg_1)}{Volume(Reg_3)}\)<br>
\(>\frac{Volume(Reg_2)}{Volume(Reg_3)}\)<br>
\(=\frac{\int_0^{\pi-\frac{\varphi}{2}}sin^{d-2}\theta_1d\theta_1\int_0^\pi sin^{d-3}\theta_2d\theta_2\dots\int_0^{2\pi} d\theta_{d-1}\int_0^rR^{d-1}dR}{\int_0^\pi sin^{d-2}\theta_1d\theta_1\int_0^\pi sin^{d-3}\theta_2d\theta_2\dots\int_0^{2\pi} d\theta_{d-1}\int_0^rR^{d-1}dR}\)<br>
\(=\frac{\int_0^{\pi-\frac{\varphi}{2}}sin^{d-2}\theta_1d\theta_1}{\int_0^\pi sin^{d-2}\theta_1d\theta_1}\)

<tbc>with<tbc>

\(\left\{\begin{array}{ c }
x_1=Rcos\theta_1, \\
x_2=Rsin\theta_1cos\theta_2, \\
\dots \\
x_{d-1}=Rsin\theta_1\dots sin\theta_{d-2}cos\theta_{d-1}, \\
x_d=Rsin\theta_1\dots sin\theta_{d-2}sin\theta_{d-1}
\end{array}\right.\)<br>
\(\left.\int_0^{\pi-\frac{\varphi}{2}}sin^{d-2}\theta_1d\theta_1=-\frac{cos\theta_1sin^{d-3}\theta_1}{d-2}\right|_0^{\pi-\frac{\varphi}{2}}\)<br>
\(+\frac{d-3}{d-2}\int_0^{\pi-\frac{\varphi}{2}}sin^{d-4}\theta_1d\theta_1\)

<tbc>because \(\pi-\frac{\varphi}{2}\in[\frac{\pi}{2},\pi]\), there is<tbc>

\(\int_0^{\pi-\frac{\varphi}{2}}sin^{d-2}\theta_1d\theta_1\ge\frac{d-3}{d-2}\int_0^{\pi-\frac{\varphi}{2}}sin^{d-4}\theta_1d\theta_1\)<br>
\(\int_0^\pi sin^{d-2}\theta_1d\theta_1=\frac{d-3}{d-2}\int_0^\pi sin^{d-4}\theta_1d\theta_1\)


We relabel the variables in _T_<sub>hole</sub> according to the permutations \(\pi_X,\pi_Y,\pi_Z\), obtaining another broken copy of _T_ with sets of holes \(\pi_X\big(P_X^{(0)}\big)\), \(\pi_Y\big(P_Y^{(0)}\big)\), \(\pi_Z\big(P_Z^{(0)}\big)\). We then zero out all parts outside _P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_. The obtained tensor, denoted by \(T'_\mathrm{hole}\), is a subtensor of the target tensor \(T\|_{P_X,P_Y,P_Z}\):

\(T'_\mathrm{hole}=T\|_{P_X\backslash P_X^{(0)^\prime},P_Y\backslash P_Y^{(0)^\prime},P_Z\backslash P_Z^{(0)^\prime}}:=T\|_{P_X^{(1)^\prime},P_Y^{(1)^\prime},P_Z^{(1)^\prime}},\)

where \(P_X^{(0)^\prime}:=P_X\cap\pi_X\big(P_X^{(0)}\big)\) is the set of holes in _X_-parts, and \(P_X^{(1)^\prime}:=P_X\backslash P_X^{(0)^\prime}\); similar for _Y_ - and _Z_-dimension.

Next, we write _T_∥_<sub>P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_</sub> as a sum of 8 subtensors:<tbc>

\(T\|_{P_X,P_Y,P_Z}=T\|_{P_X^{(1)^\prime},P_Y^{(1)^\prime},P_Z^{(1)^\prime}}+\sum_{a,b,c\in\{0,1\}0\in\{a,b,c\}}T\|_{P_X^{(a)^\prime},P_Y^{(b)^\prime},P_Z^{(c)^\prime}}.\)

<tbc>Notice that the first term \(T\|_{P_X^{(1)^\prime},P_Y^{(1)^\prime},P_Z^{(1)^\prime}}\) equals \(T'_\mathrm{hole}\) (which we already obtained by consuming one broken copy _T_<sub>hole</sub>), and the other seven subtensors are significantly smaller than _T_∥_<sub>P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_</sub>, so we can obtain them recursively. The fact that \(\big|P_X^{(1)^\prime}\big|\le|P_X|=h_X\), \(\big|P_Y^{(1)^\prime}\big|\le|P_Y|=h_Y\), \(\big|P_Z^{(1)^\prime}\big|\le|P_Z|=h_Z\) together with Eq. (26) gives us the following recursion:

\(f(h_X,h_Y,h_Z)\le 1+f\big(\frac{h_X}{\mathrm{log}M_X},h_Y,h_Z\big)+f\big(h_X,\frac{h_Y}{\mathrm{log}M_Y},h_Z\big)+f\big(h_X,h_Y,\frac{h_Z}{\mathrm{log}M_Z}\big)\)<br>
\(+f\big(\frac{h_X}{\mathrm{log}M_X},\frac{h_Y}{\mathrm{log}M_Y},h_Z\big)+f\big(\frac{h_X}{\mathrm{log}M_X},h_Y,\frac{h_Z}{\mathrm{log}M_Z}\big)\)<br>
\(+f\big(h_X,\frac{h_Y}{\mathrm{log}M_Y},\frac{h_Z}{\mathrm{log}M_Z}\big)+f\big(\frac{h_X}{\mathrm{log}M_X},\frac{h_Y}{\mathrm{log}M_Y},\frac{h_Z}{\mathrm{log}M_Z}\big).\)

Since |P_<sub>X</sub>_|=_M<sub>X</sub>_, |P_<sub>Y</sub>_|=_M<sub>Y</sub>_, |P_<sub>Z</sub>_|=_M<sub>Z</sub>_, we can solve the recursion for _f(M<sub>X</sub>,M<sub>Y</sub>,M<sub>Z</sub>_) and get

\(f(M_X,M_Y,M_Z)\le 7^{1+}\big[\mathrm{log}_{\mathrm{log}M_X}M_X\big]+\big[\mathrm{log}_{\mathrm{log}M_Y}M_Y\big]+\big[\mathrm{log}_{\mathrm{log}M_Z}M_Z\big]\)<br>
\(\le C_0\cdot M^\frac{3}{\mathrm{loglog}M}\)

where _C_<sub>0</sub> is a sufficiently large constant and _M_=max{_M<sub>X</sub>,M<sub>Y</sub>,M<sub>Z</sub>_} since the function _M_<sup>1/loglog_M_</sup> is monotonic increasing for sufficiently large _M_.

We remark that Theorem 7.2 also works for non-partitioned tensors satisfying Property 7.1 when considering on _X_-, _Y_ -, _Z_-variables as partitioned into size-1 parts where each part consists of a single variable.

Now let us return our attention to the context of fast matrix multiplication and show that we can fix the holes in the interface tensors with holes obtained in our algorithm.

**Corollary 4.2** (Restated)**.** _Let T be a level-_\(\ell\) _interface tensor with parameter list_

\(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s]}.\)

_Let_ \(N=2^{\ell-1}\cdot\sum_{t\in[s]}n_t\)_. Suppose T_<sub>1</sub>_,...,T<sub>r</sub> are broken copies of T where_ \(\le\frac{1}{8N}\) _fraction of level-1 X-, Y- and Z-blocks are holes. If_ \(r\ge 2^{C_1N/\mathrm{log}N}\) _for some large enough constant C_<sub>1</sub>_\>_0_, the direct sum_ \(\oplus_{i=1}^rT_i\) _can degenerate into an unbroken copy of T._


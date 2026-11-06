## Constraint Type 1.

The outflow from the source _s_ must be 1. Assume _f_<sub>_m_<sub>1</sub></sub>_,...,f<sub>m<sub>d</sub></sub>_ are the weights associated with the outgoing multiedges _m_<sub>1</sub>_,...,m<sub>d</sub>_ from the source _s_. Then:

\(L(\mathbf{f},\lambda):=\sum_{m\in M}f_mlog\left(\frac{f_m}{\widehat{f}_m}\right)+\widehat{f}_m-f_m-\lambda\left(\sum_{j=1}^df_{m_j}-1\right)\)<br>
\(\frac{\partial L}{\partial f_m}=log\frac{f_m}{\widehat{f}_m}=0\longrightarrow f_m=\widehat{f}_m\forall m\in M-\{m_1,\dots,m_d\}\)<br>
\(\frac{\partial L}{\partial f_{m_j}}=log\frac{f_{m_j}}{\widehat{f}_{m_j}}-\lambda=0\longrightarrow f_{m_j}=\widehat{f}_{m_j}exp(\lambda)\) (5)

\(\frac{\partial L}{\partial\lambda}=\sum_{j=1}^df_{m_j}-1=0.\) (6)

Combining equations (5) and (6) results in normalizing _f_<sub>_m_<sub>1</sub></sub>_,...,f<sub>m<sub>d</sub></sub>_, that is:

\(\forall j\in\{1..d\}f_{m_j}=\frac{\widehat{f}_{m_j}}{\sum_{j^\prime=1}^d\widehat{f}_{m_{j^\prime}}}.\)

## Constraint Type 2.

Given any internal node \(v\in V-\mathcal{T}-\{s\}\), the outflow from _v_ must be equal to the inflow of _v_. Assume \(f_1^{(\mathrm{in})},\dots,f_a^{(\mathrm{in})}\) and \(f_1^{(\mathrm{out})},\dots,f_b^{(\mathrm{out})}\) are the weights associated with the incoming and outgoing multiedges from/to the node _v_, respectively. Then:

\(L(\mathbf{w},\lambda):=\sum_{m\in M}flog\left(\frac{f_m}{\widehat{f}_m}\right)+\widehat{f}_m-f_m-\lambda\left(\sum_{b^\prime=1}^bf_{b^\prime}^{(\mathrm{out})}-\sum_{a^\prime=1}^af_{a^\prime}^{(\mathrm{in})}\right)\)<br>
\(\frac{\partial L}{\partial f_m}=log\frac{f_m}{\widehat{f}_m}=0\longrightarrow f_m=\widehat{f}_m\forall m\text{non-adjacent to}v\)<br>
\(\frac{\partial L}{\partial f_{b^\prime}^{(\mathrm{out})}}=log\frac{f_{b^\prime}^{(\mathrm{out})}}{\widehat{f}_{b^\prime}^{(\mathrm{out})}}-\lambda=0\longrightarrow f_{b^\prime}^{(\mathrm{out})}=\widehat{f}_{b^\prime}^{(\mathrm{out})}exp(\lambda)\forall b'\in\{1..b\}\) (7)

\(\frac{\partial L}{\partial f_{a^\prime}^{(\mathrm{in})}}=log\frac{f_{a^\prime}^{(\mathrm{in})}}{\widehat{f}_{a^\prime}^{(\mathrm{in})}}+\lambda=0\longrightarrow f_{a^\prime}^{(\mathrm{in})}=\widehat{f}_{a^\prime}^{(\mathrm{in})}exp(-\lambda)\forall a'\in\{1..a\}\) (8)

\(\frac{\partial L}{\partial\lambda}=\sum_{b^\prime=1}^bf_{b^\prime}^{(\mathrm{out})}-\sum_{a^\prime=1}^af_{a^\prime}^{(\mathrm{in})}=0.\) (9)

Letting \(\beta=exp(\lambda)\), for all \(a'\in\{1..a\}\) and all \(b'\in\{1..b\}\), we can obtain the following by combining equations (7), (8) and (9):

\(\beta\left(\sum_{b^\prime=1}^b\widehat{f}_{b^\prime}^{(\mathrm{out})}\right)=\frac{1}{\beta}\left(\sum_{a^\prime=1}^a\widehat{f}_{a^\prime}^{(\mathrm{in})}\right)\longrightarrow\beta=\sqrt{\frac{\sum_{a^\prime=1}^a\widehat{f}_{a^\prime}^{(\mathrm{in})}}{\sum_{b^\prime=1}^b\widehat{f}_{b^\prime}^{(\mathrm{out})}}}\)<br>
\(\forall b'\in\{1..b\},f_{b^\prime}^{(\mathrm{out})}=\widehat{f}_{b^\prime}^{(\mathrm{out})}\sqrt{\frac{\sum_{a^{\prime\prime}=1}^a\widehat{f}_{a^{\prime\prime}}^{(\mathrm{in})}}{\sum_{b^{\prime\prime}=1}^b\widehat{f}_{b^{\prime\prime}}^{(\mathrm{out})}}},\)


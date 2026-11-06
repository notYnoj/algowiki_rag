_Then, there exists an_ {_s}-regular_ \(\langle l,p_s(l)\rangle\)-\(\langle r,p_s(r)\rangle\) _path p_<sub>_s_-1</sub> _such that_

\(p_s(x-1,x]=p_{s-1}(x-1,x]\)

_holds for every x that is not a hitter of_ (_l,r_].

_Proof._ Fix \(1\le i<M\). In this proof, we show that \(|p_s(m_i-I_{s-3})-\overline{y_i}|\le I_{s-3}\) and \(|p_s(m_i+I_{s-3})-\overline{y_i}|\le I_{s-3}\), which implies that there is a \(\langle m_i-I_{s-3},p_s(m_i-I_{s-3})\rangle\)-\(\langle m_i,\overline{y_i}\rangle\)-\(\langle m_i+I_{s-3},p_s(m_i+I_{s-3})\rangle\) path. Thus to regularize _p<sub>s</sub>(m<sub>i</sub>_) to <o>_y_</o><sub>i</sub>, we only need to change the sub-path of _p<sub>s</sub>_ between column (_m<sub>i</sub>-I_<sub>_s_-3</sub>) and column (_m<sub>i</sub>+I_<sub>_s_-3</sub>), which only affects edges before hitters.

We show that \(|p_s(m_i-I_{s-3})-\overline{y_i}|\le I_{s-3}\). The other direction is similar due to symmetry. Without loss of generality, suppose that \(p_s(r)\ge p_s(l)\). We will show that:<tbc>

\(p_s(m_i)\text{\textbf{is not far from}}\overline{y_i}\text{\textbf{:}}|p_s(m_i)-\overline{y_i}|=o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right);\)

<tbc>_p<sub>s</sub>(m<sub>i</sub>-I_<sub>_s_-3</sub>) **is not far from** _p<sub>s</sub>(m<sub>i</sub>_)**:** \(|p_s(m_i-I_{s-3})-p_s(m_i)|\le\frac{(p_s(r)-p_s(l))}{M^3}+o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\). We can see that these will imply<tbc>

\(|p_s(m_i-I_{s-3})-\overline{y_i}|\le\frac{(p_s(r)-p_s(l))}{M^3}+o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right)\le\frac{r-l}{M^3}=I_{s-3}.\)

<tbc>**Preliminary:** _p<sub>s</sub>(m<sub>i</sub>_) **is not far from the** \(\langle l,p_s(l)\rangle-\langle r,p_s(r)\rangle\) **line** Recall that for every \(0\le i'\le M^3\), the \(i'\)-th _M_<sup>3</sup>-way anchor is \(m_{i^\prime}^{^\prime}=l+i'\cdot\frac{r-l}{M^3}\). Recall that \(\overline{y_i}=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{p_s(l)+i\cdot p_s(r)-p_s(l)}{I_{s-1}/\phi_y}\right\rfloor\) is the straight-line rounded to the closest multiple of \(I_{s-1}/\phi_y\). As a preliminary, we first show that for every _M_<sup>3</sup>-way anchor \(m_{i^\prime}^{^\prime}\), \(\left\langle m_{i^\prime}^{^\prime},p_s(m_{i^\prime}^{^\prime})\right\rangle\) is not far from the un-rounded straight line connecting \(\langle l,p_s(l)\rangle\) and \(\langle r,p_s(r)\rangle\):

\(\left|p_s(m_{i^\prime}^{^\prime})-\left(p_s(l)+i'\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|=o\left(\frac{(r-l)-(p_s(r)-p_s(l))}{M^3}\right).\) (25)

By telescoping, we have<tbc>

\(\left|p_s(m_{i^\prime}^{^\prime})-\left(p_s(l)+i'\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|=\left|\left(p_s(l)+\sum_{j^\prime\le i^\prime}\left(p_s(m_{j^\prime}^{^\prime})-p_s(m_{j^\prime-1}^{^\prime})\right)\right)-\left(p_s(l)+i'\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|.\)

<tbc>The two _p<sub>s</sub>(l_) terms cancel out. Thus

\(\left|p_s(m_{i^\prime}^{^\prime})-\left(p_s(l)+i'\cdot\frac{p_s(r)-p_s(l)}{M^3}\right)\right|=\left|\left(\sum_{1\le j^\prime\le i^\prime}\left(p_s(m_{j^\prime}^{^\prime})-p_s(m_{j^\prime-1}^{^\prime})\right)\right)-i'\cdot\frac{p_s(r)-p_s(l)}{M^3}\right|\)<br>
\(=\left|\sum_{1\le j^\prime\le i^\prime}\left(p_s(m_{j^\prime}^{^\prime})-p_s(m_{j^\prime-1}^{^\prime})-\frac{p_s(r)-p_s(l)}{M^3}\right)\right|\)<br>
\(\le\sum_{1\le j^\prime\le i^\prime}\left|p_s(m_{j^\prime}^{^\prime})-p_s(m_{j^\prime-1}^{^\prime})-\frac{p_s(r)-p_s(l)}{M^3}\right|\)<br>
\(\le\sum_{1\le j^\prime\le M^3}\left|p_s(m_{j^\prime}^{^\prime})-p_s(m_{j^\prime-1}^{^\prime})-\frac{p_s(r)-p_s(l)}{M^3}\right|\)<br>
\(=\mathrm{TD}_{M^3}(\Delta p_s(l,r]).\text{by definition}\)


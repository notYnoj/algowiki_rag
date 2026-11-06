_Proof of Proposition 3.1._ For convenience, we define the function<tbc>

\(s(t)=np(t)^3.\)

<tbc>Let the stopping time \(\tau\) be the smallest time \(t\le T\) at which there exists some \(\ell\in\mathcal{L}\) that is unoccupied and \(|S_\ell(t)-s(t)|>\varepsilon(t)\). Set \(\tau=T+1\) if there is no such time. It suffices to show that \(\tau=T+1\) with sufficiently high probability.

Note that for \(t<\tau\), there are _n-t=np(t_) unoccupied rows. In each, there are \(s(t)\pm\varepsilon(t)=np(t)^3\pm\varepsilon(t)\) available positions (where we have used the fact that \(\tau>t\)). Thus,<tbc>

(1) \(|\mathcal{A}(t)|=np(t)\big(np(t)^3\pm\varepsilon(t)\big)=n^2p(t)^4\pm np(t)\varepsilon(t).\)

<tbc>For every \(\ell\in\mathcal{L}\), we also define the time \(\tau_\ell\) as the minimum between \(\tau\) and the last time at which line \(\ell\) is unoccupied. For every \(\ell\in\mathcal{L}\), we define the shifted random variables<tbc>

\(S_\ell^+(t)=\left\{\begin{array}{ c c }
S_\ell(t)-s(t)-\frac{1}{2}\varepsilon(t) & \tau_\ell\ge t \\
S_\ell^+(t-1) & \text{otherwise}
\end{array}\right.\)

<tbc>and

\(S_\ell^-(t)=\left\{\begin{array}{ c c }
s(t)-S_\ell(t)-\frac{1}{2}\varepsilon(t) & \tau_\ell\ge t \\
S_\ell^-(t-1) & \text{otherwise}
\end{array}\right..\)

The motivation of freezing the random variables at time \(\tau_\ell\) is to ease the calculation of the expected one-step change: On the one hand, if \(t<\tau\), then _Q(t_) has a regularity that facilitates this calculation. On the other, if \(t\ge\tau\), then the one-step change is definitionally zero. Additionally, at the moment \(\ell\) becomes occupied, \(S_\ell\) jumps to 0. Thus, we cannot expect \(S_\ell\) itself to follow a smooth trajectory.

We note that \(\tau\le T\) only if for some \(\ell\in\mathcal{L}\) and some \(0\le t\le T\) one of \(S_\ell^+(t)\) or \(S_\ell^-(t)\) is greater than \(\varepsilon(t)/2\). This is the event whose probability we will bound.

We now show that \(\{S_\ell^+(t)\}_{t=0}^T\) and \(\{S_\ell^-(t)\}_{t=0}^T\) are supermartingales with respect to the filtration \(\{Q(t)\}_{t=0}^T\) induced by the random greedy algorithm. We first observe that for every _t\<T_ it holds that \(|S_\ell^+(t+1)-S_\ell^+(t)|,|S_\ell^-(t+1)-S_\ell^-(t)|=O(1)\). Indeed, when placing a queen on the board, it occupies exactly four lines. Each of these intersects a given line in exactly one position. Thus, \(|S_\ell(t+1)-S_\ell(t)|\le 4\). Additionally, by their definitions, _s(t_) and \(\varepsilon(t)\) change by only _O_(1) in each time step.

Next, we calculate expected one-step changes. If \(t\ge\tau_\ell\) then, by definition, the expected change is 0. It remains to show that, conditioning on \(\tau>t\) and line \(\ell\) remaining unoccupied at time _t_+1, the expected one-step change is non-positive. Consider a position (_r,c_) in line \(\ell\) that is available at time _t_. It becomes unavailable at time _t_+1 if and only if one of the other three lines containing it is occupied at time _t_. Since \(\tau>t\), each of these lines contains \(s(t)\pm\varepsilon(t)\) available positions, and they intersect only at (_r,c_). Let _B_ be the event that line \(\ell\) is unoccupied at time _t_+1. Observe that conditioning on \(\tau>t\) and _B_ implies that (_x_<sub>_t_+1</sub>_,y_<sub>_t_+1</sub>) is chosen uniformly from among<tbc>

\(|\mathcal{A}(t)|-S_\ell(t)=^{(1),t<\tau} n^2p(t)^4-np(t)^3\pm(np(t)\varepsilon(t)+\varepsilon(t))=n^2p(t)^4\pm 3np(t)\varepsilon(t)\)


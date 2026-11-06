<tbc>Fix \(v\in M\). Since \(v^\top\theta\in L^2\), Doob’s martingale convergence theorem gives<tbc>

\(\mathbb{E}[v^\top\theta|\mathcal{H}_t]\rightarrow\mathbb{E}[v^\top\theta|\mathcal{H}_\infty]\text{a.s.,}\)

<tbc>and<tbc>

\(\mathbb{E}[(v^\top\theta)^2|\mathcal{H}_t]\rightarrow\mathbb{E}[(v^\top\theta)^2|\mathcal{H}_\infty]\text{a.s.}\)

<tbc>Since \(\Omega\in\mathcal{H}_\infty\) and both \(v^\top\theta\) and \((v^\top\theta)^2\) are \(\mathcal{H}_\infty\)-measurable on \(\Omega\), we have<tbc>

\(\mathbb{E}[v^\top\theta|\mathcal{H}_\infty]=v^\top\theta,\mathbb{E}[(v^\top\theta)^2|\mathcal{H}_\infty]=(v^\top\theta)^2\)

<tbc>almost surely on \(\Omega\). Therefore,<tbc>

\(v^\top\mu_{t-1}^*=\mathbb{E}[v^\top\theta|\mathcal{H}_t]\rightarrow v^\top\theta\text{a.s. on}\Omega,\)

<tbc>and

\(v^\top\Sigma_{t-1}^*v=\mathbb{V}(v^\top\theta|\mathcal{H}_t)\rightarrow 0\text{a.s. on}\Omega.\) □

We next show that if sampling eventually remains in this recurrent span, uncertainty cannot go to zero in directions outside it.

LEMMA D.2. _Fix a deterministic set_ \(\mathcal{E}\subseteq\mathcal{D}\)_, let M_:=span(E)_, and let R<sub>M</sub> and Q be the orthogonal projectors onto M and_ \(M^\perp\)_. Suppose that on an event_ \(\Omega\):

(_i)_ _there exists an almost-surely finite round T_<sub>0</sub> _such that every sampled direction after round T_<sub>0</sub> _belongs to_ E_, and_<tbc>

_(ii)_ \(R_M\mu_{t-1}^*\rightarrow R_M\theta\) _and_ \(\|R_M\Sigma_{t-1}^*R_M\|_\mathrm{op}\rightarrow 0\) _almost surely on_ \(\Omega\).<tbc>

<tbc>_Then, almost surely on_ \(\Omega\)_, there exists_ \(\eta>0\) _such that, for all sufficiently large t,_<tbc>

\(Q\Sigma_{t-1}^*Q\unknown\eta Q.\)

<tbc>_Proof._ Work on \(\Omega\). We can decompose \(\mathbb{R}^I=M\oplus M^\perp\), so every \(\theta\in\mathbb{R}^I\) can be written uniquely as

\(\theta=u+v,u\in M,v\in M^\perp,\)

in particular \(u=R_M\theta\) and \(v=Q\theta\). Let _f_<sub>0</sub>(_u,v_) denote the posterior density for \(\theta\) after round _T_<sub>0</sub> evaluated at \(\theta=u+v\). Since \(T_0<\infty\), this density is obtained from the Gaussian prior density by multiplying finitely many one-observation likelihood factors and normalizing. Thus _f_<sub>0</sub> is continuous and strictly positive. Since each likelihood factor belongs to (0,1),

\(f_0(u,v)\le Z_{T_0}^{-1}\pi_0(u,v),\)

where \(\pi_0\) is the Gaussian prior density and _Z_<sub>_T_<sub>0</sub></sub>_\>_0 is the normalizing constant.


**Theorem 4.11.** _Given a t_-1_-transcript, within one pass over the input graph, we compute and store an exact_ \(g=-\gamma\nabla\Psi(\overline{v})^{b(\overline{\tau})}\) _where_

\(\nabla\Psi(\overline{v})^{b(\overline{\tau})}:=argmax_{\|h\|_{\overline{\tau}+\infty}=1}h^\top\nabla\Psi(\overline{v})\)<br>
\(\|\overline{v}-v^t\|_\infty\le\gamma/20\)<br>
\(\overline{\tau}\approx_\epsilon\tau^t\)

_where_ \(\Psi(\overline{v})=\sum_{e=1}^mcosh(\lambda\overline{v_e})\) _in implicit representation. This takes_ \(\widetilde{O}(logm)\) _space,_ \(\widetilde{O}(m\mathcal{T}(t-1))\) _time._

_Given edge e, querying any entry g<sub>e</sub> takes_ \(\mathcal{T}(t-1)+\widetilde{O}(1)\) _time._

Note that although _g_ is exact for <o>_v_</o> and <o>_r_</o>, <o>_v_</o> and <o>_r_</o> are not. We only require \(\|\overline{v}-v\|_\infty\le\gamma/20\) and \(\overline{\tau}\approx_\epsilon\tau\). Thus to store _g_ efficiently we define the following approximations. Specifically, the goal of these is to project _g_ onto a smaller polylog dimensional space.

**Definition 4.12.** _We use_ \(\text{round}_{1+\epsilon^\prime}(z)\) _to denote the closest_ \((1+\epsilon')^i\) _for z, we use_ \(\text{round}_{\epsilon^\prime}(z)\) _to denote the closest_ \(j\cdot\epsilon'\) _for z._

Our vector _g<sup>t</sup>_ will be computed using the following Definition 4.13.

**Definition 4.13.** _Given_ \(\epsilon',\mu>0\), \(x^{t-1},s^{t-1},\overline{\tau^t}\in\mathbb{R}_{>0}^m\) _we define_ \(\widetilde{g}^t\in\mathbb{R}^m\) _as:_

\(\widetilde{g}^t:=(\nabla\Psi(\text{round}_{\epsilon^\prime}(\frac{s^{t-1}+\mu\overline{\tau^t}\phi'(x^{t-1})}{\mu\overline{\tau^t}\sqrt{\phi''(x^{t-1})}})))^{b(\text{round}_{1+\epsilon^\prime}(\overline{\tau^t}))}.\)

To calculate this, we use the following theorem.

**Theorem 5.1.** _Given an_ \(\epsilon>0\), \(f:\mathbb{R}\rightarrow\mathbb{R}\)_, a directed weighted graph G_=(_V,E_) _given as stream, and implicit vectors_ \(v,\tau\in\mathbb{R}^E\) _satisfying_ \(n/m\le\tau\le 1\) _and_ \(-1\le v\le 1\) _such that for any given_ \(e\in E\) _we can query v<sub>e</sub> and_ \(\tau_e\) _in T time._

_Then we can construct an implicit representation of target vector_ \(g=(f(\text{round}_{\epsilon^\prime}(v))^{b(\text{round}_{1+\epsilon^\prime}\tau)}\)_. Our construction takes_ \(O(\epsilon'^{-2}logm)\) _space and O(mT_) _time._

_Given edge e, querying any entry g<sub>e</sub> takes T+O_(1) _time._

With these, we can now prove our main result for this section.

_Proof of Theorem 4.11._ We want to compute a \(g=(\nabla\Psi(\overline{v}))^{b(\overline{\tau})}\) where \(\|\overline{v}-v^t\|_\infty\le\gamma/20\) and \(\overline{\tau}\approx_\epsilon\tau^t\). We first claim that \(\widetilde{g}^t\) as defined in Definition 4.13 is a suitable choice for this _g_, when using \(\epsilon'=\gamma/60\). For this choice of _g_, we have \(\overline{v}=\text{round}_{\epsilon^\prime}(\frac{s^{t-1}+\mu\overline{\tau^t}\phi'(x^{t-1})}{\mu\overline{\tau^t}\sqrt{\phi''(x^{t-1})}})\). This satisfies \(\|\overline{v}-v^t\|_\infty\le\gamma/20\), because _x_<sup>_t_-1</sup> and _s_<sup>_t_-1</sup> are exact and \(\overline{\tau^t}\approx_{\gamma/60}\tau(x^{t-1})\) by Theorem 4.8.

We want to construct this _g_ via Theorem 5.1 using \(f=\nabla\Psi\), which requires

\(-1\le\underbrace{\frac{s^{t-1}+\mu\overline{\tau^t}\phi'(x^{t-1})}{\mu\overline{\tau^t}\sqrt{\phi''(x^{t-1})}}_{=:v}\le 1.\)

This is satisfied by centrality guarantee of the IPM (Lemma 4.7).

We now analyze the runtime of Theorem 5.1. To query _v<sub>e</sub>_ requires \(x_e^{t-1}\), \(s_e^{t-1}\), \(\overline{\tau_e^t}\), and _O_(1) calculation time. The first can be queried in time T(_t_-1), while the second is \(\widetilde{O}(1)\). We can temporarily save the value of \(x_e^{t-1}\), so that when we use Theorem 4.8, \(\tau_e\) requires time \(\widetilde{O}(1)\) as our input parameter _T<sub>x</sub>_ would be constant time. Thus parameter _T_ in Theorem 5.1 is _O_(T(_t_-1)), which leads to a total runtime of _O(m_T(_t_-1)). Querying _g<sub>e</sub>_ for an edge _e_ takes time T(_t_-1)+_O_(1) by Theorem 5.1.


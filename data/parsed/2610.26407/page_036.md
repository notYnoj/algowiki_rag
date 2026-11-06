<tbc>LEMMA 8 (EOC and posterior error rates). _For every sampling rule,_

\(-\frac{log\mathrm{EOC}(\mathcal{H}_t)}{\sum_iN_i(t)}-\Gamma(\widehat{w}(t);\theta^0)\longrightarrow 0\text{\textit{and}}-\frac{log\mathbb{P}_t(S_k(\theta)\neq S_k(\theta^0))}{\sum_iN_i(t)}-\Gamma(\widehat{w}(t);\theta^0)\longrightarrow 0.\)

_Proof_ The posterior error statement follows from Lemma 2 with \(O=\mathrm{Alt}(\theta^0)\). To prove the EOC statement, we first bound the posterior expected loss of selecting the true top-_k_ set, \(R_t:=\mathbb{E}_t[\mathrm{OC}(S_k(\theta^0),\theta)]\). We then compare _R<sub>t</sub>_ with EOC(H_<sub>t</sub>_).

For \(0<\delta<U-L\), define<tbc>

\(O_\delta:=\bigcup_{i\le k<j}\{x\in\mathcal{J}^I:x_j>x_i+\delta\}.\)

<tbc>On \(O_\delta\), the opportunity cost of selecting \(S_k(\theta^0)\) is at least \(\delta\). Also, opportunity cost is at most _k(U-L_) and is zero outside \(\mathrm{Alt}(\theta^0)\). Therefore,<tbc>

\(\delta\mathbb{P}_t(\theta\in O_\delta)\le R_t\le k(U-L)\mathbb{P}_t(\theta\in\mathrm{Alt}(\theta^0)).\) (15)

<tbc>Applying Lemma 2 to the probabilities in (15) gives<tbc>

\(\Gamma(\widehat{w}(t);\theta^0)-o(1)\le-\frac{\mathrm{log}R_t}{\sum_iN_i(t)}\le\mathrm{inf}_{y\in O_\delta}\sum_\ell\widehat{w}_\ell(t)d_\ell(\theta_\ell^0,y_\ell)+o(1).\)

<tbc>It therefore suffices to show that for every \(\varepsilon>0\), there is a \(\delta>0\) such that, for every \(w\in\Delta_I\),<tbc>

\(\Gamma(w;\theta^0)\le\mathrm{inf}_{y\in O_\delta}\sum_\ell w_\ell d_\ell(\theta_\ell^0,y_\ell)\le\Gamma(w;\theta^0)+\varepsilon.\) (16)

<tbc>The first inequality follows from \(O_\delta\subseteq\mathrm{Alt}(\theta^0)\). For the second, choose \(\delta>0\) small enough that \(x\pm\delta\in\mathcal{J}\) and<tbc>

\(|d_i(\theta_i^0,x\pm\delta)-d_i(\theta_i^0,x)|\le\varepsilon\text{for every}i\text{and}x\in[\theta_I^0,\theta_1^0].\)

<tbc>Fix **_w_** and choose _i_, _j,x_ attaining the minimum in (12). Setting \(y_i=x-\delta\), \(y_j=x+\delta\), and \(y_\ell=\theta_\ell^0\) for all other items gives a vector in \(O_\delta\). Hence<tbc>

\(\mathrm{inf}_{y\in O_\delta}\sum_\ell w_\ell d_\ell(\theta_\ell^0,y_\ell)\le w_id_i(\theta_i^0,x-\delta)+w_jd_j(\theta_j^0,x+\delta)\)<br>
\(\le w_id_i(\theta_i^0,x)+w_jd_j(\theta_j^0,x)+\varepsilon(w_i+w_j)\)<br>
\(\le\Gamma(w;\theta^0)+\varepsilon.\)

<tbc>This proves (16). Combining it with the preceding bounds on \(-\mathrm{log}R_t/\sum_iN_i(t)\) and letting \(\varepsilon\downarrow 0\) gives<tbc>

\(-\frac{\mathrm{log}R_t}{\sum_iN_i(t)}-\Gamma(\widehat{w}(t);\theta^0)\longrightarrow 0.\) (17)

<tbc>We next compare _R<sub>t</sub>_ with EOC(H_<sub>t</sub>_). Let \(g:=\theta_k^0-\theta_{k+1}^0>0\) and \(V:=\{x\in\mathcal{J}^I:\|x-\theta^0\|_\infty<g/4\}\) so that for every \(x\in V\), \(S_k(x)=S_k(\theta^0)\). If \(S_k(\mu(t))\neq S_k(\theta^0)\), its opportunity cost is at least _g/_2 when \(\theta\in V\) , thus \(\mathrm{EOC}(\mathcal{H}_t)\ge(g/2)\mathbb{P}_t(\theta\in V)\). If \(S_k(\mu(t))=S_k(\theta^0)\), then EOC(H_<sub>t</sub>)=R<sub>t</sub>_. Since selecting the largest posterior means minimizes posterior expected opportunity cost, we also have \(\mathrm{EOC}(\mathcal{H}_t)\le R_t\) in both cases. Hence<tbc>

\(\mathrm{min}\{R_t,(g/2)\mathbb{P}_t(\theta\in V)\}\le\mathrm{EOC}(\mathcal{H}_t)\le R_t.\)


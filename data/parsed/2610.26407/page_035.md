<tbc>_Proof of Proposition 4_ Fix \(\theta^0\in\Theta^*\). By Lemma 7, \(N_i(t)\rightarrow\infty\) for every _i_, almost surely. Hence \(\mu_i(t)\rightarrow\theta_i^0\) and \(v_i(t)\rightarrow 0\) for every _i_, almost surely. Next, for any realized \(\theta\),

\(\mathrm{OC}(S_k(\mu(t)),\theta)=\sum_{i\in S_k(\theta)}\theta_i-\sum_{i\in S_k(\mu(t))}\theta_i\)<br>
\(\le\sum_{i\in S_k(\theta)}|\theta_i-\mu_i(t)|+\sum_{i\in S_k(\mu(t))}|\theta_i-\mu_i(t)|\)<br>
\(\le 2k\|\theta-\mu(t)\|_\infty.\)

Taking expectation,

\(\mathrm{EOC}(\mathcal{H}_t)\le 2k\mathbb{E}_t\|\theta-\mu(t)\|_\infty\le 2k\sum_{i=1}^I\mathbb{E}_t|\theta_i-\mu_i(t)|\le 2k\sum_{i=1}^I\sqrt{v_i(t)}.\)

Since \(v_i(t)\rightarrow 0\) for every _i_, \(\mathrm{EOC}(\mathcal{H}_t)\rightarrow 0\) almost surely.

Finally, assume \(\theta_{[k]}^0>\theta_{[k+1]}^0\), and let \(g:=\theta_{[k]}^0-\theta_{[k+1]}^0>0\). Since \(\mu_i(t)\rightarrow\theta_i^0\) for every _i_, eventually \(|\mu_i(t)-\theta_i^0|<g/3\). If \(i\in S_k(\theta^0)\) and \(j\notin S_k(\theta^0)\), then \(\theta_i^0\ge\theta_{[k]}^0\) and \(\theta_j^0\le\theta_{[k+1]}^0\). Hence, eventually,

\(\mu_i(t)\ge\theta_{[k]}^0-g/3>\theta_{[k+1]}^0+g/3\ge\mu_j(t).\)

Thus \(S_k(\mu(t))=S_k(\theta^0)\) eventually almost surely. \(\square\)

**C.2. The optimal exponential rate**

Throughout this subsection and the next, assume Assumption 2 and \(1\le B_t\le B\) for every _t_, where _B_ is a fixed positive integer. All convergence statements hold \(\mathbb{P}_{\theta^0}\)-almost surely.

_Proof of Lemma 3_ By the definition of Alt\((\theta^0)\),

\(\Gamma(w;\theta^0)=\mathrm{inf}_{x\in\mathrm{Alt}(\theta^0)}\sum_{\ell=1}^Iw_\ell d_\ell(\theta_\ell^0,x_\ell)\)<br>
\(=\mathrm{min}_{i\le k<j}\mathrm{inf}_{x\in\mathcal{J}^Ix_i<x_j}\sum_{\ell=1}^Iw_\ell d_\ell(\theta_\ell^0,x_\ell)\)<br>
\(=\mathrm{min}_{i\le k<j}\mathrm{inf}_{u,v\in\mathcal{J}u<v}\{w_id_i(\theta_i^0,u)+w_jd_j(\theta_j^0,v)\}.\)

The last equality follows by setting \(x_\ell=\theta_\ell^0\) for \(\ell\notin\{i,j\}\). We conclude by showing that the inner infimum equals

\(\mathrm{min}_{x\in[\theta_j^0,\theta_i^0]}\{w_id_i(\theta_i^0,x)+w_jd_j(\theta_j^0,x)\}.\)

Under Assumption 2, \(d_\ell(\theta_\ell^0,x)\) is continuous and decreases as _x_ moves toward \(\theta_\ell^0\). By continuity of \(d_\ell(\theta_\ell^0,\cdot)\), we may replace _u\<v_ with \(u\le v\) . Since moving _u_ toward \(\theta_i^0\) and _v_ toward \(\theta_j^0\) cannot increase the sum, we may restrict to \(\theta_j^0\le u\le v\le\theta_i^0\). Within this interval, replacing _u_ by _v_ cannot increase \(d_i(\theta_i^0,u)\). Thus we may take \(u=v=x\in[\theta_j^0,\theta_i^0]\), and the infimum is a minimum by continuity and compactness. \(\square\)


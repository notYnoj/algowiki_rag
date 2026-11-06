<tbc>where _Y_ is an additional observation of item _i_.

By (5), \(\widetilde{\theta}_i(d+1)\) is a contraction of \(\widetilde{\theta}_i(d)\) about \(\mu_i(t)\) with factor _c<sub>i</sub>(t,d_+1)_/c<sub>i</sub>(t,d_). The convexity argument in the proof of Lemma 6 gives

\(0\le\left(1-\frac{c_i(t,d+1)}{c_i(t,d)}\right)J_{i,t}(d)\le D_{i,t}(d)=J_{i,t}(d)-J_{i,t}(d+1)\le J_{i,t}(d)\le J_{i,t}(0).\) (23)

This proves the upper bound in (22). For the lower bound, we next bound 1-_c<sub>i</sub>(t,d_+1)_/c<sub>i</sub>(t,d_) from below.

Let _Z<sub>d</sub>_=(_Y_<sub>1</sub>_,...,Y<sub>d</sub>_) be the next _d_ observations of item _i_, and let _Y=Y_<sub>_d_+1</sub>. Applying the variance and covariance identities in the proof of Lemma 6 conditional on (H_<sub>t</sub>,Z<sub>d</sub>_), followed by Cauchy-Schwarz, gives

\(\bar{v}_i(t,d)-\bar{v}_i(t,d+1)\ge\mathbb{E}_t\left[\frac{\mathbb{V}(\theta_i|\mathcal{H}_t,Z_d)^2}{\mathbb{V}(Y|\mathcal{H}_t,Z_d)}\right]\ge\frac{\bar{v}_i(t,d)^2}{\mathbb{E}_t[\mathbb{V}(Y|\mathcal{H}_t,Z_d)]}\ge\frac{\bar{v}_i(t,d)^2}{\mathbb{V}_t(Y)}.\)

The last inequality follows from the law of total variance. Therefore,

\(1-\frac{c_i(t,d+1)}{c_i(t,d)}=\frac{\bar{v}_i(t,d)-\bar{v}_i(t,d+1)}{\bar{v}_i(t,d)(1+c_i(t,d+1)/c_i(t,d))}\ge\frac{\bar{v}_i(t,d)}{2\mathbb{V}_t(Y)}\ge\frac{\bar{v}_i(t,B-1)}{2\mathbb{V}_t(Y)}.\)

Also, (23) gives \(J_{i,t}(d)\ge J_{i,t}(B-1)\) for _d\<B_. Substituting into the lower bound in (23) proves (22).

We now show that both _J<sub>i,t</sub>_(0) and _J<sub>i,t</sub>(B_-1) have exponential rate \(d_i(\theta_i^0,q_0)\):

\(-\frac{logJ_{i,t}(d)}{N_i(t)}\longrightarrow d_i(\theta_i^0,q_0),d\in\{0,B-1\}.\) (24)

By Lemma 9,

\(c_i(t,d)\rightarrow 1,z_i(t,d)=\mu_i(t)+\frac{q(t)-\mu_i(t)}{c_i(t,d)}\rightarrow q_0.\)

Since \(\mu_i(t)\rightarrow\theta_i^0\) and \(q_0\in(\theta_{k+1}^0,\theta_k^0)\), (7) gives, for all sufficiently large _t_,

\(J_{i,t}(d)=\left\{\begin{array}{ c c }
c_i(t,d)\mathbb{E}_t[(z_i(t,d)-\theta_i)^+], & i\le k, \\
c_i(t,d)\mathbb{E}_t[(\theta_i-z_i(t,d))^+], & i>k.
\end{array}\right.\)

Write _n=N<sub>i</sub>(t_). By (18) and monotonicity of \(d_i(\theta_i^0,x)\),

\(J_{i,t}(d)\le(U-L)e^{-n(d_i(\theta_i^0,z_i(t,d))-\varepsilon_{i,n})}.\)

For a lower bound when \(i\le k\), choose a sufficiently small \(\delta>0\) and let \(V=[q_0-2\delta,q_0-\delta]\subset\mathcal{J}\) . Eventually \(|z_i(t,d)-q_0|<\delta/2\), so

\(J_{i,t}(d)\ge c_i(t,d)\frac{\delta}{2}\Pi_{i,t}(V)\ge c_i(t,d)\frac{\delta}{2}\Pi_{i,0}(V)e^{-n(d_i(\theta_i^0,q_0-2\delta)+\varepsilon_{i,n})}.\)

For _i\>k_, take \(V=[q_0+\delta,q_0+2\delta]\) and obtain the same bound with \(q_0+2\delta\) in place of \(q_0-2\delta\). Since \(c_i(t,d)\rightarrow 1\) and \(\Pi_{i,0}(V)>0\), taking logarithms, letting \(t\rightarrow\infty\), and then letting \(\delta\downarrow 0\) proves (24).

To conclude (21) from (22), it remains to show that

\(-\frac{1}{n}log\frac{\bar{v}_i(t,B-1)}{2\mathbb{V}_t(Y)}\longrightarrow 0.\)


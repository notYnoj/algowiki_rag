<tbc>Since \(\theta^0\in V\) , the infimum in Lemma 2 is zero for _O=V_ , giving

\(-\frac{log\mathbb{P}_t(\theta\in V)}{\sum_iN_i(t)}\longrightarrow 0.\)

Taking logarithms and using (17) proves the EOC statement. □

_Proof of Proposition 5_ For part (i), \(\Gamma\) is continuous in **_w_** by (12), since each inner minimum is over a fixed compact interval. It therefore attains a finite maximum on \(\Delta_I\). If every _w<sub>i</sub>\>_0, each pair minimum is positive because the two KL terms cannot both vanish when \(\theta_i^0>\theta_j^0\). Thus \(\Gamma^*(\theta^0)>0\).

We will also use that every maximizing allocation has positive elements. To see this, take _w<sub>i</sub>_=0 and choose some _j_ on the other side of the true top-_k_ boundary. Evaluating the pair at \(x=\theta_j^0\) gives

\(0\le\Gamma(w;\theta^0)\le w_id_i(\theta_i^0,\theta_j^0)+w_jd_j(\theta_j^0,\theta_j^0)=0.\)

Such an allocation cannot attain the positive maximum.

For part (ii), Lemma 8 and the definition of \(\Gamma^*\) give

\(limsup_{t\rightarrow\infty}-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\le\Gamma^*(\theta^0).\)

For part (iii), if \(\widehat{w}(t)\rightarrow w^*\) for a maximizing allocation **_w_**<sup>∗</sup>, continuity gives

\(-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\longrightarrow\Gamma(w^*;\theta^0)=\Gamma^*(\theta^0).\)

The posterior error result follows from Lemma 8. □

## C.3. The rate of TEAk

We now prove Theorems 1 and 2. We first establish Theorem 1 for \(q(t)\rightarrow q_0\in(\theta_{k+1}^0,\theta_k^0)\). We then prove Remark 3 and Lemma 4 and apply Theorem 1 with _q_<sub>0</sub>=_q_<sup>†</sup>. Finally, we compare the resulting rate with \(\Gamma^*(\theta^0)\) to prove Theorem 2.

To prove Theorem 1, we first determine the exponential rate of _D<sub>i,t</sub>(d_). For this, we need the following lemma on the posterior density, mean, and variance. The mean and variance convergence was already established in Lemma 5 for prior-almost every true parameter. Here, under the stronger assumptions of Assumption 2, we establish it for every fixed true parameter, together with the additional estimates needed to determine the rate of _D<sub>i,t</sub>(d_). The proof relies on Russo (2020, Proposition 4 and Lemmas EC.5, EC.7, and EC.8).

LEMMA 9 (**Posterior density, mean, and variance**)**.** _Let_ \(\Pi_i^{(n)}\) _be the posterior after the first n observations of item i, with density_ \(\pi_i^{(n)}\)_, mean_ \(\mu_{i,n}\)_, and variance v<sub>i,n</sub>. Thus_ \(\Pi_i^{(0)}=\Pi_{i,0}\) _and_ \(\Pi_{i,t}=\Pi_i^{(N_i(t))}\)_. For every i,_<tbc>

\(\varepsilon_{i,n}:=sup_{x\in\mathcal{J}}\left|\frac{1}{n}log\frac{\pi_i^{(n)}(x)}{\pi_{i,0}(x)}+d_i(\theta_i^0,x)\right|\longrightarrow 0,\) (18)

\(\mu_{i,n}\longrightarrow\theta_i^0,v_{i,n}\longrightarrow 0,-\frac{1}{n}logv_{i,n}\longrightarrow 0.\)

<tbc>_If_ \(N_i(t)\rightarrow\infty\)_, then for every fixed integer_ \(m\ge 0\),

\(\frac{\bar{v}_i(t,m)}{v_i(t)}\longrightarrow 1.\) (19)


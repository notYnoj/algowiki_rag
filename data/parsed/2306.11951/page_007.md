<tbc>element in round _t_. We can further calculate the \(\chi^2\) divergence as

\(\chi^2(\mathbb{E}[\mathbb{P}_{1_j}(\cdot)],\mathbb{P}_0(\cdot))\)<br>
\(=^{(a)}\mathbb{E}_{j,j^\prime\sim q}\left[\sum_x\frac{\mathbb{P}_{1_j}(x)\mathbb{P}_{1_{j^\prime}}(x)}{\mathbb{P}_0(x)}\right]-1\)<br>
\(=^{(b)}\mathbb{E}_{j,j^\prime}\left[\prod_{t=1}^T\left(\sum_{m=1}^K\frac{(\pi_m^t)^2(1-p)^{\unknown(j\neq m)+\unknown(j^\prime\neq m)}p^{\unknown(j=m)+\unknown(j^\prime=m)}}{\pi_m^t(1-p)}\right.\right.\)<br>
\(\left.+\frac{(\pi_m^t)^2(1-p)^{\unknown(j=m)+\unknown(j^\prime=m)}p^{\unknown(j\neq m)+\unknown(j^\prime\neq m)}}{\pi_m^tp}\right)\right]-1\)<br>
\(=\mathbb{E}_{j,j^\prime}\left[\prod_{t=1}^T\left(\sum_{m=1}^K\pi_m^t\left(\frac{(1-p)^{\unknown(j\neq m)+\unknown(j^\prime\neq m)}p^{\unknown(j=m)+\unknown(j^\prime=m)}}{1-p}\right.\right.\)<br>
\(\left.+\frac{(1-p)^{\unknown(j=m)+\unknown(j^\prime=m)}p^{\unknown(j\neq m)+\unknown(j^\prime\neq m)}}{p}\right)\right]-1\)<br>
\(=\mathbb{E}_{j,j^\prime}\left[\prod_{t=1}^T\left(\sum_{m=1}^K\pi_m^t\left(1+\frac{(1-2p)^2\cdot\unknown(j=j^\prime=m)}{(1-p)p}\right)\right)\right]-1\)<br>
\(=1-\sum_{j=1}^Kp_j^2+\sum_{j=1}^Kp_j^2\prod_{t=1}^T\left(1+\frac{\pi_j^t(1-2p)^2}{(1-p)p}\right)-1\)<br>
\(=-\sum_{j=1}^Kp_j^2+\sum_{j=1}^Kp_j^2\prod_{t=1}^T\left(1+\frac{\pi_j^t(1-2p)^2}{(1-p)p}\right),\)

where (_a_) follows from Lemma A.5, and (_b_) follows from the tensorization property of \(\chi^2\) for tensor products, a direct result of Lemma A.5. Now denote \(T_j=\sum_{t=1}^T\pi_j^t\). By Jensen’s inequality, we know that \(\prod_{t=1}^T(1+\frac{\pi_j^t(1-2p)^2}{(1-p)p})\le(1+\frac{T_j(1-2p)^2}{T(1-p)p})^T\). Thus we have<tbc>

\(\chi^2(\mathbb{P}_0(\cdot),\mathbb{E}[\mathbb{P}_{1_j}(\cdot)])\)<br>
\(\le-\sum_{j=1}^Kp_j^2+\sum_{j=1}^Kp_j^2\left(1+\frac{T_j(1-2p)^2}{T(1-p)p}\right)^T.\)

<tbc>Now we take \(p_j=((1+\frac{T_j(1-2p)^2}{T(1-p)p})^T-1)^{-1/2}/(\sum_j((1+\frac{T_j(1-2p)^2}{T(1-p)p})^T-1)^{-1/2})\). We have<tbc>

\(\chi^2(\mathbb{P}_0(\cdot),\mathbb{E}[\mathbb{P}_{1_j}(\cdot)])\)<br>
\(\le\frac{K}{(\sum_{j=1}^K((1+\frac{T_j(1-2p)^2}{T(1-p)p})^T-1)^{-1/2})^2}.\)

<tbc>Since \(\sum_jT_j=T\), by Jensen’s inequality, we have \(\sum_{j=1}^K((1+\frac{T_j(1-2p)^2}{T(1-p)p})^T-1)^{-1/2}\ge K((1+\frac{(1-2p)^2}{K(1-p)p})^T-1)^{-1/2}\). Thus<tbc>

\(\chi^2(\mathbb{P}_0(\cdot),\mathbb{E}[\mathbb{P}_{1_j}(\cdot)])\le\frac{1}{K}\cdot\left(\left(1+\frac{(1-2p)^2}{K(1-p)p}\right)^T-1\right).\)

<tbc>This gives the desired result. Now solving the inequality

\(\delta\ge\frac{1}{2}\cdot\left(1-\sqrt{\frac{1}{2K}\left(\left(1+\frac{(1-2p)^2}{K(1-p)p}\right)^T-1\right)}\right),\)

we arrive at \(T\ge log(1+2K(1-2\delta^2))/log(1+\frac{(1-2p)^2}{K(1-p)p})\unknown Klog(K)p/(1-2p)^2\).


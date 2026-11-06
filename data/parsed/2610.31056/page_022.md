<tbc>Since \(\beta>0\), if<tbc>

\(\left|\frac{x}{\beta}\right|\neq\left|\frac{x+\varepsilon}{\beta}\right|,\)

<tbc>then there exists an integer \(k\in\mathbb{Z}\) such that

\(k\in\left[min\big\{\frac{x}{\beta},\frac{x+\varepsilon}{\beta}\big\},max\big\{\frac{x}{\beta},\frac{x+\varepsilon}{\beta}\big\}\right].\)

Multiplying by \(\beta\), we obtain \(k\beta\in J_\alpha\), where \(J_\alpha:=[min\{x,x+\varepsilon\},max\{x,x+\varepsilon\}]\). Thus, if \(\mathcal{E}_{\alpha,\beta}\) occurs, then \(J_\alpha\) contains an integer divisible by \(\beta\). Since \(|J_\alpha|=|\varepsilon|\le 1\), the interval \(J_\alpha\) contains at most two integers. We split into two cases.<br>
_Case 1_ (\(J_\alpha\) _contains_ 0). Then \(\alpha\in[-b-max\{0,\varepsilon\},-b-min\{0,\varepsilon\}]\), and this interval has length at most 1. Hence, it contains at most two integers, so<tbc>

\(\mathbb{P}_\alpha[0\in J_\alpha]\le\frac{2}{N^2}=\mathcal{O}\big(\frac{1}{N^2}\big).\)

<tbc>_Case 2_ (\(J_\alpha\) _does not contain_ 0). Fix such an \(\alpha\). Since \(J_\alpha\) contains at most two integers, there are at most two nonzero integers \(z\in J_\alpha\cap\mathbb{Z}\) that could be equal to \(k\beta\). Moreover, every such _z_ satisfies<tbc>

\(|z|\le max\{|x|,|x+\varepsilon|\}\le|b|+|\alpha|+|\varepsilon|\le BN+N^2+1.\)

<tbc>Each nonzero integer _z_ has at most log<sub>2</sub>|_z_|=O(log(_BN_<sup>2</sup>+_N_<sup>2</sup>)) distinct prime divisors. Since there are at most two such integers, the total number of primes \(\beta\) for which \(\mathcal{E}_{\alpha,\beta}\) can occur is O(log(_BN_<sup>2</sup>+_N_<sup>2</sup>)). Now \(\beta\) is chosen uniformly at random from the set of primes in \[_N_<sup>3</sup>\]. By the prime number theorem,<tbc>

\(\pi(N^3)=\Theta\big(\frac{N^3}{log(N^3)}\big)=\Theta\big(\frac{N^3}{logN}\big).\)

<tbc>Therefore, for every fixed \(\alpha\) with \(0\notin J_\alpha\),

\(\mathbb{P}_\beta[\mathcal{E}_{\alpha,\beta}]\le\frac{\mathcal{O}(log(BN^2+N^2))}{\Theta(N^3/logN)}\)<br>
\(=\mathcal{O}\big(\frac{log(BN^2+N^2)logN}{N^3}\big).\)

Combining the two cases gives

\(\mathbb{P}_{\alpha,\beta}[\mathcal{E}_{\alpha,\beta}]\le\mathcal{O}\big(\frac{1}{N^2}\big)+\mathcal{O}\big(\frac{log(BN^2+N^2)logN}{N^3}\big),\)

which proves the claim. If \(B\ge N\), then \(BN^2+N^2\le 2BN^2\), so log(_BN_<sup>2</sup>+_N_<sup>2</sup>)=O(log(_BN_)), yielding the final bound. \(\blacksquare\)

Fix a sample \(\mathbf{x}'^{(i)}\) satisfying \(\|\mathbf{x}'^{(i)}\|_\infty\le BN^2\tilde{\lambda}_n\). Then, for every coordinate \(j\in[n]\),<tbc>

\(\frac{(\mathbf{x}^\prime^{(i)})_j}{\tilde{\lambda}_n}\in[-N^2B,N^2B].\)

<tbc>Also, since **v**<sup>∗</sup> is a shortest nonzero vector, \(|(\mathbf{v}^*)_j|\le\|\mathbf{v}^*\|_2=\lambda_1(\mathcal{L})\le\tilde{\lambda}_n\), and hence \(\frac{(\mathbf{v}^*)_j}{\tilde{\lambda}_n}\in[-1,1]\). Applying Claim 5.2.1 with<tbc>

\(b=\frac{(\mathbf{x}^\prime^{(i)})_j}{\tilde{\lambda}_n},\alpha=s_j,\beta=r_j,\varepsilon=\frac{(\mathbf{v}^*)_j}{\tilde{\lambda}_n},\)


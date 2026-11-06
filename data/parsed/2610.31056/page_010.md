To analyze this common filtering procedure, we introduce collision-counting random variables and study their first and second moments.

## Distribution of collisions.

Now, we aim to analyze the distribution of integer and modular collisions in the final list _L_<sub>1234</sub>. For this, we first define two random variables that denote the number of non-trivial integer and modular collisions in this final list. Let C<sup>(int)</sup> and C<sup>(pqr)</sup> denote these two random variables, respectively. Our filtering algorithm succeeds if the value of these variables is at least 1. Hence, we look for the probability of this event.

For any input instance, we can compute the value of C<sup>(int)</sup>, and similarly C<sup>(pqr)</sup>, by iterating through all the possible pairs of binary vectors, and considering whether the vectors (or the corresponding subset sum) pass through the filters of the algorithm and collide, over integers or modulo _pqr_, based on the problem. For each pair of binary vectors **u**_<sub>i</sub>,_**u**_<sub>j</sub>_, we define a binary random variable \(\mathcal{C}_{ij}^{(\mathrm{int})}\) and \(\mathcal{C}_{ij}^{(\mathrm{pqr})}\), such that their value is 1 if and only if **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ pass through all the filters of the algorithm, and they collide over integers or modulo _r_ based on the problem.

## First Moment.

In the modular case, we have that the probability of vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ surviving the algorithm is 1_/p_<sup>4</sup>_q_<sup>2</sup> <sup>8</sup>, and the probability of them colliding modulo _r_ is 1_/r_, given \(\mathbf{u}_i\neq\mathbf{u}_j\). Hence, we have \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathrm{pqr})}\right)=1/p^4q^2r\). Since there are \(\Theta(4^n)\) pairs of binary vectors, using the bounds for _M,p_, and _q_, we have \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{pqr})}\right)=\Omega(1)\) (see Section 6 for details).

Next, we focus on the integer case. The vectors surviving the algorithm and their collision over the remaining bits are dependent on each other. Hence, the analysis of the first moment in this case is a bit involved. We split the integer subset sum as follows:

\(\mathbf{a}\cdot\mathbf{u}_i=\left(\mathbf{a}^{(pq)}+\mathbf{a}^{(r)}\cdot pq\right)\cdot\mathbf{u}_i,\)<br>
\(=\underbrace{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\mathrm{mod}pq}_{pq\text{bits}}+\underbrace{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i-\left(\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\mathrm{mod}pq\right)}_{pq\text{carry bits}}\cdot pq+\underbrace{\mathbf{a}^{(r)}\cdot\mathbf{u}_i}_{\text{remaining bits}}\cdot pq.\)

To make the analysis simpler, also since we are only interested in the lower bound of the first moment, we redefine the random variable \(\mathcal{C}_{ij}^{(\mathrm{int})}\) as follows: its value is 1 if and only if **u**_<sub>i</sub>,_**u**_<sub>j</sub>_ survive filtering algorithm, they collide over the carry bits, and the remaining bits separately. Since the vectors **a**<sup>(_pq_)</sup> and **a**<sup>(_r_)</sup> are independent, we can analyze the corresponding sums separately.

To characterize the distribution of the sum of integer-valued random variables, we employ the Local Central Limit Theorem (LCLT) \[IL65, MU17\]. Informally, the LCLT asserts that the distribution of the sum of I.I.D. random variables converges to a discrete Gaussian distribution, and that in a neighborhood of the mean, the point probabilities are approximately uniform up to constant factors. To apply this result in our setting, we restrict attention to binary vectors whose Hamming weight is \(\Theta(n)\). A formal statement of the theorem is provided in Section 7.

Leveraging the smoothness of the sum distributions, we first show that the carry bits converge in distribution to a discrete normal distribution, and henceforth we prove that the total sum modulo _pq_ and the left sum modulo _p_ condition on the carry bits converges to the uniform distribution asymptotically. Finally, we show that the following three events _E_<sub>1</sub>_,E_<sub>2</sub> and _E_<sub>3</sub> are asymptotically independent, where \(E_1:=\sum_{j=1}^{n/2}a_j^{(pq)}\cdot u_{ij}\equiv_p\alpha,E_2:=\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\equiv_{pq}\beta\), and \(E_3:=\left\lfloor\mathbf{a}^{(pq)}\cdot\mathbf{u}_i/pq\right\rfloor=\gamma\).

After analyzing the dependency of the events relying on the vector **a**<sup>(_pq_)</sup>, and using the probability of two Gaussian distributions colliding, we get that the probability that both **u**_<sub>i</sub>,_**u**_<sub>j</sub>_ survive the filter<tbc>

<sup>8</sup>The probability can be different if the left part (first _n/_2 elements) or the right part (last _n/_2 elements) of these two binary vectors is the zero vector. We’ll carefully analyze those cases in the main section.


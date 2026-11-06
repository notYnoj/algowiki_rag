is assigned to exactly one subset, the collection \(\{T_j\}_{j\in J}\) forms a partition of _I_ into triplets.

By flow conservation, the volume of commodity _k<sub>L</sub>_ entering node _v<sub>j</sub>_ must equal the volume exiting it. From Lemma 2.9, the load of _k<sub>L</sub>_ entering _v<sub>j</sub>_ from the object nodes is \(\sum_{i\in T_j}w_i\). From Lemma 2.7, the load of _k<sub>L</sub>_ exiting _v<sub>j</sub>_ on arc (_v<sub>j</sub>,t_) is \(\frac{W}{m}\). Therefore, we have: \(\sum_{i\in T_j}w_i=\frac{W}{m}\forall j\in J\). We can conclude that the partition \(\{T_j\}_{j\in J}\) is a valid solution for the 3-Partition problem defined by the multiset \(\{w_i\}_{i\in I}\).

## B Proof of the performance guarantee of H_<sub>threshold</sub>_

### B.1 Proof of Proposition 5.1

_Proof._ Since \(\breve{\mathcal{X}}_{\epsilon,\theta,\zeta,\eta}(x,y)\ge s_{\epsilon,\theta}(x,y)\), if \(f(\lambda x,\lambda y)\le\lambda s_{\epsilon,\theta}(x,y)\) holds, then \(f(\lambda x,\lambda y)\le\lambda\breve{\mathcal{X}}_{\epsilon,\theta,\zeta,\eta}(x,y)\) is also valid.

If \(\lambda=0\), the inequality in the proposition holds trivially. Let us then assume that \(\lambda>0\). Inequality \(f(\lambda x,\lambda y)\le\lambda s_{\epsilon,\theta}(x,y)\) is then equivalent to:

\(\lambda\le\frac{1-\frac{x}{s_{\epsilon,\theta}(x,y)}}{y}=\frac{1-\frac{x}{1-\theta-\frac{x}{y-x-\theta}}}{y}=\frac{(\theta+x)(1-\epsilon)-\theta y}{y(1-\epsilon+x)-y^2}=q_{\epsilon,\theta}(x,y).\) (36)

For a given \(y\in]\eta,1-\epsilon]\), the function \(q_{\epsilon,\theta}\) defined above is increasing in \(x\in[0,\mathrm{min}(y-\theta,1-\zeta)]\) since its derivative is given by \(\frac{(1-\epsilon-y)(1-\epsilon-\theta)}{y(1-\epsilon+x-y)^2}\) . Similarly, \(q_{\epsilon,\theta}\) is increasing with respect to \(\theta\) for any \(\theta\) satisfying (13). Therefore, given an \(x_0\in[0,1-\zeta]\), \(f(\lambda x,\lambda y)\le\lambda\breve{\mathcal{X}}(x,y)\) holds for any \(x\ge x_0\) and any \(\lambda\le q_{\epsilon,0}(x_0,y)\).

Moreover, \(q_{\epsilon,0}(x_0,y)=\frac{x_0(1-\epsilon)}{y(1-\epsilon+x_0)-y^2}\) attains its lower bound when \(y^*=\frac{1-\epsilon+x_0}{2}\) , with a value of \(\frac{4x_0(1-\epsilon)}{(1-\epsilon+x_0)^2}\). Hence \(\lambda_{\epsilon,x_0}=q_{\epsilon,0}(x_0,y^*)=\frac{4x_0(1-\epsilon)}{(1-\epsilon+x_0)^2}\) satisfies (36).


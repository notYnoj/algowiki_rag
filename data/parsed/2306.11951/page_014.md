## APPENDIX BPROOF FOR THEOREM III.1

_Proof._ We first select an arbitrary sequence \(0<X_1<X_2<\cdots<X_K<1\). Let \(\theta_0=(X_1,X_2,X_3,\cdots,X_K)\) be original sequence which has its largest value in the _K_-th element. Thus \(\text{MAX}(\theta_0)=K\). Now for any \(i\in[K-1]\), we design \(\theta_i=(X_1,\cdots,X_{i-1},X_K,X_i,X_{i+1},\cdots,X_{K-1})\), i.e., we move the _K_-th element in \(\theta_0\) and insert it between _X_<sub>_i_-1</sub> and _X<sub>i</sub>_. Let _T<sub>i,j</sub>_ be the random variable that represents the number of comparisons between the _i_-th item and _j_-th item in the _T_ rounds. We know that \(\text{MAX}(\theta_i)=i\) for all \(i\in[K-1]\). Following a similar proof as Theorem II.1, we know that

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\text{MAX}(\theta))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{2}(1-\text{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j}))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{4}exp(-D_\text{KL}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j}))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{4}exp(-\sum_{l=j+1}^K\mathbb{E}_{\theta_0}[T_{j,l}]\cdot D_\text{KL}(p\|1-p)).\)

Now since \(\sum_{i,j\in[K],i<j}\mathbb{E}_{\theta_0}[T_{i,j}]=T\), there must exists some _j_ such that \(\sum_{l=j+1}^K\mathbb{E}_{\theta_0}[T_{j,l}]\le T/K\). This gives

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\text{MAX}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\text{KL}(p\|1-p)}{K}\right).\)

On the other hand, _K_ is naturally a lower bound for the query complexity since one has to query each element at least once. Thus we arrive at a lower bound of \(\Omega(max(K,Klog(1/\delta)/D_\text{KL}(p\|1-p)))\). Note that this is equivalent to \(\Omega(K/(1-H(p))+Klog(1/\delta)/D_\text{KL}(p\|1-p))\) up to a constant factor when \(\delta<0.49\). The reason is that when _p_ is bounded away from 0, (1-_H(p_))_/D_KL(_p_∥1-_p_) is always some constant. When _p_ is close to 0, 1-_H(p_) is within constant factor of 1.

## APPENDIX BPROOF FOR THEOREM III.2

_Proof._ Consider an arbitrary sequence \(0<X_1<X_2<\cdots<X_K<1\). Since \(\sum_{i,j\in[K],i<j}\mathbb{E}_{\theta_0}[T_{i,j}]=T\), there must exists some pair (_i,j_) such that \(\mathbb{E}_{\theta_0}[T_{i,j}]\le 2T/K(K-1)\). Now we construct<tbc>

\(\theta_0=(X_1,X_2,X_3,\cdots,X_K,\cdots,X_{K-1},\cdots,X_{K-2}),\)

<tbc>where _X<sub>K</sub>_ lies in the _i_-th position and _X_<sub>_K_-1</sub> lies in the _j_-th position, and<tbc>

\(\theta_1=(X_1,X_2,X_3,\cdots,X_{K-1},\cdots,X_K,\cdots,X_{K-2}),\)

<tbc>where _X<sub>K</sub>_ lies in the _j_-th position and _X_<sub>_K_-1</sub> lies in the _i_-th position. Thus \(\text{MAX}(\theta_0)=i\), \(\text{MAX}(\theta_1)=j\). From Le Cam’s two point lemma, we know that

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\text{MAX}(\theta))\)<br>
\(\ge\frac{1}{2}(1-\text{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_1}))\)<br>
\(\ge\frac{1}{4}exp(-\mathbb{E}_{\theta_0}[T_{i,j}]\cdot D_\text{KL}(p\|1-p))\)<br>
\(\ge\frac{1}{4}\cdot exp\left(-\frac{2T\cdot D_\text{KL}(p\|1-p)}{K^2}\right).\)

On the other hand, _K_<sup>2</sup> is naturally a lower bound for the query complexity since one has to query each element at least once. Thus we arrive at a lower bound of \(\Omega(max(K^2,K^2log(1/\delta)/D_\text{KL}(p\|1-p)))\). Note that this is equivalent to \(\Omega(K^2/(1-H(p))+K^2log(1/\delta)/D_\text{KL}(p\|1-p))\) up to a constant factor when \(\delta<0.49\).


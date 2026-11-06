## B Missing Proofs from Section 3

First, let us first fix some notations. Given any two random variables _X_ and _Y_ , we will write _I(X:Y_) to denote the mutual information, _D_<sub>KL</sub>(_X:Y_) to denote the Kullback Leibler divergence, and \(\delta(X,Y)\) to denote the total variation distance between the random variables. We denote the Shannon entropy of a random variable _Z_ by _H(Z_).

**Lemma 1.** _For_ \(p\ge 1/k\)_, we have_ \(\ell(t,k,p)\ge(8loge)t(p-1/k)^2\).

_Proof._ Fix a protocol where the coordinator broadcasts \(\ell\) bits in the worst case. We will show that \(\ell\) must be large. Let _M(I_) be the (random) message that Alice sends to Bob based on her input _I_. Let \(S(I)=\langle S_1,S_2,\dots,S_t\rangle\) and \(u(I)=\langle u_1,u_2,\dots,u_t\rangle\). Then, _S(I_), _u(I_) and _M(I_) are random variables. Fix a value _S_ for _S(I_) and so that conditioned on "_S(I_)=_S_" the the probability of success is at least _p_ (such an _S_ must exist). Then,<tbc>

\(I[u(I):M(I)]=H[M(I)-H(M(I)|u(I))\le H(M(I))\le\mathbb{E}[|M(I)|]\le\ell.\)

<tbc>On the other hand, since _u_<sub>1</sub>_,u_<sub>2</sub>_,...,u<sub>t</sub>_ are independent (conditioned on "_S(I_)=_S_"), we have<tbc>

\(\ell\ge I[u(I):M(I)]\ge I[u_1:M(I)]+\cdots+I[u_t:M(I)],\)

<tbc>implying that<tbc>

\(\mathbb{E}_i\left[I[u_i:M(I)]\right]\le\frac{\ell}{t}.\)

<tbc>Let _u<sub>iz</sub>_ denote the random variable whose distribution is the same as that of _u<sub>i</sub>_ when conditioned on the event _M(I_)=_z_, and let the distance between the distributions of _u<sub>iz</sub>_ and _u<sub>i</sub>_ be<tbc>

\(\delta(u_{iz},u_i):=\sum_{w\in S_i}|Pr[u_{iz}=w]-Pr[u_i=w]|.\)

<tbc>Then, we have

\(I[u_i:M(I)]=\mathbb{E}_z\left[D_\mathrm{KL}(u_{iz}:u_i)\right]\text{(from definition)}\)<br>
\(\ge(2loge)\mathbb{E}_z\left[\left(\delta(u_{iz},u_i)\right)^2\right]\text{(by Pinsker’s inequality)}\)<br>
\(\ge(2loge)\left(\mathbb{E}_z\left[\delta(u_{iz},u_i)\right]\right)^2.\text{(by Jensen’s inequality)}\)

With one more application of Jensen’s inequality, we obtain the following<tbc>

\(\mathbb{E}_i\left[I[u_i:M(I)]\right]\ge(2loge)\mathbb{E}_i\left[\left(\mathbb{E}_z\left[\delta(u_{iz}:u_i)\right]\right)^2\right]\ge(2loge)\left(\mathbb{E}_i\left[\mathbb{E}_z\left[\delta(u_{iz}:u_i)\right]\right]\right)^2.\)

<tbc>Suppose Bob succeeds in guessing the special element of _S<sub>i</sub>_ with probability _p<sub>i</sub>_; then E_<sub>i</sub>_\[_p<sub>i</sub>_\]=_p_. Furthermore, we have \(\delta(u_{iz},u_i)\ge 2|p_i-1/k|\). Thus, by Jensen’s inequality, we have

\(\left(\mathbb{E}_i\left[\mathbb{E}_z\left[\delta(u_{iz}:u_i)\right]\right]\right)^2\ge 4(p-1/k)^2\)

It follows that \(\ell/t\ge(8loge)(p-1/k)^2\), that is, \(\ell\ge(8loge)t(p-1/k)^2\).


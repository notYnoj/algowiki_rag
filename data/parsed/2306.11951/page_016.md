<tbc>\(X^{(0)}\in(X_{i-1},X_i)\), and the second instance \(X^{(1)}\in(X_i,X_{i+1})\). From Le Cam’s two point lemma, we know that

\(inf_\hat{\mu}sup_X\mathbb{P}(\hat{\mu}\neq\mathsf{SEARCH}(X))\)<br>
\(\ge\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_{X^{(0)}},\mathbb{P}_{X^{(1)}}))\)<br>
\(\ge\frac{1}{4}exp(-\mathbb{E}[T_i]\cdot D_\mathsf{KL}(p\|1-p))\)<br>
\(\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

On the other hand, _K_ is naturally a lower bound for query complexity since one has to query each element at least once. Thus we arrive at a lower bound of \(\Omega(max(K,Klog(1/\delta)/D_\mathsf{KL}(p\|1-p)))\). □

## APPENDIX FPROOF FOR THEOREM V.1

_Proof._ From (Wang et al., 2023), it is proven with Fano’s inequality that<tbc>

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\ge\frac{1}{2}\cdot\left(1-\frac{T\cdot(1-H(p))}{Klog(K)}\right).\)

<tbc>So it suffices to prove that<tbc>

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

<tbc>To see this, consider an arbitrary sequence \(0<X_1<X_2<\cdots<X_K<1\). Now we design _K_ instances \(\theta_0,\cdots,\theta_{K-1}\). We let \(\theta_0=(X_1,\cdots,X_K)\), and \(\theta_l\) be the instance that switches the element _X<sub>l</sub>_ with _X_<sub>_l_+1</sub>, where \(l\in[K]\). From Le Cam’s two point lemma, we have

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{2}(1-\mathsf{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j}))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{4}exp(-D_\mathsf{KL}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_j}))\)<br>
\(\ge sup_{1\le j\le K-1}\frac{1}{4}exp(-\mathbb{E}_{\theta_0}[T_{j,j+1}]\cdot D_\mathsf{KL}(p\|1-p)).\)

Let _T<sub>i,j</sub>_ be the random variable that represents the number of comparisons between the _i_-th item and _j_-th item in the _T_ rounds. Now since \(\sum_{1\le j\le K-1}\mathbb{E}_{\theta_0}[T_{j,j+1}]\le T\), there must exists some _j_ such that \(\mathbb{E}_{\theta_0}[T_{j,j+1}]\le T/K\). This gives

\(inf_\hat{\mu}sup_{\theta\in[0,1]^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\ge\frac{1}{4}\cdot exp\left(-\frac{T\cdot D_\mathsf{KL}(p\|1-p)}{K}\right).\)

Altogether, this shows a lower bound on the query complexity \(\Omega(Klog(K)/(1-H(p))+Klog(1/\delta)/D_\mathsf{KL}(p\|1-p))\)). Note that this is equivalent to \(\Omega(Klog(K)/(1-H(p))+Klog(K/\delta)/D_\mathsf{KL}(p\|1-p))\) since \(1/(1-H(p))\unknown 1/D_\mathsf{KL}(p\|1-p)\). □

## APPENDIX GPROOF FOR THEOREM V.3

_Proof._ We first select an arbitrary sequence \(0<X_1<X_2<\cdots<X_K<1\). Let \(\sigma_i:[K]\mapsto[K]\) be the _i_-th permutation of the sequence, where \(i\in[K!]\). Here \(\sigma_i(k)\) refers to the _k_-th largest element under permutation


## 7 \((\alpha,\beta)\)-Approximate APSP

In Section 3, we showed the best known algorithm for (2,0)-multiplicative approximation on general graphs, as well as observed that \((\frac{7}{3},0)\)-approximation can be done in quadratic time, building on a quadratic (2,1)-approximation due to Baswana and Kavitha \[BK10\] and Berman and Kasiviswanathan \[BK07\]. Furthermore, it is well known that any \((2-\varepsilon,0)\)-approximation is as hard as Boolean Matrix Multiplication for any \(\varepsilon>0\), and therefore requires \(\Omega(n^\omega)\) time. However, it is possible to obtain \((\alpha,\beta)\) approximations for \(\alpha<2\) if we allow sufficient additive error \(\beta\). We will briefly describe the trade-off in this section.

### 7.1 \((\alpha,\beta)\)-Approximation for Unweighted Graphs

Since our algorithms on unweighted graphs generally provide additive guarantees, the limiting factors are the pairs of vertices with short distances. The following result shows the running time required to obtain an \((\alpha,\beta)\) approximation using our previous results for \(\alpha<2\).

**Theorem 7.1.** _Let_ \(\beta\ge 2\) _and_ \(1<\alpha<2\)_. Let_ \(T(\gamma)\) _denote the running time of Algorithm 7 when given approximation parameter_ \(\gamma\).

_Then, Algorithm 10 produces a_ \((\alpha,\beta)\)_-approximate_ \(\hat{\delta}\) _such that for all u,v,_<tbc>

\(\delta(u,v)\le\hat{\delta}(u,v)\le\alpha\delta(u,v)+\beta\)

<tbc>_in time_ \(\tilde{O}\left(T(\gamma)\right)\) _where_ \(\gamma\) _is the largest even integer satisfying,_

\(\gamma\le 1+\frac{\beta-1}{2-\alpha}\)

Before discussing the algorithm and proof, we give a high level overview and discuss our parameter choices.

### High Level Overview

Our goal in this section is to use our previous algorithms to obtain good bi-criteria approximations for the APSP Problem. The idea is that by increasing the tolerance for additive error, we can in fact obtain approximations where the multiplicative factor is less than 2.

The key component of our algorithm is running Algorithm 7. We will ensure small error on short paths by invoking **(2,1)-APASP** and ensure accuracy on long paths with **AdaptiveAPASP** (or alternatively **DenseAPASP**) since we can choose an arbitrary constant _k_ such that executing **AdaptiveAPASP** or **DenseAPASP** is not the computational bottleneck. The constant _C_ is chosen so that any path incurring the larger additive error _k_ is long enough to ensure that the multiplicative error component \(\alpha\) is small.

Why do we require \(\beta\ge 2\)? Let \(\gamma\) be the approximation parameter used in the invocation of Algorithm 7. Then for all paths of length \(\gamma-1\le\delta(u,v)\le C\), we obtain a \(+\gamma\) additive error. Therefore, for a fixed \(\beta\), the paths of length \(\gamma-1\) have the worst multiplicative error. Let _P_ be a path of length \(\gamma-1\). On such paths, we incur an error of \(\gamma\) and thus \(\hat{\delta}(u,v)\le 2\gamma-1\). If \(\beta=1\), then we must have \(\alpha\ge 2\), whereas we are interested in \(\alpha<2\). Thus, we require \(\beta\ge 2\) in the input of our algorithm.

As a sub-routine, we will require the (2,1)-approximation algorithm of Baswana and Kavitha \[BK10\] and Berman and Kasiviswanathan \[BK07\].

**Lemma 7.2.** _There is an algorithm **(2,1)-APASP** that runs in time_ \(\tilde{O}(n^2)\) _and outputs estimate_ \(\hat{\delta}\) _satisfying,_

\(\delta(u,v)\le\hat{\delta}(u,v)\le 2\delta(u,v)+1\)

_for all_ \(u,v\in V\) .


## 4 New Basic Tools

### 4.1 Basic Approximation Algorithm

Throughout this section we abbreviate _L=L(x,y_) and _M=M(x,y_). We start with the basic approximation algorithm that is central to our approach; most of our later algorithms use this as a subroutine. This algorithm subsamples the string _x_ and then runs Hunt and Szymanski’s algorithm (Theorem 2).

**Lemma 3** (Basic Approximation Algorithm)**.** _Let_ \(x,y\in\Sigma^n\)_. We can preprocess y in time_ \(\widetilde{O}(n)\)_. Given x, the preprocessed string y, and_ \(\beta\ge 1\)_, in expected time_ \(\widetilde{O}((n+M)/\beta+1)\) _we can compute a value_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_ \(\widetilde{L}>\frac{L}{\beta}-1\).

_Proof._ In the preprocessing phase, we run the preprocessing of Theorem 2 on _y_.

Fix a constant \(c\ge 1\). If \(\beta\ge 1/(8clogn)\), then in the query phase we simply run Theorem 2, solving LCS exactly in time \(\widetilde{O}(|x|+M)=\widetilde{O}((n+M)/\beta+1)\).

Otherwise, denote by \(x'\) a random subsequence of _x_, where each letter _x_\[_i_\] is removed independently with probability 1-_p_ (i.e., kept with probability _p_) for \(p:=8clog(n)/\beta\). Note that \(p\le 1\) by our assumption on \(\beta\). We can sample \(x'\) in expected time \(O(|x'|+1)\), since the difference from one unremoved letter to the next is geometrically distributed, and geometric random variates can be sampled in expected time _O_(1), see, e.g., \[18\]. Note that this subsampling yields \(\mathbb{E}[|x'|]=p|x|=\widetilde{O}(|x|/\beta)\) and \(\mathbb{E}[M(x',y)]=pM=\widetilde{O}(M/\beta)\).

In the query phase, we sample \(x'\) and then run the query phase of Theorem 2 on \(x'\) and _y_. This runs in time \(\widetilde{O}(|x'|+M(x',y)+1)\), which is \(\widetilde{O}((|x|+M)/\beta+1)\) in expectation.

Finally, consider a fixed LCS of _x_ and _y_, namely _z=x_\[_i_<sub>1</sub>\]_...x_\[_i<sub>L</sub>_\]=_y_\[_j_<sub>1</sub>\]_...y_\[_j<sub>L</sub>_\] for some _i_<sub>1</sub>_\<...\<i<sub>L</sub>_ and _j_<sub>1</sub>_\<...\<j<sub>L</sub>_. Each letter _x_\[_i<sub>k</sub>_\] survives the subsampling to \(x'\) with probability _p_. Therefore, we can bound \(L(x',y)\) from below by a binomial random variable Bin(_L,p_) (the correct terminology is that \(L(x',y)\) statistically dominates Bin(_L,p_)). Since _Z_=Bin(_L,p_) is a sum of independent {0,1}-variables, multiplicative Chernoff applies and yields \(Pr[Z<\mathbb{E}[Z]/2]\le exp(-\mathbb{E}[Z]/8)\). If \(L\ge\beta\) then \(\mathbb{E}[Z]=Lp\ge 2L/\beta\) and \(\mathbb{E}[Z]\ge 8clogn\), and thus \(Pr[L(x',y)\ge L/\beta]\ge 1-n^{-c}\). Otherwise, if \(L<\beta\), then we can only bound \(L(x',y)\ge 0\). In both cases, we have \(L(x',y)>L/\beta-1\) with high probability.

The above lemma behaves poorly if \(L\le\beta\), due to the "-1" in the approximation guarantee. We next show that this can be avoided, at the cost of increasing the running time by an additive \(\widetilde{O}(n)\).

**Lemma 4** (Generalised Basic Approximation Algorithm)**.** _Given_ \(x,y\in\Sigma^n\) _and_ \(\beta\ge 1\)_, in expected time_ \(\widetilde{O}(n+M/\beta)\) _we can compute a value_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_ \(\widetilde{L}\ge L/\beta\).

_Proof._ We run the basic approximation algorithm from Lemma 3, which computes a value \(\widetilde{L}\le L\). Additionally, we compute the number of matching pairs _M=M(x,y_) in time \(\widetilde{O}(n)\). If _M\>_0, then there exists a matching pair, which yields a common subsequence of length 1. Therefore, if _M\>_0 we set \(\widetilde{L}:=max\{\widetilde{L},1\}\).

In the proof of Lemma 3 we showed that if \(L\ge\beta\) then w.h.p. we have \(\widetilde{L}\ge L/\beta\). We now argue differently in the case \(L<\beta\). If _L_=0, then \(\widetilde{L}\ge 0=L/\beta\) and we are done. If \(0<L<\beta\), then there must exist at least one matching pair, so _M\>_0, so the second part of our algorithm yields \(\widetilde{L}\ge 1>L/\beta\). Hence, in all cases w.h.p. we have \(\widetilde{L}\ge L/\beta\).

We now turn towards the problem of deciding for given _x,y_ and \(\ell\) whether \(L(x,y)\ge\ell\). To this end, we repeatedly call the basic approximation algorithm with geometrically decreasing approximation ratio \(\beta\). Note that with decreasing approximation ratio we get a better approximation guarantee at the cost of higher running time. The idea is that if the LCS _L=L(x,y_) is much shorter than the threshold \(\ell\), then already approximation ratio \(\beta\approx\ell/L\) allows us to detect that \(L<\ell\). This yields a running time bound depending on the gap \(L/\ell\).

**Lemma 5** (Basic Decision Algorithm)**.** _Let_ \(x,y\in\Sigma^n\)_. We can preprocess y in time_ \(\widetilde{O}(n)\)_. Given x, the preprocessed y, and a number_ \(1\le\ell\le n\)_, in expected time_ \(\widetilde{O}((n+M)L/\ell+n/\ell)\) _we can w.h.p. correctly decide whether_ \(L\ge\ell\)_. Our algorithm has no false positives (and w.h.p. no false negatives)._


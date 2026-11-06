## B.2.4 Algorithm 3: Large L, Small \(\mu\), Large \(\lambda\)

**Algorithm 3** \[Theorem 15\] Large L, Small \(\mu\), Large \(\lambda(x,y,T,\hat{L},\hat{\lambda},\hat{\mu})\)

**Require:** Strings x,y of length n; parameter \(T\in[n,n^2]\) and parameters \(\hat{L},\hat{\lambda},\hat{\mu}\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of x,y with the guarantees of Theorem 15.

1: \(\mathcal{X}\leftarrow\{x_1,\dots,x_{n/m}\}\) where x<sub>i</sub>=x\[(i-1)m+1,im\]\}

2: \(\mathcal{Y}\leftarrow\{y_1,\dots,y_{n/m}\}\) where y<sub>i</sub>=y\[(i-1)m+1,im\]\}

3: \(\bar{L}\leftarrow 0\)

4: \(\alpha\leftarrow max\{1,\hat{\lambda}/(4T)\}\)

5: **for** \(log\alpha\le i\le logm\) **do**

6: \(g\leftarrow 2^i\)

7: \(\mathcal{S}\leftarrow\varnothing\)

8: \(p\leftarrow\frac{cgTm^2log^2n}{\hat{\lambda}n^2}\)

9: **for** \(i\in[n/m]\) **do**

10: **for** \(j\in[n/m]\) **do**

11: \(q\leftarrow 1\) with probability p and 0 otherwise

12: **if** q=1 **then**

13: \(f\leftarrow Query(x_i,y_j,g)\) of Algorithm 7

14: **if** f=1 **then**

15: \(\mathcal{S}\leftarrow\mathcal{S}\cup\{(i,j)\}\)

16: **if** \(\mathcal{S}\neq\varnothing\) **then**

17: \((i_0,j_0)\leftarrow\) select a block uniformly at random from S

18: \(d\leftarrow i_0-j_0\)

19: \(\mathcal{D}\leftarrow\{(i,j)\in[n/m]^2|i-j=d\}\)

20: \(\beta\leftarrow max\{1,\hat{\mu}/T\}\)

21: **for** \((i,j)\in\mathcal{D}\) **do**

22: \(\widetilde{L}_{ij}\leftarrow\) result of Algorithm 6 on \((x_i,y_j,\beta)\)

23: \(\widetilde{L}(g)\leftarrow\sum_{(i,j)\in\mathcal{D}}\widetilde{L}_{ij}\)

24: \(\bar{L}\leftarrow max\{\widetilde{L},\widetilde{L}(g)\}\)

25: \(\widetilde{L}\leftarrow\) repeat steps 5-24 for blogn times and compute the maximum of all \(\bar{L}\)

26: **return** \(\widetilde{L}\)


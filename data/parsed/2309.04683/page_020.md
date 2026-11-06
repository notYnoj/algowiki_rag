By induction hypothesis we know we are taking the minimum over all triangles (_v<sub>a</sub>,v<sub>b</sub>,v<sub>c</sub>_) such that

\((a,b,c)\in[1,i-n-1]\times[1,j-n]\times[n]\bigcup[1,i-n]\times[1,j-n-1]\times[n]\bigcup\{i-n\}\times\{j-n\}\times[n]\)<br>
\(=[1,i-n]\times[1,j-n]\times[n].\)

Therefore our claim is proved.

Now we show that \[Static\]2D LWS with slice rank 1 can be solved in truly sub-cubic time (which implies 2D LWS with slice rank 1 is also truly sub-cubic) but there is no truly sub-cubic algorithm for 2D LWS with slice rank 3 assuming APSP conjecture.

**Theorem 3.6.** \[Static\]2D LWS<sub>_n,N_</sub> _with slice rank_ 1 _can be solved in_ \(O(n^2\cdot N^{1-\varepsilon})\) _for some_ \(\varepsilon>0\).

_Proof._ The idea is similar to the proof of Theorem 3.4. We reduce \[Static\]2D LWS with slice rank 1 to \[Static\]LWS with rank 1, for which we know there exists an \(O(N^{1-\varepsilon}\cdot n)\) time algorithm.

Given an instance of \[Static\]2D LWS with slice rank 1, tensors _w_<sub>1</sub>_,w_<sub>2</sub>, there are 3 possibilities for _w_<sub>1</sub>:

• \(w_1[i,j,k]=f(i,k)\cdot g(j)\) for some _f,g_. In this case, we fix an \(i\in D_{a+N,a+2N}\) such that _w_<sub>1</sub>\[_i,j,k_\] becomes a matrix with rank 2. Now we can run \[Static\]LWS algorithm with rank 2 (at most _n_ times) to compute<tbc>

<tbc>\(min_{1\le k^\prime<j^\prime}\left\{T[i,k']+w_1[i,j',k']\right\}\)<tbc>

<tbc>for all \((i,j')\in D_{a+N,a+2N}\) in time \(O(N^{1-\varepsilon} n)\) for some \(\varepsilon>0\). Doing this for all _i_, we can compute<tbc>

<tbc>\(min_{1\le k<j}\left\{T[i,k]+w_1[i,j,k]\right\}\)<tbc>

<tbc>for all \((i,j)\in D_{a+N,a+2N}\) in time at most \(O(N^{1-\varepsilon}\cdot n^2)\).<tbc>

• \(w_1[i,j,k]=f(i,j)\cdot g(k)\) for some _f,g_. This is similar to the previous case but instead of fixing _i_, we fix _j_. Similarly, we can compute<tbc>

<tbc>\(min_{1\le k<j}\left\{T[i,k]+w_1[i,j,k]\right\}\)<tbc>

<tbc>for all \((i,j)\in D_{a+N,a+2N}\) in time \(O(N^{1-\varepsilon}\cdot n^2)\).<tbc>

• \(w_1[i,j,k]=f(j,k)\cdot g(i)\) for some _f,g_. Again we can run \[Static\]LWS for each _j_ and compute<tbc>

<tbc>\(min_{1\le k<j}\left\{T[i,k]+w_1[i,j,k]\right\}\)<tbc>

<tbc>for all \((i,j)\in D_{a+N,a+2N}\) in time \(O(N^{1-\varepsilon}\cdot n^2)\).<tbc>

<tbc>The analysis for _w_<sub>2</sub>\[_i,j,k_\] is the same, and thus we can compute<tbc>

<tbc>\(min_{1\le k<i}\left\{T[k,j]+w_2[i,j,k]\right\}\)<tbc>

<tbc>for all \((i,j)\in D_{a+N,a+2N}\) in time \(O(N^{1-\varepsilon}\cdot n^2)\). Finally take the pairwise minimum to give

\(min\left\{min_{1\le k<j}\left\{T[i,k]+w_1[i,j,k]\right\},min_{1\le k<i}\left\{T[k,j]+w_2[i,j,k]\right\}\right\}\)

for all \((i,j)\in D_{a+N,a+2N}\).

**Theorem 3.7.** 2D LWS _with slice rank 1 is truly sub-cubic._

_Proof._ Immediately follows from Theorem 3.6 and the fact that our reduction from 2D LWS to \[Static\]2D LWS in Theorem 3.2 preserves slice rank.


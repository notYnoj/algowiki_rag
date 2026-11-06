<tbc>Given this partition, again using the same procedure as in Lemma 4.3, we can find disjoint substrings of _X<sub>i</sub>_, _X<sub>i,j</sub>_, for all _i\>_1 such that each _X<sub>i,j</sub>_ has length at most \(2\tau/\epsilon_{m+1}^2\) and<tbc>

\(\sum_{j\in[J]}\delta_E(X_{i,j},X_j^*)+|X_i|-\sum_{j\in[J]}|X_{i,j}|\le(1+3\epsilon_{m+1})v[i]\le v[i]+6\epsilon_{m+1}d.\)

<tbc>Now, let _W_<sub>1_,j_</sub>=_X_<sub>1_,j_</sub> for all _j_. Similarly to Lemma 4.5, for each _i_, if \(|X_{i,j}|\le 2\epsilon_{m+1}max_{i^\prime}\delta_E(X_{i^\prime,j},X_j^*)+6\epsilon_{m+1}D\tau_{m+1}/|X_1|\), let _W<sub>i,j</sub>_ be the empty window "starting" at index e(_W_<sub>_i,j_-1</sub>)+1 (or index 1 if _j_=1). Otherwise, let _W<sub>i,j</sub>_ be the longest window \(W_{i,m+1,\Delta,p}\) that is a substring of _X<sub>i,j</sub>_. Note that |_X<sub>i,j</sub>_| and |_W<sub>i,j</sub>_| differ by at most \(2max_{i^\prime}\delta_E(X_{i^\prime,j},X_j^*)\). If \(\epsilon_{m+1}\) is a sufficiently small constant, similarly to the proof of Lemma 4.5, this implies there is a choice of _W<sub>i,j</sub>_ such that \(|X_{i,j}|-|W_{i,j}|\le\epsilon_{m+1}max_{i^\prime}\delta_E(X_{i^\prime,j},X_j^*)+3(\sigma_m(d)-1)\le\epsilon_{m+1}max_{i^\prime}\delta_E(X_{i^\prime,j},X_j^*)+6[\frac{\epsilon_{m+1}d\tau_{m+1}}{\tau_m}+\frac{\epsilon_{m+1}D\tau_{m+1}}{|X_1|}]\). Note that \(\sum_{j\in[J]}max_i\delta_E(X_{i,j},X_j^*)\le k\left\|v\right\|_\infty\le 2kd\). This implies \(r_i(f)-(|X_i|-\sum_{j\in[J]}|X_{i,j}|)\) is at most \(5\epsilon_{m+1}kd\). We also have by triangle inequality that:<tbc>

\(\delta_E(W_{i,j},X_j^*)\le\delta_E(X_{i,j},X_j^*)+\epsilon max_{i^\prime}\delta_E(X_{i^\prime,j},X_j^*)+6[\frac{\epsilon_{m+1}d\tau_{m+1}}{\tau_m}+\frac{\epsilon_{m+1}D\tau_{m+1}}{|X_1|}].\)

<tbc>Now consider the alignment that chooses _f(W_<sub>1_,j_</sub>)=(_W_<sub>1_,j_</sub>_,W_<sub>2_,j_</sub>_,...,W<sub>k,j</sub>_). For each _j_, by the above inequalities, one edit tuple for _f(W_<sub>1_,j_</sub>)=(_W_<sub>1_,j_</sub>_,W_<sub>2_,j_</sub>_,...,W<sub>k,j</sub>_) arising from a window-respecting alignment is element-wise at most:

\((\delta_E(X_{1,j},X_j^*),\)<br>
\(\delta_E(X_{2,j},X_j^*)+\epsilon_{m+1}max_i\delta_E(X_{i,j},X_j^*)+6[\frac{\epsilon_{m+1}d\tau_{m+1}}{\tau_m}+\frac{\epsilon_{m+1}D\tau_{m+1}}{|X_1|}],\)<br>
\(\cdots,\)<br>
\(\delta_E(X_{k,j},X_j^*)+\epsilon_{m+1}max_i\delta_E(X_{i,j},X_j^*)+6[\frac{\epsilon_{m+1}d\tau_{m+1}}{\tau_m}+\frac{\epsilon_{m+1}D\tau_{m+1}}{|X_1|}])\)

So summing up these edit tuples, and adding _r(f_), we get a vector arising from a window-respecting alignment that is at element-wise at most \(v+(\epsilon_{m+1}k\left\|v\right\|_\infty+11\epsilon_{m+1}kd+6\epsilon_{m+1}D\tau_m/|X_1|)\cdot\mathbf{1}\le v+(13\epsilon_{m+1}kd+6\epsilon_{m+1}D\tau_m/|X_1|)\cdot\mathbf{1}\).

We are now ready to state our algorithm. Our recursive algorithm for computing a sparse approximation of `tup`_<sub>D</sub>(X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>k</sub>_), denoted _k_-CED-Alg, is defined as follows:

\(k\text{-CED-Alg}(X'_1,X'_2,\dots,X'_k,d,m)\text{:}\)<br>
\(\text{Let}\mathcal{W}_i\text{denote the windows at level}m+1\text{parametrized by}d\text{restricted to}X'_1,X'_2,\dots,X'_k\text{, and}\)<br>
\(\text{s,e}\text{be the functions that take a window and gives its starting/ending index in the corresponding}X'_i\text{. We solve the following dynamic program:}\)<br>
\(c(x_1,x_2,\dots x_k)=(\cup_{i>1}c(x_1,x_2,\dots,x_i-\sigma_{m+1},\dots,x_k)\circledast\{(0,0,\dots,\sigma_{m+1},\dots,0)\})\cup\)<br>
\((\cup_{W_1,W_2,\dots W_k\in\mathcal{W}_1\times\mathcal{W}_2\times\cdots\times\mathcal{W}_k:\forall i,\text{e}(W_i)=x_i}[c(\text{s}(W_1)-1,\text{s}(W_2)-1,\dots,\text{s}(W_k)-1)\)<br>
\(\circledast\cup_{d^\prime\in\mathcal{D}:d^\prime\le 2}k\text{-CED-Alg}(W_1,W_2,\dots,W_k,d',m+1)])\)

For every _k_-tuple such that _x_<sub>1</sub> is a multiple of \(\tau_{m+1}\), _x_<sub>2</sub>_,...,x<sub>k</sub>_ are all multiples of \(\sigma_{m+1}\), and such that \(|x_i-x_1|\le 3d+\frac{\epsilon_mD\tau_m}{|X_1|}\) . The base case for the dynamic program is _c_(0,0_,...,_0)={(0,0_,...,_0)}.

After computing each entry _c(x_<sub>1</sub>_,x_<sub>2</sub>_,...x<sub>k</sub>_), we remove all elements of _c(x_<sub>1</sub>_,x_<sub>2</sub>_,...x<sub>k</sub>_) not in \(\{0,1,\dots 3d+\lfloor\frac{\epsilon_mD\tau_m}{|X_1|}\rfloor\}^k\). After getting a set of edit tuples from a call to _k_-CED-Alg, we round each coordinate of each vector up to the nearest multiple of \(\sigma_m(d)\) before taking the convolution.

Our final output is \(c(|X'_1|,|X'_2|,\dots,|X'_k|)\), and then return this set of vectors.

Our base case will be when \(m=\ell\), and we have that \(|X'_1|=N^{1/loglogN}\) and all \(|X'_i|\) are at most \(2N^{1/loglogN}/\epsilon_\ell^2\). To handle the base case, we will enumerate all substrings of length at most \(2N^{1/loglogN}/\epsilon_\ell^2\) of each of _X_<sub>1</sub>_,...,X<sub>k</sub>_, and compute their edit tuples using, e.g., the exact algorithm of \[NR05\]. Our top-level recursive call is to _k_-CED-Alg(_X_<sub>1</sub>_,...,X<sub>k</sub>,D,_0).

To keep the algorithm’s description consistent across levels, in addition to assuming _X_<sub>1</sub>’s length is a multiple of \(\tau_1\), we will assume that _X_<sub>2</sub>_,...,X<sub>k</sub>_ are multiples of \(\sigma_1(D)\); we can enforce this assumption<tbc>


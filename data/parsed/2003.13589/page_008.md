consisting of rare elements, we have O(_c_) fragments. We maintain the _dp<sub>v</sub>_ table as in the first solution, but we only update it after having processed a whole fragment. So, when considering a fragment starting at \(\sigma[v]\) we only assume that the values of _dp_<sub>_v_-1</sub> can be access in constant time. For a fragment consisting of a single frequent element, we proceed exactly as in the first solution. In the remaining part of the description we describe how to process a fragment consisting of rare elements \(\sigma[v],\sigma[v+1],\dots\).

We consider all \(\sigma[v']\)-pairs, for \(v'=v,v+1,\dots\). We will compute \(LCIS^\rightarrow(x,y)\) for each such matching pair (_x,y_), and store it in the appropriate structure _D(r_) implemented as described in Lemma 4.1. To compute the values of \(LCIS^\rightarrow(x,y)\) for all \(\sigma[v']\)-pairs, we use parallel binary search as in the second solution with the following modification. To check if \(LCIS^\rightarrow(x,y_i)>r\), we need to consider two possibilities for the corresponding sequence _C_ ending at \(A[x]=B[y_i]=\sigma[v']\):

1. If _C_\[|_C_|-1\] belongs to the same fragment then it is enough to check if _D(r_) contains a pair \((x',y')\) with \(x'<x\) and \(y'<y_i\).<tbc>

2. Otherwise, it is enough to check if \(dp_{v-1}[x][y_i]\ge r\).

Additionally, after having found \(c'\) we need to keep decreasing _i_ as long as \(i\ge 1\) and the answer for (_x,y<sub>i</sub>_) is \(c'\), and this needs to be tested in constant time per each such _i_. We again need to consider two possibilities, and either compare _y<sub>i</sub>_ with the value of \(y'\) found by querying \(D(c'-1)\) with _x_, or test if \(dp_{v-1}[x][y_i]\ge r\) in constant time. Overall, this incurs only additional constant time per every step of the binary search for every considered matching pair.

After having considered all \(\sigma[v']\)-pairs for the last element \(\sigma[v']\) in the current fragment, we need to compute \(dp_{v^\prime}\) from _dp_<sub>_v_-1</sub> and the calculated values of \(LCIS^\rightarrow\). Of course, we want to operate on \(dp'_{v^\prime}\) and \(dp'_{v-1}\) instead of \(dp_{v^\prime}\) and _dp_<sub>_v_-1</sub>. This is done row-by-row. The _i_-th row is computed in two steps.

First, we need to set \(dp_{v^\prime}[i][j]=max\{dp_{v^\prime}[i-1][j],dp_{v-1}[i][j]\}\) for every _j_=1,2_,...,n_. This is done by processing whole blocks in constant time and precomputing the result for every possible combination of the following information:

1. \(dp'_{v^\prime}[i-1][j],dp'_{v^\prime}[i-1][j+1],\dots,dp'_{v^\prime}[i-1][j+B-1]\),<tbc>

2. \(dp'_{v-1}[i][j],dp'_{v-1}[i][j+1],\dots,dp'_{v-1}[i][j+B-1]\),<tbc>

3. \(dp_{v^\prime}[i-1][j-1]\),<tbc>

4. _dp_<sub>_v_-1</sub>\[_i_\]\[_j_-1\].

This can be preprocessed in \(\mathcal{O}(4^B\cdot B^2)\) time after observing that, as in the first solution, only the difference \(dp_{v^\prime}[i-1][j-1]-dp_{v-1}[i][j-1]\) is relevant and, additionally, it can be capped at _B_ (if it is bigger than _B_ then we can set it to _B_). The time is O(_n/B_).

Second, we need to consider the values of \(LCIS^\rightarrow(i,j)\) computed for the current fragment. If the result computed for a matching pair (_i,j_) is _r_ then we need to update \(dp_v[i][j']=max\{dp_v[i][j'],r\}\), for every \(j'\ge j\). This can be done by simultaneously scanning all such _js_ and the blocks. By maintaining the maximum _r_, we can update the value of _dp<sub>v</sub>_\[_i_\]\[_j_\] at the beginning of the block. Then, we consider all other \(j'\)s belonging to the same block, and consider its corresponding result \(r'\). If \(dp_v[i][j']\ge r'\) then this result is irrelevant, and otherwise we must increase some of the values in the block by 1 (as \(dp_v[i][j'-1]\) is assumed to have been already updated and due to Lemma 3.1). As in the first solution, this is implemented by setting \(dp'_v[i][j']=1\) and changing the nearest 1 into 0. Overall, the time is bounded by the number of considered matching pairs plus additional O(_n/B_) time.


<tbc>Algorithm 1 zSort(_arr_\[\], _output_\[\]_,size_)

1: \(sum\leftarrow arr[0],min\leftarrow sum,a\leftarrow 1,d\leftarrow 1\)

2: for _i_=1 _to size_-1 do

3: \(curr\leftarrow arr[i]\)

4: _sum_+=_curr_

5: \(min\leftarrow curr<min?curr:min\)

6: end for

7: \(mean\leftarrow sum/size\)

8: if (_min_==_mean_) then

9: \(returnoutput\leftarrow arr\)

10: end if

11: _var_=0

12: for _i_=0 _to size_-1 do

13: \(res\leftarrow arr[i]mean\)

14: \(var\leftarrow var+res*res\)

15: end for

16: \(std\leftarrow sqrt(var/size)\);

17: \(Zmin\leftarrow|\frac{min-mean}{std}|\)

18: \(clusters\leftarrow sqrt(size)\)

19: \(scale\leftarrow clusters/4\)

20: _counts_\[_clusters_\], _offsets_\[_clusters_\], _clustersArr_\[_size_\]

21: for _i_=0 _to size_-1 do

22: \(b\leftarrow h(arr[i])\)

23: _counts_\[_b_\]++

24: end for

25: _countSum_=0

26: for _i_=0 _to clusters_-1 do

27: _offsets_\[_i_\]=_countSum_

28: \(countSum\leftarrow countSum+counts[i]\)

29: end for

30: for _i_=0 _to size_-1 do

31: \(b\leftarrow h(arr[i])\)

32: _clustersArr_\[_offsets_\[_b_\]++\]

33: end for

34: _lbSum_=0

35: for _i_=0 _to clusters_-1 do

36: _totalElements_=_counts_\[_i_\]

37: if (_totalElements\>_0) then

38: if (_totalElements\>_96) then

39: \(meanEst\leftarrow(((\frac{i+0.5}{scale}-zmin)*std)+mean)\)

40: _zsortRec(clustersArr,output,lbSum,totalElements,clusters,scale,meanEst_

41: else

42: _InsertionSort(clustersArr,output,lbSum,totalElements)_

43: end if

44: _lbSum_+=_totalElements_

45: end if

46: end for

itself. The reduced memory footprint of the cluster array likely results in fewer TLB (Translation Lookaside Buffer)<tbc>

<tbc>misses.

## A. Complexity Analysis

1) Worst Case: Let algorithm operates on input size _n_. The partition step takes _O(n_) time. Algorithm divides the input into \(k=\sqrt{n}\) parts in each level. Here, _k_ is computed from original input size _n_ and remain fixed throughout recursion. Subproblems of size \(\le t\) (Here, \(t\le 96\)) are solved in _O_(1). Therefore, the classical recurrence is given by,<tbc>

\(T(n)=kT(\frac{n}{k})+n\)

<tbc>As branching factor _k_ does not depend on current subproblem size, the depth behavior changes fundamentally. Also size of each partition \(\neq\frac{n}{k}\) due to skewness. Let subproblem sizes after partition be - _n_<sub>1</sub>_,n_<sub>2</sub>_,...,n<sub>k</sub>_ such that \(\sum_{i=1}^kn_i=n\). Thus the recurrence now have following form,

\(T(n)=\sum_{i=1}^kT(n_i)+cn\)

, where \(k=\sqrt{n}\) is fixed across recursion levels.<br>
Worst Case recursion Depth (_d_): We know that at every level, \(\sum n_i=n\), so work per level \(=\Theta(n)\) - irrespective of the skewness. Consider the worst case where one partition receives almost all the elements and remaining partitions contain a few elements (which can be considered as constant). Thus, at level 1, this partition _n<sub>i</sub>_ will have _n-O_(1) elements. At next level 2, this is again divided into \(k=\sqrt{n}\) parts. Maximum size partition at this level will have \(\le\frac{n}{\sqrt{n}}\le\sqrt{n}\) elements. Finally, at level 3, this is again divided in \(\sqrt{n}\) part. Therefore, maximum size partition after level \(3\le\frac{\sqrt{n}}{\sqrt{n}}=1\). Thus recursion depth (\(d\le 3\)). More precisely, \(d\le\lceil\frac{logn}{log\sqrt{n}}\rceil=\lceil 2\rceil\), which is constant. Thus, total cost,

\(T(n)=\sum_{i=0}^dcn\le cn+cn+cn\le 3cn=\Theta(n)\)

General Proof: Let \(k=n^\beta\), where \(0<\beta<1\). At level 1, largest size \(\le\frac{n}{n^\beta}=n^{1-\beta}\). Therefore, after _j<sup>th</sup>_ level, when recurrence stops, largest size partition will be \(n^{1-j^\beta}\le 1\). Taking log on both sides,

\(\Longrightarrow 1-j\beta=0\Longrightarrow j\ge\frac{1}{\beta}\Longrightarrow j=O(\frac{1}{\beta})\)

Thus for any value of \(0<\beta<1\), depth (_j_) will be always constant.

\begin{tabular}{ccc}
Scaling Factor (\(\alpha\)) & Avg. Execution Time (ms) & Relative Performance \\
1.2 & 258.83 & -17.40% \\
1 & 240.8 & Baseline \\
0.8 & 214.37 & 10.90% \\
0.6 & 213.73 & 11.20% \\
0.4 & 224.32 & 6.80% \\
\end{tabular}

TABLE II

Sensitivity Analysis for \(\alpha\)


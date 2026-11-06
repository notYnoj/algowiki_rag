**Algorithm 1** Calculate the _i_-th row of \(dp'_{v+1}\)

procedure CalculateRow(_v,i_)<br>
   \(ptr\leftarrow 1\)<br>
   \(cur\text{\_}value\leftarrow 0\)<br>
   \(prv\text{\_}value\leftarrow 0\)<br>
   \(prv\text{\_}phase\leftarrow 0\)<br>
   for j=1..n do<br>
   \(dp'_{v+1}[i][j]=dp'_v[i][j]\)<br>
   for j=1..n do<br>
   if \(ptr\le i\) then \(ptr\leftarrow i+1\)<br>
   while \(ptr\le n\) and \(dp'_{v+1}[i][ptr]=0\) do<br>
   \(ptr\leftarrow ptr+1\)<br>
   \(cur\text{\_}value\leftarrowcur\text{\_}value+dp'_{v+1}[i][j]\)<br>
   \(\trianglerightcur\text{\_}value=\sum_{j^\prime=1}^jdp'_{v+1}[i][j']=max\{dp_v[i][j],dp_{v+1}[i][j-1]\}\)<br>
   \(\trianglerightprv\text{\_}phase=dp_v[i-1][j-1]\)<br>
   if \(A[i]=B[j]=\sigma[v+1]\) and cur\_value=prv\_phase then<br>
   \(dp'_{v+1}[i][j]\leftarrow 1\)<br>
   \(cur\text{\_}value\leftarrowcur\text{\_}value+1\)<br>
   if \(ptr\le n\) then \(dp'_{v+1}[i][ptr]\leftarrow 0\)<br>
   \(prv\text{\_}phase\leftarrow prv\text{\_}phase+dp'_v[i-1][j]\)<br>
   \(prv\text{\_}value\leftarrow prv\text{\_}value+dp'_{v+1}[i-1][j]\)<br>
   \(\trianglerightprv\text{\_}value=dp_{v+1}[i-1][j]\)<br>
   if cur\_value\<prv\_value then<br>
   \(cur\text{\_}value\leftarrow prv\text{\_}value\)<br>
   \(dp'_{v+1}[i][j]\leftarrow 1\)<br>
   if \(ptr\le n\) then \(dp'_{v+1}[i][ptr]\leftarrow 0\)

We speed up Algorithm 1 by a factor of _B_ by considering whole blocks of \(dp'_{v+1}\) instead of single entries. Consider a single block of \(dp'_{v+1}\) consisting of the values of \(dp'_{v+1}[i][j],dp'_{v+1}[i][j+1],\dots,dp'_{v+1}[i][j+B-1]\), and assume that they have been already partially updated by propagating the maximum. To calculate their correct values we need the following information:

1. \(dp'_v[i-1][j],dp'_v[i-1][j+1],\dots,dp'_v[i-1][j+B-1]\),<tbc>

2. \(dp'_{v+1}[i-1][j],dp'_{v+1}[i-1][j+1],\dots,dp'_{v+1}[i-1][j+B-1]\),<tbc>

3. \(dp'_{v+1}[i][j],dp'_{v+1}[i][j+1],\dots,dp'_{v+1}[i][j+B-1]\),<tbc>

4. _dp<sub>v</sub>_[i-1][_j_-1],<tbc>

5. _dp_<sub>_v_+1</sub>[_i_-1][_j_-1],<tbc>

6. _dp_<sub>_v_+1</sub>[_i_][_j_-1],<tbc>

7. for which indices _j,j_+1_,...,j+B_-1 we have \(A[i]=B[j]=\sigma[v+1]\).

In fact, we can rewrite the procedure so that instead of the values _dp<sub>v</sub>_[_i_-1][_j_-1], _dp_<sub>_v_+1</sub>[_i_-1][_j_-1], _dp_<sub>_v_+1</sub>[_i_][_j_-1] only the differences _dp_<sub>_v_+1</sub>[_i_-1][_j_-1]-_dp<sub>v</sub>_[_i_-1][_j_-1] and _dp_<sub>_v_+1</sub>[_i_][_j_-1]-_dp_<sub>_v_+1</sub>[_i_-1][_j_-1] are needed. By Lemma 3.1 and Lemma 3.2, both differences belong to {0,1}, so the whole<tbc>


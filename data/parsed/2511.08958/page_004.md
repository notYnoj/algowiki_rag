<tbc>Orthogonal range maxima and coordinate compression are standard techniques \[7\]. The implementation below uses nested Fenwick trees, extending the prefix-aggregation idea \[8\] to maximum values with witnesses. No improvement to these data structures is asserted. On the complexity side, Duraj, Künnemann, and Polak \[1\] rule out strongly subquadratic LCIS algorithms under SETH. This is compatible with logarithmic savings in the exponent-two regime, such as the LCIS algorithms of Duraj \[9\] and Agrawal and Gawrychowski \[10\]; strongly subquadratic means \(O(N^{2-\varepsilon})\) for a fixed \(\varepsilon>0\).

## 3. Match states and peak decomposition

A match _v_=(_i,j_) has value _a(v_)=_A_\[_i_\]=_B_\[_j_\]. Write \(u\prec v\) if both coordinates of _u_ are strictly smaller than the corresponding coordinates of _v_. A chain under \(\prec\) is an embedded common subsequence. The endpoint lengths satisfy

\(I(v)=1+max\{I(u):u\prec v,a(u)<a(v)\},\) (3)

\(D(v)=1+max\{D(w):v\prec w,a(w)<a(v)\},\) (4)

where maxima over empty sets are zero. Removing the last element of an increasing chain, or the first element of a decreasing chain, proves these recurrences in both directions. A witness attaining the maximum is retained as a predecessor or successor pointer; a singleton has a null pointer.

Figure 1 illustrates these states for \(A=\langle 2,1,3,4,6,5,4\rangle\) and \(B=\langle 1,2,3,5,6,4\rangle\). The highlighted witness \(\langle 1,3,5,4\rangle\) joins an increasing prefix of length three to a decreasing suffix of length two at the same match _v_=(6,4), giving _I(v_)+_D(v_)-1=4. The arrows move forward in both input orders even when the selected values decrease after the peak.

j
1
2
3
4
5
6
B[j]
1
2
3
5
6
4
i
A[i]
One optimal witness
1
2
(1,3, 5, 4)
peak
2
1
Increasing prefix
3
3
Decreasing suffix
4
4
Other match
5
6
v = (6,4)
I(v) = 3, D(v) = 2
6
5
I(v) + D(v) 1 = 4
7
4
The shared peak is counted once.

Figure 1. Match-grid view of an LCBS. Columns list _B_ and rows list _A_, with row indices increasing downward. Every node is an equality match. Solid arrows trace the increasing prefix; the dashed arrow traces the decreasing suffix. The diamond marks their shared peak, whose value is five. Unselected matches are hollow circles.


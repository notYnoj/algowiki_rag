**Theorem 2.** _Given an array, A, of size n, and a stack-based natural mergesort algorithm,_ S_, which is almost-k-aware for constant_ \(k\ge 2\)_, we can implement A in-place in O(n_(1+H(_A_))+_T_<sub>S</sub>(_n_)) _time, where T_<sub>S</sub>(_n_) _is the running time of_ S.

## 5 Our Bit Encoding Methods

In this section, we describe our methods for encoding run sizes in-place in the runs themselves. Unlike previous encoding methods, such as those of Kuszmaul and Westover \[19\], our methods make no assumptions about the elements and their representation themselves, except that they are comparable and copyable. Recall that we define \(\lambda=\lceil\mathrm{log}n\rceil+1\). We do so because the size of each run can be represented using \(\lceil\mathrm{log}n\rceil\) bits, along with one extra bit to specify the encoding method used. More specifically, let \(b_1b_2\dots b_{\lceil\mathrm{log}n\rceil}\) be a binary encoding of the size, _r_, of a _long_ run, _R_, and let \(b_\lambda\) indicate the encoding method used, i.e., \(b_\lambda=0\) for the **_pivot-encoding_** method and \(b_\lambda=1\) for the **_marker-encoding_** method. Both of our methods efficiently encode **_b_** in-place within the run, _R_.

#### Our Pivot-Encoding Method.

Our first encoding method is a simple encoding method we call the **_pivot-encoding_** method. Let _R_ be a _long_ run, and let _F_ and _L_ be the first and last \(\lambda\) elements in _R_, respectively. Also, let _p_ be the element of _R_ that is immediately before _L_, which we call the **_pivot_** (i.e., _p_ is the element \(\lambda+1\) cells from the end of _R_). We say that the run _R_ is **_pivotable_** if the last element of _F_, \(F_\ell\), is strictly smaller than our pivot, _p_. See Figure 7.

Suppose then that _R_ is pivotable, which implies that each element in _F_ is strictly smaller than every element in _L_ and _p_. Encoding **_b_** in our pivot-encoding scheme is easy: We consider each element, _L_\[_i_\], of _L_ as corresponding to the bit, _b<sub>i</sub>_, and, if _b<sub>i</sub>_=0, then we swap _L_\[_i_\] and _F_\[_i_\]. Thus, if _L_\[_i_\]_\<p_, we know that _b<sub>i</sub>_=0, and if \(L[i]\ge p\), then we know that _b<sub>i</sub>_=1. See Figure 8. Encoding, reading, and reversing such an encoding can be done in _O_(log_n_) time.

#### Our Marker-Encoding Method.

For a long run, _R_, not to be pivotable, i.e., \(F_\ell\ge p\), it must be true that not only \(F_\ell=p\), but also that the entirety of the elements between _F_ and _L_, denoted _M_, are equal to _p_. In this case, our pivot- encoding method does not work, and we use a different encoding method, which we call the **_marker-encoding_** method.

F
L
F
p

Fig.7: Here we depict the test to determine whether a run is **_pivotable_**. We define _F_ and _L_ as the first and last \(\lambda\) cells of the run. Our pivot _p_ is the element just prior to _L_ and \(F_\ell\) is the last element of _F_. This run is pivotable if \(F_\ell<p\).


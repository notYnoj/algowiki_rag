<tbc>For our marker-encoding method, we designate the first two distinct elements encountered as **_markers_**, denoting them _m_<sub>1</sub> and _m_<sub>2</sub>, where _m_<sub>1</sub>_\<m_<sub>2</sub>, and store them using _O_(1) memory. These markers are in fact derived from the first run itself, since each run must contain at least two distinct elements.

Since _R_ is not pivotable, we know that \(F_\ell=p\), and thus all elements in _M_ are equal to _p_. First, we store a copy of _L_ in the first \(\lambda\) cells of _M_. Next, we encode **_b_** in _L_ using only our two markers, letting _L_\[_i_\] correspond to the bit _b<sub>i</sub>_, and, if _b<sub>i</sub>_=0, then we set \(L[i]\leftarrow m_1\) and if _b<sub>i</sub>_=1, then we set \(L[i]\leftarrow m_2\). Finally, we set the pivot value _p_ to _m_<sub>2</sub>. Reading this encoding is identical to how the pivot-encoding method is read, since it is still true that if _L_\[_i_\]_\<p_, then _b<sub>i</sub>_=0 and if \(L[i]\ge p\), then _b<sub>i</sub>_=1. After the encoding is read and we must reverse the encoding, we simply set _L_ back to its original values using its copy in _M_, and then we clean up _M_ by copying \(F_\ell\) into its first \(\lambda\) elements and into the original pivot location, _p_. See Figure 9.

## 6 Conclusion

We have shown how to implement stack-based natural mergesort algorithms to be strictly in-place and retain their original asymptotic running times, including showing that several such algorithms, but not all, can be implemented to be strictly in-place using a simple walk-back algorithm. Our bit-encoding methods in our jump-back are immutable, in that they do not require modifying any bits of any elements, unlike previous encoding methods.

## References


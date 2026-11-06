### 6.2 Second solution

Calculating the result for each \(\sigma[v]\)-pair consists of two phases. In the first phase, for each \(\sigma[v]\)-pair (_x,y_), we calculate the result assuming that all previous elements in the subsequence are strictly smaller than \(\sigma[v]\). In the second phase, we calculate the result assuming that the previous element is also equal to \(\sigma[v]\). The first phase can be implemented exactly as for LCIS in O(cnt(_v_)<sup>2</sup>(1+log<sup>2</sup>(_n/_cnt(_v_)))) time. We now focus on explaining how to implement the second phase. Let prev_<sub>A</sub>_\[_x_\] denote the greatest \(x'\) fulfilling \(A[x']=A[x]\), if there is no such then prev_<sub>A</sub>_\[_x_\]=0. Similarly we define prev_<sub>B</sub>_\[_y_\], both array can be prepared in negligible O(_n_log_n_) time.

We analyze all \(\sigma[v]\)-pairs in the increasing order of rows and columns. Consequently, when analysing a pair (_x,y_), for all other \(\sigma[v]\)-pairs with \(x'\le x\), \(y'\le y\) we have already correctly calculated \(LCWIS\unknown(x',y')\). The proof of Lemma 4.4 still holds for LCWIS, and implies that among all other \(\sigma[v]\)-pairs \((x',y')\) such that \(x'\le x\) and \(y'\le y\) the pair (prev_<sub>A</sub>_\[_x_\],prev_<sub>B</sub>_\[_y_\]) has the largest result. We can calculate \(LCWIS\unknown(x,y)\) as the maximum of the result computed in first phase and \(LCWIS\unknown(\text{prev}_A[x],\text{prev}_B[y])+1\).

The second phase takes only O(cnt(_v_)<sup>2</sup>) time, so the overall complexity remains O(cnt(_v_)<sup>2</sup>(1+log<sup>2</sup>(_n/_cnt(_v_)))).

## 7 Conclusions

The \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) complexity doesn’t seem to be right answer yet, at least for LCIS. It seems to us that one can apply the combinatorial bound of Duraj on the number of significant pairs, and combine it with our approach, to achieve an even better complexity. However, as this doesn’t seem to result in a clean bound of (say) O(_n_<sup>2</sup>/log_n_) yet, we leave determining the exact complexity for future work.

## References


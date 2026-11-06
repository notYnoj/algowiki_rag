Some values of the bound in Corollary 1.2 are:

The exponent convention gives an _O(n_<sup>2</sup>)-time algorithm at \(k=\frac{1}{2}\).

## 7. Applications

Corollary 1.2 and Theorem 1.1 give the following bounds through standard rectangular- multiplication balances. All bounds use arithmetic operations, with graph operations and symbol comparisons also charged.

1. **One lowest common ancestor per pair in a DAG.** Grandoni et al. \[4, Theorem 4.2 of the published version\] obtain exponent 1+2_x_ from the balance \(\omega(x)=3x\). Corol lary 1.2 permits \(x=(1+\sqrt{3})/4\), giving \(O(n^{(3+\sqrt{3})/2})\) time for finding one lowest common ancestor for every pair in an _n_-vertex DAG. The exponent is \((3+\sqrt{3})/2\approx 2.36603\).<tbc>

2. **Exact all-pairs Hamming distance.** For _n_ vectors of length _n_ over an unrestricted alphabet, the reduction to dominance products \[7\] and Yuster’s tradeoff \[13, Proposition 2.1\] give the balance \(\rho=\omega(4-\rho)\). Corollary 1.2 gives \(\rho=(13-\sqrt{7})/4\approx 2.58856\) and running time \(O(n^\rho)\) for computing every exact Hamming distance.<tbc>

3. **The standard unweighted APSP balance.** Zwick’s deterministic algorithm for directed unweighted APSP \[15, Section 6\] has exponent \(2+\mu\), where \(\omega(\mu)\le 1+2\mu\). Here \(\omega(\frac{1}{2})=2=1+2(\frac{1}{2})\), so it gives _O(n_<sup>2.5</sup>) running time. Combining the full curve with the deterministic (min,+)-product algorithm and APSP reduction of Alman and Vassilevska Williams \[1, Theorems 22 and 33-34\] further gives _O(n_<sup>2.4999</sup>) running time.<tbc>

4. **Minimum and maximum witnesses.** For two Boolean \(n\times n\) matrices, a minimum (maximum) witness for entry (_i,j_) is the least (greatest) index _k_ with _A<sub>ik</sub>=B<sub>kj</sub>_=1. The standard blocking algorithm \[3, Section 2.1\] takes \(O(n^{1-r+\omega(r)}+n^{2+r})\) time. Taking \(r=\frac{1}{2}\) gives _O(n_<sup>2.5</sup>) time for all witnesses.<tbc>

5. **Sparse matrix multiplication.** For two \(n\times n\) matrices with at most _m_ nonzero entries each, the sparse-dense decomposition of Yuster and Zwick \[14, Section 3\] gives \(O(m^2/n^r+n^{\omega(r)})\) time for \(0\le r\le 1\). Thus \(m\le n^{1.25}\) permits _O(n_<sup>2</sup>) time.<tbc>

6. **Dynamic matrix inverse and reachability.** Substituting Theorem 1.1 into van den Brand–Nanongkai–Saranurak’s tradeoff \[11, Theorem 4.2\], with _u_=0.50323551 and _v_=0.80667763 in \(max\{u+v,\omega(1,u,v)-u,\omega(v)-v\}\), gives _O(n_<sup>1.30992</sup>) worst-case time per entry update and query for maintaining the inverse of a nonsingular \(n\times n\) matrix, after _O(n_<sup>2.25</sup>) preprocessing. The associated Monte Carlo reduction gives the same bounds for directed reachability under edge updates, with _O_(1) query time for a fixed pair \[11, Corollary C.12 and Theorem C.16\].

## References

\begin{tabular}{ccccccc}
_k_ & 0.5 & 0.6 & 0.8 & 1 & 1.5 & 2 \\
\(\omega(k)\le\) & 2 & 2.0166_..._ & 2.1125 & 2.25 & 2.6666_..._ & 3.125 \\
\end{tabular}


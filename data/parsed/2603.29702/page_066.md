holds except with probability at most \(\mathrm{exp}\left(-\Omega\left(M/\mathrm{log}^{0.04}(n)\right)\right)=\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\). When (34) holds, we have \(\mathrm{min}\left(a_i,2\mathrm{log}^{0.02}(n)\widetilde{A}\right)=a_i\). Thus we can apply Hoeffding’s Inequality (Lemma 3.1, with \(c:=\mathrm{log}^{0.02}(n)\overline{A},\delta:=\Theta\left(\frac{1}{\mathrm{log}^{0.02}(n)}\sum_{i=1}^Ma_i\right)\)) on \(\sum_{i\in I}a_i\) to obtain that

\(\text{ESTSum}(A_I)\ge\left(1-O\left(1/\mathrm{log}^{0.02}(n)\right)\right)\sum_{i=1}^Ma_i\)

holds except with probability at most \(\mathrm{exp}\left(-\Omega\left(M/\mathrm{log}^{0.08}(n)\right)\right)=\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\).

## References


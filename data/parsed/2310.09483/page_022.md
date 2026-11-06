comparator), we must have \(max(x_i,x_j)-1\le x^*\le max(x_i,x_j)\). By a result from the previous section, \(x_j\le x_k+200\) with probability \(>1-\frac{1}{n^r}\). If _x<sub>i</sub>_ was _\>x<sub>k</sub>_+1, then it would compare greater than _x<sub>k</sub>_ and everything before it, contradicting _c<sub>i</sub>\<k_. Thus, \(x_i\le x_k+1\). It follows that with probability \(>1-\frac{1}{n^r}\), \(max(x_i,x_j)\le x_k+200\). Thus, if either _x<sub>i</sub>\>x<sub>k</sub>_ or _x<sub>j</sub>\>x<sub>k</sub>_, \(|x^*-x_k|\le 200\) as desired. Otherwise, if both \(x_i\le x_k\) and \(x_j\le x_k\), then \(|x_k-x^*|=x_k-x^*\le x_k-(max(x_i,x_j)-1)=min(|x_k-x_i|,|x_k-x_j|)+1\) as desired.

**Theorem 6.14.** _For r\>_0 _there exists c sufficiently large that `Select` returns a_ 202_-approximate k-selection with probability_ \(>1-\frac{1}{n^r}\).

_Proof._ We consider cases based on the sizes of _L<sub>x</sub>_ and _R<sub>x</sub>_:

If \(|L_x|\le\frac{1}{10}n^{2/3}\) and \(|R_x|\le\frac{1}{10}n^{2/3}\), then we have \(x_i\ge_{200}x_k\) and \(x_k\ge_{200}x_i\) with probability \(>1-\frac{2}{n^{r+1}}\), in which case we have \(|x_k-x_i|\le 200\). By the previous lemma it follows that \(|x^*-x_k|\le 201\) with probability \(>1-\frac{3}{n^{r+1}}\), so we return a 201-approximate _k_-selection with probability \(>1-\frac{3}{n^{r+1}}>1-\frac{1}{n^r}\) as desired.

If \(|L_x|>\frac{1}{10}n^{2/3}\) and \(|R_x|>\frac{1}{10}n^{2/3}\), then \(|x_j-x_k|\le 201\) with probability \(>1-\frac{1}{n^{r+1}}\). Thus, by the previous lemma, \(|x^*-x_k|\le 202\) with probability \(>1-\frac{2}{n^{r+1}}\). It follows that _x_<sup>∗</sup> is a 202-approximate _k_-selection with probability \(>1-\frac{2}{n^{r+1}}>1-\frac{1}{n^r}\) as desired.

If \(|L_x|\le\frac{1}{10}n^{2/3}\) and \(|R_x|>\frac{1}{10}n^{2/3}\), we have \(x_i\ge_{200}x_k\) with probability \(>\frac{1}{n^{r+1}}\). Thus, either \(x_i\le x_k+1\) in which case we have \(|x_i-x_k|\le 200\), or _x<sub>i</sub>\>x<sub>k</sub>_+1 in which case _x<sub>j</sub>_ must come from `Select+` and thus \(|x_j-x_k|\le 201\) with probability \(>\frac{1}{n^{r+1}}\). By the previous lemma, it thus follows that \(|x^*-x_k|\le 202\) with probability \(>\frac{3}{n^{r+1}}\). It follows that _x_<sup>∗</sup> is a 202-approximate _k_-selection with probability \(>1-\frac{3}{n^{r+1}}>1-\frac{1}{n^r}\) as desired.

The case where \(|L_x|>\frac{1}{10}n^{2/3}\) and \(|R_x|\le\frac{1}{10}n^{2/3}\) is symmetric.

**Theorem 6.15.** _`Select` takes n_<sup>1+_O_(1_/d_)</sup>_d_log_n comparisons and d_+102+min(100,log<sub>2</sub>_d_) _rounds._

_Proof._ All comparisons are done in `SelectSparse`, `Select`\(\pm\) and `Count`. The number of comparisons done by the two calls to `Count` is bounded by 2_n_. Thus, the total number of comparisons is bounded by _n_<sup>1+_O_(1_/d_)</sup>_d_log_n+n_log<sup>6/5</sup>_n_+2_n=n_<sup>1+_O_(1_/d_)</sup>_d_log_n_. Each call to `Count` takes one round, so the total number of rounds is bounded by \(d+min(100,log_2d)+100+2=d+102+min(100,log_2d)\).

Theorem 1.9 follows.

## 7 Open Problems

- Is there an algorithm to find a 3-approximate sorting or selection with high probability in \(\widetilde{O}(n)\) time?<tbc>

- Is there an algorithm to find a constant-approximate sorting with high probability in _O(n_log_n_) time?<tbc>

- Is there an algorithm to find a constant-approximate selection with high probability in _O(n_) time?<tbc>

**-** Can we improve the lower or upper bounds for _k_-approximate sorting and selection in _d_ rounds?<tbc>


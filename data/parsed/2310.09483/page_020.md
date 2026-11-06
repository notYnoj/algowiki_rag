## 6.2 Dense Selection

Here we give two algorithms: `Select+` and `Select-`, the former of which will return a good approximation if \(|L_x|>\frac{1}{10}n^{2/3}\), and the latter if \(|R_x|>\frac{1}{10}n^{2/3}\).

The idea is simple: take a large sample (size _cn_<sup>5/6</sup>log_n_), sort it with a constant approximate algorithm, and return the element in roughly the _k_-th position.

**Algorithm 5** Dense Selection

function \(\mathrm{Select}\pm(X,k)\)<br>
   \(n\leftarrow|X|\)<br>
   Generate a subset S of X of size cn<sup>5/6</sup>logn<br>
   \(S\leftarrow 100\)-Sort(S)<br>
   return \(S[ck\mathrm{log}n/n^{1/6}\pm cn^{5/12}\mathrm{log}n]\)<br>
end function

Let x<sup>∗</sup> be the item returned by \(\mathtt{Select}\pm\).

**Lemma 6.8.** _If_ \(|L_x|>\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough such that `Select`- returns a_ 201_-approximation with probability_ \(>1-\frac{1}{n^r}\).

_Proof._ It suffices to prove the actual (k/n<sup>1/6</sup>-n<sup>5/12</sup>)-th smallest element of S is in L<sub>x</sub>, since `100-Sort` returns a 200-approximation. The number of elements of S that are \(\le x_k\) (call this V ) follows a Hypergeometric(n,k,cn_<sup>5/6</sup>logn)<sup>‡</sup> distribution. Thus, by a tail bound:

\(\mathrm{Pr}\big[V\le ck\mathrm{log}n/n^{1/6}-cn^{5/12}\mathrm{log}n\big]=\mathrm{Pr}\big[V\le(k/n-n^{-5/12})cn^{5/6}\mathrm{log}n\big]\)<br>
\(\le e^{-2(n^{-5/12})^2cn^{5/6}\mathrm{log}n}\)<br>
\(\le n^{-2c}.\)

Similarly, the number of elements of S that are \<x<sub>k</sub>-1 (call this U) follows a Hypergeometric\((n,k-\frac{1}{10}n^{2/3},cn^{5/6}\mathrm{log}n)^\mathsection\) distribution. Thus, by a tail bound:

\(\mathrm{Pr}\big[U\ge k/n^{1/6}-n^{5/12}\big]=\mathrm{Pr}\big[((k-n^{2/3}/10)/n+n^{-1/3}/10-n^{-5/12})cn^{5/6}\mathrm{log}n\big]\)<br>
\(\le e^{-2(n^{-1/3}/10-n^{-5/12})^2cn^{5/6}\mathrm{log}n}\)<br>
\(<n^{-2c}.\)

for n sufficiently large. Thus, the probability of the actual (k/n<sup>1/6</sup>-n<sup>5/12</sup>)-th smallest element is in L<sub>x</sub> is at least \(1-2n^{-2c}>1-\frac{1}{n^r}\) for c sufficiently large by a union bound.

**Corollary 6.9.** _If_ \(|R_x|>\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough such that `Select`+ returns a_ 201_-approximation with probability_ \(>1-\frac{1}{n^r}\).

_Proof._ Symmetric.

**Lemma 6.10.** _If x_<sup>∗</sup> _is the item returned by `Select`-, for any r\>_0 _there exists c sufficiently large that_ \(x_k\ge_{200}x^*\) _with probability_ \(>1-\frac{1}{n^r}\).

<sup>‡</sup>Similarly to before, the second argument can be \>k, but it only makes the bounds better. \(^\mathsection\)Again, the second argument could be larger.


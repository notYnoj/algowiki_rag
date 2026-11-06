<tbc>We state three versions of Azuma’s Inequality, the first in terms of permutations, requiring also the definition of what it is for something to be _Lipschitz_, the second in terms of martingales, and the third a special case in terms of independent random variables. Note that we write _S<sub>n</sub>_ for the symmetric group.

Definition 2.4 (_b_-Lipschitz). For \(f:S_n\rightarrow\mathbb{R}\) and \(b\ge 0\), we say that _f_ is _b-Lipschitz_ if for any two permutations \(\sigma,\sigma'\in S_n\) differing by a transposition,

\(|f(\sigma)-f(\sigma')|\le b.\)

The next lemma follows from \[**42**, Section 11.1\] and, in particular, the discussion on page 93.

Lemma 2.5. (Azuma’s inequality, e.g. \[**42**\]) _Suppose_ \(f:S_n\rightarrow\mathbb{R}\) _is b-Lipschitz, and_ \(\sigma\in S_n\) _is a uniformly random permutation. Define_ \(X=f(\sigma)\)_. Then_

\(\mathbb{P}(|X-\mathbb{E}(X)|>t)\le 2exp\left(-\frac{t^2}{2nb^2}\right).\)

The Azuma-Hoeffding inequality which follows is perhaps the most basic concentration inequality for martingales. For random variables (_X<sub>i</sub>)<sub>i</sub>_ and (_Z<sub>i</sub>)<sub>i</sub>_ defined in the same probability space, we say that (_X<sub>i</sub>_) is a _martingale with respect to_ (_Z<sub>i</sub>_) if for every _i_ we have that _X<sub>i</sub>_ is measurable given _Z_<sub>1</sub>_,...,Z<sub>i</sub>_ (i.e. _X<sub>i</sub>=f<sub>i</sub>(Z_<sub>1</sub>_,...,Z<sub>i</sub>_)), E(|_X<sub>i</sub>_|) is finite and E(_X<sub>i</sub>|Z_<sub>1</sub>_,...,Z_<sub>_i_-1</sub>)=_X_<sub>_i_-1</sub>.

Lemma 2.6. (Azuma-Hoeffding inequality) _Let_ (_X<sub>i</sub>)<sub>i</sub> be a martingale with respect to random variables_ (_Z<sub>i</sub>)<sub>i</sub> in the same probability space. If_ \(|X_i-X_{i-1}|\le c_i\)_, then_

\(\mathbb{P}(|X_n-X_0|\ge t)\le 2exp\left(-\frac{t^2}{2\sum_{i=1}^nc_i^2}\right).\)

Corollary 2.7. (Bounded difference inequality, also known as McDiarmid’s inequality \[**41**, Theorem 3.1\]) _Let X=f(X_<sub>1</sub>_,...,X<sub>n</sub>_) _where X_<sub>1</sub>_,...,X<sub>n</sub> are independent random variables. Suppose that for every x_<sub>1</sub>_,...,x<sub>n</sub> and_ \(x'_1,\dots,x'_n\) _and every_ \(i\in[n]\) _we have_<tbc>

\(|f(x_1,\dots,x_i,\dots,x_n)-f(x_1,\dots,x'_i,\dots,x_n)|\le c_i.\)

<tbc>_Then_

\(\mathbb{P}(|X-\mathbb{E}(X)|\ge t)\le 2exp\left(-\frac{2t^2}{\sum_{i\in[n]}c_i^2}\right).\)

We finish this section with Bernstein’s inequality which enables us to bound sums of independent random variables using the second moment which can often give stronger concentration when McDiarmid’s inequality is not sufficient.

Lemma 2.8 (Bernstein’s inequality, e.g. \[**12**\])_. Let_ \(X=\sum_{i=1}^nX_i\) _be the sum of independent random variables such that_ |_X<sub>i</sub>|\<b for all_ \(i\in[n]\)_. Then_

\(\mathbb{P}(|X-\mathbb{E}(X)|>t)<2exp\left(-\frac{t^2}{2(bt/3+\sum_{i=1}^n\mathbb{E}(X_i^2))}\right).\)


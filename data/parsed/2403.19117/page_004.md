which counts the (non-trivial) equality relations among all the 2_<sup>n</sup>_ subset sums. Using Equation (2), we can rewrite Equation (3) as \(d=\sum_{0\le t<2^n}(f_t-\mathbf{1}[f_t\ge 1])=2^n-\sum_{0\le t<2^n}\mathbf{1}[f_t\ge 1]\), and thus obtain

\(d=\#\{0\le t<2^n:f_t=0\},\) (4)

which counts the non-subset-sums in {0,1_,...,_2_<sup>n</sup>_-1}. In particular, _d\<_2_<sup>n</sup>_.

The equivalence between Equation (3) and Equation (4) is powerful. In the following we will give two different algorithms for Pigeonhole Equal Sums. The first one works for small _d_ by analyzing the structure of input instances with few non-subset-sums (by Equation (4)). The second one works when _d_ is large and hence there are many solutions (by Equation (3)) which allow a subsampling approach. These two algorithms are summarized as follows:

\(\blacktriangleright\) **Lemma 4.** _Given parameter_ \(\Delta\le 2^n/(3n^2)\)_, Pigeonhole Equal Sums with_ \(d\le\Delta\) _can be solved deterministically in_ \(O^*(\sqrt{\Delta})\) _time._

\(\blacktriangleright\) **Lemma 5.** _Given parameter_ \(2^{n/2}\le\Delta<2^n\)_, Pigeonhole Equal Sums with_ \(d\ge\Delta\) _can be solved in_ \(O^*((2^{2n}/\Delta)^{1/3})\) _time by a randomized algorithm._

Combining these two lemmas implies our main result:

**Proof of Theorem 1.** Set \(\Delta=2^{0.8n}\) so that the two time bounds in Lemma 4 and Lemma 5 are balanced to _O_<sup>∗</sup>(2<sup>0.4_n_</sup>). Given an instance of Pigeonhole Equal Sums (with unknown _d_), we run both algorithms in parallel, and return the answer of whichever terminates first. \(\blacktriangleleft\)

## 3.1 Small _d_ case via structural characterization

In this section we prove Lemma 4. Assume \(d\le\Delta\le 2^n/(3n^2)\) and \(\Delta\) is known.

Since _f<sub>t</sub>_=0 for all _w_([_n_])_\<t\<_2_<sup>n</sup>_, from Equation (4) we know \(d\ge 2^n-1-w([n])\), and hence \(w([n])\ge 2^n-1-d\ge 2^n-1-\Delta\). Combined with Equation (1) for \(i\in[n-1]\), we get the following lower bound

\(w([i])\ge 2^i-1-\Delta\text{for all}i\in[n].\) (5)

The key step is to complement Equation (5) with a nearly matching upper bound:

\(\blacktriangleright\) **Lemma 6.** _For all_ \(i\in[n]\),

\(w_i\le 2^{i-1}+\Delta.\) (6)

Summing Equation (6) over _i_ gives

\(w([i])\le 2^i-1+i\Delta\) (7)

for all \(i\in[n]\).

**Proof.** Fix \(i\in[n]\). Let _M_ be the number of subsets \(S\subseteq[n]\) with _w(S)\<w<sub>i</sub>_. Since \(w_i<w_{i+1}<\cdots<w_n\), any such _S_ must be contained in [_i_-1], and thus \(M\le 2^{i-1}\). On the other hand, \(M=\sum_{t=0}^{w_i-1}f_t\ge w_i-\#\{0\le t<w_i:f_t=0\}\ge w_i-d\) by Equation (4). Hence, \(w_i\le M+d\le 2^{i-1}+\Delta\). \(\blacktriangleleft\)


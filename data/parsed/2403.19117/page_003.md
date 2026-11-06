\(\blacktriangleright\) **Lemma 3** (Counting subset sums via meet-in-middle \[14\])**.** _Given integers w_<sub>1</sub>_,...,w<sub>n</sub> and t, we can compute_ \(\#\{S\subseteq[n]:w(S)\le t\}\) _in O_<sup>∗</sup>(2<sup>_n/_2</sup>) _time. Moreover, we can list_ \(S\subseteq[n]\) _such that_ \(w(S)\le t\) _in O_<sup>∗</sup>(1) _additional time per S._

**Proof.** Divide \[_n_\] into \(S_1=\{1,\dots,\lfloor n/2\rfloor\}\) and _S_<sub>2</sub>=\[_n_\]\\_S_<sub>1</sub>, and every subset \(S\subseteq[n]\) can be represented as \(X\unknown Y,X\subseteq S_1,Y\subseteq S_2\). Compute and sort the two lists \(A=\{w(X)\}_{X\subseteq S_1}\) and \(B=\{w(Y)\}_{Y\subseteq S_2}\) of length _O_(2<sup>_n/_2</sup>) each. Then for each \(w(X)\in A\) we accumulate \(|B\cap(-\infty,t-w(X)]|\) to the answer. It is easy to augment this algorithm to support listing. \(\blacktriangleleft\)

## Pigeonhole Equal Sums via binary search

The following simple binary-search algorithm (described in \[1, Remark 6.9 of arXiv version\] and attributed to an anonymous referee) solves Pigeonhole Equal Sums in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time: Maintain an interval \(\{\ell,\ell+1,\dots,r\}\) (initialized to \(\ell=0,r=2^n-2\)) that satisfies the pigeonhole invariant \(r-\ell+1<\#\{S\subseteq[n]:\ell\le w(S)\le r\}\). Initially this invariant is satisfied due to \(w([n])\le 2^n-2\). While \(r>\ell\), pick the middle point \(m=\lfloor\frac{\ell+r}{2}\rfloor\), and use meet-in-middle (Lemma 3) to compute \(c_1=\#\{S\subseteq[n]:\ell\le w(S)\le m\}\) and \(c_2=\#\{S\subseteq[n]:m+1\le w(S)\le r\}\) in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time. Then we shrink the interval to \(\{\ell,\dots,m\}\) if \(m-\ell+1<c_1\), or to {_m_+1_,...,r_} if _r-m\<c_<sub>2</sub> (the invariant guarantees that at least one holds). After \(\lceil log_2(2^n-1)\rceil=n\) iterations we shrink to a singleton interval \(\ell=r\). By the invariant, there exist two different \(S_1,S_2\subseteq[n]\) such that \(w(S_1)=w(S_2)=\ell\), and we can report such _S_<sub>1</sub>_,S_<sub>2</sub> using meet-in-middle (Lemma 3).

This binary-search strategy will be used in our improved algorithms as well.

## 3 The improved algorithm

Let the _n_ input integers be sorted as \(0<w_1<w_2<\cdots<w_n\) (assuming no trivial solution _w<sub>i</sub>=w<sub>j</sub>_ exists).

### An assumption on prefix sums

If any proper prefix {_w_<sub>1</sub>_,...,w<sub>i</sub>_} (\(i\le n-1\)) already satisfies the pigeonhole promise _w_(\[_i_\])_\<_2_<sup>i</sup>_-1, then we can instead solve the smaller Pigeonhole Equal Sums instance {_w_<sub>1</sub>_,...,w<sub>i</sub>_} and obtain \(A,B\subseteq[i],A\neq B\) with _w(A_)=_w(B_). Hence, without loss of generality we assume such prefix does not exist, i.e.,

\(w([i])\ge 2^i-1\text{for all}i\in[n-1].\) (1)

### Frequencies _f<sub>t</sub>_ and parameter _d_

The _frequency_ (also called bin size) of \(t\in\mathbb{N}\) is the number of input subsets achieving sum _t_, denoted as \(f_t=\#\{S\subseteq[n]:w(S)=t\}\). Since _w_(\[_n_\])_\<_2_<sup>n</sup>_-1, we know _f<sub>t</sub>_=0 for all \(t\ge 2^n-1\), and

\(\sum_{0\le t<2^n}f_t=2^n.\) (2)

Two different subsets achieving equal subset sum _t_ imply _f<sub>t</sub>\>_1. This motivates the following parameter,

\(d=\sum_{0\le t<2^n}max\{0,f_t-1\},\) (3)


\[26\] Danupon Nanongkai. "Simple FPTAS for the subset-sums ratio problem". In: _Inf. Process. Lett._ 113.19–21 (Sept. 2013), pp. 750–753. issn: 0020-0190. doi: `10.1016/j.ipl.2013.07.009`.

\[27\] Christos H. Papadimitriou. "On the complexity of the parity argument and other inefficient proofs of existence". In: _Journal of Computer and System Sciences_ 48.3 (1994), pp. 498–532. issn: 0022-0000. doi: `https://doi.org/10.1016/S0022-0000(05)80063-7`.

\[28\] Tim Randolph and Karol Węrzycki. "Beating Meet-in-the-Middle for Subset Balancing Problems". In: _Proceedings of the 58th Annual ACM Symposium on Theory of Computing_. S ’26. Salt Lake City, UT, USA: Association for Computing Machinery, 2026, pp. 1314–1325. isbn: 9798400725364. doi: `10.1145/3798129.3800841`. Full version available at: `https: //arxiv.org/abs/2511.10823`.

\[29\] Richard Schroeppel and Adi Shamir. "A _T=O_(2<sup>_n/_2</sup>), _S=O_(2<sup>_n/_4</sup>) Algorithm for Certain NP-Complete Problems". In: _SIAM Journal on Computing_ 10.3 (1981), pp. 456–464. doi: `10.1137/0210033`. eprint: `https://doi.org/10.1137/0210033`.

\[30\] Katerina Sotiraki, Manolis Zampetakis, and Giorgos Zirdelis. "PPP-Completeness with Connections to Cryptography". In: _2018 IEEE 59th Annual Symposium on Foundations of Computer Science (FOCS)_. 2018, pp. 148–158. doi: `10.1109/FOCS.2018.00023`.

\[31\] Gerhard J. Woeginger and Zhongliang Yu. "On the equal-subset-sum problem". In: _Information Processing Letters_ 42.6 (1992), pp. 299–302. issn: 0020-0190. doi: `https://doi.org/ 10.1016/0020-0190(92)90226-L`.

\[32\] Zhengmin Zhang. "Estimating Mutual Information Via Kolmogorov Distance". In: _IEEE Transactions on Information Theory_ 53.9 (2007), pp. 3280–3282. doi: `10.1109/TIT.2007.903122`.

## A Proof of Lemma 2.3

We use the following lemma, which gives a lower bound on the number of primes in an interval. Recall that throughout the paper, all logarithms are base 2.

**Lemma A.1** (\[18, p.371\])**.** _For all sufficiently large x, the interval_ \[_x,_2_x_\] _contains_ \(\Omega(x/\mathrm{log}x)\) _primes._

We restate Lemma 2.3.

**Lemma 2.3.** _Given a set S of n integers satisfying_ \(|s|\le 2^m\) _for all_ \(s\in S\)_, the following holds. If_ \(0\in S\) _or_ \(m\ge 2^n\)_, then ESS on S can be solved in O_(poly(_n,m_)) _time. Otherwise, with probability at least_ 1-_O_(2<sup>-_n_</sup>)_, we can construct, in O_(poly(_n,m_)) _time, a set_ \(S'\) _of_ \(n+\lceil\mathrm{log}n\rceil\) _positive integers satisfying_ \(0<s'\le 2^{O(n)}\) _for all_ \(s'\in S'\)_, and satisfying the following properties: if_ \(S'\) _has no ESS solution, then neither does S; conversely, from any ESS solution of_ \(S'\)_, we can reconstruct a corresponding ESS solution of S in O_(poly(_n,m_)) _time._

We essentially repeat the argument from \[25, Appendix A of the full version\]. If \(0\in S\), then we can immediately return an ESS solution _A_={0} and \(B=\emptyset\). If \(m\ge 2^n\), then an algorithm running in time \(O(mn4^n)\le O(nm^3)\) is polynomial in _n_ and _m_. Thus, we may assume that \(0\notin S\) and _m\<_2<sup>_n_</sup>.

We write _S_={_w_<sub>1</sub>_,...,w<sub>n</sub>_} and construct a new set \(S'=\{w'_1,\dots,w'_{n+\lceil\mathrm{log}n\rceil}\}\) as follows. We pick a random prime \(p\in[2^{bn},2^{bn+1}]\) for a constant \(b\ge 6\). For each \(i\in[n]\), we set \(w'_i=w_i\mathrm{mod}p\). We then add \(\lceil\mathrm{log}n\rceil\) auxiliary elements by setting \(w'_{n+j}=2^{j-1}p\) for each \(j\in[\lceil\mathrm{log}n\rceil]\).


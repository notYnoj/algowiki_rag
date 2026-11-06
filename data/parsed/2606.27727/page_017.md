Now take some triple of groups \(I'\subseteq I\), \(J'\subseteq J\), \(K'\subseteq K\), where \(|I'|=|J'|=|K'|=t\). The number of bits needed to encode the weighted subgraph induced by \(I'\cup J'\cup K'\) is

\(3t^2\cdot\ell=3\left(\frac{\sqrt{w}}{6\sqrt{logw}}\right)^2\cdot(10logw)<w,\)

so the entire subgraph can be packed into a single word.

Next, we observe that the problem of checking whether a given triple \(I',J',K'\) contains an exact triangle modulo _p_ can be computed with a poly(_w_)-size AC0 circuit. Let _T<sub>p</sub>_=(_T_mod_p_) be the corresponding integer in {0,1_,...,p_-1}. Our circuit takes an OR over all \(O(t^3)\le O(w^{3/2})\) triples of nodes \(i\in I'\), \(j\in J'\), and \(k\in K'\), then checks that the edges (_i,j),(j,k),(k,i_) exist and

\(w'(i,j)+w'(j,k)+w'(k,i)\in\{T_p,p+T_p,2p+T_p\}.\)

(Since only three weights are being summed, these are all the possible choices for the integer sum to equal the target modulo _p_.) Since addition is in AC0, this construction is computable in AC0. As a consequence, there is a single word operation to determine whether the triple \(I',J',K'\) contains an exact triangle mod _p_. For notational brevity, let’s call this an _mod triangle check_ which returns a yes or no answer.

All of the ingredients are now in place for us to describe the algorithm in full. Pick a uniform random prime _p_ from \(\left[2,2^\ell\right]\), hash all edge weights modulo _p_, and for all (_n/t_)<sup>3</sup> triples \(I',J',K'\) on 3_t_ nodes, we run a mod triangle check in constant time. For each check that returns yes, we enumerate all _O(t_<sup>3</sup>) triples of nodes \(i\in I'\), \(j\in J'\), \(k\in K'\) to determine if there is an exact triangle in \(I',J',K'\) with the original unhashed weights (returning this triangle if it’s found). If more than (_n/(tw_))<sup>3</sup> checks of triples return yes, then we stop and say _don’t know_. Otherwise, we return _reject_ if no exact triangle was found after enumerating over all triples \(I',J',K'\).

First we verify the running time. By construction, our algorithm takes time poly(log_w_)+_O(n_<sup>2</sup>) to pick a random prime of \(\ell=\Theta(logw)\) bits and hash all weights to \(\ell\) bits. Next, it takes _O_((_n/t_)<sup>3</sup>) time to call the mod triangle check on all triples \(I',J',K'\). Finally, it takes \(O((n/(tw))^3\cdot t^3)\le O((n/w)^3)\) extra time to go through up to (_n/(tw_))<sup>3</sup> triples and exhaustively check the corresponding _O(t_)-node subgraph for an exact triangle. Since _t\<w_, the running time is bottlenecked by \(O(n^3/t^3)\le O(n^3(logw)^{3/2}/w^{3/2})\).

Next, we show correctness. Note that if there is an exact triangle solution, then it is in some triple \(I'\), \(J'\), \(K'\), and the mod triangle check called on \(I'\), \(J'\), \(K'\) will always return _yes_ no matter what prime is chosen. Thus the algorithm will find the exact triangle, _provided the algorithm does not stop early and return don’t know_. Moreover, if the algorithm does not return _don’t know_ when there is no exact triangle, then the algorithm correctly rejects.

Finally, similarly to Theorem 21, we prove that the algorithm outputs _don’t know_ with probability at most 1/poly(_w_). Hence with probability at least 1-1/poly(_w_), the algorithm does not stop early: it will return an exact triangle when one exists, and will correctly reject when an exact triangle does not exist.

Fix some triple \(I',J',K'\) for which we will run a mod triangle check. For each \(i\in I'\), \(j\in J'\), and \(k\in K'\), the probability that

\(w'(i,j)+w'(j,k)+w'(k,i)\neq t\text{and}w'(i,j)+w'(j,k)+w'(k,i)=tmodp\)

is at most the number of prime factors of \(t-w'(i,j)+w'(j,k)+w'(k,i)\) divided by the total number of primes in \([2,2^\ell]\), which is at most \(2w\cdot(\ell/2^\ell)\le(20logw)/w^9\). (Here, we apply the assumption that each edge weight fits in a word, in which case each weight has at most


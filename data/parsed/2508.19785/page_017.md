and we can use a Chernoff bound to write:

\(Pr\left(X^{(\rho)}<\frac{h+\eta+\rho}{2}\right)\le Pr\left(Y^{(\rho)}<\frac{h+\eta+\rho}{2}\right)\le Pr\left(Y^{(\rho)}<\frac{11\rho}{20}\right)\)<br>
\(=Pr\left(Y<\frac{11\mathbb{E}[Y]}{20q}\right)\le Pr\left(Y<\left(1-\frac{1}{3}\right)\mathbb{E}[Y]\right)\)<br>
\(\le e^{-\frac{\rho q}{18}}=e^{-\frac{\rho}{20}}\le e^{-6lnm}=m^{-6}.\) □

Lemma 4.9. _Let_ \(j\in\{0,1\}\)_. A walk on T<sub>j</sub> returns a bad vertex with probability at most m_<sup>-7</sup>.

Proof. Notice that, in order to return a bad vertex _v_, the walk must first reach a vertex _u_ at depth _h(u)=h_, and then traverse the \(\eta\) vertices of the path rooted in _u_ having _v_ as its other endpoint.

We now bound the probability that, once the walk reaches _u_, it will also reach _v_ before walking back to the parent of _u_. Notice that all the vertices in the path from _u_ to _v_ are associated to the same interval, and hence they are all bad. Since a test on a bad vertex succeeds with probability at most \(\frac{1}{50}\) (see Lemma 4.4) and tests are independent (see Lemma 4.7), the sought probability can be upper-bounded by considering a random walk on \(\{0,\dots,\eta+1\}\) that: (i) starts from 1, (ii) has one absorbing barrier on 0 and another on \(\eta+1\), and (iii) for any state \(i\in[1,\eta]\) has a probability of transitioning to state _i_+1 of \(\frac{1}{50}\) and to state _i_-1 of \(\frac{49}{50}\). Here state 0 corresponds to the parent of _u_, and state _i_ for _i\>_0 corresponds to the vertex of the _u-v_ path at depth _h+i_-1 (so that state 1 corresponds to _u_ and state \(\eta+1\) corresponds to _v_).

The probability of reaching _v_ in \(\rho\) steps is at most the probability of being absorbed in \(\eta\) (in any number of steps), which is (see, e.g., [16, pp. 344-346]):

\(\frac{\frac{49/50}{1/50}-1}{\left(\frac{49/50}{1/50}\right)^{\eta+1}-1}=\frac{48}{49^{\eta+1}-1}<\frac{1}{49\eta}\le\frac{1}{7^4\cdot 7^{2\cdot 4}log_7m}=\frac{1}{7^4m\cdot m^7}<\frac{1}{\rho m^7}.\)

Since the walk on _T<sub>j</sub>_ can reach a vertex at depth _h_ at most \(\rho\) times, by the union bound we have that the probability of returning a bad vertex is at most _m_<sup>-7</sup>. □

We are now ready to prove the main result of this section.

Theorem 4.10. _Let S be a sequence of m elements, let d be an integer with_ \(d\ge max\{disl(S),lnm\}\)_, and let_ \(x\notin S\) _be an additional element. Under our error model for approximate noisy binary searching, there exists an algorithm_ NoisySearch(_S,x,d_) _that runs in O_(log_m_) _worst-case time and returns an index_ \(\tau_x\in[rank(x,S)-\alpha d,rank(x,S)+\alpha d]\) _with probability at least_ 1-_O(m_<sup>-6</sup>)_, where_ \(\alpha\ge 2\) _is a constant that depends only on p._

Proof. We compute the index \(\tau_x\) by performing two random walks on _T_<sub>0</sub> and on _T_<sub>1</sub>, respectively. If any of the walks returns a vertex _v_, then we return any position in the interval _I(v_) associated with _v_ (if both walks return some vertex, we choose one arbitrarily). If both walks timeout, then we return an arbitrary position.

From Lemma 4.8 the probability that both walks timeout is at most _m_<sup>-6</sup> (as the walk on _T_<sup>∗</sup> timeouts with at most this probability). Moreover, by Lemma 4.9, the probability that at least one of the two walks returns a bad vertex is at most 2_m_<sup>-7</sup>_\<m_<sup>-6</sup>.

Overall, vertex _v_ exists and it is not bad with probability at least 1-2_m_<sup>-6</sup>. When this happens we can use \(\tau_x\in[minI(v),maxI(v)]\) and that max_I(v_)-min_I(v)\<cd_ to write:<tbc>

\(i^*\ge minI(v)-cd>maxI(v)-2cd\ge\tau_x-2cd,\)

<tbc>and<tbc>

\(i^*\le maxI(v)+cd<minI(v)+2cd\le\tau_x+2cd.\)


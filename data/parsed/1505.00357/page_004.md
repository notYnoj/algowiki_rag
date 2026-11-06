<tbc>**Theorem 4.** _Lemma 4 of \[11\] is incorrect: there exists an instance -- a query distribution_ \(\beta\) _-- for which it does not hold, and on which their algorithm fails._

This flaw also invalidates two algorithms, proposed in Spuler’s thesis \[18\], that are based on Huang and Wong’s algorithm. We know of no poly-time algorithm to find optimal gbsts. Of course, optimal 2wcsts are at least as good.

### 2wcst _without equality tests._

Finding an optimal _alphabetical encoding_ has several poly-time algorithms: by Gilbert and Moore -- _O(n_<sup>3</sup>) time, 1959 \[8\]; by Hu and Tucker -- _O(n_log_n_) time, 1971 \[10\]; and by Garsia and Wachs -- _O(n_log_n_) time but simpler, 1979 \[7\]. The problem is equivalent to finding an optimal 3-way-comparison search tree when the probability of querying any key is zero (\(\beta\equiv 0\)) \[14, §6.2.2\]. It is also equivalent to finding an optimal 2wcst in the successful-queries variant with only "_\<_" comparisons allowed (C={_\<_},Q=K) \[1, §5.2\]. We generalize this observation to prove Thm. 5:

**Theorem 5.** _Any_ 2wcst _instance_ I=(K={_K_<sub>1</sub>_,...,K<sub>n</sub>},_Q,C,\(\alpha,\beta\)) _where_= _is not in_ C _(equality tests are not allowed), can be solved in O(n_log_n_) _time._

**Definitions 1** _Fix an arbitrary instance_ \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\).

_For any node N in any_ 2wcst _T for_ I_, N’s_ query subset, Q_<sub>N</sub>, contains queries_ \(v\in\mathcal{Q}\) _such that the search for v reaches N. The_ weight \(\omega(N)\) _of N is the probability that a random query v (from distribution_ \((\alpha,\beta)\)_) is in_ Q_<sub>N</sub>. The weight_ \(\omega(T')\) _of any subtree_ \(T'\) _of T is_ \(\omega(N)\) _where N is the root of_ \(T'\).

_Let_ \(\langle v<K_i\rangle\) _denote an internal node having key K<sub>i</sub> and comparison operator \< (define_ \(\langle v\le K_i\rangle\) _and_ \(\langle v=K_i\rangle\) _similarly). Let_ \(\langle K_i\rangle\) _denote the leaf N such that_ Q_<sub>N</sub>_={_K<sub>i</sub>}. Abusing notation,_ \(\omega(K_i)\) _is a synonym for_ \(\omega(\langle K_i\rangle)\)_, that is,_ \(\beta_i\).

_Say T is_ irreducible _if, for every node N with parent_ \(N'\), \(\mathcal{Q}_N\neq\mathcal{Q}_{N^\prime}\).

In the remainder of the paper, we assume that only comparisons in \(\{<,\le,=\}\) are allowed (i.e., \(\mathcal{C}\subseteq\{<,\le,=\}\)). This is without loss of generality, as "_v\>K<sub>i</sub>_" and "\(v\ge K_i\)" can be replaced, respectively, by "\(v\le K_i\)" and "_v\<K<sub>i</sub>_."

## 2 Proof of Spuler’s conjecture

Fix any irreducible, optimal 2wcst _T_ for any instance \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\).

**Theorem 6 (Spuler’s conjecture).** _The key K<sub>a</sub> in any equality-comparison node_ \(N=\langle v=K_a\rangle\) _is a maximum-likelihood key:_ \(\beta_a=max_i\{\beta_i:K_i\in\mathcal{Q}_N\}\).

The theorem will follow easily from Lemma 1:

**Lemma 1.** _Let internal node_ \(\langle v=K_a\rangle\) _be the ancestor of internal node_ \(\langle v=K_z\rangle\)_. Then_ \(\omega(K_a)\ge\omega(K_z)\)_. That is,_ \(\beta_a\ge\beta_z\).

_Proof. (Lemma 1)_ Throughout, "\(\langle v\prec K_i\rangle\)" denotes a node in _T_ that does an inequality comparison (\(\le\) or _\<_, not =) to key _K<sub>i</sub>_. Abusing notation, in that context, "\(x\prec K_i\)" (or "\(x\unknown\neq K_i\)") denotes that _x_ passes (or fails) that comparison.


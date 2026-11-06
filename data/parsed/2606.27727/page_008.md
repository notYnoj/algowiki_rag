## 8:8 Beating Trivial Time for Tricky Triangle Tasks

first words of each list. Then, take the remainder word produced by the merge step, along with the next full word of the list that ran out, and merge those. Repeat that process until one of _L_<sub>0</sub> and _L_<sub>1</sub> is completely exhausted, at which point we concatenate the final remainder word with the merged list we have built up so far. Each of the merge steps takes constant time, since it is implementable via an AC0 circuit as is described in Lemma 13. At every iteration, we process a new word from either _L_<sub>0</sub> or _L_<sub>1</sub>. Thus, this algorithm terminates in 2_ku/w_ steps, which takes _O(ku/w_) time.

Now that we have a merge step, it is natural to construct a mergesort-like sorting algorithm. We note that this gives an improvement over the best-known packed sorting algorithm in the Word-RAM model, which is due to Belazzougui, Brodal, and Nielsen [9]. Their algorithm sorts _n_ integers on _w/u_ bits packed into compressed lists in \(O(\frac{n}{u}(logn+log^2u))\) time, and works for any choice of \(w=\Omega(logn)\). In particular, they are interested in the setting where each element is on _u=O_(log_n_) bits, so _u=O(w/_log_n_). Thus, their overall runtime is \(O(\frac{nlogn}{w}(logn+log^2w))\), which we will slightly improve.

\(\triangleright\) Claim 15. Given a list _L_ of _n_ elements in [2_<sup>u</sup>_] packed into words, we can sort _L_ in _O(nu_log_n/w_) time.

**Proof of Claim 15.** We are able to compute the result of one AC0 circuit that takes _w_ bits as input in constant time. Thus, in log_w_ time, we have access to circuits with unbounded fan-in and logarithmic depth, which captures at least all of NC1, which, crucially, contains sorting [3]. So we require _O_(log_w_) time to sort the elements in a single word.

This serves as the preprocessing for our merging procedure, and runs in _O(n_log_w/w_) time. The bulk of the computation is the merge step. We can now merge each of the _n_log_n/w_ words in a tree-like fashion. One can think of placing each word at the leaf of a height-_O_(log_n_) binary tree, and then storing the merged version of the children in every parent node. The recurrence associated with this is _T(m_)=2_T(m/_2)+_O(m_), so we require _O(m_log_m_) time, where _m_:=_nu/w_ is the total number of words. Thus the overall runtime is _O(nu_log_n/w_), which dominates the preprocessing.

We note that the difficulty of packed sorting may be inherent. In particular, if one could remove the log_n_-factor from the runtime above, this would resolve the longstanding open problem of linear-time sorting for (almost) all word sizes. The Belazzougui, Brodal, and Nielsen paper achieves linear-time for \(w=\Omega(log^2nlogn)\), leaving the problem open only for word sizes that are \(\omega(logn)\) (from radix sort) and _o_(log<sup>2</sup>_n_loglog_n_). However, the paper does this by reducing sorting on word size _w_ to loglog_n_ levels of packed sorting of _O(n_) elements on _O_(log_n_) bits. Thus, shaving off the log factor on the packed sorting runtime would give a _O(n_log_n_loglog_n/w_) time algorithm, which is linear when \(w=\Omega(lognloglogn)\), almost completely closing this longstanding gap in word size.

It is also known that shaving this log-factor, or more generally, solving packed sorting in time faster than \(o(min\{n,\frac{nu}{w}log\frac{nu}{w}\})\), would refute the Undirected _k_-Pairs Conjecture, which is central to the field of network coding [30, 23].

## 3.2 Indicator Masks for Compressed Lists

Beyond sorting compressed lists, we would like to efficiently indicate list elements of interest to our algorithms. To do this, we define an _indicator mask_ to be a length-_w_ bitstring that is all zeros except the leading bit of each entry. This bit will indicate the value of some


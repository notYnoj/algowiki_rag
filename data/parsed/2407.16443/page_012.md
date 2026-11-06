in the order _p_<sub>0</sub>_,q_<sub>1</sub>_,p_<sub>1</sub>_,...,q<sub>n</sub>,p<sub>n</sub>_. To show that such a property holds in our tree _T_, we first point out that each probability _q<sub>i</sub>_ necessarily occupies a distinct internal node in _T_. By the sake of contradiction let us suppose that it is not the case, that is, there exist _q<sub>i</sub>_ and _q<sub>j</sub>_, with _i\<j_, that have been assigned to the same node _x_. Then, _x_ is the lowest common ancestor both of _p_<sub>_i_-1</sub> and _p<sub>i</sub>_, and of _p_<sub>_j_-1</sub> and _p<sub>j</sub>_. This implies that _p_<sub>_i_-1</sub> and _p_<sub>_j_-1</sub> are in the left sub-tree of _x_, while _p<sub>i</sub>_ and _p<sub>j</sub>_ are in the right sub-tree of _x_. This flagrantly contradicts the fact that in the tree _B_, from which we started, the leaves appear in the order _p_<sub>0</sub>_,q_<sub>1</sub>_,p_<sub>1</sub>_,...,q<sub>n</sub>,p<sub>n</sub>_ (i.e., that _B_ represents an alphabetic code).

Thus, each _q<sub>i</sub>_ is assigned to a distinct lowest common ancestor, and the order of the _p<sub>i</sub>_’s is not affected by the transformation of the _q<sub>i</sub>_’s in internal nodes. Therefore, an in-order visit of the tree gives the nodes in the order _p_<sub>0</sub>_,q_<sub>1</sub>_,p_<sub>1</sub>_,...,q<sub>n</sub>,p<sub>n</sub>_. We conclude that _T_ is a correct binary search tree for \(\sigma\).

The manipulation of the _q<sub>i</sub>_’s to transform them from leaves of _B_ to internal nodes of _T_ can be implemented in linear time, as shown in [5].

Finally, we evaluate the cost of the obtained binary search tree _T_. From (37) the cost of _T_ satisfies the inequality

\(\mathbb{E}[T]\le\mathbb{E}[C]-\sum_{i=1}^nq_i-\sum_{i=0}^{n-1}min(p_i,p_{i+1}).\)

This concludes the proof of the theorem.

By plugging into (36) either formula (20) of Theorem 2, or formula (22) of Theorem 3, or formula (36) of Corollary 4.2 (according to the hypothesis that holds) we get a series of upper bounds on the cost of optimal binary search trees that considerably improve on the bound (8) of [21], as we asserted in Section III. For instance, by using formula (23) of Theorem 3 in formula (36), we get the upper bound

\(H(\sigma)+2-\sigma_1-\sigma_{2n+1}-\sum_{i=1}^{2n}min(\sigma_i,\sigma_{i+1})-\sum_{i=1}^nq_i-\sum_{i=0}^{n-1}min(p_i,p_{i+1}),\) (38)

already mentioned in Section III.

We remark that our upper bounds on the cost of optimal binary search trees are, in fact, upper bounds on the cost of binary search trees constructed by the _linear_ time algorithm outlined in Theorem 5.

It is worth noting that the binary search trees constructed according to Theorem 5 are not too far from being optimal, and this is due to the lower bounds on the cost of _any_ binary search tree given in [6]. For example, the authors of [6] proved that the cost of any binary search tree is lower bounded by

\(H(\sigma)+\sum_{i=1}^nq_i+H(\sigma)log_2(H(\sigma))-(H(\sigma)+1)log_2(H(\sigma)+1).\) (39)

One can see that (38) and (39) are not too far apart. In fact, the difference between the upper bound (38) and the lower bound (39) is smaller than

\(2-\sigma_1-\sigma_{2n+1}-\sum_{i=1}^{2n}min(\sigma_i,\sigma_{i+1})-2\sum_{i=1}^nq_i-\sum_{i=0}^{n-1}min(p_i,p_{i+1})-H(\sigma)log_2(H(\sigma))+(H(\sigma)+1)log_2(H(\sigma)+1)<2+log_2(H(\sigma)+1)+log_2e-\sigma_1-\sigma_{2n+1}-\sum_{i=1}^{2n}min(\sigma_i,\sigma_{i+1})-2\sum_{i=1}^nq_i-\sum_{i=0}^{n-1}min(p_i,p_{i+1}).\) (40)

Additionally, other results in [6] strengthen the lower bound (39) for particular range of values of the entropy _H_ and thus can be used the reduce the gap between the upper bound and lower bound given in (40). Therefore, in situations where the optimal but onerous _O(n_<sup>2</sup>) time algorithm by Knuth [17] cannot be used, our analysis shows that the _O(n_) time algorithm of [5] is a valid alternative. An additional merit of Theorem 5 is that any possibly improved bounds on the average length of alphabetic codes will immediately translate into improved bounds on the cost of binary search trees.

## ACKNOWLEDGMENTS

The authors would like to thank the referees for their comments, corrections, and insightful suggestions. Our paper has been greatly improved by the generous help of the referees.

## REFERENCES

[1] J. Abrahams, " and parse trees for lossless source encoding", _Commun. Inf. Syst._, vol. **1**, pp. 113-146, 2001.

[2] R. Ahlswede and I. Wegener, _Search Problems_. John Wiley & Sons, 1987.

[3] M. Aigner, _Combinatorial Search_, John Wiley & Sons and B. G. Teubner, Stuttgart, 1988.

[4] Y. Dagan, Y. Filmus, A. Gabizon and S. Moran, "Twenty (simple) questions", _Proceedings of The 49th Annual ACM SIGACT Symposium on Theory of Computing, S2017_, pp. 9-21, 2017.

[5] R. De Prisco and A. De Santis, "On binary search trees", _Information Processing Letters_, vol. **45**, pp. 249-253, 1993.

[6] R. De Prisco and A. De Santis, "New lower bounds on the cost of binary search trees", _Theoretical Computer Science_, vol. **156**, pp. 315- 325, 1996.

[7] M. Fredman, "Two applications of a probabilistic search technique: Sorting X + Y and building balanced search trees", _Proceedings of the Seventh Annual ACM Symposium on Theory of Computing, S ’75_, pp. 240-244, 1975.

[8] M. Garey, "Optimal binary identification procedures", _SIAM Journal on Applied Mathematics_, vol. **23**, pp. 173-186, 1972.

[9] E. Gilbert and E. Moore, "Variable-length binary encodings", _Bell System Technical Journal_, vol. **38**, pp. 933-967, 1959.

[10] R. Hassin and A. Sarid, "Operations research applications of dichotomous search", _European Journal of Operational Research_, vol. **265**, Issue 3, pp. 795-812, 2018.

[11] T. Hiraoka and H. Yamamoto, "Alphabetic AIFV codes constructed from Hu-Tucker codes". In: _Proceedings of the 2018 IEEE International Symposium on Information Theory (ISIT 2018)_, pp. 2182-2186, 2018.

[12] Y. Horibe, "An improved bound for weight-balanced tree", _Information and Control_, vol. **34**, 148-151, 1977.

[13] T. Hu and A. Tucker, "Optimal computer search trees and variable-length alphabetical codes", _SIAM Journal on Applied Mathematics_, vol. **21**, pp. 514-532, 1971.


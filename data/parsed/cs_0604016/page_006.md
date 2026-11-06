is most common), and (2) thus becomes:

\(c(i,i)=0c_k(i,j)=min_{s\in(i,j]}\{C_k(p(i,s-1),p(s,j),i,j,s)+c(i,s-1)+c(s,j)\}\forall kc(i,j)=min_{k\in[1,m]}\{c_k(i,j)\}\) (3)

Once again, this is a simple matter of dynamic programming, and, assuming all _C<sub>k</sub>_ are calculable in constant time, this can be done in _O(mn_<sup>3</sup>) time and _O(n_<sup>2</sup>+_n_log_m_) space, the log_m_ term accounting for recalculation and storage of the type of cost function (decision method) used for each branch. An even more general version of this could take into account properties of subtrees other than those already mentioned, but we need not consider this here.

Note that, because dynamic prediction is adaptive to dynamic branch performance, we need not explicitly code branch bias; the more and less likely branch outcomes will automatically be detected. However, most dynamic predictors begin with state that depends on the type of branch in the same manner as static prediction. That is, the first time a branch is encountered, it is usually statically predicted. Thus it might also be worthwhile to implement the search software so that initial iterations of the search tree behave as well as possible given the tree optimal for asymptotic behavior. Note that this variation adds no time or space complexity to the above algorithm.

If the software is predetermined but the tree is not -- that is, if the software is not hard coded for the specific tree -- then matters change entirely; no prediction and static prediction result in this problem being equivalent to that of ordered edges, the problem proposed by Knuth and considered by Itai. Dynamic prediction with correlations, on the other hand, can result in a number of outcomes, depending on implementation. The software on a given processor could have near-perfect distinguishing of outcomes, in which the above dynamic analysis persists. More likely, without sufficient unrolling [14] of the tree data structure, there would be confusion of outcomes, as the software would not know whether all previous branches untaken indicates we are at the root, at its right child, at its right child’s right child, etc. Optimizing for the complex dependencies involved with such a system is no longer within the above framework, and the overall averaging effect means that one might want to just use the tree optimal for the corresponding static problem Therefore the aforementioned methods are usually best suited for when the user has the option of designing software specifically for a given decision tree, or designing hardware and/or programmable logic to allow the methods to work in fixed software.

## IV. SEARCH TREES AND EQUALITY COMPARISONS

Knuth showed how a dynamic programming approach can be used for general search trees [27], in which the decision is no longer binary, but is instead, "Is the output greater than, less than, or equal to _x?_" This allows items to be implicitly<tbc>

<tbc>or explicitly stored within the internal nodes (nonleaves) of the decision tree and allows us to consider items that might not be in a search tree. This model generalizes the concept of an alphabetic decision tree and can be used for applications in which there is an inherent "dictionary" of items, such as token parsing and spell checking. Probabilities for both present and missing items are then needed.

Before formalizing this, we should note a few things about the applicability of the search tree model. Clearly the problem at the beginning of this paper does not fall into this model, as strict equality cannot be tested for. Even where this model is applicable, it can be too restrictive. For example, this model is often inferior to the alphabetic model for the simple reason that, on most hardware, including all hardware considered here, three-way branches are not native operations. They must thus be simulated by two two-way branches in a manner that actually results in greater run time. Experimental analysis of this phenomenon can be found in [4] and numerical analysis can be found in [20] and [18, pp. 344-345]. These all find that an alphabetic tree is usually preferable in practice. Thus we only briefly discuss issues of this search tree model.

For items 1 through \(n'\), \(\beta_i\) is defined as the probability that a search yields item _i_ and \(\alpha_i\) as the probability that a search fails and the item not in the search tree would be lexicographically between items _i_ and _i_+1; \(\alpha_0\) is the probability it is before \(\beta_1\) and \(\alpha_n\) is the probability it is after \(\beta_n\). Thus<tbc>

\(\sum_{i=1}^{n^\prime}\beta_i+\sum_{i=0}^{n^\prime}\alpha_i=1.\)

<tbc>The alphabetic tree scenario is a special case, with \(n'=n-1\), \(\beta_i=0\), and \(\alpha_i=p(i+1)\), as in Fig. 5(a) for _n_=5. Fig. 5(b) is a similar search tree configured for a three-way comparison; this time, there are only four items, and it is assumed that all items searched for will be in the tree. Fig. 5(c) is the same four-item search tree allowing one to search for both items in the tree (with probabilities \(\{\beta_i\}\)) and ranges of missing items (with probabilities \(\{\alpha_i\}\)).

In such a model, there are now three costs associated with a given node; the cost of the two branches _c_<sub>1</sub> and _c_<sub>2</sub>, and the cost of an equality, _e_. Thus, for static prediction or no prediction, (2) becomes:

\(c(i,i)=0\)<br>
\(p(i,i)=\alpha_i\)<br>
\(c'(i,j)=min_{s\in(i,j]}\{c_1p(i,s-1)+c_2p(s,j)+\)<br>
\(e\beta_s+c(i,s-1)+c(s,j)\}\)<br>
\(c''(i,j)=min_{s\in(i,j]}\{c_2p(i,s-1)+c_1p(s,j)+\)<br>
\(e\beta_s+c(i,s-1)+c(s,j)\}\)<br>
\(c(i,j)=min\{c'(i,j),c''(i,j)\}\)<br>
\(p(i,j)=p(i,s-1)+\beta_s+p(s,j)\forall s\)

where the root case is \(c(0,n')\) and _p(i,j_) is usually calculated using the optimizing _s_ for the overall subtree in question.

Again, one can generalize this as in (3); for example, the cost of an equality comparison need not be fixed. A further generalization in which the equality comparison key value<tbc>


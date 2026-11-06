## 2 Baseline

We will work with randomly generated binary trees of 100 to 10<sup>7</sup> nodes. In each case, we follow Knuth [10] and assign weights to the nodes using Zipf’s Law [18], so that the _n<sup>th</sup>_ most popular node has relative probability 1_/n_. A variety of other authors have concluded both through observation [3,4, and others] and theory [1, and others] that Zipf’s Law reasonably approximates the relative number of accesses to any particular web site, and therefore presumably the number of searches for a particular word or phrase on the Internet as well.<sup>2</sup>

For each size of tree investigated, we consider five basic types of trees: simple binary trees, treaps, weight-balanced trees, splay trees, and trees that are provably optimal given the underlying weight distribution. For splay trees, we generate random but appropriately distributed queries and repeatedly move the node being searched for to the root of the tree. The number of queries generated is 3_n_, where _n_ is the size of the tree.

Optimal orderings were only computed for trees of 50,000 nodes or fewer. Both the time and (more importantly) the memory needed by the best known algorithm here [10] are _O(n_<sup>2</sup>) where _n_ is the number of nodes in the tree, and _n\>_50000 was simply too large to be practical on the machine being used (a 32-core AMD Ryzen with 128GB of memory).

All experiments used 500 samples for each size considered, and the basic results appear in Figure 1. Tree size is on the _x_-axis using a log scale, and the average number of node expansions during a single (assumed to be successful) search is on the _y_-axis.

The curves in the legend are ordered from worst to best; simple binary trees perform the worst (not surprisingly), followed by splay trees, followed by treaps, and weight-balanced binary trees perform the best. Expected cost is essentially linear in the log of the size of the search tree, as one might expect.

## 3 Technique

We now turn to our new idea, which is simply to hill climb using rotations to improve the expected cost of the tree.

**Definition 1** _Let T be a tree. T will be called_ weighted _if there is a function_ \(p:T\rightarrow\text{\textit{IR}}\) _that assigns a weight to each node in T and for which_ \(\sum_{x\in T}p(x)=1\).

_If_ \(x\in T\) _is not the root of T, we will denote the parent of x by_ \(\pi(x)\).

_We will use_ \(\emptyset\) _as a placeholder for a node that is not in T. So, for example, we take_ \(\pi(x)\) _to be_ \(\emptyset\) _if x is the root of the tree._

<sup>2</sup> Some authors suggest that the popularity of node _n_ should be proportional to \(n^{-\alpha}\) for some \(\alpha\) but it appears both that the results we present are not terribly dependent on the exact nature of the distribution in question and that \(\alpha\) is close to one in any event.


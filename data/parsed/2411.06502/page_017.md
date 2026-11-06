## 2.5 Organization of the paper

The structure of this paper is as follows. In Section 3, we introduce the remaining notation not covered in this section. Next, in Section 4, we present an algorithm for computing border-to-border distances in forest alignment graphs within APSP time. With this algorithm in hand, we extend the caterpillar algorithm to the SED problem in Section 5, where we shift from a path-based approach to more formal and concise notation, offering a clearer treatment of the problem. Both Section 4 and Section 5 are structured to first discuss complexity in terms of the larger of the two input forests which is optimal when forests are similar in size. In the second part of these sections, we provide a more detailed analysis suited for unbalanced cases by parameterizing the complexity by both forest sizes. In these sections, we provide algorithms for both weighted and unweighted TED, in particular noting when the unweighted TED problem can be computed more efficiently. In Section 6, we show how to solve TED using SED, providing a generic reduction for both weighted and unweighted TED, thus completing the proofs in this paper.

## 3 Preliminaries

**Set notation.** For integers \(i,j\in\mathbb{Z}\), we use the notation [_i..j_] to represent the set {_i,...,j_}, and [_i..j_) to denote the set {_i,...,j_-1}. We define (_i..j_] and (_i..j_) similarly.

Consider the infinite grid \(\mathbb{Z}\times\mathbb{Z}\), and consider a subset of the form of a rectangle [_a..b_] ×[_a'..b_] for some \(a,b,a',b'\). We define \(B^\perp(a,a',b,b')\) and \(B^\top(a,a',b,b')\) to be set of grid points located at the bottom-left and upper-right border of such rectangle [_a..b_] ×[_a'..b_]. Put more formally:

**Definition 3.1.** _For integers_ \(a,a',b,b'\) _we define_

\(B^\top(a,a',b,b'):=(\{b\}\times[a'..b'])\cup([a..b]\times\{b'\}),\text{\textit{and}}\)<br> \(B^\perp(a,a',b,b'):=(\{a\}\times[a'..b'])\cup([a..b]\times\{a'\}).\)

**Notation on ordered trees.** For consistency, we adopt most of the notations for TED from [Mao22].

In TED we work with ordered trees. For a tree **T**, we denote its root as root(**T**). We also treat a forest **F** as ordered, meaning that the sequence of trees within the forest is relevant. In this context, we can view a forest **F** as a tree with a _virtual root_, whose children are the roots of the trees in **F**, ordered from left to right as they appear in the forest.

For a tree \(\mathbf{T}\in\mathbf{F}\), let **F**\\**T** represent the forest obtained by removing **T** from **F** while preserving the order of the remaining trees. We use |**F**| to denote the number of nodes in **F**. Occasionally, we may also abuse notation by using **F** to refer to the set of nodes in the forest, though the context will make this clear. For two forests **F** and \(\mathbf{F}'\), we denote their concatenation (from left to right) as \(\mathbf{F}+\mathbf{F}'\). An empty forest is denoted by \(\emptyset\). For a node \(v\in\mathbf{F}\), we let sub(_v_) represent the subtree rooted at _v_.

Finally, we write rev(**F**) for the _reversed forests of_ **F**, obtained by taking each node of **F** (including its virtual root), and reversing the order of the children.

**Bi-order traversal.** To compute the similarity between forests, we use the notation introduced by [Mao22], which allows us to conveniently index subforests of **F** and express calculations in a way that is well-suited to max-plus products.

**Definition 3.2** ([Mao22, Definition 2.3])**.** _Consider the depth-first traversal of a forest_ **F** _starting from the virtual root, with subtrees recursively traversed from left to right. From that we can generate an_ bi-order traversal sequence _of length_ 2|**F**|_, where each node appears twice, in the following way:_

_Start from the empty sequence._


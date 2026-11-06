# Unbalancing Binary Trees

**Matthew L. Ginsberg**

the date of receipt and acceptance should be inserted later

**Abstract** Assuming Zipf’s Law to be accurate, we show that existing techniques for partially optimizing binary trees produce results that are approximately 10% worse than true optimal. We present a new approximate optimization technique that runs in _O(n_log_n_) time and produces trees approximately 1% worse than optimal. The running time is comparable to that of the Garsia-Wachs algorithm but the technique can be applied to the more useful case where the node being searched for is expected to be contained in the tree as opposed to outside of it.

### 1 Introduction

Binary trees are often used to store and index large amounts of data. Many such trees are balanced in the sense that the left and right children of any particular parent are similar in size. A consequence of this is that every node can be reached in at most log<sub>2</sub>(_n_) steps from the root of the tree, where _n_ is the tree’s size.

While a bound on worst case performance is obviously desirable, a bound on _average_-case performance may be more important in an environment where large trees are searched often. Note that in cases where searches are frequent indeed, statistical information gathered from past searches can be used to determine the probability _p(x_) that a particular node _x_ in the tree is the target of a randomly selected query. If we denote the depth of a node _x_ by _d(x_), the problem of optimizing for average-case performance becomes that of

M.L. Ginsberg<br> Eugene, OR 97405<br> https://orcid.org/0000-0001-9343-354X<br> E-mail: mlginsberg@gmail.com

arXiv:2208.14481v1 [cs.DS] 30 Aug 2022


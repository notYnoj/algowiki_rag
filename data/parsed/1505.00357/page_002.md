(ii) stops if _v_ equals the key, or (iii) recurses right if _v_ is larger, halting at a leaf. The comparisons made in the search must suffice to determine the relation of _v_ to all keys in K. (Hence, _T_ must have 2|K|+1 leaves.) _T_ is optimal if it has minimum _cost_, defined as the expected number of comparisons assuming the query _v_ is chosen randomly from the specified probability distribution.

Knuth assumed _three-way_ comparisons at each node. With the rise of higher- level programming languages, most computers began supporting only two-way comparisons (\(<,\le,=,\ge,>\)). In the 2nd edition of Volume 3 of _The Art of Computer Programming_ [14, §6.2.2 ex. 33], Knuth commented

_...machines that cannot make three-way comparisons at once...will have to make two comparisons...it may well be best to have a binary tree whose internal nodes specify either an equality test_ **or** _a less-than test but not both._

But Knuth gave no algorithm to find a tree built from _two-way_ comparisons (a 2wcst, as in Fig. 2(a)), and, prior to the current paper, poly-time algorithms

were known only for restricted variants. Most notably, in 2002 Anderson et al. [1] gave an _O(n_<sup>4</sup>)-time algorithm for the _successful-queries_ variant of 2wcst, in which each query _v_ must be a key in K, so only |K| leaves are needed (Fig. 2(b)). The _standard_ problem allows arbitrary queries, so 2|K|+1 leaves are needed (Fig. 2(a)). For the standard problem, no polynomial-time algorithm was previously known. We give one for a more general problem that we call 2wcst:

**Theorem 1.** 2wcst _has an O(n_<sup>4</sup>)_-time algorithm._

v ? O
< <
v ? H
v=O
v ? W
< <
< <
v<H
v=H
H<v<O
O<v<W
v=W
W<v

(a)
(b)
v
v
yes
v < O?
no
yes
no
v = H?
v < W?
v=H
v = O?
y
n
y
n
y
n
v=H
v < H?
v = O?
v = W?
v=O
v=W
y
n
y
n
y
n
v<H
H<v<O
v=O
O<v<W
v=W
W<v

**Fig. 1.** A binary search tree _T_ using 3-way comparisons, for K={_H,O,W_}.

**Fig. 2.** Two 2wcsts for K={_H,O,W_}; tree (b) only handles _successful_ queries.


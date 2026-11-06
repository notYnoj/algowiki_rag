# Dynamic Trees with Almost-Optimal Access Cost

**Abstract**

An optimal binary search tree for an access sequence on elements is a static tree that minimizes the total search cost. Constructing perfectly optimal binary search trees is expensive so the most efficient algorithms construct _almost optimal_ search trees. There exists a long literature of constructing almost optimal search trees _dynamically_, i.e., when the access pattern is not known in advance. All of these trees, e.g., splay trees and treaps, provide a _multiplicative_ approximation to the optimal search cost.

In this paper we show how to maintain an almost optimal weighted binary search tree under access operations and insertions of new elements where the approximation is an _additive_ constant. More technically, we maintain a tree in which the depth of the leaf holding an element _ei_ does not exceed min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1) where _wi_ is the number of times _ei_ was accessed and _W_ is the total length of the access sequence.

Our techniques can also be used to encode a sequence of _m_ symbols with a dynamic alphabetic code in _O(m_) time so that the encoding length is bounded by _m(H+O_(1)), where _H_ is the entropy of the sequence. This is the first efficient algorithm for adaptive alphabetic coding that runs in constant time per symbol.

<sup>∗</sup>Hong Kong University of Science and Technology. Email `golin@cse.ust.hk` <sup>†</sup>Université libre de Bruxelles and New York University. Email `johniacono@gmail.com`. Supported by NSF grants CCF-1319648, CCF-1533564, a Fulbright Fellowship, and by the Fonds de la Recherche Scientifique-FNRS under Grant no MISU F 6001 1. <sup>‡</sup>Université libre de Bruxelles. Email `sl@slef.org`. Directeur de recherches du Fonds de la Recherche Scientifique- FNRS. <sup>§</sup>Cheriton School of Computer Science, University of Waterloo. Email `imunro@uwaterloo.ca` \(^\unknown\)Cheriton School of Computer Science, University of Waterloo. Email `yakov.nekrich@googlemail.com`

Mordecai Golin<sup>∗</sup> John Iacono<sup>†</sup> Stefan Langerman<sup>‡</sup> J. Ian Munro<sup>§</sup> Yakov Nekrich<sup>¶</sup>

June 28, 2018


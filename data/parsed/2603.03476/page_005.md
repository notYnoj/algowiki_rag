of the group. Consequently, _xx_ can be considered a motif of _S_ with a support value of 75%. In general, motif discovery aims to identify recurring substrings along with their frequencies and supports within the dataset.

## 3.2 Order Preserving Matching (OPM)

Order preserving matching (OPM) is a pattern matching paradigm that compares strings based on the relative ordering of their elements while ignoring absolute values [14]. OPM is particularly suited for numerical strings, where relative trends are more informative than precise magnitudes. Formally, two strings _p_ and _t_ of equal length _n_ are said to form an _order preserving match_ if, for all \(i,j\in\{1,\dots,n\}\),

\(p[i]\le p[j]\Longleftrightarrow t[i]\le t[j].\)

That is, the pairwise ordering relations between elements in _p_ and _t_ must be identical. For example, the strings (2,9,4) and (1,3,2) form an OPM match because both follow the same ordinal pattern: first element _\<_ third element _\<_ second element.

In OPM-based motif discovery, motifs are defined as substrings that recur across a collection of strings while preserving exact ordinal relationships between their elements. Unlike traditional motif discovery, which relies on exact symbol matching, OPM motifs capture recurring relative trends such as consistent increases, decreases, or local extrema. Due to its strict definition, OPM-based motif discovery identifies only highly stable and repeatable ordinal patterns. Any deviation in the relative ordering of values prevents a match, making OPM motifs particularly precise but less tolerant to noise or small fluctuations.

## 3.3 Cartesian Tree Matching (CTM)

Cartesian tree matching (CTM) is a shape-based pattern matching approach that represents a numerical string as a Cartesian tree, capturing its hierarchical structure of local minima and maxima [15]. This representation allows CTM to identify similarities between strings even in the presence of minor ordinal variations.

A Cartesian tree _CT(p_) for a string _p_ is defined recursively [21]:

• If _p_ is empty, then _CT(p_) is empty.<tbc>

• Otherwise, let _p[i_] be the leftmost minimum element in _p_. The root of _CT(p_) corresponds to _p[i_], its left subtree is _CT(p_[1_...i_-1]), and its right subtree is _CT(p[i_+1_...n_]).

In other words, the smallest value in the string becomes the root of the tree, and the same construction rule is applied recursively to the substrings on either side. Two strings _p_ and _t_ are said to form a CTM match if their Cartesian trees have identical shapes, regardless of the actual node labels. For example, the strings (7,2,16,4,8) and (10,5,17,9,18) share the same Cartesian tree structure, as illustrated in Figure 1.


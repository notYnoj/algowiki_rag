**Lemma 3.6.** _All approximate sorting algorithms are_ gap-preserving.

_Proof._ We can shift the elements on one side of the gap arbitrarily far away without affecting any comparison results. Thus, if there exists an input for which a \(\tau(n)\)-approximate algorithm is not gap-preserving, then we can make the approximation factor larger than \(\tau(n)\) by shifting one side by more than that, a contradiction.

Recall that the `Tournament` algorithm for sorting a set _X_ of items, as originally defined in \[AFHN15\], does all pairwise comparisons, and orders the items by the number of "wins" they have (i.e. the number of elements that compare less).

**Lemma 3.7.** _`Tournament` is a_ 2_-approximate sorting algorithm._

_Proof._ If _x<sub>i</sub>\>x<sub>j</sub>_+2, _x<sub>i</sub>_ must compare greater than all elements \(\le x_j+1\) including _x<sub>j</sub>_. However, _x<sub>j</sub>_ can at most compare greater than all elements \(\le x_j+1\) excluding itself, so it must come before _x<sub>i</sub>_ as desired.

We show that partitioning as in quicksort guarantees a good approximation factor, which will be the basis of our randomized sorting algorithm. This was originally shown in \[AFJ<sup>+</sup>18\].

**Lemma 3.8.** _Let x<sub>i</sub> be some item in a set X. Let S_={_x<sub>j</sub>|x<sub>j</sub>\<<sub>c</sub>x<sub>i</sub>_} _and T=X_\\_S. We must have_ \(T\ge_2S\).

_Proof._ All elements of _S_ must be \(\le x_i+1\), and all elements of _T_ must be \(\ge x_i-1\). Thus, for \(x_j\in S,x_k\in T\), \(x_j-x_k\le x_i+1-(x_j-1)=2\) as desired.

**Lemma 3.9.** _If a sorting algorithm repeatedly partitions the input set X into two sets S,T such that_ \(T\ge_kS\)_, recursively sorts S and T and then concatenates them, it is guaranteed to result in a k-approximate sorting._

_Proof._ Assume for the sake of contradiction that there exist _x<sub>i</sub>,x<sub>j</sub>_ for _i\>j_ in the final order such that \(x_i\unknown\ge_kx_j\). We must have put _x<sub>i</sub>_ in _T_ and _x<sub>j</sub>_ in _S_ in some recursive call, but this contradicts \(T\ge_kS\), as desired.

Throughout, when referring to a sorted order, we assume a fixed sorted order with ties broken arbitrarily. Unless otherwise stated, all logarithms are base _e_. We often ignore rounding errors that vanish for large _n_.

## 4 A Randomized Sorting (and Selection) Algorithm

In this section we prove Theorem 1.5 by describing an algorithm `RSort`. This algorithm is similar to quicksort in the sense that we aim to partition the original set of items _X_ into two sets _S,T_, and then recursively sort _S_ and _T_ and concatenate them. Recall by Lemma 3.9 that it is sufficient to have \(T\ge_4S\) in every call. Thus, our algorithm aims to find a partition _S,T_ of _X_ such that \(T\ge_4S\). To ensure the recursion depth is _O_(log|_X_|), we also aim to have \(|S|,|T|\ge\frac{|X|}{8}\) . Our algorithm consists of three phases, which we will analyze independently. Throughout the algorithm, we let _n_ be the size of the current set _X_ the function is being called on, and we let _N_ be the size of the initial set _X_ that `RSort` was called on. This distinction is important, as we want our probability guarantees to be with respect to the size of the original caller.


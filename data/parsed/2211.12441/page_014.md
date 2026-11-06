**Algorithm 1** BuildRanking(_C_)

**Input:** DAG _C_ on vertex set _X_

**Output:** ranking of _X_ that is a linear order of _C_

1: \(T\leftarrow\varnothing\)

2: **for** _r_=1 to _n_ **do**

3: \(x\leftarrow\) arbitrary element of \(S\doteq\{v\in X|\text{there is no}u\in X\backslash T\text{with}u\unknown v\text{in}G\}\)

4: \(\rho^{-1}(r)\leftarrow x\)

5: \(T\leftarrow T\cup\{x\}\)

end of iteration _r_-1, the edge \(\rho^{-1}(r-1)\unknown\rho^{-1}(r)\) prevents _x_ from being in _S_. Thus, whenever \(\rho^{-1}(r-1)\unknown\rho^{-1}(r)\), the item \(x=\rho^{-1}(r)\) is _lucky_ in the sense that it gets picked in step 3 as soon as it enters the set _S_. In fact, the lucky items with respect to a ranking \(\rho\in R\) are exactly those for which \(\rho^{-1}(r-1)\unknown\rho^{-1}(r)\) for some \(r\in\{2,\dots,n\}\), as well as the item \(\rho^{-1}(1)\) with rank 1. In Figure 5 the lucky items are marked black. Their number equals \(\mathrm{deg}_\overline{H}(\rho)+1\).

In order to generate a ranking \(\rho\) using BuildRanking, it suffices to know:

(a) the lucky items (as a set, not their relative ordering), and<tbc>

(b) the ordering of the non-lucky items (given which items they are).

This information suffices to make the correct choices in step 3 of Algorithm 1:

o If the set _S_ contains a lucky item, there will be a unique lucky item in _S_; pick it as the element _x_.<tbc>

o Otherwise, pick for _x_ the first item in the ordering of the non-lucky items that is not yet in _T_. Such an element will exist, and all the items that come after it in the ordering are not yet in _T_ either.

If \(\rho\) has degree \(d=\mathrm{deg}_\overline{H}(\rho)\), then there are _d_+1 lucky items, so there are at most \(\genfrac(){pt}{2}{n}{d+1}\) choices for (a), and at most (_n-d_-1)! choices for (b), resulting in a total of at most \(\genfrac(){pt}{2}{n}{d+1}\cdot(n-d-1)!=\frac{n!}{(d+1)!}\) choices. This proves Claim 19.

**Remark 20.** Suppose we allow an algorithm _A_ to have multiple valid execution traces on a given input \(\rho\), and let _R<sub>i</sub>_ denote the set of rankings on which the _i_-th execution trace is valid. The proof of Claim 19 carries over as it considers individually sets _R<sub>i</sub>_, and only depends on the DAG that the comparisons in _R<sub>i</sub>_ induce. The rest of the proof of Lemma 17 carries through modulo the first equality in (2), which no longer holds as the sets _R<sub>i</sub>_ may overlap. However, the equality can be replaced by the inequality \(\ge\), which does hold and is sufficient for the argument. This means that we can replace \(\mathrm{D}(\Pi)\) in the statement of the Sensitivity Lemma by its nondeterministic variant \(\mathrm{N}(\Pi)\).

## 4 Sensitivity Approach for General Trees

In this section we analyze the average sensitivity of the problem \(\Pi_T\) of inversion minimization on a tree _T_ with a general shape. In Section 4.1 we show that the existence of a subtree containing a fair fraction of the leaves implies high sensitivity. The lower bound on query complexity for \(\Pi_T\)<tbc>


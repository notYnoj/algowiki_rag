<tbc>Recall that we are assuming that for any particular node \(x\in T\), the weight _p(x_) is the probability that _x_ is the target of a randomly selected search query. The essential point underlying our ideas is that the impact of bumping \(x\in T\) can be computed exactly based purely on values of a handful of nodes surrounding _x_.

**Definition 4** _For a node x in a tree T, we will denote by <o>x</o> the subtree of T rooted at x. We will denote by <o>p</o>(x_) _the aggregated weight of the points in <o>x</o>:_

\(\overline{p}(x)=\sum_{y\in\overline{x}}p(y).\)

_We take_ \(\overline{\emptyset}=\emptyset\) _(the empty set), and thus_ \(\overline{p}(\emptyset)=0\).

**Proposition 5** _Let T be a weighted binary tree, and x a non-root node in T. Then_

\(C(T)-C(T^x)=p(x)+\overline{p}(\lambda(x))-p(\pi(x))-\overline{p}(\sigma(x))\) (1)

**Proof.** This is clear. Examining Figures 2 and 3, we see that the node _b_ has its depth reduced by 1, reducing the expected cost of a lookup by _p(b_); the node \(a=\pi(b)\) has its depth increased by 1. The entire subtree rooted at \(c=\lambda(b)\) has its depth decreased by 1, reducing the cost by \(\overline{p}(\lambda(b))\) while the subtree rooted at \(e=\sigma(b)\) has its depth increased by 1. Right bumps are similar, and (1) follows.

**Definition 6** _We will refer to the quantity in (1) as the_ merit _of bumping x, denoting it by_ \(\mu(x,T)\)_, or simply by_ \(\mu(x)\) _if no ambiguity is possible._

_If T is a weighted binary tree, we will say that the_ result of bumping _T, to be denoted_ \(\beta(T)\)_, is:_<tbc>

\(\beta(T)=\left\{\begin{array}{ c c }
\{T\}, & \text{\textit{if}}\mu(x,T)\le 0\text{\textit{for all}}x\in T\text{\textit{;}} \\
\{T^x|\mu(x,T)\text{\textit{is maximal}}\}, & \text{\textit{if}}\mu(x,T)>0\text{\textit{for some}}x\in T.
\end{array}\right.\)

<tbc>_For an integer_ \(k\ge 0\)_, we define_ \(\beta^k(T)\) _recursively by_ \(\beta^0(T)=\{T\}\) _and_

\(\beta^k(T)=\cup_{t\in\beta^{k-1}(T)}\beta(t)\)

The notation would be somewhat simpler (but less precise) if we either assumed there to be a unique \(x\in T\) for which \(\mu(x)\) was maximal, or allowed \(\beta(T)\) to be the result of bumping _T_ by an arbitrarily selected _x_ if multiple choices were available.

Since we only bump trees at nodes that have positive merit, we immediately have:

**Lemma 7** _Let T be a weighted binary tree and_ \(T'\) _any element of_ \(\beta(T)\)_. Then_ \(c(T)\ge c(T')\)_, with equality if and only if_ \(\beta(T)=T\).

**Proposition 8** _Let T be a weighted binary tree. Then there is some finite k such that_ \(\beta^{k+1}(T)=\beta^k(T)\).


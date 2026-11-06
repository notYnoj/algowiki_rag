**Lemma 4.7.** _There is a randomized algorithm that, given a 3SUM instance_ (_A,B,C_) _and integer parameters_ \(p,s\ge 1\) _and sets_ \(X,Y_1,\dots,Y_k\subseteq\mathbb{Z}\) _satisfying_ \(C\subseteq Pop(X,Y_1,\dots,Y_k;p)\)_, computes_

• _a subinstance_ \((A,B'\subseteq B,C)\) _so that_ \(B'\subseteq Pop(X,Y_1,\dots,Y_k,-A;p')\) _for_ \(p'=p|A|/s\)_, and_<tbc>

• _a set of 3SUM solutions_ \(\mathcal{T}\subseteq A\times B\times C\),<tbc>

<tbc>_so that each solution is either part of the subinstance or part of_ T _. The algorithm runs in time_<tbc>

\(\widetilde{O}\big(\frac{s|X||Y_1|\dots|Y_k|}{p}+|A||X|+\frac{|B||Y_1|\dots|Y_k|}{p}+\frac{|A||B|}{s}\big).\)

<tbc>**Proof.** Let \(p'=p|A|/s\). We run Lemma 3.3 to compute a set _P_ satisfying

\(Pop(X,Y_1,\dots,Y_k,-A;2p')\subseteq P\subseteq Pop(X,Y_1,\dots,Y_k,-A;p').\)

We call an item \(b\in B\) _popular_ if \(b\in P\) and _unpopular_ otherwise, and deal with the unpopular and popular items separately.

• _(Unpopular Items)_ Our strategy is to list all solutions _a+b=c_ involving an unpopular item _b_. Let \(Y\subseteq Y_1+\cdots+Y_k\) be the set obtained by sampling some tuples \((y_1,\dots,y_k)\in Y_1\times\cdots\times Y_k\) uniformly at random with rate min(1_,R/p_) for some \(R=\Theta(logn)\); for each such tuple we insert the sum \(y_1+\cdots+y_k\) into _Y_ . Then we run a meet-in-the-middle algorithm to explicitly list all solutions<tbc>

<tbc>\(a+b=x+y\)<tbc>

<tbc>with \((a,b,x,y)\in A\times(B\backslash P)\times X\times Y\) . Note that this condition is equivalent to<tbc>

<tbc>\(a-x=y-b,\)<tbc>

<tbc>an application of "Fredman’s trick" \[Fre76\]. More specifically, enumerate all pairs \((a,x)\in A\times X\), and store each pair in a hash table (with collision lists) indexed by _a-x_. Then we enumerate all unpopular \(b\in B\backslash P\) and all \(y\in Y\) , and further list all entries (_a,x_) in the hash table at index _y-b_. For each 4-tuple (_a,b,x,y_) listed in this way we test if \(a+b\in C\). We will show that this algorithm indeed lists any 3SUM solution involving an unpopular item.<tbc>

• _(Popular Items)_ The only 3SUM solutions not listed in the previous step are those involving a popular item _b_, i.e., the solutions of the subinstance \((A,B',C)\) for \(B'=B\cap P\). Recall that also \(B'\subseteq Pop(X,Y_1,\dots,Y_k,-A;p')\) by construction.

## Correctness.

We show that the first case of the algorithm indeed lists all solutions _a+b=c_ involving an unpopular item _b_. From the initial assumption \(C\subseteq Pop(X,Y_1,\dots,Y_k;p)\) we get that _c_ can be expressed in at least _p_ ways as

\(c=x+y_1+\cdots+y_k,\)

for \(x\in X\) and \(y_i\in Y_i\). Each such representation corresponds to a unique tuple (_y_<sub>1</sub>_,...,y<sub>k</sub>_) (as each such tuple uniquely determines _x_ via \(x=c-y_1-\cdots-y_k\)). By construction of _Y_ , with high probability \(1-exp(-O(R))=1-1/n^{\Omega(1)}\), at least one such tuple (_y_<sub>1</sub>_,...,y<sub>k</sub>_) is present in _Y_ in the form \(y=y_1+\cdots+y_k\). In particular, _c_ can be expressed as _c=x+y_ for some \(x\in X\) and \(y\in Y\) , and therefore there is a solution _a+b=x+y_. This solution is detected by the algorithm, and the correctness follows.


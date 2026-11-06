the heart of our algorithm lies a curious win-win paradigm: Either we can solve the instance by a clever brute-force algorithm, or we can _amplify_ structure.

Specifically, to find a 3SUM solution _a+b=c_ we could try to enumerate _all_ solutions<tbc>

\(a+b=x_1+x_2,\text{for}a\in A,b\in B,x_1,x_2\in X.\) (1)

<tbc>For each such solution we can test if _a+b=x_<sub>1</sub>+_x_<sub>2</sub> is actually an element in _C_; only then have we found a solution. This might seem like overkill--after all we are listing many more solutions than necessary. But the crucial advantage is that solutions to this equation can be listed very efficiently. Indeed, rewriting each solution as

\(a-x_1=x_2-b,\)

a natural meet-in-the-middle algorithm is to preprocess the sets _A-X_ and _X-B_ in time _O_(|_A_||_X_|+|_B_||_X_|)=\(O(n^{2-\epsilon})\). Afterwards, we can list all solutions in time _O(N_), where _N_ denotes the number of solutions. If \(N\le n^{2-\delta}\), say, then this algorithm runs in subquadratic time. But of course, _N_ might be much larger, possibly up to \(|X|^2n=n^{3-2\epsilon}\), and in that case the meet-in-the-middle strategy is doomed.

Our key insight is that, in this situation, the sets _A_ and _B_ admit amplified structure. Concretely, focus on _B_. For simplicity, assume that all elements \(b\in B\) participate in roughly the same number of solutions to Equation (1), i.e., in about _N/|B_| solutions. Then, in other words, each \(b\in B\) is an \(N/|B|\ge n^{1-\delta}\)-popular sum in the set _X+X-A_. Note that we started from the structural information that \(C\subseteq X+X\), but ended up with the information that _B_ is covered by the \(n^{1-\delta}\)- popular sums in _X+X-A_. It turns out that this argument can be iterated. By arguing as above, but exchanging the roles of _B_ and _C_, we can either solve the instance, or further derive that _C_ is covered by the \(n^{2-2\delta}\)-popular sums in _X+X-A+A_. And iterating this argument _k_ times, we eventually infer that _C_ is covered by the \(n^{2k-2k\delta}\)-popular sums in _X+X-kA+kA_.

At this point, _C_ witnesses an \(n^{2k-2k\delta}\)-popular sum in _X+X-kA+kA_. This is where our structure theorem (Theorem 1.2) comes into play. When carefully applied, it implies that there is some low-doubling set _H_ of size at about \(|X|^2n^{2k\delta}\le n^{2-2\epsilon+2k\delta}\) that covers a large fraction of _A_. Here, intuitively think of \(\delta\) as an extremely small constant, so that the \(2k\delta\) term effectively becomes 0. That is, intuitively, we have showed that _A_ is covered by a low-doubling set of size |_X_|<sup>2</sup>. All in all, it is quite intriguing _how_ the structure amplifies: We start from a weakly structured set _C_, then infer some more structure for _B_, then again for _C_, and so on. And eventually, we conclude that _A_ admits a small low-doubling container. Besides, it is interesting that for a 3SUM algorithm the relevant structure lies in the number of _k_-sums.

Of course, we are not completely done. What remains is a 3SUM instance (_A,B,C_) equipped with a container set \(H\supseteq A\) of size \(|H|\le n^{2-\epsilon}\) and with arbitrarily low doubling. But this instance can be dealt with following ideas that have already appeared in earlier work (notably, \[JX23\]), and for this reason we defer further details to Section 4.

## 1.6.2 Universe Reduction for Min-Plus Convolution

Finally, we give a brief glimpse into our new universe reduction. Only at this point will it become clear why the rank of a set is a reasonable notion in our context.

For concreteness, focus on the universe reduction from \[_n_\] to \([\sqrt{n}]\). That is, we argue that if Min-Plus Convolution over the universe \([\sqrt{n}]\) is in time \(O(n^{3/2-\epsilon})\), then Min-Plus Convolution over<tbc>


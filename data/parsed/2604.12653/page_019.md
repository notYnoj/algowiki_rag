the value _k_ only counts insert operations for which the inserted item remains in the heap until _x_ is extracted. In other words, the value _k_ skips items that are extracted before _x_ is extracted.

We designed Definition 1 to be a simple version of the unified bound for Heaps which is sufficient for our result on sorting under partial information. However, our heap construction can be adapted to achieve a stronger but more complicated version of the unified bound. Recall that we consider a sequence of insert and extractMin operations where an item _x_ is the _a(x_)-th item to be inserted and the _b(x_)-th item to be extracted. We modify Definition 1 and decrease the term |_a(x_)-_a(y_)| by only counting items inserted between _x_ and _y_ that are still in the heap. This yields:

**Definition 25.** _A heap data structure has the_ immediate unified bound _if it supports_ insert(_x_) _in amortized O_(1) _time, the very first_ extractMin _operation in amortized O_(1) _time, and subsequent_ \(x\leftarrow\text{extractMin}()\) _operations in amortized time_

\(O\big(min_{y\in Xb(y)<b(x)}\big(1+log|A(x,y)|+log(b(x)-b(y))\big)\big),\)

_where_ \(A(x,y):=\{z\in X|b(z)\ge b(x)\wedge min(a(x),a(y))\le a(z)\le max(a(x),a(y))\}\).

We sketch how the construction in Section 5 can be adapted to the immediate unified bound. This time, we consider up to _n_ leaves, numbered by some subsequence of \[_n_\]. Non-existent numbers correspond to leaves that have been deleted. Let _t_ be a time counter that starts at 0. Every integer \(i\in[n]\) has a last access time _s(i)\<t_. We define \(\overline{d}(i):=1+min_{1\le j\le n}(log(1+|\{k|\text{leaf}k\text{exists}\wedge min(i,j)\le k\le max(i,j)\}|+log(1+t-s(j)))\). Note that every integer _j_ can be used as a finger, even if no leaf _j_ exists.

**Theorem 26.** _\[Improved Theorem 12\] There is a data structure that maintains a rooted binary tree on top of up to n leaves numbered by some subsequence of_ \[_n_\] _that each store an item, such that each node in the tree stores its subtree minimum and every leaf i has depth O_(<o>_d_</o>(_i_))_. The data structure supports the operations, where i is an integer for which a leaf exists:_

• addLeaf(_x): In amortized O_(1) _time, increment n and add a new leaf with index n, value x, and_ \(s(n)=-\infty\).<tbc>

• access(_i): In amortized O_(<o>_d_</o>(_i_)) _time (computed before the operation), set s(i_)=_t and then increment t. For the very first access operation,_ <o>_d_</o>(_i_) _is ill-defined, so we require a bound of amortized O_(1) _time instead._<tbc>

• changeKey(_i,x): In O_(<o>_d_</o>(_i_)) _time, replace the item stored at leaf i with x._<tbc>

• deleteLeaf(_i): In O_(<o>_d_</o>(_i_)) _time, delete the leaf i._

_The data structure may remodel the internal tree nodes arbitrarily (within the allowed time bounds). The leaves do_ not _need to be stored in order._

Given Theorem 26, we obtain a heap with the immediate unified bound (Definition 25) as before, except that extractMin invokes deleteLeaf(_i_) instead of changeKey\((i,\infty)\).

## 6.1 Modifying our Heap Construction

We briefly sketch the changes necessary to go from Theorem 12 to Theorem 26. We call an integer \(i\in[n]\) _alive_ if the leaf _i_ still exists, and _dead_ otherwise. Each leaf of the main tree corresponds to an integer in \[_n_\] that is either dead or alive, but among two consecutive leaves, we require at least<tbc>


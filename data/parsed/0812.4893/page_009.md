### 3.4 Centralised Constant-Time Algorithms and Matchings

Our centralised constant-time approximation algorithm in Theorem 3 is based on the ideas of Parnas and Ron [29] and Nguyen and Onak [28]. Their work presents constant-time approximation algorithms for estimating the size of a maximal matching, maximum-cardinality matching, and maximum-weight matching. Our work complements this line of research by presenting an algorithm for estimating the size of a stable matching.

## 4 Algorithm

We work with the following distributed variant of the Gale-Shapley algorithm. Each blue node \(b\in B\) maintains the variable _p(b_) which is the match of _b_ in the current matching or \(\perp\) (_b_ is unmatched). Each red node \(r\in R\) maintains the following variables: _C(r_) is the list of candidates for matching; _c(r_) is the candidate from whom _r_ is waiting for a response or \(\perp\) (_r_ has no current candidate); and _p(r_) is the match of _r_ in the current matching or \(\perp\) (_r_ is unmatched).

The algorithm executes in _rounds_. Each round consists of two _turns_, a _blue turn_ followed by a _red turn_. Each node \(v\in R\cup B\) is active during turns of its colour.

#### Blue turn.

Each blue node \(b\in B\) completes the following read-compute- write cycle. Initially, \(p(b)=\perp\).

1. Receive all incoming messages; let _P_ be the subset of neighbours that sent the message ‘propose’. If _P_ is empty, do nothing during this turn.<tbc>

2. If \(p(b)\neq\perp\), then set \(Q\leftarrow P\cup\{p(b)\}\); otherwise set \(Q\leftarrow P\).<tbc>

3. Let _q_ be the node in _Q_ most preferred by _b_.<tbc>

4. If \(q\neq p(b)\):<tbc>

(a) If \(p(b)\neq\perp\) then send the message ‘break’ to _p(b_).<tbc>

(b) Send the message ‘accept’ to _q_.<tbc>

(c) Set \(p(b)\leftarrow q\).<tbc>

5. For each \(r\in P\backslash\{q\}\):<tbc>

(a) Send the message ‘reject’ to _r_.<tbc>


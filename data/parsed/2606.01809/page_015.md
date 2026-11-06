## A Construction of the Last Interval Detection Data Structure

Let us now show how the data structure presented in Theorem 5.2 can be constructed. We restate the theorem here for convenience.

**Theorem 5.2.** _\[Last Interval Detection Data Structure\] Given a universe of size U, we can maintain a data structure that allows adding at time_ \(i\ge 1\)_, a sub-interval_ \([l_i,r_i]\subseteq[1,U]\)_, and for queries at time i where on input_ \(x\in[1,U]\)_, the data structure outputs the largest integer_ \(j\le i\)_, such that_ \(x\in[l_j,r_j]\) _where we assume that_ \[_l_<sub>0</sub>_,r_<sub>0</sub>\]=\[1_,U_\] _(so j is well-defined). If the length of the update sequence is polynomially bounded in n, then the data structure can be implemented with pre-processing time_ \(\tilde{O}(1)\) _and_ \(\tilde{O}(1)\) _worst-case update and query time._


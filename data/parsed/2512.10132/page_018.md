## 7.1 Necessity of the frontier term

The dependence on the frontier width \(\omega\) cannot be removed even in very permissive single-pass models that allow re-computation, so long as the algorithm respects the topological order and never revisits earlier input. Intuitively, any algorithm that tries to decide _which_ vertex on a wide frontier lies on the optimal path must keep enough information to distinguish among many possibilities until it has seen the rest of the instance.

We formalize this for a forward-only, one-pass model over the topological order.

**Proposition 2** (Frontier lower bound in single-pass models)**.** _Let_ A _be any deterministic algorithm that solves the Traceback Problem for all DP DAGs of frontier width at most_ \(\omega\)_, under the following restrictions:_

• _the input vertices and edges are presented in order of increasing_ \(\tau\) _(topological order);_<tbc>

• A _is allowed a single left-to-right pass over this stream, and never re-reads earlier input;_<tbc>

• A _may output the witness path in any order (e.g. from sink to source)._

_Then_ A _must use_ \(\Omega(\omega)\) _bits of work-tape space in the worst case._

_Proof._ We sketch an information-theoretic construction. For a given \(\omega\), consider a layered DAG with layers _L_<sub>0</sub>_,L_<sub>1</sub>_,...,L<sub>m</sub>_, where each layer _L<sub>k</sub>_ consists of \(\omega\) vertices \(\{v_{k,1},\dots,v_{k,\omega}\}\). Between _L_<sub>0</sub> and _L_<sub>1</sub>, we embed a gadget that realizes one of \(2^\omega\) possible patterns of which vertices in _L_<sub>0</sub> are "active" in the sense that they lie on some optimal path; for instance, by assigning large negative weights to edges leaving inactive vertices and non-negative weights to edges leaving active ones. Subsequent layers are arranged so that for each active vertex in _L_<sub>0</sub> there is a unique optimal continuation to the sink, and for each inactive vertex any path is strictly suboptimal.

The resulting DAG can be topologically ordered layer by layer, and any cut between _L_<sub>0</sub> and _L_<sub>1</sub> intersects exactly \(\omega\) vertices, so the frontier width is \(\Theta(\omega)\). By varying the pattern of active vertices in _L_<sub>0</sub>, we obtain \(2^\omega\) distinct DP instances, all of frontier width at most \(\omega\), that induce \(2^\omega\) distinct canonical witness paths.

Any single-pass algorithm A that reconstructs the optimal path must, at some point during the pass, be in distinct internal states for each of these \(2^\omega\) possibilities; otherwise two different instances would induce the same internal state and hence the same output. Thus the number of distinct internal states of A must be at least \(2^\omega\), implying a work-tape size of at least

\(log_2(2^\omega)=\omega\)

bits. This proves the claimed lower bound.

Proposition 2 shows that in any forward-only, single-pass model, the \(\omega\) dependency in Theorem 2 is qualitatively optimal: even when re-computation is free and the algorithm does not need to preserve the DP table, it must still reserve \(\Omega(\omega)\) bits of state to disambiguate different canonical witness paths.

Our offline random-access algorithm also uses \(O(\omega)\) space in words (plus lower-order polylog_T_ terms), which is \(O(\omega logT)\) bits. Thus, as far as the dependence on frontier width is concerned, the Universal Hirschberg bound cannot be improved by more than a logarithmic factor in general.

The remaining question is whether the additive polylog_T_ term can be reduced further (e.g. to _O_(log_T_) or even _O_(1)), or whether some form of logarithmic overhead is inherent in traceback once indices and values must be manipulated explicitly.

## 7.2 \(\sqrt{T}\)-type terms and streaming models

Our main upper bound

\(S(T,\omega)=O\big(\omega logT+polylogT\big)\text{bits}\)

holds in the offline random-access model: we can repeatedly "restart" forward DPs from arbitrary vertices and time intervals at no additional space cost, and the only recursion overhead is the stack of size _O_(polylog_T_).

In contrast, in a strictly _streaming_ model, the DAG _G_ is presented as a single topologically ordered stream of vertices and edges, and the algorithm is constrained to a single pass without random access. In this model one cannot restart a DP pass at arbitrary earlier positions; to simulate such restarts, one<tbc>


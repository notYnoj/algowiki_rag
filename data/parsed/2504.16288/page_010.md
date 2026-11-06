\(O(n|\Sigma|)\) update steps that require time _O_(|_A_sub|), while all other update steps can be done in constant time. This yields a total running time of \(O(|w|+n|\Sigma|\cdot|A_\mathsf{sub}|)\).

The argument for _A_sub is similar. We now have that \(S_0\supseteq S_1\supseteq\dots\supseteq S_{|w|}\), which again means that there are at most _n_+1 distinct sets of active states, and again the set of active states is not changed by the symbols of the following update steps, until the state-set simulation terminates or the state set is changed to another state set. So by the same argument as before, we conclude that there are at most \((n+1)|\Sigma|\) update steps that require time _O_(|_A_sub|), while all other update steps can be done in constant time.

We conclude the proof by observing that _A_sub has \(O(n|\Sigma|+|A|)\) transitions and _A_sub has _O_(|_A_|) transitions.

This is already a significant improvement over Theorem 3.4, since the running time is linear in |_w_|. In the next two sections, we look deeper into the problem of subsequence and supersequence matching and manage to lower its complexity to the optimum of _O_(|_w_|+_m_).

## 4 Subsequence and Supersequence Matching in Linear Time

In this section, we prove that the \(\unknown_\mathsf{sub}^-\) and \(\unknown_\mathsf{sup}^-\)matching problem can be solved in linear time _O_(|_w_|+_m_). Note that this also holds for the usual regex matching problem when the input regex or \(\varepsilon\)NFA is assumed to accept an upward-closed or downward-closed language (as matching is then equivalent to \(\unknown_\mathsf{sub}^-\) or \(\unknown_\mathsf{sup}^-\)matching). We first prove the result for the subsequence relation, which is slightly easier, and then cover the supersequence relation.

### 4.1 Subsequence Matching in Linear Time

**Theorem 4.1.** _Given a string w and_ \(\varepsilon\)_NFA A with n states and m transitions, the subsequence matching problem can be solved in time O_(|_w_|+_m)._

_Proof._ We present an algorithm to decide whether there exists a subsequence _u_ of _w_ such that \(u\in\mathsf{L}(A)\).

Let \(A=(Q,\Sigma,q_0,q_\mathsf{f},\delta)\) be the input \(\varepsilon\)NFA. For this automaton, we construct the arrays \(L[\cdot]\) and \(T[\cdot,\cdot]\) defined in Section 2. Also, we assume that every transition is initially unmarked and can be marked during the algorithm (but marked transitions stay marked and cannot be set unmarked again; intuitively, these transitions were explored in our algorithm, and do not need to be considered again). One purpose of these markings is to simplify our complexity analysis: The total running time of the algorithm will be proportional to |_w_| plus the total number of times we mark a transition. Moreover, we will repeatedly compute the \(\varepsilon\)-closure \(\mathsf{C}_\varepsilon^*(S)\) of a state set _S_, but only with respect to unmarked \(\varepsilon\)-transitions, i.e., we compute \(\mathsf{C}_\varepsilon^*(S)\) as discussed in Section 3, but we simply ignore marked \(\varepsilon\)-transitions, and, furthermore, while computing the \(\varepsilon\)-closure, we will mark all unmarked \(\varepsilon\)-transitions that we traverse.

We can now describe our algorithm, which is based on a state-set simulation of _A_sub, but without explicitly constructing _A_sub, i.e., we work directly on _A_. More precisely, for every _i_=0,1,2_,...,|w_|, we compute a state-set _S<sub>i</sub>_ of all states reachable from _q_<sub>0</sub> by a path labelled with a subsequence of _w_\[1:_i_\]. Additionally, we will compute (using the arrays \(L[\cdot]\) and \(T[\cdot,\cdot]\)) and maintain a lazily initialised array \(H[\cdot]\) of lists, indexed by the symbols of \(\Sigma\), such that, after _S<sub>i</sub>_ is computed, \(H[a]=\{(q,a,q')\in\delta|q\in S_i,q'\in Q,(q,a,q')\) is unmarked}\), i.e., _H_\[_a_\] contains all unmarked transitions labelled with _a_ leaving the states contained in _S<sub>i</sub>_. Moreover, as explained in Section 3, we will have \(S_0\subseteq S_1\subseteq\dots\subseteq S_{|w|}\).

We implement all the sets _S<sub>i</sub>_ with a single Boolean characteristic array _S_, which is maintained in our algorithm in such a way that _S_<sub>_i_-1</sub> is the set indicated by _S_ after _w_\[_i_-1\] was processed and before the processing of _w_\[_i_\] is started, and during the processing of _w_\[_i_\] some positions of _S_ (namely, |_S<sub>i</sub>_\\_S_<sub>_i_-1</sub>| many) are changed from 0 to 1. This allows us to implement in constant time the membership-testing to and insertion in the manipulated sets of states. For simplicity of the exposition, and to mirror the computation of Theorem 3.5, we use the notation _S<sub>i</sub>_ to refer to the<tbc>


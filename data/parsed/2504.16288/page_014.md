To perform a push operation with a state _q_, we simply insert _q_ at the (right) end of R, which can be done in _O_(1) time if we maintain a pointer to the respective end of R. Invariant 1 is maintained (as no change is made to the elements of \(B[\cdot,\cdot]\) and the new state _q_ is now maximal for _\<_); Invariant 2 is also clearly maintained.

For a pop operation with symbol _a_, we do the following: We traverse R from right to left until we encounter a state with _B_\[_q,a_\]=1 or we finish processing R. Now, for every state \(q\in\mathcal{R}\) with \(B[q,a]\neq 1\) which is traversed, we do the following: if _q_ does not have a self-loop labelled with _a_ then we retrieve _q_ and remove it from R, and if _q_ has such a self-loop then _q_ stays in R but we set \(B[q,a]\leftarrow 1\). This maintains Invariant 2, since we set \(B[q,a]\leftarrow 1\) only in the case that _q_ has a self-loop labelled by _a_. That Invariant 1 is maintained follows from the fact that after the pop operation, we have _B_\[_q,a_\]=1 for every \(q\in\mathcal{R}\). Indeed, after the pop, the only states of R that are still in R and have not been traversed are those states \(q'\) to the left of the rightmost state _q_ for which we had _B_\[_q,a_\]=1 before the pop (if such a _q_ does not exist then all states of R were traversed); and these states \(q'\) also had \(B[q',a]=1\) as Invariant 1 held before the current pop operation.

The total running time is proportional to the total number of operations \(\ell\), plus the total number of states traversed in pop operations. Now, every state _q_ traversed in a pop operation is either returned and removed from R, or we set \(B[q,a]\leftarrow 1\) for the symbol _a_ for which we are popping. The total number of returned states, say _r_, is upper-bounded by the total number of push operations (a state had to be pushed first for it to be removed); therefore, _r_ is in \(O(\ell)\). Now, every time we set \(B[q,a]\leftarrow 1\) for a state \(q\in\mathcal{R}\) with \(B[q,a]\neq 1\) in a pop operation, this accounts for a self-loop of _q_ labelled with _a_, and we do it only once for the pair (_q,a_). This means that the total number of these assignments is bounded by _O(m_). This concludes the complexity analysis and concludes the proof.

We will use the above structure for _A_=cond(_A_<sub>sup</sub>). We can finally show our main result:

**Theorem 4.7.** _Given a string w and_ \(\varepsilon\)_NFA A with n states and m transitions, the supersequence matching problem can be solved in time O_(|_w_|+_m)._

_Proof._ We first construct cond(_A_<sub>sup</sub>) from _A_, which can be done in time _O(m_) (see Section 3 and Proposition 4.2). As noted in Section 3, we can solve the supersequence matching problem by checking whether \(w\in\mathsf{L}(A_\mathsf{sup})\), which, by Lemma 4.3, can be done by checking \(w\in\mathsf{L}(\mathsf{cond}(A_\mathsf{sup}))\). Since |cond(_A_<sub>sup</sub>)|=_O_(|_A_|), it suffices to show that we can check \(w\in\mathsf{L}(\mathsf{cond}(A_\mathsf{sup}))\) in time _O_(|_w_|+|cond(_A_<sub>sup</sub>)|).

For convenience, we set now \(A'=\mathsf{cond}(A_\mathsf{sup})=(Q',\Sigma,q'_0,q'_\mathsf{f},\delta')\) and let \(n'=|Q'|\) and \(m'=|\delta'|\). For \(A'\), we construct the arrays \(L[\cdot]\) and \(T[\cdot,\cdot]\) defined in Section 2. We will now show how to check \(w\in\mathsf{L}(A')\) in time \(O(|w|+m')\). We will still use the special structure of \(A'\) for our algorithm, i.e., it is a DAG (potentially with self-loops) and has the property described in Proposition 4.5.

We start by pre-computing several data structures:

• \(\mathsf{loops}[\cdot,\cdot]\) is a lazily initialised \(|Q'|\times|\Sigma|\) Boolean array with \(\mathsf{loops}[q,a]=1\) if \((q,a,q)\in\delta'\).<tbc>

• L_<sub>q</sub>_ for each \(q\in Q'\) is a list that contains all \(a\in\Sigma\) with \(\mathsf{loops}[q,a]=1\).<tbc>

• \(\mathsf{in}[\cdot]\) is an array with \(\mathsf{in}[q]=|\{(q',a,q)\in\delta'|q'\in Q'\backslash\{q\},a\in\Sigma\cup\{\varepsilon\}\}|\) for each \(q\in Q'\).<tbc>

• roots is a set with \(\mathsf{roots}=\{q\in Q'|\mathsf{in}[q]=0\}\).<tbc>

• \(\mathsf{mark}[\cdot]\) is an array with \(\mathsf{mark}[q]=0\) for all \(q\in Q'\).

Note that loops and L_<sub>q</sub>_ provide the information of which states have loops for which symbols, in\[_q_\] is the number of transitions that have _q_ as target (while originating in other states), roots stores all roots of \(A'\), and mark is a Boolean array that shall be used to mark states (initially, all states are unmarked). Note that since \(A'\) has a DAG structure, we know that \(\mathsf{roots}\neq\emptyset\).


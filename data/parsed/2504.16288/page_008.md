given by _T_\[_p,b_\]. Thus, we have to inspect every transition at most once. Computing the \(\varepsilon\)-closure \(\mathsf{C}_\varepsilon^*(S)\) can also be done in time _O(m_) by a breadth-first search (BFS) that starts in all states of _S_ and only considers \(\varepsilon\)-transitions (again, the entries \(T[p,\varepsilon]\) can be used for that). This means that the initialisation and each update step can be done in time _O(m_), which yields a total running time of _O_(|_w|m_) for the whole state-set simulation. What is more, this running time is conditionally optimal.

**Lemma 3.1** (\[BI16\])**.** _Given an_ \(\varepsilon\)_NFA A and string w, we can check in time_ \(O(|A|\cdot|w|)\) _whether_ \(w\in\mathsf{L}(A)\)_, but not in time_ \(O((|A|\cdot|w|)^{1-\epsilon})\) _for any_ \(\epsilon>0\) _unless SETH fails._

## 3.2 Solving Sub- and Supersequence Matching via State-Set Simulation

We now explain how we can use state-set simulation to solve the \(\unknown\)-matching problem for the subsequence and supersequence relations (which are our main focus in this paper). It is easy to see that we can transform an \(\varepsilon\)NFA _A_ into two \(\varepsilon\)NFAs _A_sub and _A_sub such that \(w\in\mathsf{L}(A_\mathsf{sub})\Longleftrightarrow\Lambda_{\unknown_\mathsf{sub}}(w)\cap\mathsf{L}(A)\neq\emptyset\) and \(w\in\mathsf{L}(A_\mathsf{sup})\Longleftrightarrow\Lambda_{\unknown_\mathsf{sup}}(w)\cap\mathsf{L}(A)\neq\emptyset\). For example, this is done in \[BLS15, Lemma 8\]. We review this construction as we adapt it later.

The \(\varepsilon\)NFA _A_sub is obtained from _A_ by simply adding a transition (_p,b,p_) for every state _p_ and \(b\in\Sigma\). Intuitively speaking, these loops equip _A_ with the general possibility to consume symbols from _w_ without transitioning in a new state, which corresponds to ignoring symbols from _w_. Hence, the "non-ignoring" transitions of an accepting run of _A_sub on _w_ spell out a subsequence of _w_ accepted by _A_. On the other hand, the \(\varepsilon\)NFA _A_sub is obtained from _A_ by simply adding a transition \((p,\varepsilon,q)\) for every existing transition (_p,b,q_) with \(b\in\Sigma\). This means that while reading _w_ the automaton can always virtually process some symbols that do not belong to _w_. Hence, in an accepting run of _A_sub on _w_, the actual transitions that read the symbols from _w_ along with the added \(\varepsilon\)-transitions that virtually read some symbols spell out a supersequence of _w_ accepted by _A_.

The correctness of these constructions is shown in \[BLS15, Lemma 8\] in slightly different terms.<sup>3</sup> For the sake of self-containment, we give full proofs of their correctness below:

**Lemma 3.2** (\[BLS15\], Lemma 8)**.** _For every_ \(w\in\Sigma^*\)_, we have that_ \(w\in\mathsf{L}(A_\mathsf{sub})\Longleftrightarrow\Lambda_{\unknown_\mathsf{sub}}(w)\cap\mathsf{L}(A)\neq\emptyset\).

_Proof._ Clearly, we have that \(\Lambda_{\unknown_\mathsf{sub}}(w)\cap\mathsf{L}(A)\neq\emptyset\Longleftrightarrow w\in\Lambda_{\unknown_\mathsf{sup}}(\mathsf{L}(A))\), so it suffices to show that \(\mathsf{L}(A_\mathsf{sub})=\Lambda_{\unknown_\mathsf{sup}}(\mathsf{L}(A))\) holds.

Let \(w\in\Lambda_{\unknown_\mathsf{sup}}(\mathsf{L}(A))\). This means that \(w[j_1]w[j_2]\dots w[j_\ell]\in\mathsf{L}(A)\) for some \(1\le j_1<j_2<\dots<j_\ell\le|w|\). We can accept _w_ by _A_sub by using the accepting run of _A_ on \(w[j_1]w[j_2]\dots w[j_\ell]\), but whenever we reach a position _i_ of _w_ with \(i\notin\{j_1,j_2,\dots,j_\ell\}\), we simply process _w_\[_i_\] with a loop (_p,w_\[_i_\]_,p_) of _A_sub. Thus, \(w\in\mathsf{L}(A_\mathsf{sub})\).

Let \(w\in\mathsf{L}(A_\mathsf{sub})\), i.e., _A_sub has an accepting run on _w_. Let \(w[j_1]w[j_2]\dots w[j_\ell]\) be the subsequence of _w_ where the _j<sub>i</sub>_ are exactly the positions of _w_ that _A_sub processes in its accepting run with original transitions of _A_ (i.e., not with the self-loops added to _A_ in order to obtain _A_sub). By construction, there must be an accepting run of _A_ on \(w[j_1]w[j_2]\dots w[j_\ell]\), which means that \(w[j_1]w[j_2]\dots w[j_\ell]\in\mathsf{L}(A)\) and therefore \(w\in\Lambda_{\unknown_\mathsf{sup}}(\mathsf{L}(A))\).

**Lemma 3.3** (\[BLS15\], Lemma 8)**.** _For every_ \(w\in\Sigma^*\)_, we have that_ \(w\in\mathsf{L}(A_\mathsf{sup})\Longleftrightarrow\Lambda_{\unknown_\mathsf{sup}}(w)\cap\mathsf{L}(A)\neq\emptyset\).

_Proof._ We have that \(\Lambda_{\unknown_\mathsf{sup}}(w)\cap\mathsf{L}(A)\neq\emptyset\Longleftrightarrow w\in\Lambda_{\unknown_\mathsf{sub}}(\mathsf{L}(A))\), so it suffices to show that \(\mathsf{L}(A_\mathsf{sup})=\Lambda_{\unknown_\mathsf{sub}}(\mathsf{L}(A))\) holds.

Let \(w\in\Lambda_{\unknown_\mathsf{sub}}(\mathsf{L}(A))\). This means that _u=u_<sub>0</sub>_w_\[1\]_u_<sub>1</sub>_w_\[2\]_...u_<sub>|_w_|-1</sub>_w_\[|_w_\]\]_u_<sub>|_w_|</sub>\in\mathsf{L}(_A). We can accept _w_ by _A_sub by using the accepting run of _A_ on _u_, but instead of the transitions that process positions of _u<sub>j</sub>_, we simply use the corresponding \(\varepsilon\)-transitions added to _A_ in order to obtain _A_sub. Thus, \(w\in\mathsf{L}(A_\mathsf{sup})\).

<sup>3</sup>The work \[BLS15\] is about the downward-closure and upward-closure of a language _L_, which are exactly the sets \(\Lambda_{\unknown_\mathsf{sub}}(L)\) and \(\Lambda_{\unknown_\mathsf{sup}}(L)\).


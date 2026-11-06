• _For each transition_ \((q,b,q')\) _with_ \(b\in\Sigma\) _and for each_ \(i\in\{1,\dots,|w|\}\) _with w_\[_i_\]=_b, there is an edge from_ (_i_-1_,q_) _to_ \((i,q')\) _in G<sub>A,w</sub> with label b and weight_ 1.

The following points about the product graph _G<sub>A,w</sub>_ are immediate:

• The product graph can be built in time \(O(|A|\cdot|w|)\).<tbc>

• Any path in _G<sub>A,w</sub>_ from a vertex of the form (_i,q_) to a vertex of the form \((j,q')\) must be such that \(j\ge i\), and it has weight precisely _j-i_.<tbc>

• For any two states _q_ and \(q'\) and integers \(0\le i\le j\le|w|\), there is a path from (_i,q_) to \((j,q')\) in _G<sub>A,w</sub>_ if and only if there is a run of _A_ going from state _q_ to state \(q'\) while reading the (possibly empty) infix _w_\[_i_+1:_j_\].

## 5.1 Proof of Theorem 5.1

We are now ready to give the proof of Theorem 5.1. The proof will be structured into a part for the infix and prefix relation, a part for the extension and left-extension relation, and a part for the subsequence and supersequence relation.

_Proof for the infix and prefix relation._ For the prefix relation, given the \(\varepsilon\)NFA _A_ and string _w_, we want to compute the minimum or maximum length of a prefix of _w_ accepted by _A_. We build in time _O_(|_w|m_) the product graph _G<sub>A,w</sub>_, then we interpret (0_,q_<sub>0</sub>) as the vertex _s_ and we add a new vertex _t_ with an \(\varepsilon\)-labelled edge with weight 0 from (_i,q_<sub>f</sub>) to _t_ for each \(i\in\{0,\dots,|w|\}\). Let us call the resulting graph _G_ and note that it can be constructed in time _O_(|_w|m_). It is now obvious that paths from _s_ to _t_ in _G_ are in one-to-one-correspondence with accepting runs over the prefixes of _w_, and that the weight of such a path is the length of the corresponding prefix. Hence, Lemma 5.2 can be used to solve the min- and max-variants of the matching problem for the prefix relation in time _O_(|_G_|)=_O_(|_w|m_), including the explicit computation of the witnessing string (as the label of the resulting path).

For the infix relation, we build again the product graph _G<sub>A,w</sub>_ and we add two vertices:

• A source vertex _s_ with \(\varepsilon\)-labelled edges with weight 0 from _s_ to (_i,q_<sub>0</sub>) for each \(i\in\{0,\dots,|w|\}\), where _q_<sub>0</sub> is the initial state of _A_.<tbc>

• A target vertex _t_ with \(\varepsilon\)-labelled edges with weight 0 from (_i,q_<sub>f</sub>) to _t_ for each \(i\in\{0,\dots,|w|\}\), where _q_<sub>f</sub> is the final state of _A_.

We call this graph again _G_ and note that its construction can be done in time _O_(|_w|m_). Moreover paths from _s_ to _t_ in _G_ are in one-to-one-correspondence with accepting runs over the infixes of _w_, with the weight of the path being the length of the corresponding infix. Hence, we conclude again with Lemma 5.2.

_Proof for the extension and left-extension relation._ For the left-extension relation, given the \(\varepsilon\)NFA _A_ with state set _Q_ and string _w_, we want to compute the minimum or maximum length of a string _vw_ accepted by _A_ across all possible choices of \(v\in\Sigma^*\). We build in time _O_(|_w|m_) the product graph _G<sub>A,w</sub>_. Further, we add to _G<sub>A,w</sub>_ a copy of the automaton _A_: its vertices are \(\{q_\leftarrow|q\in Q\}\) and for each transition \((q,x,q')\) in _A_ we add an edge from \(q_\leftarrow\) to \(q'_\leftarrow\) labelled _x_ and having weight 0 if \(x=\varepsilon\) and weight 1 otherwise. Last, for each state \(q\in Q\), we add to _G<sub>A,w</sub>_ an \(\varepsilon\)-labelled edge with weight 0 from \(q_\leftarrow\) to (0_,q_). We call the thus constructed graph _G_ and we note that it can be constructed in time _O_(|_w|m_). Let the source vertex _s_ of _G_ be \((q_0)_\leftarrow\), and let the target vertex _t_ of _G_ be (|_w|,q_<sub>f</sub>).

Let us now characterise the _st_-paths in _G_. Any _st_-path in _G_ can be decomposed in two parts: first a path from _s_ to some \(q_\leftarrow\) with \(q\in Q\), which is a path labelled with a string \(v\in\Sigma^*\), with weight |_v_| and such that there is a run from _q_<sub>0</sub> to _q_ in _A_ when reading _v_; and second a path from (0_,q_) to (|_w|,q_<sub>f</sub>), which is a path labelled by _w_, with weight |_w_|, and which witnesses that there is a run from _q_ to _q_<sub>f</sub> in _A_ when reading _w_. Hence, _vw_ is a left-extension of _w_ accepted by _A_.<tbc>


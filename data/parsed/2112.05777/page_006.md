in P<sub>1</sub> (the preferences of some of these agents will be modified slightly in the following). Moreover, for each \(a\in A_\text{repl}^*\), we add to \(A'\) a "binding" agent _b<sub>a</sub>_ and a "clone" _c<sub>a</sub>_. Agent _c<sub>a</sub>_ has empty preferences in \(\mathcal{P}'_1\) and has _a_’s preferences from P<sub>2</sub> in \(\mathcal{P}'_2\). We modify the preferences of all so far added agents such that _c<sub>a</sub>_ appears directly before _a_ (or is tied with _a_ if we have an instance with ties). Agent _b<sub>a</sub>_ has empty preferences in \(\mathcal{P}'_1\), only finds _a_ acceptable in \(\mathcal{P}'_2\), and we modify the preferences of _a_ in both \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\) such that _a_ prefers _b<sub>a</sub>_ to all other agents.

The idea behind the construction is as follows. We add _b<sub>a</sub>_ in \(\mathcal{P}'_2\) which forces \(M'_2\) to contain {_a,b<sub>a</sub>_} and further add agent _c<sub>a</sub>_, who "replaces" _a_ in \(\mathcal{P}'_2\) and has _a_’s changed preferences. However, this construction does not directly work: Let \(m\in A_\text{repl}^*\cap U\) and _w=M_<sub>1</sub>(_m_). Unfortunately, adding the edge {_m,w_} to _M_<sub>2</sub> corresponds to adding the edge {_c<sub>m</sub>,c<sub>w</sub>_} to \(M'_2\), which leads to an increase of \(|M'_1\triangle M'_2|\) but not of \(|M_1\triangle M_2|\). In order to cope with this, we replace the edge {_c<sub>m</sub>,c<sub>w</sub>_} by an _edge gadget_ consisting of multiple agents: For each man \(m\in A_\text{repl}^*\cap U\) matched by _M_<sub>1</sub> to a woman _w_, we introduce agents as depicted in Figure 1 and modify the preferences of _c<sub>m</sub>_ and _c<sub>w</sub>_ by replacing _w_ and _m_ by \(a_m^\text{lm}\) and \(a_w^\text{rm}\), respectively.<sup>2</sup> The newly introduced agents from this gadget have empty preferences in \(\mathcal{P}'_1\) and preferences as depicted in Figure 1 in \(\mathcal{P}'_2\) except for agents \(a_m^\text{rm}\) and \(a_w^\text{lm}\) who have their depicted preferences in both \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\). We set \(M'_1:=M_1\cup\{\{a_m^\text{rm},a_w^\text{lm}\}:\{m,w\}\in M_1\wedge m\in A_\text{repl}^*\cap U\}\) and \(k':=k+|A_\text{repl}^*|+7k^*\) with \(k^*:=|\{\{m,w\}\in M_1:m,w\in A_\text{repl}^*\}|\).

Next, we show the correctness of the forward direction of our reduction. Given a stable matching _M_<sub>2</sub> in P<sub>2</sub>, we construct a stable matching \(M'_2\) in \(\mathcal{P}'_2\) with \(|M'_1\triangle M'_2|=|M_1\triangle M_2|+|A_\text{repl}^*|+7k^*\) as follows. We start with \(M'_2:=M'_1\). We first implement the adjustments corresponding to edges from \(M_1\triangle M_2\): Let \(\{m,w\}\in M_2\backslash M_1\). We delete the edges containing _m_ and _w_ from \(M'_2\) (if there are any). Moreover, if \(m,w\notin A_\text{repl}^*\), then we add {_m,w_} to \(M'_2\). If \(m\in A_\text{repl}^*\) and \(w\notin A_\text{repl}^*\), then we add {_c<sub>m</sub>,w_}. If \(w\in A_\text{repl}^*\) and \(m\notin A_\text{repl}^*\), then we add {_m,c<sub>w</sub>_}. If \(m,w\in A_\text{repl}^*\), then we add {_c<sub>m</sub>,c<sub>w</sub>_}. After these adjustments, it holds that \(|M'_1\triangle M'_2|=|M_1\triangle M_2|\).

We now turn to extending matching \(M'_2\) to include edges from the edge gadgets. For every edge \(\{m,w\}\in M_1\cap M_2\) with \(m,w\in A_\text{repl}^*\), we delete {_m,w_} from \(M'_2\) and add edges \(\{c_m,a_m^\text{lm}\}\), \(\{a_m^\text{lt},a_m^\text{rt}\}\), \(\{a_m^\text{lb},a_m^\text{rb}\}\), \(\{a_w^\text{lt},a_w^\text{rt}\}\), \(\{a_w^\text{lb},a_w^\text{rb}\}\), and \(\{a_w^\text{rm},c_w\}\). This contributes seven edges to \(M'_1\triangle M'_2\) (note that the pair {_m,w_} has already been deleted from \(M'_2\) and thus already contributed to \(|M'_1\triangle M'_2|\)). For every edge \(\{m,w\}\in M_1\backslash M_2\) with \(m,w\in A_\text{repl}^*\), we first delete edge \(\{a_m^\text{rm},a_w^\text{lm}\}\) from \(M'_2\). Subsequently, we make a case distinction based on whether _m_ strictly prefers _w_ to _M_<sub>2</sub>(_m_). If yes, then the stability of _M_<sub>2</sub> implies that _w_ does not strictly prefer _m_ to _M_<sub>2</sub>(_w_). Thus, we can add the edges \(\{a_m^\text{lb},a_m^\text{rb}\}\), \(\{a_m^\text{rm},a_m^\text{rt}\}\), \(\{a_m^\text{lt},a_m^\text{lm}\}\), \(\{a_w^\text{lb},a_w^\text{rb}\}\), \(\{a_w^\text{rm},a_w^\text{rt}\}\), and \(\{a_w^\text{lt},a_w^\text{lm}\}\), and the resulting matching is not<tbc>

<sup>2</sup>We remark that this gadget is a concatenation of two parallel-edges gadgets used by Cechlárová and Fleiner \[2005\].

alt m
art m
alt w
art w
1
2
1
2
2
1
1
1
1
Cm
1
lm
m
m
2
2
lm
m
m
2
j
i
2
3
1
3
1
1
2
1
2
1
2
1
lb m
rb m
lb w
rb w

Figure 1: The edge gadget for edge _e_={_c<sub>m</sub>,c<sub>w</sub>_}, where \(m\in U\), \(w\in W\), and _m_ ranks _w_ at the _i_-th rank, and _w_ ranks _m_ at the _j_-th rank. Squared agents have empty preferences in \(\mathcal{P}'_1\). The edge contained in \(M'_1\) is bold. The numbers on the edges indicate the preferences of the agents: The number _x_ closer to an agent _a_ means that _a_ ranks the other endpoint \(a'\) of the edge at rank _x_, i.e., there are _x_-1 agents which _a_ prefers to \(a'\).


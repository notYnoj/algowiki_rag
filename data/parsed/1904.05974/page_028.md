## 6.1 A Lower Bound on the Extension Complexity of P

Here we lower bound the extension complexity of the popular matching polytope. Given a graph _H_=(_V<sub>H</sub>,E<sub>H</sub>_) which is an instance of the independent set problem, we will build an instance \(G=(A\cup B,E)\) with strict preference lists as follows. Let _V<sub>H</sub>_={1_,...,n<sub>H</sub>_}.

- For every edge \(e\in E_H\), there will be a gadget _Y<sub>e</sub>_ in _G_ on 6 vertices \(s_e,t_e,s'_e,t'_e,s''_e,t''_e\).<tbc>

- For every vertex \(i\in V_H\), there will be a gadget _Z<sub>i</sub>_ in _G_ on 4 vertices \(a_i,b_i,a'_i,b'_i\).<tbc>

**-** There are 2 more vertices in _G_: these are _a_<sub>0</sub> and _b_<sub>0</sub>.

We let \(A=\{a_0\}\cup\{a_i,a'_i:i\in V_H\}\cup\{s_e,s'_e,s''_e:e\in E_H\}\) and \(B=\{b_0\}\cup\{b_i,b'_i:i\in V_H\}\cup\{t_e,t'_e,t''_e:e\in E_H\}\). We now describe the edge set of _G_. We first describe the preference lists of the 6 vertices in _Y<sub>e</sub>_, where _e_=(_i,j_) and _i\<j_ (see Fig. 12, right).

Recall that _e_=(_i,j_) and _i\<j_. The preference lists of _s<sub>e</sub>_ and _t<sub>e</sub>_ are given below:<tbc>

\(s_e:t'_e\succ\underline{b_j}\succ t''_e\text{and}t_e:s''_e\succ\underline{a_i}\succ s'_e.\)

<tbc>The underlined vertices _a<sub>i</sub>_ and _b<sub>j</sub>_ belong to the gadgets _Z<sub>i</sub>_ and _Z<sub>j</sub>_, respectively. The preference lists of \(s'_e,s''_e\) and \(t'_e,t''_e\) are given below:<tbc>

\(s'_e:t'_e\succ t_e\text{and}s''_e:t''_e\succ t_e\text{and}t'_e:s'_e\succ s_e\text{and}t''_e:s''_e\succ s_e.\)

<tbc>We now describe the preference lists of the 4 vertices \(a_i,b_i,a'_i,b'_i\) in _Z<sub>i</sub>_ (see Fig. 12, left).

\(a'_i:b_i\succ b'_ia_i:b_i\succ b'_i\succ b_0\succ\cdots\)<br>
\(b'_i:a_i\succ a'_ib_i:a_i\succ a'_i\succ a_0\succ\cdots\)

The vertex _a<sub>i</sub>_ has _b_<sub>0</sub> as its third choice followed by all the vertices _t_<sub>_e_<sub>1</sub></sub>_,t_<sub>_e_<sub>2</sub></sub>_,..._ where _i_ is the _lower-indexed_ endpoint of _e_<sub>1</sub>_,e_<sub>2</sub>_,..._. Similarly, _b<sub>i</sub>_ has _a_<sub>0</sub> as its third choice followed by all the vertices \(s_{e_1^\prime},s_{e_2^\prime},\dots\) where _i_ is the _higher-indexed_ endpoint of \(e'_1,e'_2,\dots\).

The order among the vertices _t_<sub>_e_<sub>1</sub></sub>_,t_<sub>_e_<sub>2</sub></sub>_,..._ (similarly, \(s_{e_1^\prime},s_{e_2^\prime},\dots\)) in the preference list of _a<sub>i</sub>_ (resp., _b<sub>i</sub>_) does not matter; hence these are represented as "\(\cdots\)" above.

The vertex _a_<sub>0</sub> (resp. _b_<sub>0</sub>) has _b_<sub>1</sub>_,...,b<sub>n<sub>H</sub></sub>_ (resp. _a_<sub>1</sub>_,...,a<sub>n<sub>H</sub></sub>_) as its neighbors and its preference list is some arbitrary permutation of them . Thus the number of vertices in _G_ is _n_=6_m<sub>H</sub>_+4_n<sub>H</sub>_+2, where _m<sub>H</sub>_=|_E<sub>H</sub>_|.<tbc>

Se
1
3
te
3
1
1
1
bi
2
2
2
2
1
1
1
2
2
2
2
2
2
2
1
1

**Fig.12.** To the left is the gadget _Z<sub>i</sub>_ on vertices \(a_i,b_i,a'_i,b'_i\) and to the right is the gadget _Y<sub>e</sub>_ on vertices \(s_e,t_e,s'_e,t'_e,s''_e,t''_e\). The numbers on edges denote vertex preferences: 1 is top choice and so on.


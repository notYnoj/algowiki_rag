_Proof._ Let \(A=\pi(A^*)\) be the output of the algorithm, where _A_<sup>∗</sup> is the \((M_1^*,M_2^*)\)-kernel given by Fleiner’s algorithm. Since \(A^*\in\mathcal{I}_1^*\cap\mathcal{I}_2^*\), it is clear from the definitions of \(\mathcal{I}_i^*\) that \(A\in\mathcal{I}_1\cap\mathcal{I}_2\). Suppose for contradiction that there exists \(u\in S\backslash A\) that blocks _A_; we claim that _y<sub>u</sub>_ blocks _A_<sup>∗</sup>. As _u_ blocks _A_, for each _i_=1,2, we have \(A+u\in\mathcal{I}_i\) or \(u\succ_iv\) holds for some \(v\in C_A^i(u)\). In the former case, \(A^*+y_u\in\mathcal{I}_i^*\) immediately follows. In the latter case, \(u\succ_iv\) implies that \(v^*:=\{x_v,y_v,z_v\}\cap A^*\) satisfies \((y_u,v^*)\in\mathcal{R}_i^*\), and therefore \(y_u\succ_i^*v^*\) by the construction of \(\succ_i^*\), while _v_<sup>∗</sup> belongs to the fundamental circuit of _y<sub>u</sub>_ for _A_<sup>∗</sup> in \(M_i^*\). Thus, _y<sub>u</sub>_ blocks _A_<sup>∗</sup>.

We now provide the postponed proof.

_Proof of Lemma 9._ Since the constructions of \(\mathcal{R}_1^*\) and \(\mathcal{R}_2^*\) are symmetric, it is sufficient to show that the digraph _D_<sub>1</sub> defined from \(\mathcal{R}_1^*\) is acyclic.

Suppose, to the contrary, that _D_<sub>1</sub> has directed cycles. Let _C_ be a cycle of minimum length. By the definition of \(\mathcal{R}_1^*\), we can observe the following properties. We say that an element \(s\in S^*\) is an _x_-element (resp., _y_-element, _z_-element) if _s=x<sub>u</sub>_ (resp., _s=y<sub>u</sub>_, _s=z<sub>u</sub>_) for some \(u\in S\).

• Every _z_-element has no leaving arcs. So, _C_ consists of only _x_-elements and _y_-elements.<tbc>

• No arc connects two _x_-elements. So in _C_ there are no consecutive _x_-elements.<tbc>

• There are no consecutive _y_-elements in _C_. Indeed, if _y_<sub>_u_<sub>1</sub></sub>_,y_<sub>_u_<sub>2</sub></sub>_,x_<sub>_u_<sub>3</sub></sub> (resp., _y_<sub>_u_<sub>1</sub></sub>_,y_<sub>_u_<sub>2</sub></sub>_,y_<sub>_u_<sub>3</sub></sub>) appear in _C_ in this order consecutively, then _D_<sub>1</sub> has arcs (_y_<sub>_u_<sub>1</sub></sub>_,y_<sub>_u_<sub>2</sub></sub>) and (_y_<sub>_u_<sub>2</sub></sub>_,y_<sub>_u_<sub>3</sub></sub>) (resp., (_y_<sub>_u_<sub>2</sub></sub>_,x_<sub>_u_<sub>3</sub></sub>)), and hence \(u_1\succ_1u_2\) and \(u_2\succ_1u_3\). Then, the transitivity of \(\succ_1\) implies \(u_1\succ_1u_3\), and hence _D_<sub>1</sub> has an arc (_y_<sub>_u_<sub>1</sub></sub>_,x_<sub>_u_<sub>3</sub></sub>) (resp, (_y_<sub>_u_<sub>1</sub></sub>_,y_<sub>_u_<sub>3</sub></sub>)), contradicting the minimality of _C_.<tbc>

• Therefore, _C_ has an even length and _x_-elements and _y_-elements appear alternately.<tbc>

• Suppose that four distinct elements _y_<sub>_u_<sub>1</sub></sub>_,x_<sub>_u_<sub>2</sub></sub>_,y_<sub>_u_<sub>3</sub></sub>_,x_<sub>_u_<sub>4</sub></sub> appear in _C_ in this order consecutively. Then we have \(u_1\neq u_3\), \(u_2\neq u_4\), \(u_1\succ u_2\), and \(u_3\succ u_4\).<tbc>

– If \(u_1\neq u_4\) and \(u_2\neq u_3\), then all _u<sub>i</sub>_ are distinct. Since \(\succ_1\) is an interval order (i.e., (2+2)-free), then the relations \(u_1\succ u_2\) and \(u_3\succ u_4\) imply that \(u_1\succ u_4\) or \(u_3\succ u_2\). Hence there exists an arc (_y_<sub>_u_<sub>1</sub></sub>_,x_<sub>_u_<sub>4</sub></sub>) or (_y_<sub>_u_<sub>3</sub></sub>_,x_<sub>_u_<sub>2</sub></sub>).<tbc>

**–** If _u_<sub>1</sub>=_u_<sub>4</sub> (resp., _u_<sub>2</sub>=_u_<sub>3</sub>), then \(u_3\succ u_4=u_1\succ u_2\) (resp., \(u_1\succ u_2=u_3\succ u_4\)), and hence there exists an arc (_y_<sub>_u_<sub>3</sub></sub>_,x_<sub>_u_<sub>2</sub></sub>) (resp. (_y_<sub>_u_<sub>1</sub></sub>_,x_<sub>_u_<sub>4</sub></sub>)).

The existence of an arc (_y_<sub>_u_<sub>1</sub></sub>_,x_<sub>_u_<sub>4</sub></sub>) or (_y_<sub>_u_<sub>3</sub></sub>_,x_<sub>_u_<sub>2</sub></sub>) contradicts the minimality of _C_.

Then _C_ must be of length two, but it is impossible by the definition of \(\mathcal{R}_1^*\).

## 3.2 Proof of 1.5-approximation

We now show the approximation ratio of our algorithm. As in the previous section, we denote by \(C_I^1(u)\) and \(C_I^2(u)\) fundamental circuits in _M_<sub>1</sub> and _M_<sub>2</sub>, respectively.

**Theorem 11.** _The approximation ratio of the above algorithm is at most_ 1.5.

_Proof._ Let \(A=\pi(A^*)\) be the output of the algorithm, where _A_<sup>∗</sup> is an \((M_1^*,M_2^*)\)-kernel, and let _B_ be a largest (_M_<sub>1</sub>_,M_<sub>2</sub>)-kernel. Suppose for contradiction that |_B|\>_1.5|_A_|. Let _B<sub>i</sub>_ be a subset of _B_\\_A_ such that \(A\cup B_i\in\mathcal{I}_i\) and \(|A\cup B_i|=|B|\) for each \(i\in\{1,2\}\). (The existence of such _B<sub>i</sub>_ follows from axiom (ii) of matroids.) The sets _B_<sub>1</sub> and _B_<sub>2</sub> are disjoint because _A_<sup>∗</sup> is an inclusion-wise maximal common independent set of \(M_1^*\) and \(M_2^*\). In the following, we say that an element \(u\in A\) is _of type x_ (resp., _y,z_) if \(\{x_u,y_u,z_u\}\cap A^*=x_u\) (resp., _y<sub>u</sub>,z<sub>u</sub>_).


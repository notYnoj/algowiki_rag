To calculate the total cost of Strassen’s algorithm, we also need to count the additions and subtractions at the internal vertices of the recursion tree. At depth _k_ of the recursion tree, there are 7_<sup>k</sup>_ internal vertices. Both on the way down and on the way up the tree, the algorithm must compute linear combinations of \(2^{L-k}\times 2^{L-k}\) matrices at each of these vertices, which uses _O_(4<sup>_L-k_</sup>) operations. The total across the whole tree is therefore \(\sum_{k=0}^{L-1}7^k4^{L-k}=O(7^L)\), a geometric series dominated by its last term, so the additions only increase the running time by a constant factor. This phenomenon is prevalent in recursive matrix multiplication algorithms, although in the new algorithm we develop in Section 2.4 below, this same argument will no longer apply, and we will need to count the additions and subtractions more carefully.

## 2.2 Schönhage’s identity for an inner product and an outer product

While we will still use Strassen’s recursive approach here, we will replace his identity with another one due to Schönhage \[Sch81\]. In this subsection we give the notation to introduce this identity and explain its usefulness.

It will be convenient to write such identities as trilinear polynomials.<sup>5</sup> As an example, we first show how to write Strassen’s identity from Section 2.1 in this way. Introduce four **_output variables_** _c_<sub>11</sub>_,c_<sub>12</sub>_,c_<sub>21</sub>_,c_<sub>22</sub>, one for each entry of the product _AB_, and multiply each of the seven products _S_<sub>1</sub>_,...,S_<sub>7</sub> of Strassen’s identity above by the signed sum of the output variables of the entries where it appeared in the decoding phase. For instance, _S_<sub>1</sub> appears in the formulas for (_AB_)<sub>11</sub> and (_AB_)<sub>22</sub>, so it is multiplied by _c_<sub>11</sub>+_c_<sub>22</sub>, and _S_<sub>5</sub> appears in the formula for (_AB_)<sub>11</sub> with a minus sign and in the formula for (_AB_)<sub>12</sub>, so it is multiplied by _c_<sub>12</sub>-_c_<sub>11</sub>. Strassen’s identity then reads

\(S_1(c_{11}+c_{22})+S_2(c_{21}-c_{22})+S_3(c_{12}+c_{22})+S_4(c_{11}+c_{21})\)<br>
\(+S_5(c_{12}-c_{11})+S_6c_{22}+S_7c_{11}=\sum_{i,j,k=1}^2a_{ij}b_{jk}c_{ik},\)

where _S_<sub>1</sub>_,...,S_<sub>7</sub> are the products of two linear forms from (1). Now the coefficient of _c<sub>ik</sub>_ on the right-hand side is the entry (_AB_)<sub>_ik_</sub>=_a_<sub>_i_1</sub>_b_<sub>1_k_</sub>+_a_<sub>_i_2</sub>_b_<sub>2_k_</sub> that we want, and its coefficient on the left-hand side is the combination of the seven products that computes it, such as _S_<sub>1</sub>+_S_<sub>4</sub>-_S_<sub>5</sub>+_S_<sub>7</sub><tbc>

<sup>5</sup>These are often called tensors, or order-3 tensors, in the literature.


The inputs and outputs of our algorithm will be arrays that contain the entries of many different matrices concatenated together. (Later in Section 2.3.4 we will use this algorithm as a subroutine to multiply a single pair of matrices.) We will index the entries of these arrays by strings of _L_ variables of Schönhage’s identity. Whether each variable is an inner or outer variable will tell us which of the 2_<sup>L</sup>_ matrix products the array entry corresponds to, and the specific variables will tell us which entry of the matrix it corresponds to.

A **_left string_** of length _L_ is a string \(u=u_1u_2\cdots u_L\) of _L_ left variables, and we call \(u_\ell\) its variable at **_level_** \(\ell\). An **_array_** _a **on the left strings of length** L_ assigns an integer _a_\[_u_\] to each _u_ that is a left string of length _L_. The array _a_ has 7_<sup>L</sup>_ entries in total (since there are 7 left variables). We define right strings, output strings, and arrays on them in the same way. For instance, an array on the output strings of length _L_ has 10_<sup>L</sup>_ entries (since there are 10 output variables).

For a term \(\lambda\) and a left variable _s_, let \(\varphi_\lambda(s)\in\{0,\pm 1\}\) denote the coefficient of _s_ in \(\varphi_\lambda\), and define \(\psi_\lambda(t)\) similarly for right variables _t_. Recall from Schönhage’s identity that, for each term \(\lambda\), at most three of the seven values \(\varphi_\lambda(s)\) are nonzero since each \(\varphi_\lambda\) has at most three monomials, and similarly for the seven values \(\psi_\lambda(t)\).

Just as Strassen’s algorithm cuts matrices into blocks, we cut an array _a_ on strings of length \(L\ge 1\) into **_slices_** according to the variable at level 1: the slice of _a_ at a left variable _s_ is the array _a<sub>s</sub>_ on the strings of length _L_-1 given by \(a_s[u']:=a[su']\). Thus, _a_ consists of its seven slices, just as a block matrix consists of its blocks. We similarly define the slices _b<sub>t</sub>_ of an array _b_ on right strings, and _c<sub>z</sub>_ of an array _c_ on output strings.

The recursion Full(_a,b_), for arrays _a,b_ on the left and right strings of length _L_, returns an array on the output strings of length _L_:

(1) If _L_=0, return the number _ab_.<tbc>

(2) For each term \(\lambda\) of Schönhage’s identity, form \(A_\lambda:=\sum_s\varphi_\lambda(s)a_s\) and \(B_\lambda:=\sum_t\psi_\lambda(t)b_t\).<tbc>

(3) For each term \(\lambda\), recursively compute \(C_\lambda:=\mathrm{Full}(A_\lambda,B_\lambda)\).<tbc>

(4) Return the array _c_ whose slices are _c<sub>z<sub>ij</sub></sub>_:=_C<sub>P<sub>ij</sub></sub>_ and \(c_{z_0}:=\sum_\lambda C_\lambda\).

For _L_=1, Full is one application of Schönhage’s identity: step (2) evaluates the linear forms \(\varphi_\lambda\) and \(\psi_\lambda\) at the seven numbers _a_\[_s_\] and the seven numbers _b_\[_t_\], step (3) multiplies the two values for each \(\lambda\), and step (4) sums the products into the ten outputs as the forms \(\chi_\lambda\) prescribe. In the terms of Section 2.1, step (2) is the encoding and step (4) the decoding.

The calls of Full form a recursion tree. We refer to the call reached by choosing the terms \(\tau_1,\dots,\tau_k\) at levels 1_,...,k_ as the **_vertex_** \(\tau_1\cdots\tau_k\), a string of _k_ terms. It is at depth _k_, and its input arrays are on strings of length _L-k_. The root is the vertex with _k_=0, and the **_leaves_**, the vertices \(\tau=\tau_1\cdots\tau_L\) at depth _L_, are the 10_<sup>L</sup>_ multiplications performed in step (1).

Let us now count the operations performed by this algorithm. At depth _k_ there are 10_<sup>k</sup>_ vertices (since Schönhage’s identity has 10 terms), each with two input arrays of 7<sup>_L-k_</sup> entries and an output array of 10<sup>_L-k_</sup> entries. Step (2) takes _O_(7<sup>_L-k_</sup>) operations at a vertex, and step (4) takes _O_(10<sup>_L-k_</sup>) operations. Hence, Full uses \(\sum_{k=0}^L10^k\cdot O(7^{L-k}+10^{L-k})=O(L\cdot 10^L)\) operations in total, which is not much more than the 10_<sup>L</sup>_ multiplications. Of this, the encodings, step (2), account for only \(\sum_{k=0}^L10^k\cdot O(7^{L-k})=O(10^L)\) operations, and the decodings, step (4), for the rest.


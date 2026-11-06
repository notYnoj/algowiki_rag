<tbc>scalar products. Its exponent satisfies

\(\frac{\mathrm{log}(64\rho^{6d})}{\mathrm{log}R}=\frac{18c^2+O(c)}{8c^2+O(c)}=\frac{9}{4}+O(1/c).\)

Choose _c_ so that \(64\rho^{6d}<R^\tau\), and then _k_ so that \(r_k<v_k^\tau\). These choices are finite and effective.

### Removing the formal parameter.

Since \(r_k<v_k^\tau\), Bini’s approximate-to-exact lemma \[Bin80\], stated and proved for completeness as Lemma B.1, converts this packing into an exact rational identity (6) at a computable finite side _v_, using \(r<v^\tau\) scalar products. All coefficients arise from the stated encodings, permutations, and rational interpolations.

The choice _d=c_<sup>3</sup> gives convergence 9/4+_O_(1_/c_). One can instead take _d=c_<sup>2</sup>: then log_R_=8_c+O_(log_c_) and \(\mathrm{log}(64\rho^{6d})=18c+O(1)\), giving 9/4+_O_(log_c/c_). This uses 6_c_<sup>2</sup> rather than 6_c_<sup>3</sup> polynomial variables, at the cost of slower convergence.

## 4.2 Integer arithmetic

We finish by applying standard block recursion to the fixed identity, as in Strassen’s algorithm \[Str69\]. Its parameters and coefficients are constants once the requested exponent is fixed.

_Proof of Theorem 1.1._ Choose the identity in Theorem 4.1 with \(\tau=9/4+\gamma\). This identity also holds for matrix blocks: expanding both sides gives the same coefficient for every ordered product of a left-input block and a right-input block. Clear the fixed denominators in the encoders and decoder to obtain integer linear maps whose decoded output is \(\delta AB\) for a fixed positive integer \(\delta\).

For _n=v<sup>j</sup>_, partition the input matrices into \(v\times v\) blocks, encode, recursively multiply the _r_ encoded pairs, decode, and divide every output entry exactly by \(\delta\). All operations outside the recursive products cost _O(n_<sup>2</sup>), so

\(T(n)\le rT(n/v)+O(n^2)=O(n^\tau),\)

since \(r<v^\tau\) and \(\tau>2\). Padding to the next power of _v_ handles every positive integer _n_.

For _B_-bit integer inputs, encoding adds only _O_(1) bits per level. Products have at most twice the resulting input length, and decoding adds _O_(log_n_) bits over the remaining levels. All intermediate integers therefore have _O(B_+log_n_) bits. The bit cost is \(O(n^{9/4+\gamma}\mathsf{M}(B+\mathrm{log}n))\), where M(_b_) is the cost of multiplying _b_-bit integers; multiplication and exact division by the fixed constants take linear time.

### AI Use Statement.

OpenAI x (Astra) was used extensively to study \[Ope26a\], learn about the problem, and explore candidate constructions. The main ideas behind the construction, analysis, and abstractions are my own; x was invaluable in exploring definitions and proof approaches and in formalizing my proof ideas and sketches. Most of the text has been written and revised with x through detailed prompts from me. Claude provided feedback on the manuscript and its presentation.


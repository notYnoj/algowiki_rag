has _M_ column blocks; we recover the _M_<sup>2</sup> narrow output blocks using 2_M_-1 applications of the same-left packing.

**Lemma 2.8** (Separating left inputs)**.** _Let M,N,u,p,q,r be positive integers with_ \(M\ge 2\)_, and let F_<sub>0</sub>_,...,F_<sub>_M_-1</sub>_,S be maps of the form_ (1)_. Suppose a same-left packing modulo_ \(\varepsilon\) _computes_ \((F_i(A,B_i))_{i=0}^{M-1}\) _on coefficient sizes_ \(p\times q,q\times r\) _using N copies of S on sizes_ \(p\times q,q\times ur\)_. Assume the F<sub>i</sub> have the same left-input space. Then a packing modulo_ \(\varepsilon\) _computes_ \((F_i(A_i,B_i))_{i=0}^{M-1}\) _on sizes_ \(p\times q,q\times Mr\) _using N_(2_M_-1) _copies of S on sizes_ \(p\times q,q\times ur\).<sup>3</sup>

_Proof._ Given independent pairs _A<sub>i</sub>,B<sub>i</sub>_, write<tbc>

\(B_i=[B_{i,0}\cdots B_{i,M-1}],\)

<tbc>splitting every \(q\times Mr\) coefficient matrix horizontally into _M_ blocks of size \(q\times r\). Since _F<sub>i</sub>_ applies the same coefficient formula to each column block,

\(F_i(A_i,B_i)=[F_i(A_i,B_{i,0})\cdots F_i(A_i,B_{i,M-1})].\)

Thus we must recover all _M_ output blocks in each group _i_.

_Encode._ Interpolate one input-valued polynomial \(A(\xi)\) of degree at most _M_-1 with _A(i_)=_A<sub>i</sub>_. For each group _i_, interpolate a right-input-valued polynomial _C<sub>i</sub>(v_) of degree at most _M_-1 with _C<sub>i</sub>(j_)=_B<sub>i,j</sub>_, and define<tbc>

\(B'_i(\xi)=C_i\big(\frac{\xi-i}{\varepsilon}\big).\)

<tbc>The division by \(\varepsilon\) preserves the distinct right inputs as their interpolation points approach _i_:

\(B'_i(i+\varepsilon j)=C_i(j)=B_{i,j}(0\le j<M).\)

Meanwhile, _A_ is independent of \(\varepsilon\), so \(A(i+\varepsilon j)\equiv A_i(mod\varepsilon)\). We substitute \(\xi=i+\varepsilon j\) before taking the constant term: the coefficients of \(B'_i\) may contain negative powers of \(\varepsilon\). The points \(i,i+\varepsilon,\dots,i+\varepsilon(M-1)\) are distinct over \(\mathbb{Q}(\varepsilon)\). Since _C<sub>i</sub>_ has degree at most _M_-1, the coefficients of \(B'_i\) are Laurent polynomials in \(\varepsilon\) whose powers have exponents at least -(_M_-1). Both encodings are linear in their respective inputs.

_Compute and interpolate._ Consider the univariate polynomials

\(P_i(\xi)=F_i(A(\xi),B'_i(\xi)).\)

Bilinearity gives degree at most 2_M_-2 in \(\xi\). For each _k_=0_,...,_2_M_-2, use the given same-left packing to compute their values with common left input _A(k_) and right inputs \(B'_i(k)\). Replace the given packing’s parameter by \(\varepsilon^M\). Its decoded error is then divisible by \(\varepsilon^M\) before substituting the inputs. The left input contains no negative powers of \(\varepsilon\), and the powers in the right inputs have exponents at least -(_M_-1). Since the error is bilinear, after substitution it is still divisible by \(\varepsilon^{M-(M-1)}=\varepsilon\).

Interpolate the actual decoded values at these 2_M_-1 points. The interpolation coefficients are rational numbers independent of \(\varepsilon\), so the resulting polynomials satisfy<tbc>

\(\widetilde{P}_i(\xi)=P_i(\xi)+\varepsilon R_i(\xi,\varepsilon),\)

<sup>3</sup>The encoding at the points \(i+\varepsilon j\) in the proof was proposed by x after I prompted it to solve this separation problem using Reed-Muller decoding \[Sud02, Section 2.2\].


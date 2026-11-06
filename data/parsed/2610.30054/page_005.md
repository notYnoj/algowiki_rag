We will be working a lot with these partial direct sums \(\oplus_1\), but in the end we will need a way to transform these back into the usual world of direct sums \(\oplus\):

(D2) **Separating partial direct sums into direct sums.** For a partial direct sum \(T_1\oplus_1\cdots\oplus_1T_m\) and every integer \(t\ge 1\),<tbc>

<tbc>\((T_1\oplus\cdots\oplus T_m)\otimes\mathsf{P}_{1,t}\unknown(T_1\oplus_1\cdots\oplus_1T_m)\otimes\mathsf{P}_{m,t}\)<tbc>

<tbc>(Proposition 3.5).

Note how ingredient (D2) turns a partial direct sum into a direct sum, at the cost of turning a factor P_<sub>m,t</sub>_ into P<sub>1_,t_</sub>, thus using P_<sub>m,t</sub>_ as a "partially consumed catalyst" for this degeneration.

Finally, we need two families of degenerations that relate partial direct sums of polynomial multiplication tensors. The first family is:

(D3) **Concavity degeneration.** For \(b\ge 2\), \(\mathsf{P}_{a,b+1}\oplus_1\mathsf{P}_{a,b-1}\triangleup_1\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\), and the same with arbitrary \(\oplus_1C\) added on both sides (Lemma 3.6).<tbc>

<tbc>(Here the subscript in \(\triangleup_1\) indicates that these degenerations do not act on the first leg, which indeed allows adding arbitrary \(\oplus_1C\) on both sides.) In terms of polynomials, ingredient (D3) is using two multiplications of the same polynomial _f_ by polynomials of degree at most _b_-1 to compute multiplications of _f_ by polynomials of degree at most _b_ and _b_-2. The construction of (D3) is related to the representation theory of SL<sub>2</sub>.

The second family is:

(D4) **Tripling degeneration.** \(\mathsf{P}_{a,b}\oplus_1((23)\cdot\mathsf{P}_{a,b})\oplus_1\mathsf{P}_{a,b}\triangleup_1\mathsf{P}_{a,3b+a-1}\), where \((23)\cdot\mathsf{P}_{a,b}\) is P_<sub>a,b</sub>_ with its second and third legs exchanged; and again the same with arbitrary \(\oplus_1C\) added on both sides (Lemma 3.11).

In terms of polynomials, ingredient (D4) is using one multiplication of _f_ by a polynomial _g_ of degree at most 3_b+a_-2 to compute three smaller ones. We can use the lowest _b_ and the highest _b_ coefficients of _g_ to do two multiplications of _f_ by polynomials of degree at most _b_-1, the two copies of P_<sub>a,b</sub>_. Using degeneration we are able to squeeze in an extra, permuted polynomial multiplication, \((23)\cdot\mathsf{P}_{a,b}\).

## 1.1.2 Combination rules

The proof will combine the above degeneration ingredients (D0)-(D4) by basic combination rules to obtain more degenerations, as to eventually obtain degenerations of the form \(\langle n,n,n\rangle\unknown\langle r\rangle\), hopefully such that log_r/_log_n_ is small. These rules are:

(C1) reflexivity: \(T\triangleup T\);<tbc>

(C2) transitivity: if \(T_1\triangleup T_2\) and \(T_2\triangleup T_3\), then \(T_1\triangleup T_3\);<tbc>

(C3) direct sums and tensor products: if \(T_1\triangleup S_1\) and \(T_2\triangleup S_2\), then \(T_1\oplus T_2\triangleup S_1\oplus S_2\) and \(T_1\otimes T_2\triangleup S_1\otimes S_2\);<tbc>

T1
T1
T2
T2
T1
T2
T1
T2
T1
T2
Figure 2: The direct sum T1 T2 (left) and the
partial direct sum T1 T2 (right), drawn as three- dimensional arrays. All coefficients outside the two
boxes are zero.


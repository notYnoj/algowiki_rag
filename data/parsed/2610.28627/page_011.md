Write _I_<sub>0</sub>=\[_d_\] and \(F_{a,b}^{(d)}=F_{a,b,I_0}\). Thus \(F_{a,b}^{(d)}\) is full in the first _d_ variables and middle in the last _d_.

We first count words with two types of letters. Different letters of the same type will represent different outputs of a packing.

**Lemma 2.6** (Counting words by type)**.** _For positive integers c,d, let_<tbc>

\(\mathcal{P}=\{\mathsf{F}_1,\dots,\mathsf{F}_{c+1},\mathsf{M}\},\mathcal{D}=\{\mathsf{F},\mathsf{M}_1,\dots,\mathsf{M}_{c+1}\}.\)

<tbc>_The letters_ F,F_<sub>i</sub> have type Full, and the letters_ M,M_<sub>i</sub> have type Mid. The number of words whose first d letters lie in_ P_, whose last d letters lie in_ D_, and which contain exactly d letters of each type is_

\(\sum_{h=0}^d\genfrac(){pt}{2}{d}{h}^2(c+1)^{2(d-h)}\ge\frac{(c+2)^{2d}}{d+1}.\)

_Proof._ Fix the number _h_ of Mid letters in the first half. Choose their _h_ positions; each must contain M. Each remaining position can contain any of the _c_+1 distinct letters F<sub>1</sub>_,...,_F<sub>_c_+1</sub>. There are therefore \(\genfrac(){pt}{2}{d}{h}(c+1)^{d-h}\) choices for the first half.

The first half contains _d-h_ Full letters, so the second half must contain exactly _h_ Full letters. Choose their positions and put F in each. Each remaining position can contain any of the _c_+1 Mid letters, giving the same number of choices. The two halves can be chosen independently, so multiplying their counts and summing over _h_ gives the stated equality. Finally,

\(\sum_{h=0}^d\left[\genfrac(){pt}{2}{d}{h}(c+1)^{d-h}\right]^2\ge\frac{\left[\sum_{h=0}^d\genfrac(){pt}{2}{d}{h}(c+1)^{d-h}\right]^2}{d+1}=\frac{(c+2)^{2d}}{d+1}\)

by Cauchy-Schwarz and the binomial theorem.

**Lemma 2.7** (Same-left multivariate packing)**.** _For positive integers c,d, set_

\(u=c^{2d},w=\left\lfloor\frac{(c+2)^{2d}}{d+1}\right\rfloor.\) (4)

_There are sets_ \(I_1,\dots,I_w\subseteq[2d]\) _of size d, depending only on c,d, such that for all positive integers a,b,t with_ \(ct\ge a+2b-1\)_, the list_

\(\left(F_{a,b,I_i}(A,B_i)\right)_{i=1}^w\)

_has a same-left packing modulo_ \(\varepsilon\) _using u copies of_ \(F_{a,b+t}^{(d)}\)_. All input coefficient sizes are_ \(p\times q,q\times r\) _for arbitrary positive integers p,q,r._

_Proof._ We begin with a common left input _A_ and an entire array of right inputs. Label the primal packing’s _c_+1 Full outputs and one Mid output by the letters of P in Lemma 2.6, and label the dual packing’s one Full output and _c_+1 Mid outputs by the letters of D. Index the array by words whose first _d_ letters lie in P and whose last _d_ letters lie in D. The letter at position _k_ specifies the local output in variable _z<sub>k</sub>_. A right input has length _b_ where its word has a Full letter and length _s_ where it has a Mid letter. There are (_c_+2)<sup>2_d_</sup> such positions; their right inputs are arbitrary and need not factor across variables.


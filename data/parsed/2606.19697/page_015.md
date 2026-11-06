_Proof._ Noting that (_s_<sub>1</sub>_,s_<sub>2</sub>,-_s_<sub>1</sub>,-_s_<sub>2</sub>) is simply \(\phi(s_1,s_2)\) and that \(\phi(v)=\phi(v,1)\), scale invariance of \(\phi\) and the precondition in the proposition implies \(v=\frac{s_1}{s_2}\). Thus \(av+b=a\frac{s_1}{s_2}+b\). It follows that \(\phi(av+b)=\phi(a\frac{s_1}{s_2}+b)=\phi(a\frac{s_1}{s_2}+b,1)=\phi(as_1+bs_2,s_2)\), where the last equality follows from scale invariance of \(\phi\).

## B Proofs for Restricted Word RAMs

**Lemma 1.** _Let M be a 1-dimensional Word RAM with word size w=c_log(_n+t_) _for some_ \(c\in\mathbb{N}\)_. Then there exists a c-dimensional restricted Word RAM_ \(M'\) _with word size_ \(w'=\mathrm{log}(n+t)\) _and the same instruction set as M that simulates t steps of M using_ O(_t_) _steps._

_Proof._ We will show how to simulate _M_ with \(M'\). The following invariant will be helpful: _M_ has size \(w=cw'\), so any value _x_ can represented with _c_ values \(x'_1,\dots,x'_c\), each of word size \(w'\).

For any instruction in _M_ that retrieves the value at _x_ and stores it into _y_, we will instead have _c_ instructions that retrieve the value at each \(x'_i\) and store it into \(y'_i\) for \(1\le i\le c\). Similarly, whenever we write the value at _y_ into _x_, we will have _c_ instructions that write value \(y'_i\) into \(x'_i\). Thus, each read or write instruction in _M_ can be simulated by _c_ instructions in \(M'\).

It remains to be shown that arithmetic instructions in _M_ can also be simulated in \(M'\):

• _Adding x_ and _y_ in _M_ can be implemented in \(M'\) by starting with \(\kappa_1=0\) and adding blocks \(x'_i+y'_i+\kappa_i\) iteratively for _i_=1,2_,...,c_, with \(\kappa_{i+1}=\unknown[x'+y'\ge 2^w]\) being the carry bit for the subsequent step. This takes at most 2_c_ steps.<tbc>

• _Subtracting_ mirrors addition, with the _borrow_ bit \(\beta_{i+1}=\unknown[x'+\beta_i<y']\). (If the final borrow bit \(\beta_{c+1}=1\), the result is negative.)<tbc>

• _Multiplying x_ and _y_ in _M_ can be implemented in \(M'\) via long multiplication in base \(m=2^{w^\prime}\). Write \(x=\sum_{i=1}^cx'_i\cdot m^{i-1}\) and \(y=\sum_{j=1}^cy'_j\cdot m^{j-1}\). For each _j_=1_,...,c_, we compute the partial product \(a_j=x\cdot y'_j\cdot m^{j-1}\) and keep a running sum \(S\leftarrow S+a_j\). The partial product \(x\cdot y'_j\) is itself computed block-by-block: for each _i_=1_,...,c_, multiply \(x'_i\cdot y'_j\) (a product of two \(w'\)-bit numbers, fitting in \(2w'\) bits) and add it into block _i_ of the partial product together with any carry from block _i_-1. Since each \(x'_i,y'_j<2^{w^\prime}\), the product \(x'_i\cdot y'_j<2^{2w^\prime}\), so the carry into block _i_+1 is at most \(2^{w^\prime}-1\), which fits in \(w'\) bits. Computing one partial product \(x\cdot y'_j\) thus takes _O(c_) steps; summing it into _S_ (via the addition procedure above) takes another _O(c_) steps. Over all _c_ values of _j_, the total cost is _O(c_<sup>2</sup>) steps.<tbc>

• _Dividing x_ by _y_ in _M_ can be implemented in \(M'\) via long division in base \(m=2^{w^\prime}\), analogously to multiplication (Knuth, 1997, §4.3.1, Alg. D). The quotient \(\lfloor x/y\rfloor\) has _c_ base-_m_ digits \(q'_1,\dots,q'_c\); we recover them one by one from most to least significant. At each step, the top two blocks of the running remainder and the top block of _y_ together determine the next quotient digit exactly via a single \(w'\)-bit division (available as a primitive in \(M'\)). Each of the _c_ digits thus costs O(_c_) steps (one scalar division plus a multiply-and-subtract to update the remainder), giving O(_c_<sup>2</sup>) total.<tbc>

• _Taking mod_: the remainder \(r=x-\lfloor x/y\rfloor\cdot y\) is computed alongside the quotient in the procedure above at no extra asymptotic cost.<tbc>

• _Left or right shifting_. We describe the left shift case; the right shift case is analogous. Suppose we want to compute \(z=x\checkmark k\). Decompose the shift amount as \(k=q\cdot w'+r\) where \(q=\lfloor k/w'\rfloor\) is the number of whole blocks to shift and \(r=k\mathrm{mod}w'\) is the intra-block shift.<sup>6</sup> Thus, shifting left by _k_ bits moves block _i_ of the input to block _i+q_ of the output, with an _r_-bit internal shift. Concretely, for _i_=1_,...,c_:<tbc>

<tbc>\(z'_i=\left\{\begin{array}{ c c }
0 & \text{if}i\le q, \\
(x'_{i-q}\checkmark r)|(x'_{i-q-1}\gg(w'-r)) & \text{if}i>q\text{and}i-q-1\ge 1, \\
x'_{i-q}\checkmark r & \text{if}i>q\text{and}i-q-1<1,
\end{array}\right.\)<tbc>

<sup>6</sup>Note that since \(k<w=cw'\), the shift amount fits in a single \(w'\)-bit block of \(M'\). Thus, \(q=\lfloor k/w'\rfloor\) and \(r=k\mathrm{mod}w'\) are each single-block values computable in O(1) steps with primitives in \(M'\).


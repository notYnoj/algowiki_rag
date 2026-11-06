<tbc>where \(n\equiv a\) mod 12. Then we let

\(W^+=\)<br>
\(\{a_i^X,x_i^X,b_i^Y,y_i^X(a_i+b_i)^{X+Y},(a_i+b_i+n/6)^{X+Y},(a_i-b_i)^{X-Y},(x_i-y_i)^{X-Y}\}_{i\in[3]}\)

and

\(W^-=\)<br>
\(\{c_i^X,w_i^X,d_i^Y,z_i^X(c_i+d_i)^{X+Y},(w_i+z_i)^{X+Y},(c_i-d_i)^{X-Y},(c_i-d_i+n/6)^{X-Y}\}_{i\in[3]}\)

and let \(W:=W^+\cup W^-\).

When _n_ is even and 3 \(\unknown n\) we instead additionally ensure that<tbc>

\(2+a+2\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in 4\mathbb{Z}\)

<tbc>where \(n\equiv a\) mod 12. Then we define \(W:=W^+\cup W^-\) via<tbc>

\(W^+=\)<br>
\(\{a_i^X,x_i^X,b_i^Y,y_i^X(a_i+b_i)^{X+Y},(a_i+b_i+n/2)^{X+Y},(a_i-b_i)^{X-Y},(x_i-y_i)^{X-Y}\}_{i\in[3]}\)

<tbc>and<tbc>

\(W^-=\)<br>
\(\{c_i^X,w_i^X,d_i^Y,z_i^X(c_i+d_i)^{X+Y},(w_i+z_i)^{X+Y},(c_i-d_i)^{X-Y},(c_i-d_i+n/2)^{X-Y}\}_{i\in[3]}.\)

<tbc>When _n_ is odd and 3 |_n_ our additional constraint is that<tbc>

\(1+2\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in 3\mathbb{Z},\)

<tbc>and we define \(W:=W^+\cup W^-\) via<tbc>

\(W^+=\)<br>
\(\{a_i^X,x_i^X,b_i^Y,y_i^X(a_i+b_i)^{X+Y},(a_i+b_i+n/3)^{X+Y},(a_i-b_i)^{X-Y},(x_i-y_i)^{X-Y}\}_{i\in[3]}\)

<tbc>and

\(W^-=\)<br>
\(\{c_i^X,w_i^X,d_i^Y,z_i^X(c_i+d_i)^{X+Y},(w_i+z_i)^{X+Y},(c_i-d_i)^{X-Y},(c_i-d_i+n/3)^{X-Y}\}_{i\in[3]}.\)

Note that Theorem 1.3 holds for \(n\equiv 1,5\) mod 6 as an immediate corollary to Theorem 1.2, so this covers all remaining cases. Now let T<sup>∗</sup>:=T\[_V_(T)\\_W_\]. We claim that T<sup>∗</sup> has at least \(\left((1+o(1))\frac{n}{e^3}\right)^n\) perfect matchings, and that each of these extends to a distinct placement of _n_ non-attacking queens on the \(n\times n\) classical board such that at most 6 pairs of queens attack toroidally. Indeed, supposing that T<sup>∗</sup> has at least \(\left((1+o(1))\frac{n}{e^3}\right)^n\) perfect matchings, this translates to a placement of _n_-12 queens on the \(n\times n\) toroidal board so that no two queens can attack each other. Then adding the 12 queens dictated by \(\{(a_i,b_i),(c_i,d_i),(x_i,y_i),(w_i,z_i)\}_{i\in[3]}\), these queens cannot attack any of the _n_-12 previously placed queens on the toroidal board (and therefore nor on the classical board), and these 12, by construction, do not attack classically and divide into three pairs which attack toroidally on the _X+Y_ diagonal, and three pairs which attack toroidally on the _X-Y_ diagonal.


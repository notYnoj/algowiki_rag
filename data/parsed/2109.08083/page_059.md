<tbc>_to_ \(\Phi\)_), we have_ \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\) _a vector with SQ-gens decomposition consisting of_ \((\mathcal{A}\backslash\{(a,a+b,a+c,a+b+c)\})\cup\{(s,s+b,s+c,s+b+c)\}\).

Proof. This follows directly from the structure of _Q_-gens. Let \(a':=s-a\). Then, if (_a,a+b,a+c,a+b+c_) is in the _SQ_-gens decomposition of **v** with weights (1,-1,-1,1), adding _Q_-gen \((a,a+b,a+c,a+b+c,a'+a,a'+a+b,a'+a+c,a'+a+b+c)\) with weights (-1,1,1,-1,1,-1,-1,1) to **v** gives what is required. □

We refer to changing **v** in this way as _shifting_ an _SQ_-gen, and say that we _shift_ a copy of an _SQ_-gen when we interchange _SQ_-gens in the decomposition of **v** (potentially modifying **v**) by adding a _Q_-gen to **v** which cancels one _SQ_-gen out and leaves another _SQ_-gen in the decomposition.

Proposition 4.16. _Queens vectors of the form_ (_a,a_+2_<sup>x</sup>,a_+2_<sup>y</sup>,a_+2_<sup>x</sup>_+2_<sup>y</sup>,a,a_+2<sup>_x_-1</sup>_,a_+2<sup>_y_+1</sup>_,a_+2<sup>_x_-1</sup>+2<sup>_y_+1</sup>) _with weights_ (1,-1,-1,1,-1,1,1,-1) _are efficiently generated._

Proof. Note that (_a,a_+2_<sup>x</sup>,a_+2_<sup>y</sup>,a_+2_<sup>x</sup>_+2_<sup>y</sup>,a,a_+2<sup>_x_-1</sup>_,a_+2<sup>_y_+1</sup>_,a_+2<sup>_x_-1</sup>+2<sup>_y_-1</sup>)=(_a,a_+2<sup>_x_-1</sup>_,a_+2_<sup>y</sup>,a_+2<sup>_x_-1</sup>+2_<sup>y</sup>,a_+2_<sup>y</sup>,a_+2<sup>_x_-1</sup>+2_<sup>y</sup>,a_+2<sup>_y_+1</sup>_,a_+2<sup>_x_-1</sup>+2<sup>_y_+1</sup>)-(_a,a_+2<sup>_x_-1</sup>_,a_+2_<sup>y</sup>,a_+2<sup>_x_-1</sup>+2_<sup>y</sup>,a_+2<sup>_x_-1</sup>_,a_+2_<sup>x</sup>,a_+2<sup>_x_-1</sup>+2_<sup>y</sup>,a_+2_<sup>x</sup>_+2_<sup>y</sup>_), and those on the RHS are _Q_-gens which we know can be generated efficiently. □

Recall from Section 3.2.1 that an integer marked with a superscript \(\circ\) means that it should be read without modular arithmetic.

Proposition 4.17. _Let_ **v**=(_a,a+b,a+c,a+b+c_) _be an SQ-gen written so that_ \(a=a^\circ\le a+b=(a+b)^\circ\le(a+c)^\circ=a+c\)_. Then we can write_ **v** _as the sum of O_(log(_n_)) _SQ-gens, where each is of the form_ \((a',a'+b,a'+2^j,a'+b+2^j)\) _for some_ \(a'<n\)_, and_ \(2^j<min\{n-a',n/2\}\).

Proof. Write \(c=\sum_{i=1}^k2^{c_i}\) such that \(2^{c_i}\le n/2\) for every _i_, and \(c_i\ge c_{i+1}\) with equality if and only if _c\>n/_2 and _c_<sub>1</sub>=_c_<sub>2</sub> is necessary to get a sum of the above form. Since _c\<n_ we have that _k=O_(log(_n_)). We can then decompose **v** into _k=O_(log(_n_)) vectors of the required form via an iterative shifting process which ensures that weight added to any coordinates in a way that would modify **v** is cancelled out by adding other vectors with carefully chosen first coordinates.

In particular, writing \(c'_i:=2^{c_i}\) for every _i_, it is easy to see that

\((a,a+b,a+c,a+b+c)=(a,a+b,a+c'_1,a+b+c'_1)\)<br>
\(+(a+c'_1,a+c'_1+b,a+c'_1+c'_2,a+c'_1+c'_2+b)\)<br>
\(+(a+c'_1+c'_2,a+c'_1+c'_2+b,\)<br>
\(a+c'_1+c'_2+c'_3,a+c'_1+c'_2+c'_3+b)\)<br>
\(+\dots\)<br>
\(+(a+\sum_{i=1}^{k-2}c'_i,a+\sum_{i=1}^{k-2}c'_i+b,a+\sum_{i=1}^{k-1}c'_i,a+\sum_{i=1}^{k-1}c'_i+b)\)<br>
\(+(a+\sum_{i=1}^{k-1}c'_i,a+\sum_{i=1}^{k-1}c'_i+b,a+c,a+b+c),\)

where each of the vectors on the RHS is an _SQ_-gen of the form (_s,s+b,s_+2_<sup>j</sup>,s+b_+2_<sup>j</sup>_) for some _s\<a+c\<n_ and 2_<sup>j</sup>\<_min{_n-s,n/_2}. □


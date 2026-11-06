computing all _x_-coefficients and the _y_-coefficients at exponents _a_-1_,...,a+b_-1. Apply the dual decoder in _y_, then the primal decoder in _x_.

Encoding in _x_ and then in _y_, computing the source products, and decoding in reverse order recovers all the requested outputs modulo \(\varepsilon\). This follows by applying the correctness of the two univariate packings along their separate coefficient indices.

We therefore recover (_c_+2)<sup>2</sup> outputs from _c_<sup>2</sup> source products. Furthermore, continuing this process in additional variables amplifies the compression exponentially. Use 2_d_ variables _z_<sub>1</sub>_,...,z_<sub>2_d_</sub>, applying the primal packing in the first _d_ and the dual packing in the last _d_. Encode in each variable, compute the resulting products, and decode in reverse order. This gives (_c_+2)<sup>2_d_</sup> outputs from _c_<sup>2_d_</sup> source products, a compression factor of ((_c_+2)_/c_)<sup>2_d_</sup>.

There is one issue: the source products are all Full in the first _d_ variables and Mid in the last _d_, whereas the recovered outputs can have different numbers of Full and Mid directions. To obtain a recursive rule that we can apply repeatedly, we need to "end where we started": the targets must have the same form as the sources. This requires, in particular, _d_ Full and _d_ Mid directions in each target, so we keep only these outputs. For example, in the two-variable table, the yellow and green outputs have two Full or two Mid directions, respectively, so they do not qualify. The (_c_+1)<sup>2</sup> blue outputs and the single purple output have one of each: 26 of the 36 outputs when _c_=4. With 2_d_ variables, we recover at least<tbc>

\(\frac{(c+2)^{2d}}{d+1}\)

<tbc>outputs of this shape.<sup>1</sup> Thus requiring this common shape costs at most a factor _d_+1 in the output count, while the compression gain grows exponentially in _d_. (Their Full and Mid directions may<tbc>

<sup>1</sup>To see why, consider the following equivalent counting question. Form a word whose first _d_ letters are chosen from {F<sub>1</sub>_,...,_F<sub>_c_+1</sub>,M} and whose last _d_ letters are chosen from {F,M<sub>1</sub>_,...,_M<sub>_c_+1</sub>}. All F-letters have type Full and all M-letters have type Mid; subscripts distinguish different letters of the same type. How many words contain exactly _d_ letters of each type? The answer is \(\sum_{h=0}^d\genfrac(){pt}{2}{d}{h}^2(c+1)^{2(d-h)}\), which is at least (_c_+2)<sup>2_d_</sup>/(_d_+1) by Cauchy-Schwarz and the binomial theorem.


<tbc>(0,1) with probability \(\varepsilon/2\), and (1,1) with probability \(\varepsilon/2\) (or equivalently when (_x_<sub>1</sub>_,x_<sub>2</sub>)=(0,0) with probability \(1-\varepsilon\), (0,1) or (1,0) with probability \(\varepsilon/2\), and (1,1) with probability \(\varepsilon/2\)). The expected heat release of a gate with one of these heat functions, when the input distribution is optimal, is

\((1-\varepsilon)log_2(1/(1-\varepsilon))+\varepsilon log_2(2/\varepsilon)=O(\varepsilon log(1/\varepsilon)),\)

using the fact that \(log_2(1/(1-\varepsilon))=O(\varepsilon)\) by application of Taylor’s expansion of \(log(1-\varepsilon)\). Moreover, on distributions where \((x_1,x_2)=(b,b')\) with probability _at least_ \(1-\varepsilon\), the expected heat release of a gate with heat function \(\tilde{Q}_\varepsilon^{(b,b^\prime)}\) is \(O(\varepsilon log1/\varepsilon)\).

We will also use heat function \(\tilde{Q}^{(\mathrm{unif})}\) that is optimal on the uniform input distribution. Its values are \(\tilde{Q}^{(\mathrm{unif})}(0,0)=\tilde{Q}^{(\mathrm{unif})}(1,1)=2\), and \(\tilde{Q}^{(\mathrm{unif})}(0,1)=1\) and the expected heat release is

\((1/4)2+(1/4)2+(1/2)=3/2.\)

Moreover, for any input distribution, the expected heat release with respect to \(\tilde{Q}^{(\mathrm{unif})}\) is at most 2; it approaches 2 as the probability of inputs (0,1) or (1,0) approaches 0.

A key difference between the overwriting model and our circuit model is that _logically reversible_ operations do not buy you anything extra in the overwriting model. In Section 5.2 we saw that we could always set _Q_(0,0)=_Q_(1,1)=0 since these inputs give unique outputs. On the other hand, we need to dissipate heat when we write over these outputs in the overwriting model.

As in the analysis of Batcher’s network for our model, we partition the comparator gates into log<sub>2</sub>_n_+1 layers, with layer 0 encompassing the recursive sub-networks, as in Figure 2. Within each layer \(\ell\), we will partition the gates into the same three regions as in the proof of Theorem 5.2, but will pick heat functions that are amenable to the overwriting model. Again \(\alpha\in(0,1)\) is a parameter we will specify later.

## Layer 1

In this layer, there are _n/_2 comparator gates. The _i_’th gate has input wires _i_ and _i+n/_2.

• Upper region: \(i\in[0,(n-n^{(1+\alpha)/2})/4]\). Since just after layer 0, bits 0,1_,...,n/_2-1 are sorted, and also the remaining _n/_2 bits are independently sorted, it follows from Proposition 2.14 that for _i_ in this region,<tbc>

\(\mathrm{Pr}[w_i(0)=1]\le\mathrm{exp}(-n^\alpha/4)\text{and also}\mathrm{Pr}[w_{n/2+i}(0)=1]\le\mathrm{exp}(-n^\alpha/4).\) \(\text{(15)}\)

Consequently, the _i_th comparator gate has the input (0,0) with probability at least \((1-\mathrm{exp}(-n^\alpha/4))^2\ge 1-2\mathrm{exp}(-n^\alpha/4)\). If the gate has heat function \(\tilde{Q}_{2\mathrm{exp}(-n^\alpha/4)}^{(0,0)}\), the expected heat release is \(O(n^\alpha\mathrm{exp}(-n^\alpha/4))=O(\mathrm{exp}(-n^\alpha/5))\).<tbc>

• Lower region: \(i\in[(n+n^{(1+\alpha)/2})/4,n/2-1]\). A similar analysis shows that the _i_th comparator gate in this region gets (1,1) as input with probability at least \(1-2\mathrm{exp}(-n^\alpha/4)\). If the gate has heat function \(\tilde{Q}_{2\mathrm{exp}(-n^\alpha/4)}^{(1,1)}\), the expected heat release is \(O(\mathrm{exp}(-n^\alpha/5))\).<tbc>

• Middle band: \(i\in[(n-n^{(1+\alpha)/2})/4,(n+n^{(1+\alpha)/2})/4]\). The expected heat release each gate in this region is at most 2 if the gates have heat function \(\tilde{Q}^\mathrm{unif}\).

Summing up over all three regions, the total expected heat dissipation for layer 1 is dominated by the middle band, and is \(O(n^{(1+\alpha)/2})\), using three different types of heat functions.


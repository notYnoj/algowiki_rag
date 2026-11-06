2. Apply the algorithm of Theorem 5.4 to correct the remaining errors and output the fully sorted result.

Given Theorems 3.2 and 5.4, it is not hard to see that the algorithm takes _O(nk_) work and _O_(log_n_) depth.

## 6 Building Blocks for the Circuit Model

### 6.1 Our Operational Circuit Model

Our result will be stated using the standard circuit model of computation \[Sav97\] where the circuit consists of AND, OR, and NOT gates; and moreover each AND and OR gate has constant fan-in and constant fan-out.

For convenience, we shall use an operational model that consists of generalized boolean gates and (reverse) selector gates. A _generalized boolean gate_ has constant fan-in and constant fan-out, and implements any truth table between the inputs and outputs. A _w-selector gate_ is a selector gate that takes in a 1-bit flag and two _w_-bit payload strings, and outputs one of the two payload strings determined by the flag. A _reverse selector_ gate is the opposite. A _w_-reverse selector gate takes one element _x_ of bit-width _w_ and a flag \(b\in\{0,1\}\) as input and outputs (_m,_0_<sup>w</sup>_) if _b_=0 and (0_<sup>w</sup>,m_) if _b_=1. In our construction later, we will often use reverse selector gates to preform "reverse routing", where we reverse the routing decisions made by earlier selector gates. Henceforth in the paper whenever we count selector and reverse selector gates, we do not distinguish between them and count both towards selector gates.

We say a circuit is in the _indivisible_ model if and only if the input to the circuit consists of elements with _k_-bit keys and _w_-bit payloads, and the circuit never performs boolean computation on the payload strings, that is, the payload strings are only moved around using _w_-selector gates.

**Lemma 6.1** (Technical lemma about our operational circuit model)**.** _In the indivisible model, any circuit with n generalized boolean gates,_ \(n'\) _number of w-selector gates and of depth d can be implemented as a boolean circuit (having constant fan-in and constant fan-out) of size_ \(O(n+n'\cdot w)\) _and depth O(d_+log_w)._

_Proof._ Generalized boolean gates can be easily replaced with AND, OR, and NOT gates without incurring additional asymptotical overhead. The key is how to instantiate all the _w_-selector gates without blowing up the circuit’s depth by a log_w multiplicative_ factor.

First, imagine we have a "partial evaluation" circuit where payloads are fake and of the form 0_<sup>w</sup>_. In this way, we can implement every _w_-selector gate as a degenerate one that takes _O_(1) depth, since the outputs are always 0_<sup>w</sup>_. Evaluating this partial evaluation circuit will populate the flags on all selector gates. Notice such partial evaluation relies on the circuit being indivisible and thus populating a flag is independent of any result of any _w_-selector.

Since we are subject to constant fan-in and constant fan-out gates, to implement an actual selector gate will require replicating the gate’s flag _w_ times, and then use _w_ generalized boolean gates, one for selecting each bit. After the partial evaluation phase, all selector gates can perform this _w_-way replication in parallel, incurring an additive rather than multiplicative log_w_ overhead. At this point, we can instantiate each _w_-selector gate using one generalized boolean gate for each of the _w_ bits being selected.

Therefore, the total circuit size is \((n+n'\cdot w)\) and the depth is _O(d_+log_w_).

We define some useful circuit gadgets below.


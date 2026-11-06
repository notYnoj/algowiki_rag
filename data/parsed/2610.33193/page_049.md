An example of the erasure subcircuit for stage _i_ is shown in Figure 5. There are _i_+1 pairs of clean wires, one pair for each possible numerator \(j\in\{0,\dots,i\}\). Set a clean wire to 1 with a NOT gate and, using a reversible (_i_+1)-way demultiplexer,<sup>38</sup> route the pair (1_,b<sub>i</sub>_) (the first bit is a control bit _c_ for the controlled erasure gate downstream) to output wires addressed by the binary value _z<sub>i</sub>_ in register _Z_. Thus the selected pair contains (1_,b<sub>i</sub>_) and every other pair contains (0,0). On pair _j_, apply a controlled erasure gate to each such pair for \(j\in\{0,\dots,i\}\), using a heat function optimal for probability _j/i_. Consequently only the selected gate performs an erasure, using the heat function optimal for the probability _z<sub>i</sub>/i_; all other gates act reversibly with zero heat since their control bits are 0. After these gates act in parallel, reverse the demultiplexer (a.k.a., multiplexing) using the same address _z<sub>i</sub>_. It returns the pair (1,0), after which a NOT gate restores the control wire to 0, while the original _b<sub>i</sub>_ wire and all routing wires are also 0.

A binary-tree demultiplexer uses _O(i_)=_O(n_) constant-size gates and _O_(log_i_)=_O_(log_n_) depth. Together with the _i_+1 controlled erasure gates, stage _i_ therefore uses _O(n_) gates and _O_(log_n_) depth for routing and erasure.

Computing _z<sub>i</sub>_ from scratch with a straightforward sequential implementation would require _O(n_) depth, and since this must be done sequentially for each bit erasure, the total depth would be _O(n_<sup>2</sup>) if computed naïvely. Instead, we observe that _z<sub>i</sub>_ can be updated incrementally using only _O_(log_n_) depth as we erase bits. Maintain a register _Z_, initially 0. Just before stage _i_, maintain the invariant that _Z_=|_b<sub>\<i</sub>_|<sub>1</sub>, the number of 1’s among the already-erased prefix bits. At stage _i_, do the reversible increment \((b_i,Z)\mapsto(b_i,Z+b_i)\) to update _Z_ to represent \(|b_{\le i}|_1=h-|b_{>i}|_1=z_i\).<sup>39</sup> This requires only _O_(log_n_) depth per bit erasure (using a standard ripple-carry increment),<sup>40</sup> so _O(n_log_n_) total depth for all _n_ bit erasures. After the final erasure, _Z=h_=|_s_|<sub>1</sub>. To restore this<tbc>

<sup>38</sup>A demultiplexer takes as input a value _v_ (one or more bits), and an address _a_ interpreted as a binary integer, and routes _v_ to one of several output lines based on the value of _a_. <sup>39</sup> The increment must precede the demultiplexing that selects the erasure gate. If the pre-increment value _Z=z<sub>i</sub>-b<sub>i</sub>_ were used as the address instead, then (_s,W_), _b<sub>\>i</sub>_, and _Z_ would together determine _b<sub>i</sub>=z<sub>i</sub>-Z_, since _z<sub>i</sub>_=|_s_|<sub>1</sub>-|_b<sub>\>i</sub>_|<sub>1</sub> is determined by the first two. Erasing _b<sub>i</sub>_ would then destroy the mutual information between _b<sub>i</sub>_ and the rest of the circuit, which by Proposition D.1 produces entropy no matter which heat function the erasure gate uses. After the increment, _Z=z<sub>i</sub>_ carries no information about _b<sub>i</sub>_ beyond what (_s,W_) and _b<sub>\>i</sub>_ already determine. <sup>40</sup>We could actually do better than _O_(log_n_) depth to increment _Z_, using _O_(loglog_n_) depth by using a parallel prefix circuit \[LF80\]. However, we forsake such optimizations, since we are already using \(\Omega(logn)\) depth for the

demultiplexer
multiplexer
O control bits
0
p = 0/3
0
0
b<3 (b<3 erased)
0
b3
0
p = 1/3
0
1
1
demux
0
0
mux
b>3
1
0
0
1
0
b3 erased
1
1
1
needs cleaning
Z + b3
0
0
p = 3/3
0
0
initial Z for next stage erasing b4
Z
1
1
1
0
0
address Z3 = 2

Figure 5: The subcircuit for erasing bit _b_<sub>3</sub> when _b_=1011, so \(z_3=|b_{\le 3}|_1=2\) and the gate must assume Pr\[_b_<sub>3</sub>=1\]=2/3. Reversible demultiplexer drawn without extra clean input wires needed to supply 0’s to unaddressed output wires, and similarly for unshown output wires of multiplexer that simply pass through unaddressed inputs.


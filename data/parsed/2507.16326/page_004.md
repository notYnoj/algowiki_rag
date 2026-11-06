<tbc>to register _D_<sub>0</sub> first, then register _D_<sub>1</sub>. Thus, the valid signal \(V_1\Longrightarrow V_0\) by also shifting _V_<sub>1</sub>_,D_<sub>1</sub> to _V_<sub>0</sub>_,D_<sub>0</sub> when necessary. \(\neg V_1\) can be passed to the input to indicate register availability.

Separately, writes are performed to _D_<sub>0</sub> if it is empty (\(\neg V_0\)). Note that it is not necessary to check for validity of input _V_ since if \(\neg V\) , then \(\neg V_0\) holds next cycle. When it is full, different decisions are taken depending on if the value is being read by the next node or not. In the first case, the value is replaced by either the input, or register 1 if it was full. In the second case, register 0 has nowhere to go so register 1 is filled with the input.

Synchronization of both input and output is done via two signals valid (_V_ ) and ready (_R_) which are asserted by the producer and consumer respectively. When both have asserted their signals, and see the symmetric signal asserted as well, the transaction is assumed completed in that cycle. This means that the produce must empty its register, and the consumer must fill up theirs.

This design achieves our two main goals: First, the input is decoupled from the output, as there is no combinatorial dependency between values or flags going up and down the tree, resulting in no cascading signals. This keeps the critical path under control, and signal fan-out to a minimum. Secondly, _bubbles_ can’t appear since a node is capable of both inputting and outputting a value in the same cycle.

**Algorithm 3** Hourglass cell behavior

**Input:** Data _D<sub>L</sub>_, _D<sub>R</sub>_

**Input:** Valid data flags _V<sub>L</sub>_, _V<sub>R</sub>_

**Output:** Ready data flags _V<sub>L</sub>_, _V<sub>R</sub>_

**Output:** _D<sub>out</sub>_; _V<sub>out</sub>_

**Input:** _R<sub>out</sub>_

**Variables:** _D_, _V_ , _R_

**Registers:** _D_<sub>1</sub>, _D_<sub>0</sub>, _V_<sub>1</sub>, _V_<sub>0</sub>

**Ensure:** Values output in ascending order; sorting is stable.

1: **for** Each cell in the tree, in parallel **do**

2: \(R\leftarrow\neg V_1\)

3: **if** _D<sub>L</sub>\<D<sub>R</sub>_ **then**

4: **if** _V<sub>L</sub>_ **then** {Select left branch}

5: \(D,V,R_R,R_L\leftarrow D_L,V_L,\text{\textbf{false}},R\)

6: **else** {Select right branch}

7: \(D,V,R_R,R_L\leftarrow D_R,V_R,R,\text{\textbf{false}}\)

8: **end if**

9: **else**

10: **if** _V<sub>R</sub>_ **then** {Select right branch}

11: \(D,V,R_R,R_L\leftarrow D_R,V_R,R,\text{\textbf{false}}\)

12: **else** {Select left branch}

13: \(D,V,R_R,R_L\leftarrow D_L,V_L,\text{\textbf{false}},R\)

14: **end if**

15: **end if**

16: \(D_{out},V_{out}\leftarrow D_0,R_0\)

17: **if** \(\neg V_0\) **then** {IN: Fill empty first register}

18: \(D_0,V_0\leftarrow D,V\)

19: **else if** \(\neg V_1\) **then**

20: **if** _R<sub>out</sub>_ **then** {Simultaneous IN/OUT}

21: \(D_0,V_0\leftarrow D,V\)

22: **else** {IN: Fill second register}

23: \(D_1,V_1\leftarrow D,V\)

24: **end if**

25: **else if** _R<sub>out</sub>_ **then** {OUT: Shift out values}

26: \(D_0,V_0\leftarrow D_1,V_1\)

27: **end if**

28: **end for**

To prove this, consider the case of a _bubble_ appearing at a node. If this was the case, we know both internal registers are empty. If, in the cycle prior, one of the inputs had been available, it would have been shifted into one of the registers since \(\neg V_1\) would have held, so both inputs had to be unavailable. This reasoning can be recursively followed up to the leaf nodes, confirming that, in order for a _bubble_ to appear, the full tree above must be empty. Therefore it must be the case that the root node is only empty when the full array is sorted. Note that this can only be assured after the first value has been received at the root. This is bound to happen in log(_n_) cycles after initialization since, by construction, all of the nodes will have received a value from both parents at that point. Since we can’t have _bubbles_ afterwards, it follows that the rest of the array is sequentially output in _n_ cycles.

The only thing left is to see that the output is indeed sorted. Consider that, if we assume that both incoming branches for a node are sorting properly, we will always have at our<tbc>

9
1
4
2
6
1
5
3
9
4
6
5
1
2
1
3
4
5
9
2
6
3
1
1
9
4
6
5
3
2
1
1
9
6
5
4
2
3
1

Fig. 3. _Bubbling_ avoidance by doubling the registers at each node.


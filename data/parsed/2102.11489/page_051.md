the input array **I**; let **X** denote the outcome.<tbc>

2. _Count and label_. Count how many 0-keys there are in the array **I**, let the result be `cnt`. For each \(i\in[n]\) in parallel:<tbc>

• if **X**\[_i_\] has the key 1 and \(i\le\mathtt{cnt}\), mark it as `red`;<tbc>

• else if **X**\[_i_\] has the key 0 and _i\>_`cnt`, mark it as `blue`;<tbc>

• else the element **X**\[_i_\] is uncolored.<tbc>

3. _Sparse loose compaction_. Apply a sparse loose compactor to the outcome of the previous step; the outcome is an array **Y** whose length is \(\lfloor n/\mathrm{log}n\rfloor\) containing all colored elements in **X**, padded with filler elements to a length of \(\lfloor n/\mathrm{log}n\rfloor\).<tbc>

4. _Slow swap_. Let \(\mathbf{Y}':=\mathbf{SlowSwap}(\mathbf{Y})\).<tbc>

5. _Reverse route_. Reverse route the array \(\mathbf{Y}'\) by reversing the routing decisions made in Step 3, and let the outcome be **Z** which has length _n_.<tbc>

6. _Output_. The output **O** is obtained by performing a coordinate-wise select operation between **Z** and **X**:<tbc>

<tbc>\(\forall i\in[n]:\mathbf{O}[i]:=\left\{\begin{array}{ c c }
\mathbf{Z}[i] & \text{if}\mathbf{X}[i]\text{was marked "\texttt{misplaced}}\text{"} \\
\mathbf{X}[i] & \text{o.w.}
\end{array}\right.\)<tbc>

<tbc>**Implementing the algorithm in circuit.** Step 1 is implemented with the approximate tight compaction circuit of Theorem 12.1.

Step 2 is implemented as follows. First, use the counting circuit of Fact 6.3 to compute `cnt`. Then, use the binary-to-unary circuit of Fact 6.5 to write down a string of _n_ bits where the beginning `cnt` bits are 0 and all other bits are 1. Next, all positions \(i\in[n]\) uses the comparator circuit of Fact 6.2 to compute its "`misplaced`" label.

Step 3 is implemented with the sparse loose compactor circuit of Theorem 13.3. Step 4 is implemented using the **SlowSwap** circuit of Theorem 9.2. Step 5’s costs are absorbed by Step 3. Finally, Step 6 can be accomplished with _n_ generalized boolean gates.

Summarizing the above, the entire tight compaction circuit requires \(O(nw)\cdot\mathrm{max}(\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w),1)\) generalized boolean gates, \(O(n)\cdot\mathrm{max}(\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w),1)\) number of _w_-selector gates, and has depth _O_(log_n_).

## 15 Sorting Circuit for Short Keys

### 15.1 Circuit Implementations of Additional Building Blocks

Earlier, we described various building blocks for an Oblivious PRAM model. We now discuss the size and depth bounds for these building blocks in the circuit model.

**Sorting elements with ternary keys.** Given Theorem 14.1, and Fact 6.3, we can implement the algorithm of Theorem 4.1 using a circuit with \(O(nw)\cdot\mathrm{max}(1,\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w))\) generalized boolean gates, \(O(n)\cdot\mathrm{max}(1,\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w))\) number of _w_-selector gates, and of depth _O_(log_n_). This leads to the following fact:

**Fact 15.1.** _There exists a circuit with_ \(O(nw)\cdot\mathrm{max}(1,\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w))\) _generalized boolean gates,_ \(O(n)\cdot\mathrm{max}(1,\mathtt{poly}(\mathrm{log}^*n-\mathrm{log}^*w))\) _number of w-selector gates, and of depth O_(log_n), capable of_<tbc>


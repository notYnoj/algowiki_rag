<tbc>lowest of both in an output register. Let’s call this process an "operation" and consider that, for a registered comparator to perform an operation, the following conditions need to be satisfied:

\(\bullet\) Both input registers contain a valid value, or<tbc>

\(\bullet\) One input register is valid and the other empty (neither it nor any parent is valid)<tbc>

\(\bullet\) The output register is empty

This process is illustrated in Algorithm 2. Each node waits for both inputs to be either valid or empty, and selects the minimum value to pass forward. This is conditioned to the output register being empty, in which case the value is moved down a level within the tree. When both inputs are empty (i.e: no more values will fall through them) and the output has been read, it is marked as empty, continuing the process below.

**Algorithm 2** Registered comparator algorithm

**Input:** Data Registers _D_<sub>1</sub>, _D_<sub>2</sub><br>
**Input:** Valid data flags _V_<sub>1</sub>, _V_<sub>2</sub><br>
**Input:** Empty subtree flags _E_<sub>1</sub>, _E_<sub>2</sub><br>
**Outputs:** _D<sub>out</sub>_; _E<sub>out</sub>_; _V<sub>out</sub>_<br>
**Ensure:** \(V_i\Longrightarrow\neg E_i\)<br>
**Ensure:** Values output in ascending order; sorting is stable.<br>
**for** Each triplet of nodes in the tree, in parallel **do**<br>
1: Input registers belong to the first layer **then**<br>
2: **if**<br>
\(E_i\leftarrow\neg V_i\)<br>
4: **end if**<br>
5: **if** _V_<sub>1</sub> **and** _V_<sub>2</sub> **and** \(\neg V_{out}\) **then**<br>
6: \(D_{out}\leftarrow min(D_1,D_2)\)<br>
7: \(V_{argmin(D_1,D_2)}\leftarrow\) **false**<br>
8: \(V_{out}\leftarrow\) **true**<br>
9: **else if** _V_<sub>1</sub> **and** _E_<sub>2</sub> **and** \(\neg V_{out}\) **then**<br>
10: \(D_{out},V_1,V_{out}\leftarrow D_1,\) **false**, **true**<br>
11: **else if** _V_<sub>2</sub> **and** _E_<sub>1</sub> **and** \(\neg V_{out}\) **then**<br>
12: \(D_{out},V_2,V_{out}\leftarrow D_2,\) **false**, **true**<br>
13: **else if** _E_<sub>1</sub> **and** _E_<sub>2</sub> **and** \(\neg V_{out}\) **then**<br>
14: \(E_{out}\leftarrow\) **true**<br>
15: **end if**<br>
16: **end for**

Note that, because the valid signal in a register can only be modified by the parent when it is false, and by the child when it is true, the critical path no longer travels through more than one comparator, making it constant with respect to _n_. However, this causes an undesired effect where a register can’t possibly output two values in a row. We call this effect, illustrated in Figure 2 _bubbling_, and it renders the output non- streaming after the first value is output in O(log(_n_)) cycles.

_Bubbles_ appear due to the fact that each register can only be in read or write mode to prevent the critical path from growing with tree depth. In fact, this is the cause of needing the empty signal _E_ at each register, since a parent could be invalid but still have more data lagging behind, in which case we can’t make a decision and have to wait. If this effect is looked at at the root of the tree, we find that the output will alternate between valid and empty, for a total sorting time of \(\mathcal{O}(2\cdot n)\). For the first _m_ elements, it would take an acceptable \(2\cdot m+log(n)\) cycles.

However, it must be considered that timing is critical \[16\] within the context of BP+OSD, and dropping the 2 from the equation lowers total time from 4_m_ to 3_m_, an acceleration of \(1.33\times\), quite interesting for real-time error correction.

To achieve this goal, a final idea is proposed, named "hourglass sorting"<sup>1</sup>: nodes will have two output registers instead of one, thereby being able to both accept and emit a value each cycle. This idea is commonly known as double or ping-pong buffering \[17\]. This avoids the creation of _bubbles_ while keeping a constant critical path with respect to _n_. How this works is seen in Figure 3, and ensures that after the initial O(log(_n_)) initialization cost, the rest of the data streams out sequentially.

The algorithm outline is laid out in Algorithm 3. In short, both inputs are compared to decide which one (lowest) moves forward. In case one input is not valid (i.e: no more values will come from that sub-tree) the comparison is ignored. The active input is selected internally to move forward.

The input will be read only if at least a register is empty. Note that, by having two registers, this ensures that we will only prevent writing when both are full, guaranteeing data availability even after a branch is stalled. We always write

<sup>1</sup>The name is inspired by how the values falling down the tree resemble the grains of sand inside a hourglass

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
9
4
6
5
2
3
1
1
4
5
9
2
6
3
1
1
4
5
9
6
3
2
1

Fig. 2. _Bubbling_ effect on a simple tree with registers. _Bubbles_ are shown in dark, and appear on nodes that are outputting their values, unable to read at the same time.


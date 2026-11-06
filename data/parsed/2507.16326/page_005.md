<tbc>disposal the minimum of both trees. In each case, we select the minimum of the two and pass it on. Neither tree can have _bubbles_, so a value jumping ahead of others, which would disrupt ordering, is also not possible. This not only sorts the tree, but does it in a stable fashion if we give preference to the leftmost sub-tree, which is interesting for many applications. The base case, where a node only has two inputs, will always send the minimum first by construction. (This is, in essence, merge sort with a parallel construction of each level).

## IV. IMPLEMENTATION

A hardware implementation has been done in VHDL and is available on GitHub \[18\]. The most important modules within the system are the nodes themselves that implement the functionality described in Section III. An overview of their implementation is presented in Figure 4.

Both inputs and outputs are controlled using very lightweight interfaces. They include a data (_D_) signal, along with ready (_R_) and valid (_V_) control bits. A transaction is performed by the endpoints of an interface if and only if valid and ready signals are asserted, respectively, by the sender and receiver.

Following Algorithm 3, data is first sorted and selected according to the availability from the input valid signals, and<tbc>

<tbc>the values themselves. By default, data will flow from the input to register zero (which contains both data _D_<sub>0</sub> and valid _V_<sub>0</sub> registers). In the event that the output is not ready and _V_<sub>0</sub> is asserted, register one will receive the incoming datum instead. By construction, _D_<sub>1</sub>_\>D_<sub>0</sub> and \(V_1\Longrightarrow V_0\). Thus, we always output from register zero, and input when _V_<sub>1</sub>=0, therefore \(R_{in}=\neg V_1\). To ensure this property holds, register one is "shifted" to register zero when both are full, and the output is accepting a new value.

As seen, these operating principles make it so that no paths cross from the output to the input without first going through a register. The critical path is thus extremely fast, spanning just the comparator logic and a few gates and multiplexers.

To create a sorter for wider arrays, the basic cell is replicated in a tree-like structure (Figure 5). Special care is taken when a layer of the tree is not a power of two in size, by inserting nodes even when they don’t have both parents. This preserves timing integrity, since otherwise values from a sub-tree could jump ahead of others breaking the ordering of the output.

Our implementation can also include index registers, which are used to keep track of the position of the element within the array along with its value (this is not pictured in the diagrams). This is important for the BP+OSD application. Results in this work do not include these index registers, but the overhead in both logic and flip-flop elements would be \(n\cdot log(n)\).

## V. RESULTS

Various configurations have been synthesized on a xcvu9p- flga2104-2L-e \[19\] device using Vivado \[20\]. Values regarding resource use and maximum frequency of operation, with respect to array depth and element width, are presented for various configurations in  I.

It is noteworthy to point out that both LUT and REG usage are linearly proportional to \(n\cdot w\), where _w_ is the width of each input element. Doubling the number of elements in the array _n_ results in more resources than doubling the width of the elements _w_. Frequency is dependent on element width _w_, which is consistent with the design. Latency is given by log(_n_)+_n_, where log(_n_) indicates the time to the first output, and _n_ the number of cycles to wait until the array is fully sorted and output.

When compared to other implementations, sorting networks \[21\], \[8\] offer much better latency in the order of O(log<sup>2</sup>(_n_)), but rapidly run out of resources at costs proportional to \(\mathcal{O}(n\cdot\)<tbc>

RL
VL
DL
DR
VR
RR
<
V1
D1
Vo
Do
Rout
Vout
Out



Fig. 4. A single sorting cell. In dark blue, the inputs and output, in blue, the registers, with a top enable signal (green) and a bottom clear signal (red). Clock and reset signals are omitted for clarity.

Fig. 5. An example of a full tree for _n_=6. Note that the node in layer 2 is not removed even though it only has one parent.


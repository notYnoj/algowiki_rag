<tbc>integers from different original columns, allowing subsequent column sorts to compare previously separated values.

We accelerate these movements determined by position. The algorithm may form linear combinations of integer bits along the way, but ultimately restores the input integer that belongs at each destination. The rearrangements required by Columnsort have a special structure: they can be expressed using a constant number of exchanges of two fields in an address, together with sequential scans, which read or write an array in its storage order.

## 4.2 Circuits and the coding counterexample

A coding counterexample requires both a scheme recovering every message and a proof that routing on the same network cannot achieve its rate. A finite circuit specifies a predetermined sequence of XOR operations. Bits may be mixed in intermediate steps, but each original bit must reach its designated output. Turning the circuit wires into network edges gives a coding scheme; assigning matrix labels to nodes will bound the routing rate.

Figure 2(a) illustrates the circuit’s input-output requirement. The three _registers A,B,C_ are storage locations holding one bit each, initially _x,y,z_. Each horizontal line follows one register, and operations proceed from left to right. A black dot and an \(\oplus\) on the same vertical line form a _gate_: the black-dot value is unchanged, and the \(\oplus\) value is XORed with it. For example, the first gate changes _C_ from _z_ to \(z\oplus x\).

For every input (_x,y,z_), the six gates produce (_y,x,z_). Register _C_ assists communication during the computation and is therefore called an _auxiliary register_. Its initial value may be arbitrary and is restored to _z_ at the end. Thus an auxiliary register can also carry an independent message and need not start at zero.

Figure 2(b) turns each gate into a node, and wire segments between successive gates or endpoints on a register into unit-capacity undirected edges. Three sessions deliver _x,y,z_ to the destinations bearing the same letters. Nodes receive, compute, and transmit in circuit order, recovering every message. This example only illustrates the correspondence between a circuit and a communication scheme; a coding advantage additionally requires a circuit whose associated network cannot route at the same rate.

Assign each node an \(m\times m\) rational matrix, requiring the sink matrix minus the source matrix of each message to have full rank _m_. Define an edge’s _length_ as the rank of the difference between its endpoint matrices. These lengths are used to bound routing; the actual edge capacities remain<tbc>

(a) Fixed rearrangement
8
3
Transpose
8
6
6
1
3
1
(b) Column sorts and rearrangement
9
2
7
4
2
1
4
6
9
1
3
7
4
8
1
Sort
Transpose
2
3
8
Sort
2
5
8
6
3
5
9
8
7
1
5
7
4
6
9

Figure 1: (a) A fixed position interchange preserves values. (b) Colors identify original columns; rearrangement brings different colors into the same column. The figure illustrates the operations only; Section 7 gives the full Columnsort procedure.


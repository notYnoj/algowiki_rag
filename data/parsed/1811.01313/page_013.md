External Memory
External Memory
Array A
Array C
Array A
Array C
π(1) d1
π(2) d2
π(8) ds
C[1] C[2]
C[7] C[8]
π(1) d1
π(2) d2
π(8) ds
C[1] C[2]
C[7] C[8]
1
2
8
9
12
1
2
8
9
12
1
0
0
Memory Nodes
Memory Nodes
(a)
(b)
External Memory
External Memory
Array A
Array C
Array A
Array C
π(1) d1
π(2) d2
π(8) ds
C[1] C[2]
C[7] C[8]
π(1) d1
π(2) d2
π(8) ds
C[1] C[2]
C[7] C[8]
1
2
8
9
12
1
2
8
9
12
1
9
1
9
0
0
Memory Nodes
Memory Nodes
(c)
(d)
External Memory
Array A
Array C
π(1) d1
π(2) d2
π(8) ds
C[1] C[2]
C[7] C[8]
1
2
8
9
12
13
1
9
1
0
0
Memory Nodes
(e)

Figure 1: I/O-graph for an array _A_ consisting of 3-bit strings \(d_1,\cdots,d_8\) . In this example, each disk block contains two words of _w_=3 bits, i.e., _B_=2 (and _b=Bw_=6). Also, the main memory holds _M_=6 words (_m_=18). Figure (a) shows the initial I/O graph. For each disk block, we have initially one block node which is illustrated underneath them. Black nodes are dead, and white nodes are live. Figure (b) shows the updated I/O-graph after making an I/O to access the first disk block. Figure (c) is the I/O graph after accessing the block containing _C_\[1\] and _C_\[2\]. Figure (d) shows the graph after making another I/O on the first disk block. Also, we create a new memory node after every _m/b=M/B_=3 I/Os and mark the old memory node as dead. Figure (e) shows the updated graph after accessing some block other than the input or output.


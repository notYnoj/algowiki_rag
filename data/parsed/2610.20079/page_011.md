Our circuits consist of registers and XOR gates. Each register stores one bit. A gate reads the current values of specified registers and updates some of them according to a prescribed linear rule; registers not updated retain their values. A gate acting on _r_ registers is thus a linear map \(g:\mathbb{F}_2^r\rightarrow\mathbb{F}_2^r\), where F<sub>2</sub>={0,1} with addition and multiplication modulo two. We specify its action directly by register names: for example, \(y\leftarrow y+x\) replaces _y_ by the XOR of the two current values and leaves _x_ unchanged. The circuit executes its gates in a predetermined order.

In the circuit diagram, each gate is a vertex. For each register, wires connect the gates involving it in execution order, with an input and an output at the two ends of this path. A wire entering a gate carries the value before the update, and the outgoing wire carries the value after it. Thus a register persists along a path of wire segments, and its value may change at a gate. All wires participating in a gate meet at its vertex, which computes the register value for each outgoing wire.

To compare coding with routing, regard every wire segment as an undirected edge of unit capacity, obtaining a graph _G_=(V_,E_). Write _s<sub>i</sub>,t<sub>i</sub>_ for the input and output of register path _i_. If the circuit sends all initial values to the outputs according to a permutation \(\sigma\), create the sessions \(s_i\rightarrow t_{\sigma(i)}\) and give the sources independent messages. The gate computations specify how to encode these messages. Routing may use an edge in either direction, with the two directions sharing its capacity; the circuit order specifies only how this particular coding scheme runs. Edges belonging to different register paths are retained separately, so the graph may contain parallel edges.

A temporary wire is created by copying an existing value and ends after its last use. It begins at a copy gate and has no independent source message or session. Such wires are nevertheless edges of the same graph and are included in every capacity and rank sum. Copying and later discarding a value are local linear operations, so they fit the same gate semantics.

## 5.1 A Finite Linear Circuit

We start with a finite circuit on bits and attach subspaces of an eight-dimensional rational vector space to its registers. We later combine copies of the circuit and their labels in a 512-dimensional space. The local circuit has _v_=111 pairs of data registers and _R_=439 auxiliary registers. Every auxiliary initial value is arbitrary and is restored; it can therefore carry an independent message. A temporary copy, in contrast, is created during a computation and carries no additional source message.

We use the local circuit of eumemic and DreamingOfClouds \[eum26,Dre26\], with the properties stated below. Let _E_=Q<sup>8</sup> with its usual positive definite dot product, and let \(\ell_t\), \(t\in[v]\), be the 111 one-dimensional rational subspaces in that construction. Their spanning vectors are drawn from the _E_<sub>8</sub> root system, a fixed configuration of vectors in eight dimensions. We use their rational coordinates and the relations below, then prove the properties of the combined circuit and its application to sorting.

Write \(x=(x_t)_{t\in[v]}\) and \(y=(y_t)_{t\in[v]}\) for the two collections of data bits, and \(z=(z_r)_{r\in[R]}\) for the auxiliary bits. All these data and auxiliary registers remain present from input to output. For a subspace \(U\subseteq E\), \(U^\perp\) denotes its orthogonal complement, and 0 denotes the zero subspace.

**Lemma 5.1** (Properties of the finite circuit)**.** There is a finite binary linear schedule on 2_v+R_=661 independent inputs that maps

\((x,y,z)\longmapsto(x,y+x,z).\)

Each data or auxiliary register is assigned rational subspaces of _E_ that form an inclusion chain \(U_0\subseteq U_1\subseteq\cdots\) . These are labels for the analysis, independent of the register’s bit value. The input<tbc>


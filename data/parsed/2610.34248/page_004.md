retrieve its neighbor list, then accesses the vector database to obtain these neighbors’ vectors for distance computation.

### 2.4 Secure Multi-Party Computation

Secure multi-party computation (MPC) enables multiple parties to jointly compute a function over their private inputs while only revealing the output to designated parties [47]. We use secret-sharing MPC protocols where, for each intermediate value _x_, all parties hold its secret sharing denoted as \(\unknown x\unknown\). The security ensures that the adversary cannot learn the value even when corrupting some number of parties as allowed by the threat model. Our system treats MPC protocols as black boxes; thus, we describe computation directly over secret shares. In particular, we use \(\unknown x\unknown+\unknown y\unknown\) and \(\unknown x\unknown\times\unknown y\unknown\) to denote addition and multiplication in MPC over secret-shared values. Typically, given network bandwidth BW and round-trip time RTT, MPC protocols follow this online latency model:

\(T_\text{online}\approx\text{Round}\cdot\text{RTT}+\frac{\text{Communication}}{\text{BW}}+\text{Computation}.\)

Here, Computation is each party’s local, non-interactive work and is often almost free. Communication is the total data exchanged and scales linearly with the multiplication gate count. Round is the number of sequential interaction steps, determined by the circuit’s multiplicative depth.

**Making Algorithms Oblivious.** Under MPC, oblivious execution has three requirements:

(1) **Logic flow.** For fixed public parameters, the algorithm follows the same sequence of operations. For example, each loop runs for a fixed number of iterations.

(2) **Data structures.** For fixed public parameters, intermediate data structures have the same sizes and update schedule.

(3) **Data access pattern.** For fixed public parameters, physical- address sequences are indistinguishable across private inputs.

**Oblivious Access in MPC.** Among these requirements, oblivious data access has been widely studied as a general primitive. MPC protocols based on secret-sharing can typically support any circuit, but random accesses are expensive to represent as circuits. To support private accesses on large arrays without incurring a cost linear to the array, one would need to use an Oblivious RAM (ORAM) [18] by executing the ORAM client in MPC [19]. This protocol is also called Distributed ORAM (DORAM). Given a secret-shared array \(\unknown\vec{v}\unknown\) and secret-shared index \(\unknown i\unknown\), DORAM enables parties to jointly compute \(\unknown\vec{v}[\unknown i\unknown]\unknown\) (the secret-shared value at secret-shared position) without revealing the index or the value to any party. DORAM has been optimized in different ways, including circuit-based minimization (e.g., [44]) and protocol-level adaptation (e.g., [14]). Although the most efficient construction can achieve _O_(log_N_) communication overhead [39], DORAM still incurs an _O(N_) computational cost. Moreover, DORAM accesses are stateful and often sequential, making batched accesses difficult to parallelize. Therefore, rather than directly adopting generic DORAM in our MPC protocol, we propose a specialized algorithm to implement an oblivious access pattern.

**Security Models.** Beyond these requirements, oblivious algorithm design also depends on the security model. For secure ANN, we distinguish four models based on who has plaintext access to each input and who performs the search, from general to specific:

(1) **Symmetric MPC.** The computation parties have no access to the database, index, or query in plaintext. They perform the search over secret values. This is also the standard setting in the MPC literature. Our paper targets this model for data collaboration between untrusted organizations and computation outsourcing by a single data owner.

(2) **Client-server search.** The client has plaintext access to the query, while the server has plaintext access to the database and index. They jointly perform the search without learning the other’s input beyond the result. SANNS and PANTHER follow this model [11, 28].

(3) **Storage outsourcing.** The client has plaintext access to the database, index, and query. It encrypts the database and index and then outsources them to an untrusted server. During search, the client retrieves data from the server and performs the search locally. Compass follows this model [51].

(4) **Query-private search.** The client has plaintext access to the query. The database and index are public and stored on the server, so both the client and server have plaintext access to them. During search, the client retrieves database and index entries from the server and searches locally. Thus, only the query is hidden from the server. Pacmann follows this model [50].

## 3 SYSTEM OVERVIEW

We consider a private HNSW search involving two input-holding parties and a set of _s_ MPC servers; Figure 1 gives the high-level architecture. The two input parties are: (1) the database owner (DO), who holds a private vector dataset \(\mathcal{D}=\{\vec{x}_i\}_{i=0}^{N-1}\subset\mathbb{R}^d\) together with an HNSW graph index G built over D, and (2) the Puerier, who holds the private query vector \(\vec{q}\in\mathbb{R}^d\). DO and Puerier are two logical parties who do not need to trust each other, but they could be instantiated as the same physical party, in which case the protocol reduces to the standard outsourced computation model. The functionality of the protocol is shown in Figure 2.

### 3.1 Threat Model

We assume a semi-honest, probabilistic polynomial-time (PPT) adversary who may corrupt at most _t_ MPC servers and one or both input parties. Our protocol achieves standard simulation-based security [7]. For any PPT adversary corrupting at most _t_ MPC servers and one or both input parties, there exists a PPT simulator whose output is computationally indistinguishable from the adversary’s output, using only the corrupted parties’ inputs, their outputs under

MPC Servers Database Owner Querier Secret-share D, G Oblivious HNSW search Secret-share q ?
Database privacy Query privacy Top-k results Vector data D S semi-honest servers up to t corrupt Query vector q HNSW index G

**Figure 1: System overview of Oblivious HNSW**


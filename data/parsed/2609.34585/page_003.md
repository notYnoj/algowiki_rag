<tbc>during training when an instance stops recursing (Graves, 2016). This acts as hard mining, because easy instances leave early and the remaining steps go to hard ones. Adding noise to _z_ at test time and running several copies in parallel yields extra samples (Sghaier et al., 2026).

## 2.2 THE TRM4CO FRAMEWORK

**Input embedding and encoder.** The encoder maps an instance _x_ to _n_ node tokens in R_<sup>d</sup>_ and, for MIS, passes on the adjacency matrix \(A\in\{0,1\}^{n\times n}\) ( 4). _P_ learnable prefix tokens are prepended and serve as global registers, _i.e._ tokens attached to no node that every node can attend to, and we write _e_ for the resulting _P+n_ tokens. _A_ is zero-padded on the prefix rows and columns, so those registers receive no bias. No global positional encoding over the token order is used for either problem, so the model is permutation equivariant by construction. For MIS, the node tokens are a linear projection of the degree, a random-walk positional encoding (RWPE, Dwivedi et al., 2022), and a uniform random scalar that breaks the symmetry between structurally identical nodes. The edges enter the recursion through _A_. For TSP, the geometry is entirely in the coordinates _X_. The TSP node tokens are a linear projection of _X_ lifted with sinusoidal features at _L_<sub>pe</sub> octaves per axis (Mildenhall et al., 2020), and no attention bias is needed. This asymmetry is deliberate. The graph structure of MIS has to be injected into attention, whereas for TSP on the unit square, the coordinates already determine locality and the model can recover it via standard self-attention.

**Recursive core with edge-biased attention.** The core of our model is the two-block network of Eq. (1) with one change. Every attention head _h_ of every call computes

\(\mathrm{softmax}\left(\frac{\mathbf{Q}_h\mathbf{K}_h^\top}{\sqrt{d_h}}+\gamma_hA\right),\) (2)

where **Q**_<sub>h</sub>_ and **K**_<sub>h</sub>_ are the queries and keys of head _h_ with dimension _d<sub>h</sub>_, and \(\gamma_h\) is a learnable scalar per head and block, initialized at zero. _A_ is the adjacency matrix of the instance, with _A<sub>ij</sub>_=1 when nodes _i_ and _j_ are neighbors and 0 otherwise, so the bias raises or lowers the attention between adjacent nodes. With \(\gamma_h=0\) the head is standard self-attention, as \(\gamma_h\rightarrow\infty\) it attends only to<tbc>

Recursive backbone Weight-tied, 7M parameters Depth: D steps Width: K rollouts
Instance
Encoder
Decoder
Solution
y
Output head MIS: node scores TSP: edge scores
Structure MIS: adjacency
MLP
Lx
MIS: graph
Node features MIS: degree, RWPE, noise TSP: sinusoidal
1x
Independent set
2x
Decode & select MIS: greedy TSP: edge insertion
Self-attention logits + γh A
Linear + P prefix tokens
Post-processing MIS: peel kp, restart TSP: 2-opt
TSP: cities
Tour
e tokens
y answer
z latent
H cycles per step, gradient in the last
Train: halt once solved
Self-relabel: better solution becomes label

Figure 1: TRM4CO overview. An encoder turns an instance into node tokens plus _P_ prefix tokens and, for MIS, the adjacency matrix _A_ that biases every attention call of the shared recursive backbone (Eq. 2). Each step runs one TRM recursion, and test-time compute scales along depth _D_, the number of steps, and width _K_, the number of parallel rollouts. A problem-specific decoder turns the answer state of every step into a feasible solution, with sequential peeling for MIS and edge insertion with 2-opt for TSP, and the objective keeps the best candidate. In training, a solved check against the label halts an instance, and better solutions can replace the labels. Red marks what we add to TRM.


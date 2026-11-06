## A ALGORITHM AND PROBLEM-SPECIFIC HOOKS

Algorithm 1 lists the procedures of Section 2.3 that MIS and TSP share, and  4 the problem- specific hooks it calls. Figure 4 unrolls one recursion step.

## B HYPERPARAMETERS

**Training.** The loss is a cross-entropy per node (MIS) or per successor (TSP) against the labels of  4, with peel augmentation for MIS and the eight symmetries of the square for TSP applied on the fly (see below). Each model trains on two H100 GPUs. Several reported checkpoints continue earlier runs, and the epoch counts in  5 are summed over all stages. The ER supervised checkpoint runs 10,000 epochs with the edge-biased architecture, 5000 at _D_=64 and 5000 at _D_=32, warm-started from a run with a message-passing encoder. Its self-relabeling continuation adds 3000 epochs. The SATLIB and TSP-10000 checkpoints continue a first run of 1000 epochs for another 1000. The label-free ER chain of  3 runs 5000 epochs with one-shot relabeling and three stages of 3000 epochs with peeling, and the label-free TSP-500 chain runs stages of 500, 500, and 1000 epochs.

**Implementation details.** The halting head of TRM is retained, but we block its gradient. Its loss is still computed with weight 0.5 as in TRM for logging, and the head is used neither for halting nor<tbc>

\begin{tabular}{ccc}
Hook & MIS & TSP \\
Instance _x_ & Adjacency \(A\in\{0,1\}^{n\times n}\) & Coordinates \(X\in[0,1]^{n\times 2}\) \\
Tokens Emb(_x_) & Linear\[deg, RWPE, _u_∼U(0,1)\] & \(\text{Linear}[X,\mathrm{sin}/\mathrm{cos}(2^l\pi X)]_{l<L_\mathrm{pe}}\) \\
Attention bias & Adjacency _A_ & None (standard self-attention) \\
Head \(g_\theta(y)\) & Node logits \[_n,_2\] & Bilinear successor logits \[_n,n_\] \\
Decoder Dec & Greedy independent set in score order & Greedy edge insertion by <o>_g_</o><sub>ij</sub>_/d<sub>ij</sub>_ \\
Wrapper W & Sequential peeling around the recursion & 2-opt on the tour returned by SOLVE \\
Objective _c(s_) & |_S_| (max) & Tour length (min) \\
Solved\((g_\theta(y),\ell,x)\) & Greedy \(|S|\ge|\ell|\) & Successors match the canonical \(\ell\) \\
Labels \(\ell\) & KaMIS 10s (ER), exact (SATLIB) & LKH-3 (1000 trials) \\
Augmentation & Random peel of label nodes & Dihedral-8 of the unit square \\
\end{tabular}

+yh A in every fo
Train: CE loss vs. label l
A
Cycles 1 to H - 1, no gradient
Cycle H, with gradient
Halt once solved
y
fo
y
y
fo
y
go
e
Test: decode s, score with c(s)
Tokens
Run D steps, keep best s
z
fo
z
fo
z
z
fo
Test: z + σξ K rollouts
L latent updates
Carry (y, z) detached to step t+1

Figure 4: One recursion step of TRM4CO, unrolled. Gray is the TRM schedule of Eq. (1), with _L_ latent updates and one answer update per cycle, _H_ cycles per step, gradient only through the last cycle, and (_y,z_) carried detached to the next step. Test-time noise on _z_ (Sghaier et al., 2026) gives _K_ independent rollouts. Red is what we change. For MIS, the adjacency _A_ biases every attention call (Eq. 2). At test time, every step (TSP) or every peeling round (MIS) is decoded into a feasible solution and scored with the objective. In training, the solved check of  4 halts an instance in place of the learned halting signal.

4: Problem-specific hooks of Algorithm 1. Everything not listed here (the core, the recursion schedule, deep supervision, and the self-relabeling loop) is shared.


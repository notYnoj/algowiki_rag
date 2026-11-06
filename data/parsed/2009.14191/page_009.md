Summarizing, any stable matching matches _c<sub>j</sub>_ and _d<sub>j</sub>_ to exactly one variable occurring in clause _C<sub>j</sub>_, and for each variable _x<sub>i</sub>_, either all or none of the agents \(x_i^k\) are matched to such 2-sets {_c<sub>j</sub>,d<sub>j</sub>_}. In other words, setting those variables _x<sub>i</sub>_ such that \(x_i^k\) is matched to a 2- set {_c<sub>j</sub>,d<sub>j</sub>_} to true and all other variables to false, we get a solution of the 1-in-3 Positive 3-Occurrence-SAT instance from each stable matching.

"Inverting" this process (i.e., matching each clause to its true variable, and then matching the variable gadgets as described above), allows to construct a stable matching from a solution to the 1-in-3 Positive 3-Occurrence-SAT instance.

Note that MDSR is in NP as the size of the input is \(\Omega(\genfrac(){pt}{2}{n}{d-1})\), where _n_ is the number of agents, as the master preference list contains \(\genfrac(){pt}{2}{n}{d-1}\) sets of size _d_-1, and, thus, stability can be verified in time polynomial in the input size by just checking for each _d_-set whether it is blocking.

We now formally describe the reduction and prove its correctness.

## 3.2.1 The reduction

Let _x_<sub>1</sub>_,...,x<sub>n</sub>_ be the variables and let _C_<sub>1</sub>_,...,C<sub>m</sub>_ be the clauses of a 1-in-3 Positive 3- Occurrence-SAT instance I. We construct a 3-DSR-ML instance \(\mathcal{I}'=(A,(\succ a)_{a\in A})\) as follows.

For each clause _C<sub>j</sub>_, we add two agents _c<sub>j</sub>_ and _d<sub>j</sub>_ to _A_. For the _k_-th occurrence (\(k\in[3]\)) of a variable _x<sub>i</sub>_ in a clause, we add an agent \(x_i^k\). We refer to the agent corresponding to the \(\ell\)-th literal of clause _C<sub>j</sub>_ as \(y_j^\ell\). The _k_-th occurrence of _x<sub>i</sub>_ is also the \(\ell\)-th literal of some clause _C<sub>j</sub>_, and we will denote the agent \(x_i^k\) also by \(y_j^\ell\), i.e., \(x_i^k=y_i^\ell\). For each agent \(x_i^k\), we add six agents \(z_i^{k,1},\dots,z_i^{k,6}\) to _A_.

For each \(j\in[m]\), we define A_<sub>j</sub>_ to be the following part of the master list:<tbc>

\(\{c_j,d_j\}\succ\{y_j^1,d_j\}\succ\{y_j^3,c_j\}\succ\{y_j^2,d_j\}\succ\{y_j^2,c_j\}\succ\{y_j^3,d_j\}\succ\{y_j^1,c_j\}.\)

<tbc>For each agent \(x_i^k\), we define \(\mathcal{B}_i^k\) to be the following part of the master list (note that (by renaming \(x_i^k\) to _a_, agent \(z_i^{k,1}\) to _b_, agent \(z_i^{k,2}\) to _c_, _..._, and \(z_i^{k,5}\) to _f_) this contains the instance I<sub>instable</sub> from Observation 3.1; this ensures that \(x_k^i\) has to be matched to a 2-set which is before \(\mathcal{B}_i^k\) in the master list):

\(\{x_i^k,z_i^{k,1}\}\succ\{x_i^k,z_i^{k,2}\}\succ\{x_i^k,z_i^{k,3}\}\succ\{x_i^k,z_i^{k,5}\}\succ\{z_i^{k,1},z_i^{k,4}\}\succ\{z_i^{k,2},z_i^{k,3}\}\)<br>
\(\succ\{x_i^k,z_i^{k,4}\}\succ\{z_i^{k,1},z_i^{k,5}\}\succ\{z_i^{k,2},z_i^{k,4}\}\succ\{z_i^{k,1},z_i^{k,3}\}\succ\{z_i^{k,3},z_i^{k,4}\}\)<br>
\(\succ\{z_i^{k,1},z_i^{k,2}\}\succ\{z_i^{k,2},z_i^{k,5}\}\succ\{z_i^{k,3},z_i^{k,5}\}\succ\{z_i^{k,4},z_i^{k,5}\}\succ\{x_j^i,z_i^{k,6}\}\)<br>
\(\succ\{z_i^{k,1},z_i^{k,6}\}\succ\{z_i^{k,2},z_i^{k,6}\}\succ\{z_i^{k,3},z_i^{k,6}\}\succ\{z_i^{k,4},z_i^{k,6}\}\succ\{z_i^{k,5},z_i^{k,6}\}.\)

We extend this to a sublist C_<sub>i</sub>_ as follows:<tbc>

\(\{x_i^1,x_i^2\}\succ\{x_i^2,x_i^3\}\succ\{x_i^1,x_i^3\}\succ\mathcal{B}_i^1\succ\mathcal{B}_i^2\succ\mathcal{B}_i^3.\)

<tbc>The complete master list looks as follows.

\(\mathcal{A}_1\succ\dots\mathcal{A}_m\succ\mathcal{C}_1\succ\cdots\succ\mathcal{C}_n\succ\dots,\) where the rest is arbitrarily ordered.

We call the constructed 3-DSR-ML instance \(\mathcal{I}'\).


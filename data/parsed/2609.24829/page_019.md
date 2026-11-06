**Definition 5.1** (Random Partition Communication Model)**.** Consider the following two-player communication game for evaluating a function on an input graph _G_=(_V,E_):

1. Let \(\sigma:E\rightarrow\{A,B\}\) be a random mapping where \(\mathrm{Pr}[\sigma(e)=A]=p\) for each \(e\in E\) and all edges are mapped independently. Let \(\sigma_A(E)=\{e\in E:\sigma(e)=A\}\) and \(\sigma_B(E)=\{e\in E:\sigma(e)=B\}\)<tbc>

2. Alice receives input \(S_A=\sigma_A(E)\).<tbc>

3. Bob receives input \(S_B=\sigma_B(E)\), and<tbc>

4. Both have access to a string of public random bits _R_.

A one-way protocol _P_ to evaluate a function _f_ on _G_ has two components:

1. A message \(M(S_A,R)\in\{0,1\}^*\) that Alice sends to Bob.<tbc>

2. An output computed by Bob, out(_M(S<sub>A</sub>,R),S<sub>B</sub>,R_).<tbc>

<tbc>We define the error of _P_ to be<tbc>

\(\mathrm{err}(P,f):=\mathrm{max}_G\{\mathrm{Pr}[\mathrm{out}(M(S_A,R),S_B,R)\neq f(G)]\}\)

<tbc>where the probability is taken over the random choices of \(\sigma\) and _R_. Let<tbc>

\(\mathrm{cost}(P):=\mathrm{max}_{G,\sigma,R}|M(S_A,R)|\)

<tbc>i.e., the longest message sent under any input, partition, and value of the public random string. Let<tbc>

\(\mathrm{cost}_\mathcal{K}(P):=\mathrm{max}_{G\in\mathcal{K},\sigma,R}|M(S_A,R)|\)

<tbc>be the cost of the protocol amongst graphs _G_ in some set K. Define,<tbc>

\(\mathrm{R}_{\delta,p}(f):=\mathrm{min}_P\{\mathrm{cost}(P):\mathrm{err}(P,f)\le\delta\}\)

<tbc>and let

\(\mathrm{R}_{\delta,p}^\mathcal{K}(f):=\mathrm{min}_P\{\mathrm{cost}_\mathcal{K}(P):\mathrm{err}(P,f)\le\delta\}\)

We emphasize that \(\mathrm{R}_{\delta,p}^\mathcal{K}(f)\) is the maximum length of a message sent when \(G\in\mathcal{K}\) by a protocol that has error at most \(\delta\) on _any G_.

We first define two communication problems.

**Definition 5.2** (Triangle Testing and Tolerant Triangle Testing)**.** For \(0<\tau\), define the function \(\mathrm{TRITEST}_{\tau,m}(\cdot)\) on graphs with at most _m_ edges and either 0 or \(\tau\) triangles where<tbc>

\(\mathrm{TRITEST}_{\tau,m}(G)=\left\{\begin{array}{ c c }
0 & \text{if}G\text{is triangle-free} \\
1 & \text{if}G\text{contains exactly}\tau\text{triangles}
\end{array}\right.\)

<tbc>For \(0<\tau_1<\tau_2\), define the function \(\mathrm{TOLTRITEST}_{\tau_1,\tau_2}(\cdot)\) on graphs at most _m_ edges with either 0, \(\tau_1\), or at least \(\tau_2\) triangles where<tbc>

\(\mathrm{TOLTRITEST}_{\tau_1,\tau_2,m}(G)=\left\{\begin{array}{ c c }
0 & \text{if}G\text{is triangle-free} \\
1 & \text{if}G\text{contains exactly}\tau_1\text{triangles} \\
2 & \text{if}G\text{contains at least}\tau_2\text{triangles}
\end{array}\right.\)


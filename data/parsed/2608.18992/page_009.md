\(\hat{\Pi}=\{(2,v_1-\rightarrow^{m_1}u_1)(2,v_2-\rightarrow^{m_2}u_2),(5,v_1-\rightarrow^{m_3}u_1),(5,v_3-\rightarrow^{m_4}u_3)\}\)

**(b)** The table shows a possible execution on the network in Figure 1a and the resulting extended transcript \(\hat{\Pi}\) (see Def. 12). For simplicity, we do not distinguish between a node and its ID in this example.

\(\blacktriangleright\) **Lemma 1** (Cut-based Energy Lower Bound)**.** _Consider a randomized_ \(\epsilon\)_-error algorithm_ A _in the sleeping_ CONGEST _model, and let_ G _be a probability distribution of n-node graphs such that every_ \(G\in\mathcal{G}\) _has the same set of nodes. Let Z be a random variable that is a function of G._

_Suppose that there exist sets V<sub>A</sub> and V<sub>B</sub> such that_ (_V<sub>A</sub>,V<sub>B</sub>_) _is a cut of every G. Let_ \(U\subseteq V_A\) _and_ \(\partial U\subseteq V_B\) _be any sets such that the edges in_ \((U,\partial U)\) _form an edge cut, and every node in U has a neighbor in_ \(\partial U\)_. Let_ \(d_U=max_{G\in\mathcal{G}}max_{u\in U}e(u,\partial U)\) _be the maximum number of such neighbors. Moreover, the choice of V<sub>A</sub> and V<sub>B</sub> must be independent of the algorithm’s execution._

_Finally, let_ \(\Pi_U\) _be the transcript of the messages sent to the nodes in U across_ \((U,\partial U)\)_. If, for some L=O_(poly(_n_))_, we have_ \(\mathbf{I}[\Pi_U:Z|S_{V_A}]\ge L\)_, where S<sub>V<sub>A</sub></sub> is the initial state of the nodes in V<sub>A</sub>, then the following hold:_

(_i)_ _Let_ \(\alpha_U\) _be the number of total awake rounds summed over the nodes in U._ _If_ \(|\text{supp}(Z)|\le 2^{c\cdot L}\)_, for some positive constant c, then_ \(\mathbf{E}[\alpha_U]=\Omega\big(\frac{L}{d_Ulogn}\big)\).

_(ii)_ _The worst-case energy complexity bound of_ A _is_ \(\Omega\big(\frac{L}{d_U|U|logn}\big)\).

Figure 1a shows how the different node sets and the cut relate to each other.

Overview of the Proof of Lemma 1. We first outline the high-level ideas and provide the full details in Section A. There are several technical challenges that we need to overcome. First, we do not impose any restriction on the algorithm’s round complexity. This, combined with the fact that nodes have access to a global clock and know the current round number, may lead us to believe that the algorithm could employ a time-encoding trick, where information of _L_ bits is conveyed across the cut by sending just a single bit in a specific round of an interval of length 2_<sup>L</sup>_, thus drastically reducing the number of required awake rounds.<sup>3</sup> If successful, then the algorithm would be able to convey _L_ bits of information across an edge in just a single awake round of the sender and receiver.

<sup>3</sup> In fact, it is known [44] that time-encoding can reduce the _message complexity_ for many graph problems from \(\Theta\big(n^2\big)\) to near-optimal _O(n_polylog_n_) messages at the cost of increasing the number of rounds.

\begin{tabular}{ccc}
Round & Awake Nodes & Communication (\(\partial U\rightarrow U\)) \\ 2 & _u1, u2, v1, v2_ & _v1 -\rightarrow^{m_1}u_1, v2 -\rightarrow^{m_2}\{u_2,u_3\} \\ 5 & _u1, u3, v1, v3_ & _v1 -\rightarrow^{m_3}u_1, v3 -\rightarrow^{m_4}u_3 \\ \end{tabular}

u1 v1 u2 v2 u3 v3 U
U 4
8U VA VB

**(a)** The cut-based lower bound approach. Lemma 1 gives a bound on the total number of awake rounds of the nodes in _U_.

**Figure 1**


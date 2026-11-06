**Algorithm 1** Vanntec(_S_, #tree _k_, #cluster _n_, threshold \(\theta\))

**for** \(1\le i<k\) **do** ; Tree \(T_i\leftarrow\emptyset\) # set of edges

function REC (parent _p_, strings _S_)

**If** \(|S|\le\theta\) **then** \(\forall x\in S;T_i\leftarrow T_i\cup\{(p,x)\}\); **else**

\(x,y\leftarrow\) randomly chosen from _S_

\(T_i\leftarrow T_i\cup\{(p,x),(p,y)\}\)

\(S_x\leftarrow\{z\in S||\|x-z\|<\|y-z\|\}\)

REC(_x,S<sub>x</sub>_);REC(_y,S_\\_S<sub>x</sub>_)

REC("root", _S_)

return EAC(_n_, \(\{T_1,\cdots T_k\}\))

in the appendix Fig.9 shows the ensemble effect of Vanttec, which demonstrates the importance of aggregating multiple trees via consensus clustering (EAC), and the visualization of the first tree formed by Vanttec in the first list of Medrxiv dataset, which showcases its interpretability.

## 6 Verbalized Submodular Maximization

A _submodular set maximization_ task is a task of maximizing the utility _f(S_) of a solution \(S\subseteq C\) in a search space _C_, where _f(S_) has _diminishing returns_, i.e., \(\forall x\in C,S\subseteq S'\subseteq C;f(S'\cup\{x\})-f(S')\le f(S\cup\{x\})-f(S)\). The task has various applications including information retrieval as well as resource allocations. This approach, however, only works in a setting that has a well-defined submodular evaluation function _f_. Once the set _C_ is the universe of natural language input, and when the criteria for optimization can be only informally specified, classical approaches toward submodular maximization are not directly applicable. We propose _Verbalized Greedy Submodular Maximization (VGSM)_, a verbalized algorithm that follows the classical greedy algorithm that guarantees 1-1_/e_ optimality. VGSM is an (_O_(|_C_|)_,O_(|_C_|))-VA for selecting |_S_|=_k_ elements from _C_, whose step _i_ selects an element from |_C_|-_i_ remaining elements. It is based on chat interactions, whose step incrementally asks for a new element. While traditionally submodular maximization requires a concrete evaluation function _f_, VGSM specifies an implicit score function by giving a prompt to the LLM (available in the appendix). Although it does not produce an absolute score value \(f(S\cup\{x\})\) for a newly selected element \(x\in C\backslash S\), this is not an issue because greedy algorithm only requires a contrastive measure that encodes the selection policy. We evaluated this approach on WiFi Access Point (AP) Optimization and two Retrieval Augmented Generation tasks.

### WiFi AP Optimization

This is a classic application of submodular maximization. Using 10 real- world floor plans obtained from HouseExpo dataset \[Li et al., 2020\], we created a coarse grid of height and width at least 16 cells, then obtained the exact optimal WiFi AP locations for _k_=3 APs using a branch-and-bound procedure under the submodular log-distance path loss model (appendix Sec. D.3). Visualization of the optimal locations indicated that the APs should be placed near the center of or the boundaries between the rooms to provide the maximum coverage (appendix Fig. 14), matching our natural intuition. This suggests that an LLM could return a reasonable location assignments, albeit imprecise or suboptimal, if it actually has a strong common-sense.

We compared VGSM with a **baseline** which uses JSON-structured decoding to return the entire assignment as a list of (_x,y_) coordinates. Both approaches are given the same prompt prefix which specifies the evaluation function in python code and an ASCII art floor map, ensuring the same amount of information is given. We measured the runtime and the optimality gap against the optimal<tbc>

medarxiv
better
Vanttec, k:5, 0:16
kwick
0.5
vanttec, k:5, 0:16, sym
kwick, sym
vanttec, think, k:5, 0:16
kwick, think
vanttec, think, k:5, 0:16, sym
kwick, think, sym
0.4
emb.
32
32
adjusted. mi
0.3
8
8
32
8
8
0.022
8
0.2
0:125
8
32
8
32
0.1
32
8
10-1
100
101
102
103


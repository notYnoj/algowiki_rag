The general assumption in finding an optimal decision tree is that these goals are identical, that is, that each decision (edge) takes the same amount of time (cost) as any other; this is noted in Section 6.2.2 of Knuth’s _The Art of Computer Programming_ [10, p. 429]. In exercise 33 of Section 6.2.2, however, it is conceded that this is not strictly true; in the first edition, the exercise asks for an algorithm for where there is an inequity in cost between a fixed cost for a left branch and a fixed cost for a right branch [11], and, in the second edition, a reference is given to such an algorithm [12]. Such an approach has been extended to cases where each node has a possibly different, but still fixed, asymmetry [13].

In practice the asymmetry of branches in a microprocessor is different in character from any of the aforementioned formulations. On complex CPUs, such as those in the Pentium family, branches are predicted as taken or untaken ahead of execution. If the branch is predicted correctly, operation continues smoothly and the branch itself takes only the equivalent of one or two other instructions, as instructions that would have been delayed by waiting for the branch outcome are instead speculatively executed. However, if the branch is improperly predicted, a penalty for misprediction is incurred, as the results of speculatively executed instructions must be discarded and the processor returned to the state it was at prior to the branch, ready to fetch the correct instruction stream [14]. In the case of the Pentium 4 processor, a mispredicted branch takes the equivalent of dozens of instructions [15]. This penalty has only increased with the deeper pipelines of more recent processors.

In this paper, we discuss the construction of alphabetic binary trees that are optimized with respect to the behavior of conditional branches in microprocessors. We introduce a general dynamic programming approach, one applicable to such architecture families as the Intel Pentium architectures, which use advanced dynamic branch prediction, and the ARM architectures, most instances of which use static branch prediction. These are not only representative of two styles of branch prediction; they are also by far the most popular processor architecture families for 32-bit personal computers and 32-bit embedded applications, respectively. ARM architectures such as those of the ARM7 and ARM9 families use no or static branch prediction [16]. Such processors are used for most mobile devices, including cell phones and iPods. ("ARM" originally stood for "Acorn RISC Machine," then "Advanced RISC Machine," although now it is no longer considered an acronym.) Pentium designs and the XScale [17] -- which is viewed as the successor to ARM architecture StrongARM -- use dynamic prediction.

Because the approach introduced here is more general than extant alphabetical and search dynamic programming methods, using it to find optimal decision trees is somewhat slower, having _O(n_<sup>3</sup>)-time _O(n_<sup>2</sup>)-space performance. This generality allows for different costs (run times) for different comparisons due to such behaviors as dynamic branch prediction and the use of conditional instructions other than branches. In the simplest case of static branch prediction, entropy-based<tbc>

<tbc>performance bounds are obtained based on known results from related unequal edge-cost problems. It should be emphasized that the one-time _O(n_<sup>3</sup>)-time _O(n_<sup>2</sup>)-space cost of optimization of these (usually small) problems is dwarfed by even the slightest gain in repeated run-time performance. The main contribution is thus a method by which decision trees can be coded on known hardware with minimum expected execution time.

## II. NO PREDICTION AND STATIC PREDICTION

It is easy to code the asymmetric bias of the branch for implementations of static branch prediction. In static prediction, opcode or branch direction is used to determine whether or not a branch is presumed taken, the most common rule being that forward conditional branches are presumed taken and backward conditional branches are presumed not taken [14]. If the presumption is satisfied, the branch takes a fixed number of cycles, while, if it is not, it takes a greater fixed number of cycles. Assume, for example, that we want to use a forward branch, which is assumed not to be taken. We thus want the less likely outcome to be the costlier one, that the branch is taken: If it is less likely than not that the item is less than _vi_, the branch instruction should correspond to "branch if less than _vi_," as in all branches used in Fig. 1.

This _branching problem_, applicable to problems with either no true branch prediction or static branch prediction, considers positive weights _c_<sub>0</sub> and _c_<sub>1</sub> such that the cost of a binary path with predictability \(b_1b_2\cdots b_k\) is \(\sum_{j=1}^kc_{b_j}\) where _b<sub>j</sub>_=0 for a mispredicted result and _b<sub>j</sub>_=1 for a properly predicted result. Such tree paths are often pictorially illustrated via longer edges on the corresponding tree, so that path depth corresponds to path cost, e.g., Fig. 2. This tree corresponds to the C and pseudocode of Fig. 1. The overall expected cost (time) to minimize is

where _p(i_) is the probability of the _i_th item, _l(i_) is the number of comparisons needed, and _j(i_) is 0 if the result of the _j_th branch for item _i_ is contrary to the prediction and 1 otherwise.

More formally,

1
b1 (2) = b1 (3) = b1 (4) = 1
1
3
0
1
b2 (3) = b2 (4) = 1
b1 (1) = 0
1
3
3
b3 (4) = 1
p(1)
b2 (2) = 0
p(4)
3
3
p(2)
p(3)

P
n
j
1
(i)
c
bj
(i)

Fig. 2. An optimal branch tree with edge costs for _c_=(_c_<sub>0</sub>_c_<sub>1</sub>)=(31)


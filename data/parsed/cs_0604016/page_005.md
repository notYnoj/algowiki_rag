given branch direction as a function of the probability of the branch.

For example, if branch prediction uses a saturating up-down counter -- the two-bit Markov chain of [33] shown as a Moore state diagram in Fig. 3(a) -- then the probability of misprediction is given by

where _p_<sub>1</sub> is the probability the less likely event will occur given the branch being considered. This Markov chain is used by the more recent Pentium architectures [8] and is referred to by Yeh and Patt as Automation A2 [39]. If branch prediction instead uses the two-bit Markov chain of [32], as in the MIPS- influenced pedagogical architecture in [14] and in Fig. 3(b), then the probability of a misprediction is given by

This chain is referred to by Yeh and Patt as Automation A3. (Other state diagrams considered by Yeh and Patt are not in as wide use, either being too simple or lacking symmetry between taken and untaken branches.)

The Moore state diagrams for Automations A2 and A3 in Fig. 3 have N representing an untaken branch and T representing a taken branch. The state determines which prediction is made, and the actual branch outcome determines the transitions between the states. The corresponding stationary misprediction rate (Fig. 4) is worst for Automation A3 (dotted plot), which has a rate up to 26.92% worse than that for static prediction (solid plot). Automatic A2 (dashed plot) does better, being at most 20.71% worse than static prediction.

In either dynamic case, we can calculate expected cost from the probabilities of each branch. We initially assume that taken and untaken branches are symmetric, that is, a branch rightly predicted as untaken will have the same cost as a branch rightly predicted as taken, and mispredicted branches<tbc>

<tbc>will similarly have identical costs. Let the type of dynamic prediction be _A_, let the probability of the more likely subtree be _p_max, and let the probability of the less likely subtree be _p_min, so that \(p_\mathrm{min}+p_\mathrm{max}\le 1\) and _p_<sub>1</sub>=_p_min/(_p_min+_p_max) is the probability of the less likely outcome conditional on the branch being decided upon. Then, instead of the static cost of _c_<sub>1</sub>_p_min+_c_<sub>2</sub>_p_max, the expected cost of a given branch is

Thus this plus the costs of the subtrees is the overall tree cost.

Asymmetries in taken and untaken branches are easily accounted for. Similarly, if a \((<,\ge)\) comparison with a certain value has a smaller cost than a comparison with another value -- say a comparison with a power of two times a variable is faster due to the inherently reduced calculation time -- then this can also be taken into account. Another variant can be found by noting that some processors allow conditional instructions, that is, instructions only executed given certain conditions. On platforms such as those in the Pentium family, a conditional instruction is often preferable to a conditional branch, but this might only reasonably be used to eliminate a branch to leaves in the decision tree. Thus branches deciding between only two items might be accounted differently.

With such a variety of options, there could be multiple possible costs for any particular branch. General cost functions for a branch taking all this into account are of the form \(C_k(p',p'',i,j,s)\) for _k_ from 1 to some _m_ (where _m_=2<tbc>

\(f_{\mathrm{A}2}(p_1)\unknown P[\mathrm{mispredictonA2}]=\frac{p_1-p_1^2}{1-2p_1+2p_1^2}\)

\(f_{\mathrm{A}3}(p_1)\unknown P[\mathrm{mispredictonA3}]=\frac{p_1+p_1^2+4p_1^3+2p_1^4}{1-p_1+p_1^2}.\)

T
T
T
T
0/N
1/N
2/T
3/T
N
N
N
N
N

T
T
T
T
0/N
1/N
2/T
3/T
N
N
N
N

\(C(p_\mathrm{min},p_\mathrm{max})\unknown\)<br> \(c_1(p_\mathrm{min}+p_\mathrm{max})f_A\left(\frac{p_\mathrm{min}}{p_\mathrm{min}+p_\mathrm{max}}\right)+\)<br> \(c_2(p_\mathrm{min}+p_\mathrm{max})\left(1-f_A\left(\frac{p_\mathrm{min}}{p_\mathrm{min}+p_\mathrm{max}}\right)\right).\)

(a) A2 (recent Pentium architectures)

(b) A3 (_Computer Architecture - A Quantitative Approach_)

Fig. 3. Moore state diagrams for branch prediction

Fig. 4. Static and dynamic branch misprediction rates


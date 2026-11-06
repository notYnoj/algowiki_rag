where \(p(i,j)=\sum_{k=i}^jp(i)\) can be calculated on the fly along with _c(i,j_). The last minimization determines which branch condition to use (e.g., "assume taken" vs. "assume untaken"), while the minimizing value of _s_ is the splitting point for that subtree. The branch condition to use -- i.e., the bias of the branch -- must be coded explicitly or implicitly in the software derived from the tree.

Knuth \[7\] and Itai \[12\] begin with similar algorithms, then reduce complexity by using the property that the splitting point of an optimal tree for their problems must be between the splitting points of the two (possible) optimal subtrees of size _n_-1. Note that \[12\] claims that this property can be extended to nonbinary decisions, a claim that was later disproved in \[27\]. The branching problem considered here also lacks this property. Consider _p_=(0.30.20.20.3) and _c_=(31), for which optimal trees split either at 2, as in Fig. 2, or at 4, the mirror image of this tree. In contrast, the two largest subtress, as illustrated in the figure and its mirror image, both have optimal splitting points at 3.

The optimal tree of Fig. 2 is identical to the optimal tree returned by Itai’s algorithm for order-restricted edges \[12\]. Consider a larger example in which this is not so, the binomial distribution _p_=(1615201561)/128 with _c_=(112). If edge order is restricted as in \[12\], the optimal tree has an expected cost of 15.109375. If we relax the restriction, as in the problem under consideration here the optimal method, has an expected cost of 12.984375, a 14% improvement.

A practical application of this problem, involving a decision tree, is encountered in implementation of the ONE-SHIFT Huffman decoding technique introduced in \[6\]. This implementation of optimal prefix coding is fastest for applications with little memory or small caches. Where the ONE-SHIFT technique is the preferred technique, we can apply the methods of this section to optimize the method’s decision tree. In the implementation illustrated in \[6\], the decision tree is used to determine codeword lengths based on 32-bit keys. The suggested "optimal search" strategy involves a hard-coded decision tree in which branches occur if "greater than or equal to" each splitting point; in most static branch schemes, this would result in "less than" taking fewer cycles than "greater than or equal to," but the tree used in \[6\] was found assuming fixed branch costs \[28\]. Here we show that we can improve upon this.

Consider the optimal prefix code for random variable _X_ drawn from the Zipf distribution with _n_=2<sup>16</sup>, that is, \(\mathbb{P}[X=i]=1/(i\sum_{j=1}^nj^{-1})\) which is approximately equal to the distribution of the _n_ most common words in the English language \[29, p. 89\]. Using Huffman coding, one can find that this code has codeword lengths, \(\ell(X)\), between 4 to 20, with the number of codewords of each size and the probability that the codeword will be a certain size given by  II.

Consider a decision tree to find codeword lengths with an architecture in which comparisons that result in untaken branches take 3 cycles (for both compare and branch), while comparisons that result in taken branches take 5 cycles. This asymmetry, similar to that of many ARM architectures, is<tbc>

<tbc>small, but taking advantage of it results in an improved tree. This optimal tree, shown in Fig. 3, takes an average of 15.93 cycles, while the "optimal search" takes an average of 16.44 cycles. This 3.1% improvement, although not as large as that of the binomial example, is still significant due to the impact of the decision tree on overall algorithm speed.

## III. MORE ADVANCED MODELS

With dynamic branch prediction \[14\], which in more advanced forms includes branch correlation, branches are predicted based on the results of prior instances of the same and different branch instructions. This results in complex processor behavior. Often several predictors will be used for the same branch instruction instance; the predictor in a given iteration will be based on the history of that branch instruction instance and/or other branches. In the problem we are concerned with, however, this does not result in as many complications as one might expect; the probability of a given branch outcome

\begin{tabular}{cccccc}
length (\(\ell\)) & \multicolumn{3}{c}{# of codewords} & \multicolumn{2}{c}{_p(i_)} \\
4 & 1 & (2<sup>0</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=4]\) = 0.08570759} \\
5 & 2 & (2<sup>1</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=5]\) = 0.07142299} \\
6 & 4 & (2<sup>2</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=6]\) = 0.06509695} \\
7 & 8 & (2<sup>3</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=7]\) = 0.06216987} \\
8 & 16 & (2<sup>4</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=8]\) = 0.06076807} \\
9 & 32 & (2<sup>5</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=9]\) = 0.06008280} \\
10 & 64 & (2<sup>6</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=10]\) = 0.05974408} \\
11 & 128 & (2<sup>7</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=11]\) = 0.05957570} \\
12 & 256 & (2<sup>8</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=12]\) = 0.05949175} \\
13 & 512 & (2<sup>9</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=13]\) = 0.05944984} \\
14 & 1024 & (2<sup>10</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=14]\) = 0.05942890} \\
15 & 2048 & (2<sup>11</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=15]\) = 0.05941844} \\
16 & 4096 & (2<sup>12</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=16]\) = 0.05941321} \\
17 & 8192 & (2<sup>13</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=17]\) = 0.05941059} \\
18 & 16384 & (2<sup>14</sup>) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=18]\) = 0.05940928} \\
19 & 32747 & (2<sup>15</sup>-1) & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=19]\) = 0.05940732} \\
20 & 2 & & \multicolumn{2}{c}{\(\mathbb{P}[\ell(X)=20]\) = 0.00000262} \\
\end{tabular}


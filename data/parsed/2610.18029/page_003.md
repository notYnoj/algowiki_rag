We introduce a deterministic repair procedure for sampled bit strings in section 4.1, and incorporate the repaired solution quality into the QAOA optimisation objective. In section 4.2, we also study a relaxed penalty regime in which the Hamiltonian is used to produce candidates for repair rather than to encode feasibility exactly. In section 4.3, we evaluate the resulting sampler on a 64-qubit quantum circuit and compare it with a random-shot baseline under the same sampling budget. We give graph reduction and reconstruction rules in section 5.1 that preserve the complete set of maximum weight cliques. These rules are designed specifically for the enumeration problem rather than for the recovery of only one optimum. In section 5.2, we use a hybrid solver to seek stronger lower bounds and vertex colouring- based upper bounds during preprocessing. Our method is modular: when preprocessing produces a sufficiently small graph, the residual instance is completed classically and exactly.

## 2 Preliminaries

### 2.1 Phylogeny

Phylogenetic trees have been fundamental to understanding evolution since the very beginning of the field - Charles Darwin sketched one in his notebook soon after his trip aboard _The Beagle_, where he conceived of the idea of natural selection.

A phylogenetic tree is a tree whose leaves correspond to sampled taxa and whose internal structure represents inferred evolutionary relationships. Depending on the application and the construction method, the tree may be rooted or unrooted. Molecular phylogenetic methods commonly take a multiple sequence alignment (MSA) as input. An MSA represents a hypothesis of positional homology between the input sequences; the phylogenetic procedure then uses the aligned characters to infer a tree according to a chosen criterion [22].

It should also be noted that there are also many methods of constructing MSAs, each representing a different philosophy. This in itself is a hugely complex process, and one that we shall isolate from the construction of the phylogenetic trees for now. Together, this yields a wide range of potential methods of constructing a phylogenetic tree from a set of sequences, all answering somewhat different questions.

In this work, we consider the maximum compatibility criterion. The objective is to find a largest-weight collection of characters that can be realised together on one tree with the minimum possible number of state changes. This differs from maximum parsimony, another commonly used method, which minimises the total number of changes over all retained characters. However, the requirement to consider all characters can be problematic, for example in the case where there are random, noisy characters [20].

One of the latest maximum compatibility phylogenetic tree algorithms comes from Joshua Cherry [5].

#### 2.1.1 Cherry’s Maximum Compatibility Algorithm

Phylogeny operates in terms of "characters", observable traits of the sample organisms. For us, this corresponds exactly to the columns of the MSA.


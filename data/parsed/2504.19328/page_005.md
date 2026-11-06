<tbc>substructure S as a node, and DL(G) (or DL(S)) represents the description length of the original graph (or the substructure S.) The substructure of the graph achieves the highest compression when the MDL value is the highest. Both the frequency of the subgraph and its connectivity have an impact on compression. The frequency of substructures can also be used as a metric as used in FSG and others.

## V. ARCHITECTURE AND COMPOSITION ALGORITHM

Instead of a single network, we have multiple layers and the goal is to find _interesting_ substructures in the MLN (across all layers). Substructures in a Multilayer Network (MLN) can exist in different ways: i) can exist solely in one layer (intra-layer substructure) or ii) can span multiple layers (inter-layer substructure). An algorithm exists for detecting substructures within a graph or a layer. For scalability, this algorithm has been extended to use range-based partitions and generate substructures across partitions correctly [27]. Hence, our primary focus is on generating all inter-layer substructures correctly during the composition phase so MDL (or some other metric) can be applied to rank the MLN substructures.

Below we present the Iterative Composition Algorithm (**Ho-ICA**) for Homogeneous MLNs which performs composition _after each iteration_. That is, substructures for each participating layer are generated during an iteration and the generated layer substructure instances are used for composing **missing** inter-layer substructures. After that, duplicate elimination is done for generated instances using canonical representation and substructures are counted using canonical substructures to apply MDL. This process repeats after each iteration until the substructure discovery algorithm terminates and outputs the best substructures based on the given parameters.

As inter-layer substructures are composed in every iteration, our conjecture is that this approach should not have any accuracy drop (if done correctly) as all substructures (intra and inter) are generated in each iteration and evaluated using the metric before keeping the _top-beam_ substructures for the next iteration. We will validate this conjecture experimentally. We will also provide the operational correctness of the algorithm. Although we may be adding an extra step of computation (composition) as compared to the ground truth computation, yet the efficiency (as compared to ground truth) will improve by an order of magnitude while preserving accuracy, as we are dealing with smaller graphs that can be processed in parallel.

We will experimentally evaluate the developed algorithm for correctness, efficiency, and scalability. We will also discuss how distributed processing resources can be matched to the input graph size to keep the desired response time.

### A. Ho-ICA: HoMLN Iterative Composition Algorithm

Figure 8 provides a comprehensive diagrammatic overview of Ho-ICA for substructure discovery for a HoMLN.

This approach generates substructures for each layer in each iteration, converts them to canonical instances, and eliminates duplicates. Composition algorithm is applied at the end of layer substructure generation in each iteration to generate<tbc>

<tbc>missing inter-layer substructures. After that, all substructures from the individual layers and composed substructures spanning layers (after duplicate elimination) are aggregated. They are converted into canonical substructures for applying a ranking metric (such as MDL) to generate the _top-beam_ substructures for the next iteration. Each iteration corresponds to a particular size of substructure. In each iteration, the substructures are expanded by a single edge in their own layer, starting with size one substructures (an edge) for the first iteration. This generates all the intra-layer substructures for that size. Also, in the first iteration which generates 2-edge substructures, the composition function generates inter-layer substructures by expanding instances from each layer using the adjacency list of other layers. In subsequent iterations, composition function will generate composed substructures of size _k_+1, using the composed substructures from the previous iteration (size _k_).

At the end of each iteration, the substructures from each layer and the inter-layer substructures are separated for the next iteration. This is critical for the decoupling principle which stipulates that layers are processed independently and without using the knowledge of the other layers. In the next iteration, substructures from each layer are expanded by an edge from that layer and in the next composition stage, intra- layer substructures are expanded using edge from the other layer and inter-layer substructures are expanded with one edge from either layer and the process repeats. Note that composition can make use of information from both layers.

The input of the Ho-ICA algorithm is a set of composed substructures from the previous iteration, each of size _k-1_, where _k_ is at least 2. We then expand these substructures using adjacency lists of other layers, to get inter-layer composed substructures of size _k_. The inter-layer substructures, in addition to the intra-layer substructures generated in the current iteration, are forwarded to the metric evaluation process followed by beam application. Given that the beam substructures now consist of both intra-layer and inter-layer substructures, they are separated (to be consistent with the decoupling philosophy) and sent to their respective tasks for the next iteration. Algorithm 1 describes the composition function used to compose substructures after each iteration.

The algorithm expands each previously generated inter-layer substructure using adjacency lists of all layers (line 3).

Analysis Phase
Find all the substructures in each layer individually
Layer 1
Node
Substructure instances in Layer 1
Expansion by one edge
(k+1) size Substructures
Transition
Composition Phase
For first Iteration
(k+1) size composed Substructures
Composed Inter-layer Substructure instances
Find all the substructures that exist across the layers
Composition Function (Ho(CA)
Beam + MDL
Layer 2
Node
Expansion by one edge
(k+1) size Substructures
Substructure instances in Layer 2

Fig. 8: Decoupling Approach Overview for Iterative Composition


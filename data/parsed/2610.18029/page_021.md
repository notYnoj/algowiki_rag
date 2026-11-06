Now on this fully reduced graph, it is clear what the MWISs should be: simply the individual vertices of the graph that has the maximum vertex weight. In this case, they all have weight 1, so we have exactly 5 MWIS for this reduced graph, and with our MWIS reconstruction postprocessing, we can deterministically recover the _entire_ set of MWIS. It should be noted that we do not mandate that we must use quantum devices in every step of our pipeline. Indeed, given a very small reduced graph, it clearly does not make sense to do so. Therefore, with our quantum pipeline, we recover the potential to determine the full set of MWISs and output the _exact_ maximum compatibility phylogenetic tree.

It is important to stress the variability of the reductive power of our preprocessing based on the D-Wave clique and vertex-colouring samplers. Due to our limited quantum resources, we do not attempt to fully optimise the graph reductions for every instance, but simply perform a single pass of the algorithm on the instances to gain an insight on its behaviour and potential.

## 6 Discussion and Outlook

We have studied the maximum weight clique subproblem arising in maximum compatibility phylogenetic tree construction algorithm [5], aiming to improve the recovery of multiple optimum solutions. The main algorithmic distinction is between finding one maximum weight clique and recovering a useful portion of the complete optimum set. The numerical experiments show that these can be very different tasks: _SCCWalk4L_ found an optimum on 383 of the 385 tested instances, but repeated runs on one graph still missed 62 of the 896 optima after 10,000 executions. A solver can therefore perform well under the usual best weight metric while providing limited coverage for applications that require several equally optimal solutions, including strict consensus tree construction.

Our contributions are twofold. The first is a more efficient reduction method that allows us to use enumeration methods that also include quantum algorithms on current devices. We apply a stricter reduction scheme by removing vertices from the complement graph and separately record the information required to reconstruct the corresponding maximum weight independent sets. This reduces the graph which is passed to the main enumeration algorithm while making the reconstruction step more computationally costly.

(a) Original complement graph (b) Complement graph with classical reductions (c) Complement graph with D-Wave reductions

Figure 10: The graph reductions on an example set of 350 SARS-CoV-2 samples.


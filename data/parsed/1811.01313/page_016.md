## Reduction to Network Coding.

We are now ready to make our reduction to network coding. The basic idea in our proof is to use Lemma 10 to obtain an I/O-graph _G_ and permutation \(\pi\) with large distance between the node containing _A_\[_i_\] and the node containing \(C[\pi(i)]\) for many _i_. We will then create a source _s<sub>i</sub>_ at the node representing _A_\[_i_\] and a corresponding sink _t<sub>i</sub>_ at the node corresponding to \(C[\pi(i)]\). These nodes are far apart, but using the external memory permutation algorithm A<sup>∗</sup>, there is an algorithm for transmitting _d<sub>i</sub>_ from _s<sub>i</sub>_ to _t<sub>i</sub>_. Since the distance between _s<sub>i</sub>_ and _t<sub>i</sub>_ is at least (1/2)lg<sub>2_m/b_</sub>(_nw/b_) for (4/5)_n_ of the pairs (_s<sub>i</sub>,t<sub>i</sub>_), it follows from Conjecture 1 that the sum of capacities in the network must be at least \(\Omega(nwlg_{2m/b}(nw/b))\) (we can transmit _w_ bits between each of the pairs). However, running the external memory algorithm results in a network/graph _G_ with only _O(t_) edges, each needing to transmit only _b_ bits (corresponding to the contents of block on a read or write). Thus each edge needs only have capacity _b_ bits for the reduction to go through. Hence the sum of capacities in the network is _O(tb_). This means that \(t=\Omega((nw/b)lg_{2m/b}(nw/b))\) as desired.

However, the reduction is not as straightforward as that. The problem is that Lemma 10 leaves us only with a subset F of all the possible values _d_<sub>1</sub>_,...,d<sub>n</sub>_ that one wants to transmit. For other values of _d_<sub>1</sub>_,...,d<sub>n</sub>_, we cannot use the algorithm A<sup>∗</sup> to transmit the data via the network/graph _G_. We could of course try to sample (_d_<sub>1</sub>_,...,d<sub>n</sub>_) uniformly from F and then have a network coding solution only for such inputs. The problem is that for such a uniform \((d_1,\dots,d_n)\in\mathcal{F}\), it no longer holds that the inputs to the sources in the coding network are independent! Network coding rate only speaks of independent sources, hence we need a way to break this dependency. We do this by adding an extra node _u_ and some edges to the coding network. This extra node _u_ serves as a coordinator that takes the independent sources _X_<sub>1</sub>_,...,X<sub>n</sub>_ and replaces them with an input \((d_1,\dots,d_n)\in\mathcal{F}\) in such a way that running A<sup>∗</sup> on (_d_<sub>1</sub>_,...,d<sub>n</sub>_) and using a little extra communication from _u_ allows the sinks to recover \(X_{\pi^{-1}(i)}\) from \(d_{\pi^{-1}(i)}\). We proceed the give the formal construction.

Let _G_ be the I/O-graph, \(\pi\) the permutation and \(\mathcal{F}\subseteq\{\{0,1\}^w\}^n\) the values promised by Lemma 10. From _G_, construct a coding network _G_<sup>∗</sup> as follows (see Figure 2):

1. Add source and sink nodes _s_<sub>1</sub>_,...,s<sub>n</sub>_ and _t_<sub>1</sub>_,...,t<sub>n</sub>_ to _G_<sup>∗</sup>.<tbc>

2. For each source _s<sub>i</sub>_, add an additional node _p<sub>i</sub>_.<tbc>

3. Add all nodes of _G_ to _G_<sup>∗</sup>.<tbc>

4. Add all edges of _G_ to _G_<sup>∗</sup>. Edges between a block node and a memory node has capacity _b_ bits. Edges between two memory nodes have capacity _m_ bits.<tbc>

5. Remove all block nodes that have an incoming and outgoing edge to the same memory node (this makes the graph acyclic).<tbc>

6. Add a directed edge with capacity _w_ bits from each source _s<sub>i</sub>_ to _p<sub>i</sub>_, and add a directed edge with capacity _w_ bits from each _p<sub>i</sub>_ to the input block node containing _A_\[_i_\].<tbc>

7. Add an edge with capacity _w_ bits from the output block node containing \(C[\pi(i)]\) to the sink _t<sub>i</sub>_.<tbc>

8. Add a special node _u_ to _G_<sup>∗</sup>. Add an edge of capacity _w_ bits from each source _s<sub>i</sub>_ to _u_. Also add a directed edge from _u_ to each _p<sub>i</sub>_ having capacity \(\rho_i\) for parameters \(\rho_i>0\) to be fixed later. Also add an edge from _u_ to sink _t<sub>i</sub>_ with capacity \(\rho_i\).<tbc>


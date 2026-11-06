<tbc>assumes a black-box fundamental cycle separator algorithm that runs in \(\tilde{O}(D)\) rounds and applies it recursively. In case there is no such separator, it is sufficient that the algorithm provides a path separator and (the endpoints and embedding) of a virtual edge, that if added, closes a cycle with the path separator. Replacing the black-box randomized separator algorithm in the BDD construction with ours (or with that of [12]) immediately derandomizes the BDD and hence the following state-of-the-art algorithms for classical problems in _directed_ planar graphs:

• Computing \(\tilde{O}(D)\)-bit distance labels to every vertex (in a planar graph with positive and negative weights) in \(\tilde{O}(D^2)\) rounds [14] (s.t. the distance between any two vertices can be deduced by their labels alone), hence also single-source shortest-paths in \(\tilde{O}(D^2)\) rounds.<tbc>

• Computing \(\tilde{O}(D)\)-bit reachability labels to every vertex in \(\tilde{O}(D)\) rounds [16] (s.t. the reachability between any two vertices can be deduced by their labels alone), hence also single-source reachability in \(\tilde{O}(D)\) rounds.<tbc>

• Detecting strongly connected components in \(\tilde{O}(D)\) rounds [16].<tbc>

• Maximum _st_-flow in \(\tilde{O}(D^2)\) rounds [1].<tbc>

• Global directed minimum cut in \(\tilde{O}(D^2)\) rounds [1].<tbc>

• Minimum weight cycle in \(\tilde{O}(D^2)\) rounds [16].

## References


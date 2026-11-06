since \(d_{max}\le c_{min}/3\le c_a/3\). Hence, each additional round is feasible. Therefore, if \(d_{max}\le c_{min}/3\), then all demands can be routed unsplittably in six rounds.

## Routing in four rounds when \(d_{max}\le c_{min}/4\).

As above, we build the auxiliary graph \(D'\) from two copies of _D_ and run the Modified DGG algorithm. Sinks that are not critically split are already routed feasibly in one of the two copies (rounds), since \(c_a/2+d_{max}\le c_a/2+c_{min}/4<c_a\).

Each critically split sink is labeled by the copy of _D_ containing its forward path(s). Critically split sinks with the same label are grouped, and their paths are superimposed to form two additional rounds. No finer grouping is required for feasibility as \(c_a/2+d_{max}+d_{max}\le c_a/2+c_{min}/2\le c_a\).


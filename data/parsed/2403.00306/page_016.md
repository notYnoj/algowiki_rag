## 1.3.1 Exact PMS Algorithms

An exact algorithm can find all the motifs in input sequences. In our research paper, we only consider exact algorithms. The exact variant of the PMS problem has been shown to be NP- hard [5]. It means that there is no PMS algorithm that takes only polynomial time to iterate. As a result, all known exact algorithms have an exponential worst case runtime. Due to NP- hardness approximate algorithm arises for PMS. An exact PMS algorithm can be built using two approaches:

### Sample Driven Approach

For all (_m-l_+1)_<sup>n</sup>_ possible combinations of _l_-mers coming from different strings generate the common neighborhood. Unlike pattern driven approach in _Sample Driven (SD)_ approaches all possible motifs generated from the _l_-mers in input strings are of interest which could be found in polynomial time. _Sample Driven_ algorithms try to find comparative patterns by comparing the given length strings and looking for local similarities between them. They are based on constructing a local multiple alignment of the given non-coding DNA sequences and then extracting the comparative patterns from the alignment by combining the segments which is common to most of the non-coding DNA sequences.

### Pattern Driven Approach

For all |<sup>Σ</sup>|<sup>l</sup> possible _l_-mers check which are motifs. Trying all possible motif candidates take exponential space. _Pattern Driven (PD)_ algorithms are based on enumerating candidate patterns in a given length string and inputting substrings with high fitness. Compared with SD algorithms, PD algorithms can be performed intelligently so that patterns are not present in the data that are not generated.

All existing exact algorithms solve PMS problem in exponential time in some of its parameters. The most recent exact algorithms that have been proposed in the literature are Algorithm _qPMS9_ due to [6], Algorithm _PMS8_ due to [7], Algorithm _Pampa_ due to [8], Algorithm _qPMS7_ due to [1], Algorithm _PMSPrune_ due to [9], Algorithm _PMS6_ due to [10], Algorithm _Voting_ due to [11], and Algorithm _RISSOTO_ due to [12].

## 1.3.2 Approximate PMS Algorithms

Approximate PMS algorithms usually tend to be faster than exact PMS algorithms. Typically, approximate PMS algorithms employ heuristics such as local search, Gibbs sampling, expectation optimization etc. Some examples of approximate algorithms are Algorithm _MEME_ due


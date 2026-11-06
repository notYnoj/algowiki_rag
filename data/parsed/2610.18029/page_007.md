<tbc>to keep backtracking and finding new cliques, but these will likely all be in the same domain of the wider search space and potentially unhelpful for consensus tree generation unless a full enumeration is tackled.

Conversely the approximate clique finders can return a different clique each execution, but usually require many execution runs. These approximate tools may be modifiable to yield many trees in a single run, but this is a complex task and considered out of scope for our evaluation purposes. Nonetheless we implemented our own approximate clique finder, _AClique_, based on genetic algorithms, which can yield up to a specified number of cliques of the maximum size found in a single execution run.

## 3.1 Classical Benchmarking

The primary data set for our benchmarking, both classical and quantum, is a database of SARS-CoV-2 (COVID-19) genome sequences. This genome is clearly biologically relevant while being small (29903 base pairs). It is one of the largest studied organisms which allows us to test large cohorts.

Our test corpus contains 271,417 sequences, from which we choose a random selection varying between 50 and 20,000. The COVID genome has very few insertions, which means we can use _minimap2_ to align our chosen sequences back to the canonical reference as a suitable proxy for performing a full multiple sequence alignment. This aligned sequence is then the input to Cherry’s _compat_ tool. We modified _compat_ to output the weighted graph and an expanded unweighted equivalent graph in DIMACS format after the modified graph reduction preprocessing steps had been applied. The graphs have a very high edge density (the percentage of possible edges that are present), with most larger graphs having _\>_=99% density, favouring some classical tools over others.


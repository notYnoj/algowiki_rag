<tbc>Here _l_ is the length of the pattern. The superposition of the _l_-mers of Figure 2.15 is shown in Figure 2.16. Now taking the _l_-mers starting at these positions we can compile a _alignment matrix_ of \(t\times l\). The (_i,j_)th element of the _alignment matrix_ is the nucleotide at the _s<sub>i</sub>+j_-1th position in the _i_th sequence. Illustrations are shown in Figure 2.17.

## 2.5.2 Profile Matrix

The _profile matrix_ or profile, illustrates the variability of nucleotide composition at each position for a particular group of _l_-mers. Let the alphabet \(\Sigma\) in our motif search. Then the size of the _profile matrix_ will be \(|\Sigma|\times l\). For DNA \(|\Sigma|=4\). Based on the _alignment matrix_, we can compute the \(4\times l\) _profile matrix_ whose (_i,j_)th element holds the number of times nucleotide _i_ appears in column _j_ of the _alignment matrix_, where _i_ varies from 1 to 4. In Figure 2.17 we see that positions 3, 7, and 8 are highly conserved, while position 4 is not.

CGGGGCTATcCAgCTGGGTCGTCACATTCCCTT ...
TTTGAGGGTGCCCAATAAggGCAACTCCAAAGCGGACAAA
GGATGgAtCTTGATGCCGTTTGACGACCTA ...
AAGGAAAGCAACCCCAGGAGCGCCCTTTGCTGG ...
AATTTTCTAAAAAGATTATAATGTCGGTCCTTGgAAACTTC
CTGCTGTACAACTGAGATCATGCTGCATGCcAtTTTCAAC
TACATGATCTTTTGATGgcACTTGGATGAGGGAATGATGC


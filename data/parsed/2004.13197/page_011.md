As in the RAM setting, since we have three subproblems, their maximum complexity, and hence the complexity of their sum, is a lower bound on Sort(_S,L_). We have thus reduced the sorting problem to the batched predecessor problem, which will occupy the rest of this article.

## 4 Main Challenges in the Batched Predecessor Problem

For PLE(_S,L_), one can see that there is not much point comparing large records to each other; one would rather compare a large record to more small records than one large record. We need the notion of a **fan-out**, which measures the efficiency of an I/O. In PLE(_S,L_), large elements are the ones trying to find their locations amongst the small elements. A large element is called active during an I/O if it is either in memory or in the block transferred during this I/O. Before an I/O, any active large element has a set of locations where it might lie, and this set gets reduced by a certain factor (possibly 1) after this I/O. The fan-out of an I/O is defined to be the product of all such factors for all large elements active during this I/O.

We now describe the three main challenges in extending the RAM solution to external memory.

**1.Non-uniformity:** In the unit-sized setting, the transfer of a block to main memory can decrease the number of permutations to be checked by a factor of at most<sup>4</sup> \(B!\genfrac(){pt}{2}{M}{B}\). In our setting, the number of comparisons performed by an I/O varies depending on whether the block transfer carries large records or small records, and what the contents of RAM are at the time of the I/O.

• The transfer of a large element into main memory full of large elements gives only \(\genfrac(){pt}{2}{M/w}{1}\) per _w/B_ I/OS as a large-element transfer costs _w/B_.<tbc>

• The transfer of _B_ small records into main memory filled with small records gives \(\genfrac(){pt}{2}{M}{B}\).<tbc>

• The transfer of a large element into a memory full of _M_ small elements gives a fan-out of _M_+1.

<sup>4</sup>The proof of the lower bound for sorting _N_ unit-sized keys in \[15\] proceeds in the following fashion: assuming that all blocks are sorted (using a linear scan costing _N/B_ I/Os), there are _N!/(B!_)<sup>(_N/B_)</sup> permutations required to achieve, and the transfer of a block of _B_ sorted elements into the main memory containing _M-B_ sorted elements can at most an \(\genfrac(){pt}{2}{M}{B}\) fraction of these permutations (the "fan-out," since this is the degree of the node in the decision tree). Standard algebra gives a lower bound of \(\frac{N}{B}log_{M/B}\frac{N}{B}\) .

\(\square\)<br>
\(\square\)


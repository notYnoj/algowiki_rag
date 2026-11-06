Sort rows by size

Sorted rows speed up the filtering step. As for sorted rows we need less tuples for lower stack size, it helps to reduce expensive filtering. It is because fewer _l_-mers remain to be filtered when the stack size increases.

Compress _l_-mers

To calculate the hamming distance between two _l_-mers at first we have to perform exclusive or of their compressed representation. One compressed _l_-mer requires \(1\times\lceil log|\Sigma|\rceil\) bits of storage. So the table of compressed _l_-mers only requires O(n(m-l+1)) words of memory as we only need the first 16 bit of this representation.

Preprocess distances for pairs of _l_-mers

For every pair of _l_-mers we test if the distance is no more than 2d in advance.

Cache locality

As a certain row of an updated matrix is the subset of that row so we can store the updated row in the previous location of the row. so we have to keep track the number of elements belongs to the new row. This process can be repeated in every step of recursion and can be perform using by only a single stack where the subset elements are in contiguous position of memories and thus cache locality sustains.

Find motifs for a subset of strings

we will find the motif for some input strings and then test them against the remaining strings.

Memory and Runtime

since we store all the matrices in the place of a single matrix they only require _O(n(n-l+1_)) words of memory. _O(n_<sup>2</sup>) words of row size will be added for at most n matrices which share the same space. So total bits of _l_-mer pair takes _O_((_n(m-l+1_)<sup>2</sup>)/w_) words where w is the number of bits in a machine word. So total memory used for this algorithm is _O(n(n-l+1_)+(_n(m-l+1_)<sup>2</sup>)/w_).


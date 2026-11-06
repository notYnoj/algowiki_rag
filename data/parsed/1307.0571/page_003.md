<tbc>PMS8 consists of a sample driven part followed by a pattern driven part. In the sample driven part we generate tuples of _l_-mers originating from different strings. In the pattern driven part we generate the common _d_-neighborhood of such tuples. Initially we build a matrix _R_ of size \(n\times(m-l+1)\) where row _i_ contains all the _l_-mers in _Si<sub>i</sub>_. We pick an _l_-mer _x_ from row 1 of _R_ and push it on a stack. We filter out any _l_-mer in _R_ at a distance greater than 2_d_ from _x_. Then we pick an _l_-mer from the second row of _R_ and push it on the stack. We filter out any _l_-mer in _R_ that does not have a common neighbor with the _l_-mers on the stack; then we repeat the process. A necessary and sufficient condition for 3 _l_-mers to have a common neighbor is discussed in section 2.4. For 4 or more _l_-mers we only have necessary conditions, so we may generate tuples that will not lead to solutions. If any row becomes empty, we discard the top of the stack, revert to the previous instance of _R_ and try a different _l_-mer. If the stack size is above a certain threshold (see section 2.2) we generate the common _d_- neighborhood of the _l_-mers on the stack. For each neighbor _M_ we check whether there is at least one _l_-mer _u_ in each row of _R_ such that \(Hd(M,u)\le d\). If this is true then _M_ is a motif. PMS8 is illustrated in figure 1 and its pseudocode is given in appendix B.

### 2.1 Speedup techniques

**Sort rows by size.** An important speedup technique is to reorder the rows of _R_ by size after every filtering step. This reduces the number of tuples that we consider at lower stack sizes. These tuples require the most expensive filtering because as the stack size increases fewer _l_-mers remain to be filtered.

**Compress _l_-mers.** We can speed up Hamming distance operations by compressing all the l-mers of _R_ in advance. For example, for DNA we store 8 char<tbc>

S6
I-mers compatible with those on the stack
S5
S4
S3
S2
Stack of I-mers
S1

**Fig.1.** Illustration of PMS8. We repeatedly push _l_-mers from different strings on a stack. From the remaining strings, we filter out _l_-mers incompatible with those on the stack. Once the stack has a certain size we generate the common _d_-neighbors of its _l_-mers. We compare the neighbors against the surviving _l_-mers to identify the motifs.


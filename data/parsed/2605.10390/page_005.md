<tbc>by defining a subset of histogram nodes at configurable maximum depth _L<sub>c</sub>_=32 with identifiers determined by memory location, eliminating the need for explicit identifiers of size \(w_i=O(\frac{p}{\lceil log(n)\rceil})\) and pointers of size _w<sub>r</sub>=O(log(n_)), enabling the sparse section of the histogram to be updated bandwidth-efficiently using only counter variables of size \(w_{c,l}=O(\lceil log(n)-l\rceil)\) for level \(l\in\{0,log(n)\}\) as shown in Algorithm 4.

**Algorithm 4** New Node Creation and Resolution

**Require:** Level and counter value _l_, _counter_

1: **function** NODEORTUPLE(_l_, _counter_)

2: \(node\leftarrow\text{\texttt{root}}\)

3: **if** \(l\le L_c\) **then** \(\triangleright\) Write to computable location

4: **return** {**counter**: _counter_}

5: **else** \(\triangleright\) Allocate a new node and return its pointer

6: **return** NEWNODE(_counter_)

7: **end if**

8: **end function**

### G. FractalSortCPU Complexity

#### 1) Complexity:

The sort complexity where _p_ is the precision, _n_ is the number of inputs in a batch, and \(n_L=\frac{W}{w_c}\) is the number of _W_-bit registers needed to store _p_ counters of \(w_c\approx\frac{log(n)}{2}\) size along the key path, is approximately \(O(n\lceil\frac{p}{n_L}\rceil)\) serial and \(O(2min(\lceil\frac{p}{n_L}\rceil,2log(n)))=O(2min(\lceil\frac{pw_c}{W}\rceil,2log(n)))\) complexity since each key has to update its associated path in the histogram, which represents either a sparse trie with depth _L<sub>n</sub>=log(n_) or full histogram with depth _L=p_ as shown in  I.

#### 2) Memory usage:

The storage space utilized by the algorithm is determined by the size of the sparse histogram

\(O(\left\{\begin{array}{ c c }
nw_c, & \text{if}n\le 2^p \\
2^pw_c, & \text{if}n>2^p
\end{array}\right\})\)

#### 3) FractalSortCPUA Algorithm:

The FractalSortCPUA algorithm produces a sorted array of keys from the histogram in a bandwidth-efficient streaming operation shown in Algorithm 5. The algorithm iterates over all 2<sup>_l<sub>n</sub>-l<sub>b</sub>_</sup> bins in tree-walk order for trie depth _l<sub>n</sub>=L<sub>n</sub>_ and bin width<tbc>

<tbc>**Algorithm 5** FractalSortCPUA: Sorted Array Reconstruction

**Require:** Entries _E_, index array _I_, bin counts _C_, precision _p_, tree depth _l<sub>n</sub>_, bin depth _l<sub>b</sub>_

**Ensure:** Sorted array _K_ of _n_ reconstructed _p_-bit keys

1: **function** RECONSTRUCTALL(_E,I,C,p,l<sub>n</sub>,l<sub>b</sub>_)

2: \(n_{bins}\leftarrow 2^{l_n-l_b}\), \(t\leftarrow p-l_n\)

3: \(offset\leftarrow 0\), \(idx\leftarrow 0\)

4: **for** _b_=0 **to** _n<sub>bins</sub>_-1 **do**

5: **if** \(C\[b\]=0\) **then continue**

6: **end if**

7: \(key_{low}\leftarrow\) BITREVERSE(_b_, _l<sub>n</sub>-l<sub>b</sub>_)

8: **for** _s_=0 **to** \(C\[b\]-1\) **do**

9: \(entry\leftarrow E[offset+I[offset+s]]\)

10: \(trailing\leftarrow entry\&(2^t-1)\)

11: \(tree_{off}\leftarrow entry\gg t\)

12: \(off_{val}\leftarrow\) BITREVERSE(_tree<sub>off</sub>,l<sub>b</sub>_)

13: \(K[idx]\leftarrow key_{low}|(off_{val}\checkmark(l_n-l_b))|(trailing\checkmark l_n)\)

14: \(idx\leftarrow idx+1\)

15: **end for**

16: \(offset\leftarrow offset+C\[b]\)

17: **end for**

18: **return** _K_

19: **end function**

<tbc>_l<sub>b</sub>=log(n<sub>bins</sub>_)<tbc>

<tbc>). The last level of the histogram contains the counter variable associated with each bin _C_. For each bin _b_, the bin identifier bits are recovered by reversing the tree ordering of the bin index. Within each bin, the sorted entries are traversed using the index array which maps each sorted position to an arrival position. Each entry is decoded by extracting the trailing bits and tree-reversed offset, and the full _p_-bit key is reconstructed by combining the bin identifier bits, offset bits and trailing bits.

The outer loop is _O(n<sub>bins</sub>_) and the inner loop process _n_ entries exactly once with _O_(1) work per entry (index lookup, bit extraction, bit-reverse via LUT, and concatenation), giving total complexity _O(n_). Memory traffic is one sequential read of the index array and one indexed read of the entry array, totaling \(\approx 2\times\frac{p}{8}\) bytes per key. The FractalSortCPUA algorithm demonstrates 41% bandwidth efficiency as shown in Figure 10.

## IV. EVALUATION

The experiments are performed on a Windows 11 Pro device with an Intel(R) Core(TM) i7-8665U CPU at 1.90GHz capable of 2.11GHz processing with 32 GB RAM, 950 GB SK Hynix SSD storage and Intel Emerald Rapids 32 vCPU Debian 120GB RAM host for benchmarking \[53\]. The runtime environment includes 64 bit Python 3.9.1, and the tests involve comparison of FractalSortCPU to state-of-the-art CPU-based sorting algorithms baseline implemented in<tbc>

\begin{tabular}{ccccc}
\multicolumn{5}{c}{Complexity Comparison} \\
HRS & GPU & Paradis & Bonsai & FractalSortCPU \\
 & Terasort & & & \\
 & \& & & & \\
 & Bitonic & & & \\
 & Network & & & \\
\(O(\lceil\frac{k}{d}\rceil n)\) & _O(log_<sup>2</sup>_n_) & \(O(\frac{n}{P})\) & \(O(n\lceil log_l(n)\rceil)\) & _O_(2_min(p,_2_log(n_))) \\
\end{tabular}

TABLE I

FRACTALSORTCPU COMPLEXITY SUMMARY \[17\] \[6\] \[10\]


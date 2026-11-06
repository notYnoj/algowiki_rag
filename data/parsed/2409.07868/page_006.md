**Algorithm 1** Algorithm for merging \(\pi\)-avoiding input _S_ partitioned into presorted sequences _S_<sub>1</sub>_,...,S<sub>m</sub>_ with prior knowledge of \(\pi\).

\(d\leftarrow\lceil 2c_\pi\rceil\)<br>
\(m'\leftarrow\lfloor\frac{m}{d}\rfloor\)<br>
\(S'_1,\dots,S'_{\lceil m/d\rceil}\leftarrow\) merges of consecutive _d_-tuples from _S_<sub>1</sub>_,...,S<sub>m</sub>_<br>
**if** _m_ is not divisible by _d_ **then**<br>
\(S'_{\lfloor m/d\rfloor}\leftarrow\) merge of \(S'_{\lfloor m/d\rfloor}\) and \(S'_{\lceil m/d\rceil}\triangleright\) _The number of sequences is now exactly_ \(m'\).<br>
\(Q\leftarrow\) priority queue containing \(S'_1,\dots,S'_{m^\prime}\) ordered by their initial elements<br>
**while** _Q_ is non-empty do<br>
   if \(|Q|\le d\) then<br>
Output<br>
the<br>
merge<br>
of<br>
all<br>
sequences<br>
in<br>
_Q_<br>
and<br>
terminate.<br>
\((i_1,i_2,\dots,i_{d+1})\leftarrow\) pop _d_+1 sequences from _Q_<br>
\(x\leftarrow\)<br>
initial<br>
element<br>
of<br>
the<br>
sequence<br>
\(S'_{i_{d+1}}\)<br>
Output<br>
_d_<br>
-way<br>
merge<br>
of<br>
\(S'_{i_1},S'_{i_2},\dots,S'_{i_d}\)<br>
restricted<br>
to<br>
elements<br>
smaller<br>
than<br>
_x_<br>
.<br>
**for** \(j\in\{1,\dots,d+1\}\) **do**<br>
   if \(S'_{i_j}\) is still non-empty then<br>
Push<br>
\(S'_{i_j}\)<br>
back<br>
to<br>
_Q_<br>
.

## 3.1 Prior knowledge of \(\pi\)

First, let us assume that the algorithm knows (or is given) the Füredi-Hajnal limit \(c_\pi\). Moreover, we assume that the input is a permutation sequence, i.e., its all elements are pairwise distinct.

Set \(d=\lceil 2c_\pi\rceil\). We first reduce the number of presorted sequences to \(m'\le\frac{n}{d\mathrm{log}n}\) by merging together consecutive _d_-tuples of sequences, with potentially doing one extra two-way merge at the end. Let \(S'_1,\dots,S'_{m^\prime}\) denote the resulting sequences. If all sequences already got merged into a single one, the algorithm simply copies it on output and terminates.

Afterwards, the algorithm initializes a priority queue _Q_ containing sequences \(S'_1,\dots,S'_{m^\prime}\) ordered by their initial elements and proceeds in rounds. In each round, the algorithm extracts from _Q_ the _d_+1 sequences starting with the smallest elements. Let _i_<sub>1</sub>_,...,i_<sub>_d_+1</sub> denote their indices. The algorithm then performs a standard _d_-way merge of \(S'_{i_1},S'_{i_2},\dots,S'_{i_d}\) restricted to the elements smaller than the initial element (minimum) of \(S'_{i_{d+1}}\). We say that the sequences \(S'_{i_1},S'_{i_2},\dots,S'_{i_d}\) are _touched_ by the algorithm in this round. At the end of the round, each sequence \(S'_{i_j}\) is pushed back in _Q_ unless it has already been emptied. Note that if _Q_ contains at most _d_ sequences at the beginning of any round, the algorithm simply merges them all together and terminates. This is repeated until all sequences \(S'_1,\dots,S'_{m^\prime}\) are exhausted. See Algorithm 1. Observe that the algorithm produces the same result as a standard multi-way merge and thus, it correctly outputs a sorted sequence.

### Running time.

Clearly, each element in the input incurs a time of _O_(log_d_) when written on the output, since it is obtained from a merge of the _d_ way. It remains to bound the initial preprocessing time and the extra overhead per one round together with the total number of rounds.

The initial merging of input sequences in _d_-tuples takes \(O(\mathrm{log}d\cdot n)\) time using the standard multi-way merge implementation with binary heap. It suffices to implement the priority queue _Q_ using the standard binary heap. Its initialization takes only \(O(m')\subseteq O(\frac{n}{\mathrm{log}n})\) time. In each round, we pop _d_+1 sequences from the priority queue _Q_ and push at most _d_+1 sequences back for a total time of \(O(d\cdot\mathrm{log}m')\subseteq O(d\cdot\mathrm{log}n)\). Therefore, each round incurs an overhead of \(O(d\cdot\mathrm{log}n)\).<tbc>


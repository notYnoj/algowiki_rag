**Algorithm 2** Algorithm for merging \(\pi\)-avoiding input _S_ partitioned into presorted sequences _S_<sub>1</sub>_,...,S<sub>m</sub>_ without prior knowledge of \(\pi\).

\(d\leftarrow 1\)<br>
while there are some elements remaining do<br>
   \(d\leftarrow 2\cdot d\)<br>
   \(S_1,\dots,S_{\lceil m/2\rceil}\leftarrow\) merges of consecutive pairs from S<sub>1</sub>_,...,S<sub>m</sub>_<br>
   if m is odd then<br>
   \(S_{\lfloor m/2\rfloor}\leftarrow\) merge of \(S_{\lfloor m/2\rfloor}\) and \(S_{\lceil m/2\rceil}\triangleright\) The number of sequences is at most \(\frac{m}{2^i}\).<br>
   \(m\leftarrow\lfloor\frac{m}{2}\rfloor\)<br>
   \(Q\leftarrow\) priority queue with all non-empty sequences ordered by their initial elements<br>
   \(r\leftarrow 1\triangleright\) Counter for the number of rounds<br>
while Q is non-empty and \(r\le m\) do<br>
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
   \((i_1,i_2,\dots,i_{d+1})\leftarrow\) pop d+1 sequences from Q<br>
   \(x\leftarrow\) initial element of the sequence S<sub>i<sub>d+1</sub><br>
   Output d-way merge of S<sub>i<sub>1</sub></sub>,S<sub>i<sub>2</sub></sub>,...,S<sub>i<sub>d</sub></sub> restricted to elements smaller than x.<br>
   for \(j\in\{1,\dots,d+1\}\) do<br>
   if S<sub>i<sub>j</sub></sub> is still non-empty then<br>
Push<br>
S<sub>i<sub>j</sub></sub><br>
back<br>
to<br>
_Q_<br>
.<br>
   \(r\leftarrow r+1\)

As before, the algorithm clearly outputs a correctly sorted sequence, and it only remains to bound its running time.

**Claim 3.3.** _On a_ \(\pi\)_-avoiding permutation sequence S, Algorithm 2 terminates after at most_ \(\lceil logc_\pi\rceil+1\) _phases._

_Proof._ Assume for a contradiction that more phases than \(\lceil logc_\pi\rceil+1\) are needed and set \(i=\lceil logc_\pi\rceil+1\). In other words, the algorithm is not able to terminate in the _i_th phase. Observe that \(2^i\ge 2c_\pi\) and therefore, we have \(d_i\ge 2c_\pi\). Recall that _m<sub>i</sub>_ denotes the number of sequences in the _i_th phase. But since \(d_i\ge 2c_\pi\) and \(m_i\le\frac{n}{d_ilogn}\), the exact same argument as in Claim 3.2 implies that _m<sub>i</sub>_ rounds suffice to merge all remaining elements, and thus the algorithm should have terminated in the _i_th phase regardless of the number of elements processed in previous phases.

## Running time.

As before, we charge each element with the time needed to retrieve it when it is outputted. In the _i_th phase, the algorithm outputs elements using 2_<sup>i</sup>_-way merges, and thus each element incurs a cost of _O(i_) which is at most \(O(logc_\pi+1)\) by Claim 3.3.

Now, we show that we only use linear extra overhead in each phase, again totaling \(O((logc_\pi+1)\cdot n)\) time by Claim 3.3. The merging at the beginning of each phase takes clearly only linear time, since each element participates in at most two 2-way merges. Moreover, the _i_th phase consists of at most \(m_i\le\frac{n}{2^ilogn}\) rounds by design. Each round can be handled with an overhead of \(O(2^i\cdot logm_i)\subseteq O(2^i\cdot logn)\) for retrieving the 2_<sup>i</sup>_ smallest sequences from the binary heap at the beginning of the round and inserting them back at the end of the round. In total, this produces an overhead of \(O(2^i\cdot logn\cdot m_i)\subseteq O(n)\) per each phase as promised.


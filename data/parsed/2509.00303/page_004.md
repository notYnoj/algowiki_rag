<tbc>their peers are firmly classified into the Less (_L_) or Greater (_G_) sets, then a voting routine (Algorithm 2) determines their final placement. This ensures that high-confidence decisions anchor the partition structure before uncertain cases are resolved. Only when a deadlock occurs (i.e., no remaining unresolved items have fully classified peers), then the voting routine is triggered on an unresolved item in order to resolve the cyclic dependencies.

**Prompt Block 3: External Comparison Prompt**

To address the limitation of high running cost in the external bubble sort proposed in RankGPT [61], we propose a new semantic external merge sort approach inspired by the relational external merge sort approach [27]. As shown in Algorithm 3, our approach operates in two distinct phases: First, the Run Generation phase divides the input into sorted runs of size _m_, using LLMSort with Prompt Block 3. Second, the Merge Phase (Algorithm 4) iteratively merges two sorted runs into one sorted run. The two-way merge operation employs a sliding-window mechanism: it buffers _m_ keys (_m/_2 keys from each sorted run) for the LLMSort to derive a partial ordering on this buffer. From this local ranking, we extract items and add them to the final output until the candidates from one of the input runs are exhausted within the current window. This buffer must be refilled again before the next extraction, as the unseen element from the exhausted run must be compared with the remaining items in the buffer to determine the total order. This process continues until one of the input runs is completely exhausted.

## 3.3 Limit K

A common usage pattern is to combine the **ORDER BY** clause with **LIMIT K**, where the user wants to retrieve _K_ items from the sorted results. This pattern offers an additional opportunity to save the number of LLM invocations and costs. For example, the external bubble sort [61] issues \(O(\frac{2N}{m})\) LLM calls per round and places \(\frac{m}{2}\) keys in their positions per round; retrieving the top _K_ keys therefore needs \(\frac{2K}{m}\) rounds, reducing the cost from _O(N_<sup>2</sup>_/m_<sup>2</sup>) (full sort) to _O(KN/m_<sup>2</sup>). See  1 for the number of LLM function calls used in each algorithm in both full sort and LIMIT _K_. Assume the user wants to retrieve the first _K_ rows in descending order based on some criteria (e.g. retrieve the _K_ most relevant passages to the user question). In quick sort, after it partitions rows into _L_ (lesser) and _G_ (greater) lists comparing each row to the pivot and _v_-1 validation samples, if _G_ contains more than _K_ rows, then only _G_ needs to be sorted and _L_ can be discarded. This is also known as partial quick sort [40]. It can be seen as a quick select, which uses _O(N_) comparisons to find the partition with _K_ rows, and then applies quick sort on _K_ rows. For External Merge Sort (Algorithm 3 and Algorithm 4), it first performs the run generation phase (i.e., generating sorted runs with _m_ rows) and then performs 2-way merge. The run generation phase requires \(\frac{N}{m}\) LLM calls. During the 2-way merge, if the merged list reaches _K_ items, then it can discard all the rest. As a result, having the LIMIT _K_ clause also reduces the number of invocations for external merge sort. For the first \(O(log\frac{K}{m})\) rounds, each run size will be less than _K_, and each round requires \(O(\frac{N}{m})\) function calls. Once the run size reaches _K_, the behavior changes. For all subsequent rounds, we merge two runs of size _K_ but strictly cap the output at _K_ items (discarding the remaining _K_). As a result, the total number of items decrease by a factor of 2 for each round. Hence, the LLM function calls decrease from \(\frac{N}{m}\), to \(\frac{N}{2m}\), to \(\frac{N}{4m}\), etc. This is a geometric sequence which<tbc>

Input: Dataset D, batch size m, sorted LLMSort(\(\cdot\)), two-way merger LLMerge(\(\cdot\))<br>
Phase 1: Run generation;<br>
Partition D into C<sub>0</sub>,...,C<sub>\(\lceil\lceil D|/m\rceil-1\)</sub> of size at most m;<br>
for \(i\leftarrow 1\) to \(\lceil|D|/m\rceil-1\) do in parallel<br>
  \(S_i\leftarrow LLMSort(C_i)\) // listwise sorting<br>
  \(Runs\leftarrow[S_0,\dots,S_{\lceil|D|/m\rceil-1}]\);<br>
Phase 2: Iterative merging;<br>
while |Runs|\>1 do<br>
  \(NewRuns\leftarrow[]\);<br>
   for i=0,2,4,...,|Runs|-1 do<br>
   if \(i+1\le|Runs|-1\) then<br>
  \(S\leftarrow LLMerge(Runs[i]\), Runs[i+1], m)<br>
// Algorithm 4<br>
   append S to NewRuns;<br>
   else<br>
   append Runs[i] to NewRuns<br>
  \(Runs\leftarrow NewRuns\);<br>
return Runs[1] // final sorted sequence

Input: Sorted runs L<sub>1</sub>, L<sub>2</sub>; batch size m; LLMSort(\(\cdot\))<br>
Output: Merged sorted run S<br>
  \(i\leftarrow 0\), \(j\leftarrow 0\) // read positions in L<sub>1</sub> and L<sub>2</sub><br>
   \(S\leftarrow[]\);<br>
  \(h\leftarrow max(\lfloor m/2\rfloor,1)\);<br>
   while i<<|L<sub>1</sub>| or j<|L<sub>2</sub>| do<br>
   if \(i\ge|L_1|\vee j\ge|L_2|\) then<br>
   append \(\big(i\ge|L_1|?L_2[j:]:L_1[i:]\big)\) to S;<br>
   break;<br>
  // Buffer up to h items from each run<br>
  \(a\leftarrow min(h,|L_1|-i)\); \(b\leftarrow min(h,|L_2|-j)\);<br>
  \(B\leftarrow L_1[i:i+a]\cup L_2[j:j+b]\);<br>
  \(R\leftarrow LLMSort(B)\);<br>
  // Emit in sorted order until one run’s buffer is exhausted<br>
  \(e_1\leftarrow 0\), \(e_2\leftarrow 0\);<br>
   for each \(x\in R\) do<br>
   append x to S;<br>
   if \(x\in L_1\) then \(e_1\leftarrow e_1+1\);<br>
   else \(e_2\leftarrow e_2+1\);<br>
   if e<sub>1</sub>=a or e<sub>2</sub>=b then break;<br>
  \(i\leftarrow i+e_1\); \(j\leftarrow j+e_2\);<br>
return S

Rank the passages based on how well they answer the question in ascending order. Question: {question} Passages: [1] {passage\_1} [2] {passage\_2} ...

**Algorithm 3:** LLM External Merge Sort

**Algorithm 4:** LLM Two-Way Merge


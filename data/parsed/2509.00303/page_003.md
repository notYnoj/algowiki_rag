<tbc>number of rows. Prompt Block 1 shows the template used to generate the relevance score for the passage ranking task.

To even further reduce the number of LLM function calls, a commonly used technique is to use the _external pointwise_ approach, where _m_ keys are batched into a single prompt and the model returns a list of _m_ values [8]. With the external pointwise approach, the number of LLM function calls becomes _O(N/m_). Also, the external pointwise method often leads to less monetary cost. This cost saving is achieved by sharing the instructional prefix across a batch of keys, rather than repeating it for each individual item. By amortizing the prompt’s token cost across _m_ items, the total number of billed input tokens is substantially reduced. Specifically, instead of evaluating a single key as shown in Prompt Block 1, this approach provides the LLM with a list of keys and requests it to generate a corresponding list of values.

## 3.2 Comparison-Based Ordering

In comparison-based ordering, the LLM is asked to directly compare two or more keys and decide the ranking order. Instead of assigning independent values to each key, the model outputs a permutation of the input keys. Compared to value-based ordering, comparison-based methods are typically more expensive, as the number of comparisons can grow quadratically with the number of keys in the worst case. Typically, researchers have implemented quick sort and external bubble sort on top of the LLM comparators. In the case of external bubble sorting algorithm (sliding window strategy) [61], it sorts _m_ keys at a time and then advances by \(\frac{m}{2}\) steps. It allows the model to repeatedly compare overlapping groups of keys (i.e., \(\frac{m}{2}\) keys), so that \(\frac{m}{2}\) items of higher rank gradually ’bubble up’ in successive windows.

We introduce two new comparison-based algorithms: (i) **quick sort with majority voting** to improve sorting quality compared to vanilla quick sort, and (ii) a **semantic external merge sort** inspired by the classical two-way external merge sort to reduce the cost compared to external bubble sort. Later in the evaluations, we empirically demonstrate the effectiveness of these methods, showing that our quick sort variant leads to better accuracy than vanilla quick sort, and the external merge sort yields substantial cost savings while maintaining high quality outputs.

As shown in Algorithm 1, LLM quick sort algorithm follows the classical divide-and-conquer strategy, and uses an LLM comparator (LLMSort) which takes in two keys and then determines the semantic order between these two keys. Prompt Block 2 shows the template used to generate the correct order between<tbc>

Input: Dataset D, LLMSort(\(\cdot\)), votes v \(\ge\) 1<br>
if \(|D|\le 1\) then return D;<br>
\(p\leftarrow D[0]\); L, G, L<sub>initial</sub>, \(G_{initial}\leftarrow[]\); \(\mathcal{R}'\leftarrow\emptyset\);<br>
\(\mathcal{R}\leftarrow\{(x,LLMSort(p,x))\text{for}x\in D[1:]\}\)<br>
for each \((x,r)\in\mathcal{R}\) do<br>
   if r=l then \(L_{initial}\leftarrow L_{initial}\cup\{x\}\) else<br>
\(G_{initial}\leftarrow G_{initial}\cup\{x\}\);<br>
   for each \((x,r_0)\in\mathcal{R}\) do<br>
   \(P\leftarrow(r_0=l)?G_{initial}:L_{initial}\);<br>
   \(Y\leftarrow Sample(P,v-1)\);<br>
   \(R_Y\leftarrow\{LLMSort(x,y)|y\in Y\}\);<br>
   if all(R<sub>Y</sub>=l) then \(L\leftarrow L\cup\{x\}\);<br>
   if all(R<sub>Y</sub>=g) then \(G\leftarrow G\cup\{x\}\);<br>
   \(\mathcal{R}'=\mathcal{R}'\cup(x,r_0,Y,R_Y)\) ;<br>
while |L|+|G|<|D|-1 do<br>
   \(deadLock\leftarrow\) True;<br>
   for each \((x,\dots)\in\mathcal{R}'\) with \(x\notin L\cup G\) do<br>
   if \(Y\subseteq L\cup G\) then<br>
   \(deadLock\leftarrow\) False;<br>
   // Vote refers to Alg 2<br>
   if VOTE(tuple, L, G)=l then<br>
   \(L\leftarrow L\cup\{x\}\);<br>
   else<br>
   \(G\leftarrow G\cup\{x\}\);<br>
   if deadLock then<br>
   Find any \((x,\dots)\in\mathcal{R}'\) with \(x\notin L\cup G\);<br>
   if VOTE(tuple, L, G)=l then<br>
   \(L\leftarrow L\cup\{x\}\);<br>
   else<br>
   \(G\leftarrow G\cup\{x\}\);<br>
   \(SL\leftarrow\) LLMQUICKSORT(L, LLMSort,v);<br>
   \(S_G\leftarrow\) LLMQUICKSORT(G, LLMSort,v);<br>
return \(SL||[p]||S_G\);

if r<sub>0</sub>=l then \(L_\text{vote},G_\text{vote}\leftarrow 1.5,0\);<br>
   else \(L_\text{vote},G_\text{vote}\leftarrow 0,1.5\);<br>
   for each peer \(y_i\in Y\) with result \(r_i\in R_Y\) do<br>
   if \(y_i\in L\wedge r_i=l\) then \(L_\text{vote}\leftarrow L_\text{vote}+1\);<br>
   if \(y_i\in G\wedge r_i=g\) then \(G_\text{vote}\leftarrow G_\text{vote}+1\);<br>
   if L<sub>vote</sub>\>G<sub>vote</sub> then return l;<br>
   else return g;

two passages. Unlike quick sort, which relies on a single comparison against the pivot to partition items, quick sort with majority votes aims to further improve the sorting robustness by validating the partition through majority voting. In this method, an item is compared not only with the pivot but also with a set of sampled ’peers’. The core intuition relies on transitivity: if a key _x_ is less than the pivot _p_, it should logically be less than any item _y_ that is greater than _p_. Items that achieve full consensus across all peer comparisons are partitioned immediately. Items with conflicting results are resolved iteratively; they wait until<tbc>

Evaluate how well the passage answers the question by assigning a score from 0 to {max\_point}, where 0 is not relevant and {max\_point} is prefectly relevant. Question: {question}<br>
Passage: {key}

Determine which passage answers the question better. Question: {question}<br>
Passage A: {key1}<br>
Passage B: {key2}

**Prompt Block 1: Value-based Ranking Prompt**

**Prompt Block 2: Comparison Prompt**

**Algorithm 1:** Quick Sort with Majority Voting

**Algorithm 2:** Vote Routine in Quick Sort


**Algorithm 4** TimSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

while true do<br>   if |S|\>3 and r<sub>1</sub>\>r<sub>3</sub> then \(\triangleright\) merge condition #1<br>   if \(R_2\leftarrow\) Merge(R<sub>3</sub>,R<sub>2</sub>)<br>   else if |S|\>2 and \(r_1\ge r_2\) then \(\triangleright\) merge condition #2<br>   if \(R_1\leftarrow\) Merge(R<sub>2</sub>,R<sub>1</sub>)<br>   else if |S|\>3 and \(r_1+r_2\ge r_3\) then \(\triangleright\) merge condition #3<br>   if \(R_1\leftarrow\) Merge(R<sub>2</sub>,R<sub>1</sub>)<br>   else if |S|\>4 and \(r_2+r_3\ge r_4\) then \(\triangleright\) merge condition #4<br>   if \(R_1\leftarrow\) Merge(R<sub>2</sub>,R<sub>1</sub>)<br>   else<br> break

sequence of _n/_16 runs, each of size 2. For simplicity, assume _n_ evenly divides into these runs. See Figure 11. Our proof exploits the following key observations, which follow directly from TimSort’s merge policy (see Algorithm 4).

**Observation 7.** _If a merge sequence in TimSort produces a stack of runs whose lengths form a sequence of strictly decreasing powers of 2, then the merge sequence terminates._

**Observation 8.** _We must know r_<sub>2</sub> _to validate that all merge conditions are false at the end of a merge sequence._

Observation 7 has two notable effects. First, the beginning three runs, those of lengths _n/_2, _n/_4, and _n/_8, are only ever merged at the very end of the main loop. Second, repeatedly adding runs of size 2 causes them to collapse into powers of 2. For example, adding the first four runs to the stack produces the series of run lengths {_n/_2_,n/_4_,n/_8,2}. This produces no merges. However, adding the next run produces a stack like so: {_n/_2_,n/_4_,n/_8,2,2}, which collapses into {_n/_2_,n/_4_,n/_8,4} by merge condition #2 of Algorithm 4. We generalize this with the following definition.

**Definition 1.** _Let **stage** i of TimSort run on our input instance be defined as follows. Consider a set of runs on the stack with sizes_

\(\{n/2,n/4,n/8,2^{i-1},2^{i-2},\dots,8,4,2\}.\)

_Since their sizes are decreasing powers of 2, no merges occur by Observation 7. In the next iteration of the main loop, an additional run is added. We say this is the beginning of stage i. The run lengths are like so:_

\(\{n/2,n/4,n/8,2^{i-1},2^{i-2},\dots,8,4,2,2\},\)

_which causes merge condition #2 to be repeatedly applied. For i\<_log(_n/_8) _and by Observation 7, the merge sequence terminates when the stack is of size four, with run lengths like so:_

\(\{n/2,n/4,n/8,2^i\}.\)


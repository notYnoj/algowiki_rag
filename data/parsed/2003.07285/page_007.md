Data: s and <o>s</o><br>
Result: An approximate solution for LCS.<br>
Divide s and <o>s</o> into \(\sqrt{n}\) blocks as explained;<br>
for \(i\in[\sqrt{n}]\) do<br>
   for each symbol c that appears in b<sub>i</sub> do<br>
   randomly choose one appearance and remove the rest of the appearances of c from b<sub>i</sub>;<br>
   for each symbol c that appears in <o>b</o><sub>i</sub> do<br>
   randomly choose one appearance and remove the rest of the appearances of c from <o>b</o><sub>i</sub>;<br>
   \(r\leftarrow\)a random integer number between 1 and \(\sqrt{n}\).;<br>
   \(A,B\leftarrow 0\);<br>
   for i=1 to \(\sqrt{n}-r\) do<br>
   \(A\leftarrow A+|\text{lcs}(b_i,\overline{b_{i+r}})|\);<br>
   for \(i=\sqrt{n}-r+1\) to \(\sqrt{n}\) do<br>
   \(B\leftarrow B+|\text{lcs}(b_i,\overline{b_{i+r-\sqrt{n}}})|\);<br>
   return max{A,B}

<tbc>remove some characters from each block to make sure no symbol appears more than once. Next, we choose a random integer r uniformly from \([\sqrt{n}]\). We then construct a solution in which each block b<sub>i</sub> is associated to block <o>b</o><sub>i+r</sub>. Since the blocks are all semi-permutations, we can compute their LCS’s in linear time and therefore we can run Algorithm 4 in near linear time. The details about the running times of Algorithms 3 and 4 can be found in Section 8.

To better understand the relation between Algorithms 3 and 4, fix an optimal solution opt to be the longest common subsequence for a nontrivial instance of s and <o>s</o>. We can break opt into at most \(2\sqrt{n}\) parts such that the corresponding characters of each part lie within a single block in both of the strings. If a symbol c appears at least \(\overline{\omega}(1)\) times in one part of opt, then we call the corresponding characters of that part crebris. We call the rest of the characters of opt rarus <sup>2</sup> . Algorithm 3 aims to approximate the crebris characters of the optimal solution and Algorithm<tbc>

<sup>2</sup>Crebris and rarus are Latin equivalents of words frequent and infrequent

S
cacbbb
cccacc
cccbc
ccbcab
cccccccc
accaa
opt:
abbb
abbb
aaa
S
daddb
ddddd
ddabb
abbadd
ddddd
ddadd
aaddd

**Algorithm 4:** random shifting

Figure 1: An example of the decomposition of the optimal solution into several parts.


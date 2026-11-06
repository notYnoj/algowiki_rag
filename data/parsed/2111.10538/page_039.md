**Algorithm 6** Dynamic programming algorithm for block-based lcs problem

procedure DP-LCS(W<sub>A</sub>,W<sub>B</sub>,M) \(\triangleright\) Lemma 4.8<br>
   Note that M is table s.t. \(M(k_1,k_2)\le\text{lcs}(A_{k_1},B_{k_2})\).<br>
   Note that W<sub>A</sub> and W<sub>B</sub> are sets of windows.<br>
   Let S<sub>1</sub> denote the sorted list of right-indices of W<sub>A</sub>-windows.<br>
   Let S<sub>2</sub> denote the sorted list of right-indices of W<sub>B</sub>-windows.<br>
   for \(i_1\in S_1\) do<br>
   for \(i_2\in S_2\) do<br>
   \(C[i_1][i_2]\leftarrow 0\)<br>
   \(x_1\leftarrow 0\)<br>
   for A<sub>k<sub>1</sub></sub>,B<sub>k<sub>2</sub></sub> have right index i<sub>1</sub>,i<sub>2</sub> do \(\triangleright\) Case 1<br>
   \(\text{left}_1\leftarrow\text{left index of}A_{k_1}\)<br>
   \(\text{left}_2\leftarrow\text{left index of}B_{k_2}\)<br>
   \(\text{tmp}\leftarrow C[\text{left}_1][\text{left}_2]+M(A_{k_1},B_{k_2})\)<br>
   if tmp\>x<sub>1</sub> then<br>
   \(x_1\leftarrow\text{tmp}\)<br>
   end if<br>
   end for<br>
   Let prev(i<sub>1</sub>) denote the first index \(\in S_1\) that is earlier than i<sub>1</sub><br>
   Let prev(i<sub>2</sub>) denote the first index \(\in S_2\) that is earlier than i<sub>2</sub><br>
   \(x_2\leftarrow C[\text{prev}(i_1)][i_2]\triangleright\) Case 2<br>
   \(x_3\leftarrow C[i_1][\text{prev}(i_2)]\triangleright\) Case 3<br>
   \(C[i_1][i_2]\leftarrow\text{max}(x_1,x_2,x_3)\)<br>
   end for<br>
   end for<br>
end procedure

We also throw out all the \(\widetilde{B}_j\)’s such that \(|\widetilde{B}_j|>d/(2\epsilon_0)\). Throwing out each such \(\widetilde{B}_j\) can decrease the LCS by at most d, but removes \(d/(2\epsilon_0)\) characters; hence the total loss to LCS is at most \(2\epsilon_0\cdot n\).

Finally, we further throw out either all the \(\widetilde{B}_j\)’s that are contained in some \(W_B^0\)-window of length d, or all the ones that aren’t; again this step loses at most half of the LCS.

**Case 1: we keep all the** \(\widetilde{B}_j\)**’s that are contained in some** \(W_B^0\)**-window of length** d**.** By the previous paragraph, each of them is the only \(\widetilde{B}_j\) contained in that window, so we can just match A<sub>j</sub> to that window.

**Case 2: we keep** \(\widetilde{B}_j\)**’s that are not contained in any** \(W_B^0\)**-window of length** d**.** For each \(\widetilde{B}_j\), consider the index that is a multiple of \(d\cdot 2^i\) for the largest possible i (notice that this is unique). We truncate \(\widetilde{B}_j\) to the left of this index; wlog the total contribution of truncated characters to the LCS is at most half (otherwise we reverse both strings). Each \(\widetilde{B}_j\) is now contained in a disjoint \(W_B^i\)-window, so we can match A<sub>j</sub> to that window.

## 4.3 Dynamic Programming for window-compatible LCS

**Lemma 4.8** (Dynamic Programming for Longest Common Sequence)**.** _Given two strings A,B of length n, respective sets of windows W<sub>A</sub>,W<sub>B</sub>, and estimates-table M on the pairwise LCS, Algorithm 6 computes the longest common subsequence of A,B that is both: (i) window-compatible, and_<tbc>


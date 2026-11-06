**Algorithm 1** \(O(fn_1(n_2-\ell+1))\)-time algorithm for SegLCS

**Input:** Strings T<sub>1</sub> of length n<sub>1</sub> and T<sub>2</sub> of length n<sub>2</sub>, and a positive integer f

**Output:** slcs(T<sub>1</sub>,T<sub>2</sub>,f)

1: **for** \(h\leftarrow 1\) to f do

2: \(\text{MaxVIdx}[h]\leftarrow 0\)

3: diag=0

4: **while** diag\<n<sub>1</sub>-MaxVIdx\[h\] **do**

5: \(L(diag,0,h)\leftarrow 0\)

6: _FillDiagonally_(h,diag,MaxVIdx) \(\triangleright\) May update MaxVIdx\[h\].

7: \(diag\leftarrow diag+1\)

8: **end while**

9: **end for** \(\triangleright\text{MaxVIdx}[h]=\text{slcs}(T_1,T_2,h)\) holds at this line.

10: **return** MaxVIdx\[f\]

<tbc>diagonal lines of table L<sub>h</sub> for diag=0,1,2,..., i.e., from left to right. The subroutine to fill a diagonal line is denoted by FillDiagonally, which is shown in Algorithm 2. Here, we introduce an array MaxVIdx of size f such that, while computing each table L<sub>h</sub> in the while-loop, MaxVIdx\[h\] keeps the largest vertical index s satisfying that the s-th row of table L<sub>h</sub> has a finite value. Thus, at the end of the computation of the last table L<sub>f</sub> (at line 10), slcs(T<sub>1</sub>,T<sub>2</sub>,f)=MaxVIdx\[f\] holds. By the definition of MaxVIdx\[h\], the condition of the while-statement is valid since for every \(e\ge n_1-\text{MaxVIdx}[h]\), the e-th diagonal cannot reach the MaxVIdx\[h\]-th row as discussed above.

In subroutine FillDiagonally (Algorithm 2), we fill the diag-th diagonal line from upper-left to lower-right, where s is a vertical index and i is a horizontal index of the table L<sub>h</sub>. Each cell in the diagonal line is computed in the while-loop. Lines 6–10 are due to Lemma 4. Also, if L(i,s,h) is not updated in the while-loop, its value is \(\infty\), and thus, we update \(\text{MaxVIdx}[h]\leftarrow s-1\). Further, as discussed above, we do not need to compute below s on the diagonal line anymore since they are all \(\infty\). Then we terminate the procedure.

We give an example of the sparse table computed by Algorithms 1 and 2 for input strings T<sub>1</sub>=abcabbac, T<sub>2</sub>=bcbcbbca and f=3 in  3. For example, in the third diagonal line of L<sub>2</sub>, let us consider computing L(6,4,2) and assume that L(5,3,2) has already been computed. We can start searching the index of T<sub>2</sub> satisfying the condition of recurrence from L(5,3,2)+1=4. Then, the smallest index 6 of T<sub>2</sub> satisfying lcsuf(T<sub>1</sub>\[1..6\],T<sub>2</sub>\[1..6\])=2 and L(6-2,4-2,1)=2\<6 is the answer of L(6,4,2).

Finally, we discuss the complexity of our algorithm. For each table L<sub>h</sub>, our algorithm computes<tbc>


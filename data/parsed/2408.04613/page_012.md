`Multiply(A`<sup>∗</sup>_,B_<sup>∗</sup>**) begin`<br>
   \(A,B\leftarrow\mathtt{Compress}(A^*,B^*)\);<br>
   \(p\leftarrow\) height of A; \(q\leftarrow\) width of A; \(r\leftarrow\) width of B;<br>
   if p=1 and r=1 then<br>
   \(C\leftarrow 1\times 1\) matrix with the entry equal to \(min\{A_{0,j}+B_{j,0}|j\in[0..q)\}\);<br>
   return`Decompress`(A<sup>∗</sup>_,B_<sup>∗</sup>_,C_);<br>
   Sort core(A) by columns and core(B) by rows; // needed to find m<br>
   Pick the largest \(m\in(0..q)\) with<br>
   \(\delta(A[0..p)[0..m))+\delta(B[0..m)[0..r))\le(\delta(A)+\delta(B))/2\);<br>
   Build the condensed representations of A\[0_..p_\][0..m) and B\[0..m_\][0..r);<br>
   \(C^L\leftarrow\mathtt{Multiply}(A[0..p)[0..m),B[0..m)[0..r))\); Build`co`(_C<sup>L</sup>_) using Lemma 4.4;<br>
   Build the condensed representations of A\[0_..p_\][_m..q_) and B\[_m..q_\][0..r);<br>
   \(C^R\leftarrow\mathtt{Multiply}(A[0..p)[m..q),B[m..q)[0..r))\); Build`co`(_C<sup>R</sup>_) using Lemma 4.4;<br>
   \(lst\leftarrow\) list of length p; // vertical edges of the ladder from Figure 2<br>
   \(i\leftarrow p-1,j\leftarrow-1\); // current matrix coordinates while traversing the ladder<br>
   Maintain the well-defined values in _C<sup>L</sup>_\[_i..i_+1\]\[_j..j_+1\] and _C<sup>R</sup>_\[_i..i_+1\]\[_j..j_+1\] using`lc`(_C<sup>L</sup>_) and`lc`(_C<sup>R</sup>_), and the values in _C_\[_i..i_+1\]\[_j..j_+1\] as element-wise minima;<br>
   \(Core\leftarrow\{\}\);<br>
   while \(i\ge 0\) do<br>
   if i\<p-1 and \(0\le j<r-1\) and \(C_{i,j+1}+C_{i+1,j}\neq C_{i,j}+C_{i+1,j+1}\) then<br>
   \(Core\leftarrow Core\cup\{(i,j,C_{i,j+1}+C_{i+1,j}-C_{i,j}-C_{i+1,j+1})\}\);<br>
   if j=r-1 or \(C_{i,j+1}^L>C_{i,j+1}^R\) then<br>
   \(lst_i\leftarrow j\);<br>
   \(i\leftarrow i-1\);<br>
   else<br>
   \(j\leftarrow j+1\);<br>
   \(Core\leftarrow Core\cup\{(i,j,C_{i,j}^{L\square})\in core(C^L)|j<lst_{i+1}\}\cup\{(i,j,C_{i,j}^{R\square})\in core(C^R)|j>lst_i\}\);<br>
   Compute the topmost row and the leftmost column of _C_ as the element-wise minima of the topmost rows and the leftmost columns of _C<sup>L</sup>_ and _C<sup>R</sup>_;<br>
   Condensed representation of \(C\leftarrow(C[0..0][0..r),C[0..p)[0..0],Core)\);<br>
   return`Decompress`(A<sup>∗</sup>_,B_<sup>∗</sup>_,C_);

**Algorithm 1** The algorithm from Theorem 1.2. Given the condensed representations of the Monge matrices _A_<sup>∗</sup> and _B_<sup>∗</sup>, the algorithm returns the condensed representation of \(A^*\otimes B^*\).


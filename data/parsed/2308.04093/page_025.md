Input: q[-L...L] and S[-L...L], where \(S[i]\subseteq[w_\mathrm{max}],|S[i]|\le 1,q[i]\in\mathbb{Z}\cup\{-\infty\}\) for all i<br>
Output: (**x**\[-L...L\],z[-L...L\],r[-L...L\]) as a solution to Problem 1<br>
SMAWKAndScan(q[-L...L\],S[-L...L\]):<br>
begin<br>
   /\* Stage 1: use SMAWK to find all candidate updates \(q[j]+Q_w(\frac{i-j}{w})\) where<br>
   \(w\in S[j]\), expressed as difference-w APs consisting of indices i \*/<br>
   Initialize \(\mathcal{P}\leftarrow\varnothing\)<br>
   for \(w\in[w_\mathrm{max}]\) and \(c\in\{0,1,\dots,w-1\}\) do<br>
   \(J:=\{j:w\in S[j]\) and \(j\equiv c(\mathrm{mod}w),-L\le j\le L\}\)<br>
   \(I:=\{i:i\equiv c(\mathrm{mod}w),-L\le i\le L\}\)<br>
   Run SMAWK (Theorem A.1) on matrix \(A_{I\times J}\) defined as \(A[i,j]:=q[j]+Q_w\left(\frac{i-j}{w}\right)\).<br>
   for \(j\in J\) do<br>
   Suppose SMAWK returned the AP \(P_j\subseteq I\) of difference w, such that for every<br>
\(i\in P_j\), \(j=\mathrm{argmax}_{j^\prime\in J}A[i,j']\)<br>
   \(P_j\leftarrow P_j\cap\{i\in\mathbb{Z}:i>j\}\) // focus on candidate updates where \(\frac{i-j}{w}\) is a positive integer<br>
   Suppose P<sub>j</sub>={c+kw,c+(k+1)w,...,c+\ell w}, and insert \((j;c,w,k,\ell)\) into P<br>
  /\* Stage 2: combine all candidate updates by a linear scan from left to right, extending winning APs and discarding losing APs \*/<br>
   Initialize empty buckets B[-L\],B[-L+1\],...,B[L]<br>
   for \((j;c,w,k,\ell)\in\mathcal{P}\) do<br>
   Insert \((j;c,w,k,\ell)\) into bucket B[c+kw] // insert to the bucket indexed by the beginning element of the AP<br>
   for \(i\leftarrow-L,\dots,L\) do<br>
   \(r[i]\leftarrow q[i],z[i]\leftarrow i,x[i]\leftarrow 0\). // the trivial solution for i<br>
   if \(B[i]\neq\varnothing\) then<br>
   Pick \((j;c,w,k,\ell)\in B[i]\) that maximizes \(q[j]+Q_w\left(\frac{i-j}{w}\right)\)<br>
   if \(q[j]+Q_w\left(\frac{i-j}{w}\right)>r[i]\) then<br>
   \(r[i]\leftarrow q[j]+Q_w\left(\frac{i-j}{w}\right),z[i]\leftarrow j,x[i]\leftarrow\frac{i-j}{w}e_w\). // solution for i<br>
   if \(i+w\le c+\ell w\) then<br>
   Insert \((j;c,w,k,\ell)\) into bucket B[i+w] // extend this winning AP by one step, and all other APs in the bucket B[i] are discarded<br>
return (**x**\[-L...L\],z[-L...L\],r[-L...L\])

**Algorithm 1:** Solving HintedKnapsackExtend<sup>+</sup> with singleton hint sets


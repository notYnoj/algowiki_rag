<tbc>_Proof._ We begin with the first bound. Let _A,B_ be the input matrices. Construct a \(n_1B_1\times n_2\) matrix _X_ and \(n_2\times n_3B_2\) matrix _Y_ as follows

\(X[(i,b),k]=\unknown[A[i,k]=b],Y[k,(j,c)]=\unknown[B[k,j]=c].\)

Note that construction takes _O(n_<sub>1</sub>_n_<sub>2</sub>_B_<sub>1</sub>+_n_<sub>2</sub>_n_<sub>3</sub>_B_<sub>2</sub>) time. Compute _XY_ and note that (_A∗B_)\[_i,j_\]=min{_b+c_s.t. _XY_\[(_i,b),(j,c_)\]=1} can be recovered from _XY_ in _O(n_<sub>1</sub>_n_<sub>3</sub>_B_<sub>1</sub>_B_<sub>2</sub>) time, or linear time in the size of _XY_ .

We now prove the second bound. Construct \(n_1B\times n_2B_2\) matrix _X_ and \(n_2B_2\times n_3\) matrix _Y_ as follows

\(X[(i,b),(k,c)]=\unknown[A[i,k]=b-c],Y[(k,c),j]=\unknown[B[k,j]=c].\)

Note that _X,Y_ can be constructed in _O(n_<sub>1</sub>_Bn_<sub>2</sub>_B_<sub>2</sub>+_n_<sub>2</sub>_B_<sub>2</sub>_n_<sub>3</sub>) time. Compute _XY_ and note that (_A∗B_)\[_i,j_\]=min{_b_s.t. (_XY_)\[(_i,b),j_\]=1} can be recovered from _XY_ in _O(n_<sub>1</sub>_n_<sub>3</sub>_B_) time, or linear time in the size of _XY_ . The second term in the minimum follows by a symmetric argument.

Figure 4 compares the running time of our directed MSSP algorithm (Theorem 1.6), the directed MSSP algorithm of \[GV19\], and the best known algorithms for computing Equation (2).

Comparison of Algorithms for computing Directed MSSP
Theorem 1.6
2.6
Equation (2)
Grandoni and Vassilevska Williams
2.5
2.4
Runtime exponent
2.3
2.2
2.1
2.0
0.0
0.2
0.4 S_in size exponent
0.6
0.8
1.0

Figure 4: Comparison of known algorithms for computing MSSP on unweighted DAGs against known algorithms for computing Equation (2) when \(|S_\mathrm{in}|=n^\sigma\). The blue dotted line denotes the running time of known algorithms for Equation (2). The red dotted line shows the running time of Theorem 1.6 and the yellow dotted line the running time of \[GV19\].


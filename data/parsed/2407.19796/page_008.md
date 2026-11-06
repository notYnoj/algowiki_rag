The following lemma is the core of our algorithm.

**Lemma 4.**<tbc>

\(L(i,s,h)=min\{L(i-1,s,h),j_{i,s,h}\}\)

<tbc>_where_<tbc>

\(j_{i,s,h}=min\{j|j\ge L(i-x,s-x,h-1)+xforx=min\{\text{lcsuf}(T_1[\text{\textit{..}}i],T_2[\text{\textit{..}}j]),s\}\}.\)

<tbc>_Proof._ By Equations (1) and Lemma 2, \(L(i,s,h)\le min\{L(i-1,s,h),j_{i,s,h}\}\) holds. Suppose _L(i,s,h)\<L(i_-1_,s,h_). Then, the last segment of an _h_-segmentation witnessing _L(i,s,h_)=_j_ must involve the last letter of _T_\[1_..i_\]. By Lemma 3, there is an _h_-segmentation witnessing _L(i,s,h_)=_j_ whose last segment has length _x_=min{lcsuf(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\])_,s_} and the other _h_-1 segments are embedded into _T_<sub>1</sub>\[1_..i-x_\] and _T_<sub>2</sub>\[1_..j-x_\]. That is, \(L(i-x,s-x,h-1)\le j-x\), i.e.,

\(L(i,s,h)=j\ge L(i-x,s-x,h-1)+x\ge j_{i,s,h}.\)

Therefore, _L(i,s,h_)=_j<sub>i,s,h</sub>_ if _L(i,s,h)\<L(i_-1_,s,h_).

Our algorithm computes values in the table _L_ based on Lemma 4.

Let _L<sub>h</sub>_ be the _h_-th table which stores _L(i,s,h_) for \(1\le i,s\le|T_1|\). Here, slcs(_T_<sub>1</sub>_,T_<sub>2</sub>_,f_) is the largest _s_ such that \(L(i,s,f)\neq\infty\) for \(0\le i\le|T_1|\), i.e., the _s_-th row is the lowest row which has an integer value in the _L<sub>f</sub>_. We show an example of three-dimensional table _L_ for _T_<sub>1</sub>=`abcabbac`, _T_<sub>2</sub>=`bcbcbcbbca` and _f_=3 in  2.

Next, we introduce the main part of our algorithm. In our algorithm, we compute the values for each diagonal line from upper left to lower right in left-to-right order. Then, we do not compute all values in the tables, since there are unrelated values for obtaining the length of a longest _f_-SegCS. While computing a diagonal line from upper-left to lower-right, we can stop the computation when we meet \(\infty\) since the values of the remaining cells on the line are guaranteed to be \(\infty\) by Equation (2). This is reflected to lines 13 and 15 of Algorithm 2 we will see later. Also, while processing diagonal lines from left to right in table _L<sub>h</sub>_, we can stop the iteration once we reach a cell in the rightmost column of _L<sub>h</sub>_ in the computation of some _p_-th diagonal. This is because, for any _q\>p_, the lowest endpoint of _q_-th diagonal must be higher than that of _p_-th diagonal, and thus, computing such diagonal is meaningless for our purpose. This is reflected to line 4 of Algorithm 1 we will see later.

From the above, we propose an algorithm shown in Algorithms 1 and 2. For convenience, we assume that the values of uninitialized \(L(\cdot,\cdot,\cdot)\) are \(\infty\). The main procedure is shown in Algorithm 1. We compute tables _L<sub>h</sub>_ for incremental _h_=1_,...,f_. In the while-loop, we compute the _diag_-th<tbc>

\begin{tabular}{ccccccccccccccccc}
_s_\\_i_ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & & & & & & & & & & & \\
1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 \\
2 & \(\infty\) & \(\infty\) & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 \\
3 & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 & 8 \\
4 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
5 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
6 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
7 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
8 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
\end{tabular}

\begin{tabular}{ccccccccccccccccc}
_s_\\_i_ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & & & & & & & & & & \\
1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
2 & \(\infty\) & \(\infty\) & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 3 & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 3 & 3 & 3 & 3 \\
3 & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 3 & 3 & 3 & 3 & 4 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & 6 & 6 & 6 \\
5 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
6 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
7 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
8 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
\end{tabular}

\begin{tabular}{ccccccccccccccccc}
_s_\\_i_ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & & & & & & & & & & \\
1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 8 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
2 & \(\infty\) & \(\infty\) & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 3 & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 3 & 3 & 3 & 3 \\
3 & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 3 & 3 & 3 & 3 & 4 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & 5 & 5 & 4 \\
5 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & 8 & 7 & 6 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
7 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
8 & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) & \(\infty\) \\
\end{tabular}

2: An example of three-dimensional table _L_=(_L_<sub>1</sub>_,L_<sub>2</sub>_,L_<sub>3</sub>) for strings _T_<sub>1</sub>=`abcabbac`, _T_<sub>2</sub>=`bcbcbcbcbbca` and _f_=3. From left to right, the tables are _L_<sub>1</sub>, _L_<sub>2</sub>, and _L_<sub>3</sub>.


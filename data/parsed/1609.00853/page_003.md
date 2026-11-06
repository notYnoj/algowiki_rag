<tbc>and semirooks in Section 3, we discuss the current state of knowledge and ignorance about bishops and semibishops in Section 4. Section 5 treats the queen as well as the partial queens that are not the rook, semirook, bishop, and semibishop. Section 7 concerns the nightrider and its sub-pieces, whose nonattacking placements have not been the topic of any previous theoretical discussion that we are aware of and consequently receive detailed treatment.

We conclude with questions related to these ideas and with proposals for research. For example, we suggest in Section 8.1 fairy chess pieces with relatively simple behavior that might provide insight into the central open problem of a good general bound on the period of the counting quasipolynomial in terms of _q_ and the set of moves.

We append a dictionary of notation for the benefit of the authors and readers.

## 2. Essentials, Mostly from Before

Our _board_ B is the unit square \[0,1\]<sup>2</sup>. (In Section 4.2 it may also be a right triangle; for simplicity here we assume the square.) Pieces are placed on integral points, (_x,y_) for \(x,y\in[n]:=\{1,\dots,n\}\), in the interior of an integral dilation (_n_+1)B of the board; e.g., the square board (_n_+1)\[0,1\]<sup>2</sup> has interior (_n_+1)(0,1)<sup>2</sup>. We also call these integral points the _board_; it will always be clear which board we mean.

A piece P has _moves_, which are the integral multiples of a finite set **M** of _basic moves_, which are non-zero, non-parallel integral vectors \(m=(c,d)\in\mathbb{Z}^2\). For instance, **M**={(1,0),(1,1),(0,1),(1,-1)} for the queen and **M**={(2,1),(1,2),(2,-1),(1,-2)} for the nightrider. Each basic move must be reduced to lowest terms and no basic move may be a scalar multiple of another. Thus, the slope _d/c_ contains all necessary information and can be specified instead of _m_ itself. We say two distinct pieces _attack_ each other if the difference of their locations is a move. In other words, a piece in position \(z:=(x,y)\in\mathbb{Z}^2\) attacks any other piece in the lines _z+rm_ for \(r\in\mathbb{Z}\) and \(m\in\mathbf{M}\). Attacks are not blocked by a piece in between, and they include the case where two pieces occupy the same location.

A _configuration_ **z**=(_z_<sub>1</sub>_,...,z<sub>q</sub>_) is a choice of locations _z<sub>i</sub>_:=(_x<sub>i</sub>,y<sub>i</sub>_) for the _q_ pieces on the dilated board (_n_+1)B, including the boundary. Thus **z** is an integral point in the dilated<tbc>

\begin{tabular}{ccccc}
_q_ & Rooks & Bishops & Queens & Nightriders \\
1 & A000290 & A000290 & A000290 & A000290 \\
2 & A163102\* & A172123 & A036464 & A172141 \\
3 & A179058 & A172124 & A047659 & A173429 \\
4 & A179059 & A172127 & A061994 & -- \\
5 & A179060 & A172129 & A108792 & -- \\
6 & A179061 & A176886 & A176186 & -- \\
7 & A179062 & A187239 & A178721 & -- \\
8 & A179063 & A187240 & -- & -- \\
9 & A179064 & A187241 & -- & -- \\
10 & A179065 & A187242 & -- & -- \\
\end{tabular}

1.1. Sequence numbers in the OEIS for nonattacking placements of _q_ rooks, bishops, queens, and nightriders. In each sequence the board size _n_ varies from 1 to (usually) 1000. \* means _n_ in the OEIS is offset from our value.


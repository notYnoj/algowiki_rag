Since det_B_<sub>_n_+1</sub> is unchanged under the elementary row operation of adding a multiple of one row to another, we write

\(\mathrm{det}B_{n+1}=\mathrm{det}_{(n+1)\times(n+1)}\left(\begin{array}{ c c c c c }
1 & \rho & \dots & \rho & \rho \\
0 & 1-\rho^2 & \dots & \rho-\rho^2 & \rho-\rho^2 \\
\vdots &  & \ddots &  & \vdots \\
0 & \rho-\rho^2 & \dots & 1-\rho^2 & \rho-\rho^2 \\
0 & \rho-\rho^2 & \dots & \rho-\rho^2 & 1-\rho^2
\end{array}\right).\) (19)

We can thus simplify the determinant as

\(\mathrm{det}B_{n+1}=(1-p)^n\mathrm{det}_{n\times n}\left(\begin{array}{ c c c c c }
1+\rho & \rho & \dots & \rho & \rho \\
\rho & 1+\rho & \dots & \rho & \rho \\
\vdots &  & \ddots &  & \vdots \\
\rho & \rho & \dots & 1+\rho & \rho \\
\rho & \rho & \dots & \rho & 1+\rho
\end{array}\right).\) (20)

To evaluate the determinant of this matrix we follow a similar procedure, where we eliminate most of the elements in the first column. We then repeat this process as the resulting matrix becomes smaller and smaller, until we reach a trivial case. The _k_th step in this iterative procedure has the following structure (where _k_=0,1_,...,n_-1_,n_):

\(\mathrm{det}B_{n+1}=(1-p)^n(1+k\rho)\mathrm{det}_{(n-k)\times(n-k)}\left(\begin{array}{ c c c c c }
\frac{1+(k+1)\rho}{1+k\rho} & \frac{\rho}{1+k\rho} & \dots & \frac{\rho}{1+k\rho} & \frac{\rho}{1+k\rho} \\
\frac{\rho}{1+k\rho} & \frac{1+(k+1)\rho}{1+k\rho} & \dots & \frac{\rho}{1+k\rho} & \frac{\rho}{1+k\rho} \\
\vdots &  & \ddots &  & \vdots \\
\frac{\rho}{1+k\rho} & \frac{\rho}{1+k\rho} & \dots & \frac{1+(k+1)\rho}{1+k\rho} & \frac{\rho}{1+k\rho} \\
\frac{\rho}{1+k\rho} & \frac{\rho}{1+k\rho} & \dots & \frac{\rho}{1+k\rho} & \frac{\rho}{1+(k+1)\rho} \\
1+k\rho
\end{array}\right)\) (21)

We now subtract \(\frac{\rho}{1+(k+1)\rho}\) times the first row from all other rows. In the first column, all except the first row thus becomes zeros, and there are two main cases we need to consider for the other elements. In the first case, for diagonal elements, we have we have

\(\frac{1+(k+1)\rho}{1+k\rho}-\frac{\rho}{1+k\rho}\frac{\rho}{1+(k+1)\rho}=\frac{[1+(k+1)\rho]^2-\rho^2}{[1+k\rho][1+(k+1)\rho]}\) (22)

\(=\frac{1+(k+2)\rho}{1+(k+1)\rho}.\) (23)

In the second case, for off-diagonal elements, we instead have

\(\frac{\rho}{1+k\rho}-\frac{\rho}{1+k\rho}\frac{\rho}{1+(k+1)\rho}=\frac{\rho}{1+k\rho}\left[\frac{1+(k+1)\rho-\rho}{1+(k+1)\rho}\right]\) (24)

\(=\frac{\rho}{1+(k+1)\rho}.\) (25)

Thus we have that

\(\mathrm{det}B_{n+1}=(1-p)^n(1+k\rho)\mathrm{det}_{(n-k)\times(n-k)}\left(\begin{array}{ c c c c c c }
\frac{1+(k+1)\rho}{1+k\rho} & \frac{\rho}{1+k\rho} & \dots & \frac{\rho}{1+k\rho} & \frac{\rho}{1+k\rho} \\
0 & \frac{1+(k+2)\rho}{1+(k+1)\rho} & \dots & \frac{\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} \\
\vdots &  & \ddots &  & \vdots \\
0 & \frac{\rho}{1+(k+1)\rho} & \frac{1+(k+2)\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} &  \\
0 & \frac{\rho}{1+(k+1)\rho} & \dots & \frac{\rho}{1+(k+1)\rho} & \frac{1+(k+2)\rho}{1+(k+1)\rho}
\end{array}\right)\) (26)

\(=(1-p)^n(1+(k+1)\rho)\mathrm{det}_{(n-(k+1))\times(n-(k+1)}\left(\begin{array}{ c c c c c c }
\frac{1+(k+2)\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} & \dots & \frac{\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} \\
\frac{\rho}{1+(k+1)\rho} & \frac{1+(k+2)\rho}{1+(k+1)\rho} & \dots & \frac{\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} \\
\vdots &  & \ddots &  & \vdots \\
\frac{\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} & \dots & \frac{1+(k+2)\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} \\
\frac{\rho}{1+(k+1)\rho} & \frac{\rho}{1+(k+1)\rho} & \dots & \frac{\rho}{1+(k+1)\rho} & \frac{1+(k+2)\rho}{1+(k+1)\rho}
\end{array}\right).\) (27)


## B Likelihood tion

### B.1 SE(3)-Invariance and Chirality of Frame-Distance Likelihood

The potential in eq. (7) has distance and chiral components--both of which are translation invariant. It remains to be shown that the chiral component is invariant to rotations but not reflections.

Suppose we have a protein’s three-dimensional C-\(\alpha\) coordinates **x**. It can be converted into a set of frames \(\{(\mathbf{R}_i,\mathbf{t}_i)\}_{i=1}^L\) via Alg. 2. Note that the positions for the N and C atoms are fixed, given the rigid body assumption, and are determined based on the adjacent C-\(\alpha\) coordinates. We consider the case of a reflected protein **x**<sub>ref</sub>:=-**x** and a rotated protein \(\mathbf{x}_\mathrm{rot}:=\mathbf{R}_\theta\mathbf{x}\). Under the Gram-Schmidt process, we get the frame representations

\(\mathbf{x}_{\mathrm{ref},i}\mapsto\left(\mathbf{R}_i\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right),-\mathbf{t}_i\right),\mathbf{x}_{\mathrm{rot},i}\mapsto\left(\mathbf{R}_\theta\mathbf{R}_i,\mathbf{R}_\theta\mathbf{t}_i\right).\)

First, the pairwise deviations between each residue are computed. For a pair (_i,j_), we have

\(\mathbf{R}(\mathbf{x}_{\mathrm{ref},i})^\top\mathbf{R}(\mathbf{x}_{\mathrm{ref},j})=\left(\mathbf{R}_i\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)\right)^\top\mathbf{R}_j\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)\mathbf{R}_i^\top\mathbf{R}_j\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right),\)<br>
\(\mathbf{R}(\mathbf{x}_{\mathrm{rot},i})^\top\mathbf{R}(\mathbf{x}_{\mathrm{rot},j})=\left(\mathbf{R}_\theta\mathbf{R}_i\right)^\top\mathbf{R}_\theta\mathbf{R}_j=\mathbf{R}_i^\top\mathbf{R}_\theta^\top\mathbf{R}_\theta\mathbf{R}_j=\mathbf{R}_i^\top\mathbf{R}_j,\)

which shows that such a deviation, and therefore the chiral component as a whole, is invariant to rotations. We remark that this expression is different from \(\mathbf{R}_i\mathbf{R}_j^\top\), the rotation matrix that transforms the _j_th frame’s orientation to that of the _i_th frame. Next, the cosine of the deviations’ angles are computed. In the reflection case, we have

\(d_\mathrm{cos}(\mathbf{R}_i^\top\mathbf{R}_j,\mathbf{R}(\mathbf{x}_{\mathrm{ref},i})^\top\mathbf{R}(\mathbf{x}_{\mathrm{ref},j}))=\frac{1}{2}\left(\mathrm{Tr}\left(\mathbf{R}_i^\top\mathbf{R}_j\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)\mathbf{R}_j^\top\mathbf{R}_i\left(\begin{array}{ c c }
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)\right)-1\right).\)

Setting \(\mathbf{V}=\mathbf{R}_i^\top\mathbf{R}_j\) and expanding the expression, we have

\(=\frac{1}{2}\left(\mathrm{Tr}(\mathbf{V}\mathbf{V}^\top)-2(v_{13}^2+v_{23}^2+v_{31}^2+v_{32}^2)-1\right)\)<br>
\(=1-(v_{13}^2+v_{23}^2+v_{31}^2+v_{32}^2),\)

where we have used the fact that \(\mathrm{Tr}(\mathbf{V}\mathbf{V}^\top)=\mathrm{Tr}(\mathbf{I})=3\) for rotation matrix **V**. For the above to be equal to one, i.e. the cosine of zero, we must have _v_<sub>13</sub>=_v_<sub>23</sub>=_v_<sub>31</sub>=_v_<sub>32</sub>=0 which precisely requires \(\mathbf{R}_i^\top\mathbf{R}_j\) to be a rotation matrix strictly about the _z_-axis--which is not true in general. Hence, the orientation component is not generally reflection-invariant.


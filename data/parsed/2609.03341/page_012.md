## Quantitative Evaluation.

Due to the lack of ground truth, we use VBench \[6\] to quantitatively evaluate the editing quality of our method and GSTex. VBench is a benchmark suite that assesses generated videos along several dimensions, and is now widely used for video quality evaluation in general \[7, 33\]. Specifically, for each of the five scenes in Fig. 4, we render a 360\(^\circ\) orbit video in which the edited texture is shown while the geometry is animated over the video’s time span using their artist-created motions. As shown in  1, our method either outperforms or matches GSTex across all five dimensions.

\begin{tabular}{cccccc}
Method & subject consistency & bkg consistency & motion smooth & aesthetic quality & imaging quality \\
GSTex & 0.827 & 0.923 & **0.985** & 0.434 & 0.520 \\
Ours & **0.844** & **0.925** & 0.982 & **0.437** & **0.585** \\
\(\Delta\)% & +2.16 & +0.24 & -0.40 & +0.55 & +12.48 \\
\end{tabular}

Original Scene and Edited Texture Map
Texture Edited (Ours)
UV under Deformation
Texture + Geometry Edited (Ours)
Texture + Geometry Edited (GSTex)
emperor-fish
blossom
dress
flag
rexy

**Fig.4:** Simultaneous geometry and texture editing under non-rigid deformation with both local and global texture edits.

** 1:** VBench evaluation for Figure 4. \(\Delta\)% is the relative improvement.


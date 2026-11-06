<tbc>When instantiated with the AlexNet backbone, LPIPS captures how well the overall, large-scale structure of the recovered image matches the original, placing greater emphasis on shapes, strokes, and contours than on fine-grained texture differences. This makes it better suited for inscription restoration than the VGG-based LPIPS variant, whose deeper architecture is more sensitive to subtle texture and contrast patterns. Nevertheless, for completeness, next we also report results using the VGG-based LPIPS metric.

8 and Figure 13 report the performance of our method, which is substantially better than training-free alternatives such as Deep Image Prior variants. As noted above, LPIPS is a perceptual metric that leverages pre-trained CNN features to compare the feature spaces of two images; in this VGG-based variant, higher importance is assigned to fine-grained differences between the original and recovered images (with lower values indicating better similarity). This metric therefore penalizes minor artifacts that are not critical for letter and texture readability.

Our primary objective is to recover the global structure and shapes of damaged letters and words, rather than to perfectly reproduce all low-level texture details, which lie somewhat outside the core scope of text restoration. Nonetheless, our method still achieves competitive VGG-based LPIPS scores, even for subtle details, and these could be further improved through multiple passes of our method, complementary techniques, or manual post-processing.

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Average** \\
DIP-DENOISE TF & 0.2238 & 0.3568 & 0.3318 & 0.3041 \\
DIP-INPAINTING TF & 0.1427 & 0.2507 & 0.1672 & 0.1869 \\
DNCNN TN & 0.0577 & 0.1083 & 0.2342 & 0.1334 \\
DNCNN TS & 0.0834 & 0.1382 & 0.1142 & 0.1119 \\
DRUNET TN & 0.1284 & 0.1486 & 0.1007 & 0.1259 \\
DRUNET TS & 0.2341 & 0.1528 & 0.1229 & 0.1699 \\
ESRGAN TN & 0.0545 & 0.1076 & 0.0974 & 0.0865 \\
ESRGAN TS & 0.0782 & 0.1257 & 0.1222 & 0.1087 \\
MESA TF & 0.1214 & 0.1725 & 0.1343 & 0.1428 \\
\end{tabular}

8. LPIPS VGG Network used per method across datasets and their averages.


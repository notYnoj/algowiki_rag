<tbc>our method outperforms existing homography transformation techniques in terms of both mean Peak Signal-to-Noise Ratio (mPSNR) and visual quality.

## 4.4 . Ablation Study

To validate the importance of each module in our proposed method, particularly the structure estimation branch<tbc>

<tbc>(SEB) and the structure-texture fusion module (STF), we design four different network architectures on the SCI1KW dataset and conduct ablation experiments in both in-scale and out-of-scale scenarios. In the experiments, we first explore the importance of the SEB module. To do this, we remove the SEB module from the model framework and perform feature fusion using direct upsampling of features. As shown in  3, the use of the SEB module significantly improves performance metrics in both in-scale and out-of- scale cases, indicating that the SEB plays a crucial role in feature aggregation and information extraction. Next, we assess the effectiveness of the STF module. In this experiment, we directly combine the features from the Structure Estimation Branch and the Texture Estimation Branch before decoding. The results demonstrate that removing the STF module leads to a substantial decline in all performance metrics, highlighting its significance in detail reconstruction and visual quality enhancement.

When both the SEB and STF modules are absent, the model performs the worst, further validating the synergistic and essential roles of these two modules in our framework. These experimental results clearly indicate that our<tbc>

\begin{tabular}{ccccccc}
\multirow{2}{*}{TEB} & \multirow{2}{*}{SEB} & \multirow{2}{*}{STF} & \multirow{2}{*}{B-splines} & \multirow{2}{*}{Fourier} & \multicolumn{2}{c}{SCI1KW} \\
 & & & & & isc & osc \\
\(\unknown\) & \<|unk|\> & \<|unk|\> & \(\unknown\) & \<|unk|\> & 36.65 & 29.01 \\
\(\unknown\) & \<|unk|\> & \(\unknown\) & \(\unknown\) & \<|unk|\> & 36.80 & 29.14 \\
\(\unknown\) & \(\unknown\) & \<|unk|\> & \(\unknown\) & \<|unk|\> & 36.79 & 29.10 \\
\(\unknown\) & \(\unknown\) & \(\unknown\) & \<|unk|\> & \(\unknown\) & 36.83 & 29.13 \\
\(\unknown\) & \(\unknown\) & \(\unknown\) & \(\unknown\) & \<|unk|\> & **36.97** & **29.29** \\
\end{tabular}


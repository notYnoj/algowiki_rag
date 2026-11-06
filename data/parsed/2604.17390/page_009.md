<tbc>where _L_ is the number of layers that contribute to the loss. The final total loss is then computed as a weighted sum defined as

\(\mathcal{L}_\text{total}=\sum_{l=1}^Lweight_lL_l^\text{Min}.\)

where \(L_l^\text{Min}\) is the layer’s min exemplar loss as described above.

Thus, we employ a novel, data-driven, statistically informed weighting scheme that ensures that the loss contribution of each layer is proportional to how well its filter width aligns with the statistical distribution of letter widths in our dataset.

### 3.4 A Roadmap for Inscription Texture Restoration

Each method is shown to perform better in specific scenarios.

MESA is a training-free method for inscription restoration, relying solely on pre-trained generic deep learning feature extractors (e.g., from a VGG19 network) rather than requiring new training on inscription-specific data.

Histogram of Letter Widths with Fitted Best Distribution
Fitted norm Distribution
0.05
0.04
0.03
Density
0.02
0.01
0.00
0
20
40
60
80
100
120
Width

Histogram of Letter Widths with Fitted Best Distribution
0.05
Fitted cauchy Distribution
0.04
0.03
Density
0.02
0.01
0.00
0
25
50
75
100
125
150
Width

Histogram of Letter Widths with Fitted Best Distribution
0.05
Fitted rayleigh Distribution
0.04
0.03
Density
0.02
0.01
0.00
0
20
40
60
80
100
120
Width

(a) Dataset A

(b) Dataset B

(c) Dataset C

Fig. 4. Best-fit distributions of letter widths for the three datasets used in our experiments.


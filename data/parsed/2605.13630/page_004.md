they continue to grow together. In our setting, this concept is translated into the coexistence of two or more types of cells, each associated with a different genome, within a single automaton. Such grafted textures can be obtained by initializing, either at timestamp 0 or at a random timestamp, a subset of cells with the seed values corresponding to a different genome. This initialization allows multiple textures to coexist and interact within the same automaton, leading to visually interesting results, which are presented in the following section.

Cells associated with different genomes can be arranged in various spatial configurations, such as concentric circles, stripes, or other patterns. An example of a texture generated as a combination of concentric stripes from two textures is shown in Fig. 3.

To achieve a smooth transition between the two textures, the genome channels of the cells located at the boundary between them are initialized with intermediate values. For instance, if genome _q_<sub>1</sub>=(0,0,0) and genome _q_<sub>2</sub>=(0,0,1), the cells along the interface between the two textures are initialized with values of the form (0,0_,x_), where \(0\le x\le 1\). In Fig. 3, blue corresponds to cells with value 0, yellow to cells with value 1, and intermediate shades represent intermediate values in the last genome channel. The corresponding grafting procedure is summarized in Algorithm 2.

**Algorithm 2** Grafting inference

**Require:** _nca_ - nca model with associated hyperparameters, _h,w_ - height and width of expected texture, _g_<sub>0</sub> - expected genome index for the left half of the texture, _g_<sub>1</sub> - expected genome index for the right half of the texture, _t\.max_ - timestamp at which to extract the generated texture.

**Ensure:** The grafted texture (RGB image) at timestamp _t\.max_.

1: \(left\text{\textit{t}}\text{\textit{seed}}\Leftarrow seed\text{\textit{of}}\text{\textit{genome}}(h,w/2,g_0)\)

2: \(right\text{\textit{t}}\text{\textit{seed}}\Leftarrow seed\text{\textit{of}}\text{\textit{genome}}(h,w/2,g_1)\)

3: \(texture\Leftarrow concat(left\text{\textit{t}}\text{\textit{seed}},right\text{\textit{seed}},dim=1)\)

4: **for** \(t\in range(0,t\text{\textit{\unknown}})\) **do**

5: \(texture\Leftarrow nca(texture)\)

6: **end for**

7: **return** _texture<sub>RGB</sub>_

There is no need to train the NCA separately for grafting. The NCA trained on multiple textures, as presented in \[13\], can be directly used at inference. In Algorithm 2, the seeds of the desired textures are generated in lines 1 and 2, and the input texture is constructed in line 3 by concatenating the seeds in the desired configuration, in our example, a circular arrangement. The NCA is then evolved for _t<sub>max</sub>_ steps (lines 4-6), and the resulting grafted texture is returned (line 7).

## 3. RESULTS AND DISCUSSIONS

In this section, we present and discuss the results of the methods and algorithms described in the previous section. The examples utilize an NCA trained on sets of 4 or 8 textures, as those illustrated in Fig. 2. Furthermore, these algorithms are applicable to NCAs trained on any number of textures, provided the total count is a power of two, a constraint imposed by the binary representation of the genomes. Moreover, the model supports variable texture sizes, demonstrating significant flexibility.

### 3.1. Qualitative and quantitative assessment

Regeneration experiments were conducted to evaluate whether the automaton trained using Algorithm 1 can consistently inpainted damaged regions. Regeneration and inpainting behaviors have been studied in various NCA architectures \[18, 19, 20\], and the inpainting task is also addressed by other texture synthesis models \[21\]. Our experimental results highlight that the rich genomic representation leads to successful regeneration. Notably, all NCAs trained with our adapted methodology exhibited enhanced regeneration capabilities. Fig. 4 compares the regeneration performance before and after applying the training adjustments detailed in Algorithm 1.

Quantitative results for the NCA trained with Algorithm 1 are provided in s 1 and 2. To enable a direct comparison, we re-evaluated the baseline from \[13\] using our own implementation of the Structural Similarity (SSIM), Learned Perceptual Image Patch Similarity (LPIPS), and Gram Matrix Distance (GMD) metrics, ensuring a standardized benchmark for all comparisons.

As shown in  1, which presents results for 20 instances per genome, the regeneration-adapted NCA performs competitively with the baseline, indicating that the adaptation process does not degrade generative performance. How<tbc>

\begin{tabular}{cccc}
Model & GDM \(\uparrow\) & LPIPS \(\downarrow\) & SSIM \(\downarrow\) \\ Baseline NCA & 2.839138 & 0.475461 & 0.07361 \\ Regeneration NCA & 2.848067 & 0.476379 & 0.07393 \\ \end{tabular}

500
1.00
400
0.90
300
0.75
0.60
200
0.45
0.30
100
0.15
0
0
100
200
300
400
500
0.00

1.00
0.90
0.75
0.60
200
0.45
0.30
100
0.15
0
0
100
200
300
400
500
0.00

(a)

(b)

(c)

**Fig. 3**. Grafting the NCA trained on 8 textures. Initialization example with genomes _g_<sub>0</sub>=(0,0,0), _g_<sub>1</sub>=(0,0,1). (a) Initialization of the last genome channel. Yellow represents genome _g_<sub>0</sub>, while blue represents genome _g_<sub>1</sub>. (b) Comparison of the channel initialization with the evolution of the NCA at timestamp 30. (c) The state of the NCA at timestamp 110

** 1**. Quantitative assessment of texture generation at step 300.


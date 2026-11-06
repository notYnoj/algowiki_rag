## 4 Experiments & Results

We conducted experiments on three different inscription datasets. Each dataset is divided into scratched and noise subsets. These datasets are used in our method both as clean exemplars and as ground-truth images for supervised baseline methods, which require paired ruined and clean images for training (see Figures 16, 17, and 18). In addition, synthetic datasets of ruined inscriptions, affected by either noise or scratches (see the aforementioned figures with ruined segments), are generated for the training phase of these supervised methods, ensuring a fair comparison.

### 4.1 Metrics

Some well-known metrics that we used to evaluate our method are PSNR\[11\], SSIM\[25\], and LPIPS\[30\]. Peak Signal-to-Noise Ratio (PSNR) measures how close the pixels of the restored inscription are to those of the ground- truth image. Moreover, the Structural Similarity Index (SSIM) between two images captures perceptual aspects such as luminance, contrast, and structural information. On the other hand, a metric that is closer to human visual judgment is the Learned Perceptual Image Patch Similarity (LPIPS), a deep learning-based perceptual measure that uses correlations of deep neural network features to compute a similarity score.

Another metric that we employ, both for evaluating our method and for making the newly proposed metrics presented below more interpretable and their assessment more comprehensive, is the Levenshtein distance \[13\]. This metric measures the minimum number of character-level operations required to transform the recovered text into the original text.

Our work additionally contributes to the field of text restoration by introducing two new metrics which can be combined with image quality metrics bounded to \[0,1\] (e.g. SSIM, PSNR, etc). The first is called Text Recovery Score (TRS) which uses a Normalized Edit Distance which fixes the normalization denominator at 100 edits. To prevent values greater than 1 we cap the score at 1. This produces a bounded metric in the interval \[0,1\] ensuring that very long or highly corrupted texts do not dominate the evaluation. Formally:

\(\text{TextRecoveryScore}(o,r)=1-min\left(1,\frac{LD(o,r)}{S}\right)\) (5)

\begin{tabular}{ccc}
**Method** & **Training Strategy** & **Description** \\
**MESA** & Multi-exemplar, Per-input Optimization, Training Free & Multi-exemplar style-aware method without pretraining; ideal for inscription restoration when paired data are unavailable (e.g., denoising, inpainting). \\
**Deep Image Prior (DIP)** & Self-supervised (single image), Per-input optimization, Training Free & Learns directly from a single corrupted image; effective for denoising, inpainting when dataset is not available. \\
**DRUNET** & Supervised (pretrained) & Requires dataset pretraining; robust for general restoration (denoising, deblurring, artifact removal). \\
**DNCNN** & Supervised (pretrained) & CNN trained on large datasets; is highly effective for Gaussian denoising and overall noise removal. \\
**ESRGAN (generator part)** & Supervised (pretrained) & Trained on damaged/ground truth paired inscription images; best for super-resolution and perceptual enhancement while in this work we use only the generator part of it. \\
\end{tabular}

1. Comparison of image restoration methods regarding training strategy and suitable use cases.


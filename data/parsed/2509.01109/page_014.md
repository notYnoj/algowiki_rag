The Gaussian calibration algorithm is described in Sec. 3.2 of the main paper. It is used to refine the predicted Gaussians during the layout synthesis phase. The algorithm is summarized in Algorithm 2.

Input: predicted Gaussian parameters {g<sub>0</sub>, \(\cdots,\mathbf{g}_{l-1}\}\); minimal size of region s<sub>min</sub>;<br>
image size \(W\times H\).<br>
Output: calibrated Gaussian parameters {g<sub>0</sub><sup>cal</sup>, \(\cdots,\mathbf{g}_{l-1}^{cal}\}\).<br>
// step 1: calibrate the means \((\mu_x,\mu_y)\)<br>
Let \(\Delta x=\Delta y=s_\mathrm{min}\);<br>
Define grid G as all points in \([0,W-1]\times[0,H-1]\) spaced by \((\Delta x,\Delta y)\);<br>
Quantize each mean \((\mu_x^{(i)},\mu_y^{(i)})\in\mathbf{g}_i\) to the nearest central point in G, obtaining \((\hat{\mu}_x^{(i)},\hat{\mu}_y^{(i)})\);<br>
// step 2: re-initialize sigmas via region partitioning<br>
Initialize region list L={(0,W,0,H)};<br>
while |L|\<l do<br>
   Let m<sub>i</sub> be the count of quantized means in region \(I_i\in L\);<br>
   Let \(\hat{L}=\{I_i\in L|\text{at least one side of}I_i\text{is greater than}s_\mathrm{min}\}\);<br>
   Let \(I_\mathrm{max}=\mathrm{arg}\mathrm{max}_{I_i\in\hat{L}}m_i\);<br>
   Let \(x1,x2,y1,y2\leftarrow I_\mathrm{max}\) and \((\hat{w},\hat{h})=(x2-x1,y2-y1)\);<br>
   if \(\hat{w}>\hat{h}\) then<br>
   Replace I<sub>max</sub> in L with its two equal sub-regions split vertically along the x-axis;<br>
   elif \(\hat{w}<\hat{h}\) then<br>
   Replace I<sub>max</sub> in L with its two equal sub-regions split horizontally along the y-axis;<br>
   else<br>
   if no Gaussian falls exactly on the split line x=(x<sub>1</sub>+x<sub>2</sub>)/2 then<br>
   Replace I<sub>max</sub> in L with its two equal sub-regions split vertically along the x-axis;<br>
   else<br>
   Replace I<sub>max</sub> in L with its two equal sub-regions split horizontally along the y-axis;<br>
   end<br>
   end<br>
end<br>
Obtain size (w<sub>i</sub>,h<sub>i</sub>) and center (x<sub>i</sub>,y<sub>i</sub>) for each region \(I_i\in L\);<br>
Compute \(\mathbf{g}_i^{cal}=\{\sigma_x^{cal-(i)},\sigma_y^{cal-(i)},\rho^{cal-(i)},\mu_x^{cal-(i)},\mu_y^{cal-(i)}\}=\big\{\frac{w_i}{6},\frac{h_i}{6},0,x_i,y_i\big\}\).

## B Experimental Settings

**Training and Inference Settings.** For the _image reconstruction task_, we train the encoder-decoder framework for 1M steps with a batch size of 96. The model is first trained using only the reconstruction loss L<sub>rec</sub> for the initial 600K steps. Subsequently, the perceptual loss L<sub>perc</sub> and adversarial loss L<sub>adv</sub> \[11\] are incorporated for the remaining 400K steps to enhance texture details. We use the Adam optimizer \[19\] with a fixed learning rate of \(5\times 10^{-5}\). Additionally, we apply an exponential moving average (EMA) with a decay rate of 0.9999 to stabilize the training process. We set s=5 for Eq. 2 (in the main paper), \(\lambda=2.5\) for Eq. 4 (in the main paper) and s<sub>min</sub>=4 for Algorithm 1.

For the _image generation task_, we adopt the velocity matching loss from SiT \[23\] and train the layout and conditional texture generators sequentially. Specifically, the layout synthesis model is trained for 500K iterations, and the conditional layout-to-texture generation model for 4M iterations. To mitigate overfitting to the conditions, we add 0.5 Gaussian noise to the condition during training of the conditional texture generator. Both models are trained with a batch size of 256 and a learning rate of \(1\times 10^{-4}\) using the Adam optimizer. All experiments are conducted on eight A100 GPUs. During inference, we use a 5-step ODE sampler \[23\] to predict **g**<sup>init</sup>, followed by a 250-step SDE sampler \[23\], as used in SiT \[23\], for texture synthesis. We set the classifier-free guidance strength \[14\] to 1.5, following common practice. We set s<sub>min</sub>=4 for Algorithm 2.

**Network Architecture.** In the _image reconstruction task_, the encoder architecture comprises two residual blocks for extracting image features, followed by 30 transformation blocks designed to process initial Gaussian parameters and extract textual features for each region. During the rendering<tbc>

**Algorithm 2:** Gaussian Calibration Algorithm


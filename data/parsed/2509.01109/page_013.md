**Appendix**

In this appendix, we provide the following materials:

**A** Spatially-adaptive token initialization and Gaussian calibration algorithms (referring to Sec. 3.2 and Sec. 3.3 of the main paper);

**B** Experimental settings for reconstruction and generation (referring to Sec. 4.1 of the main paper);

**C** Generalization on higher resolutions and other datasets (referring to Sec. 4.2 of the main paper);

**D** FLOPs, memory and latency in reconstruction (referring to Sec. 4.2 of the main paper);

**E** Ablation studies on architecture designs and parameters (referring to Sec. 4.2 of the main paper);

**F** Training and inference efficiency of GPSToken generators (referring to Sec. 4.3 of the main paper);

**G** More visual comparisons and results on reconstruction and generative tasks (referring to Sec. 4.2 and Sec. 4.3 of the main paper);

**H** Broader impacts of GPSToken and its generator.

## A Spatially-adaptive Token Initialization and Gaussian Calibration

The spatially-adaptive token initialization algorithm is described in Sec. 3.1 of the main paper. It outlines a procedure for segmenting the entire image based on regional complexity and for initializing the Gaussian parameters of the GPS-tokens accordingly. The algorithm is summarized in Algorithm 1.

Input: image I; target token count l; metric hyper-parameter \(\lambda\); minimal size of region s<sub>min</sub>.<br>
Output: regions list L; initialized Gaussian parameters \(\{\mathbf{g}_0^{init},\cdots,\mathbf{g}_{l-1}^{init}\}\).<br>
Initialize region candidate list L={I};<br>
while |L|\<l do<br>
   Calculate complexities \(\{m_0,\cdots,m_{|L|-1}\}\) for regions in L using Eq. 4 in the main paper;<br>
   Let \(\hat{L}=\{I_i\in L|\text{at least one side of}I_i\text{is greater than}s_\mathrm{min}\}\);<br>
   Let \(I_\mathrm{max}=\mathrm{argmax}_{I_i\in\hat{L}}m_i\);<br>
   Obtain size (w,h) of I<sub>max</sub>;<br>
   if \(w\neq h\) then<br>
   Equally divide I<sub>max</sub> into two sub-regions I<sub>1</sub> and I<sub>2</sub> along the longer side;<br>
   Update L by replacing I<sub>max</sub> with {I<sub>1</sub>,I<sub>2</sub>};<br>
   else<br>
   // step1: width-wise division -\> compute complexities<br>
   Divide I<sub>max</sub> into I<sub>1</sub>,I<sub>2</sub> along width;<br>
   Calculate complexities m<sub>1</sub>,m<sub>2</sub> for I<sub>1</sub>,I<sub>2</sub> using Eq. 4 in the main paper;<br>
   // step2: hidh-wise division -\> compute complexities<br>
   Divide I<sub>max</sub> into I<sub>3</sub>,I<sub>4</sub> along height;<br>
   Calculate complexities m<sub>3</sub>,m<sub>4</sub> for I<sub>3</sub>,I<sub>4</sub> using Eq. 4 in the main paper;<br>
   // step3: compare the complexities<br>
   if \(\mathrm{min}(m_1,m_2)\le\mathrm{min}(m_3,m_4)\) then<br>
Update<br>
L<br>
by<br>
replacing<br>
_I_<br>
max<br>
with<br>
{<br>
_I_<br>
<sub>1</sub><br>
_,I_<br>
<sub>2</sub><br>
}<br>
;<br>
   else<br>
Update<br>
L<br>
by<br>
replacing<br>
_I_<br>
max<br>
with<br>
{<br>
_I_<br>
<sub>3</sub><br>
_,I_<br>
<sub>4</sub><br>
}<br>
;<br>
   end<br>
   end<br>
end<br>
Obtain size (w<sub>i</sub>,h<sub>i</sub>) and center (x<sub>i</sub>,y<sub>i</sub>) for each region \(I_i\in L\);<br>
Initialize \(\mathbf{g}_i^{init}=\{\sigma_x^{(i)},\sigma_y^{(i)},\rho^{(i)},\mu_x^{(i)},\mu_y^{(i)}\}=\big\{\frac{w_i}{6},\frac{h_i}{6},0,x_i,y_i\big\}\).

**Algorithm 1:** Spatially-adaptive Token Initialization Algorithm


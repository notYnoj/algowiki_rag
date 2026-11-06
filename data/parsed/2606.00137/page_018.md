\begin{tabular}{cccccc}
**Methods** & **Model Type** & **Guidance** & **Training Strategy** & **Generation Strategy** & **Texture Type** \\
TextureFields \[OMN\*19\] & Neural fields & Uncond./Image & Custom & Feed-forward & RGB textures \\
NMR \[KUH18\] & VGG & Image & Pre-trained & Optimization & RGB textures \\
Huang _et al._ \[HTD\*20\] & GAN & Image & Custom & Optimization & RGB textures \\
LTG \[YDPT21\] & GAN & Unconditional & Custom & Feed-forward & RGB textures \\
Texturify \[STM\*22\] & GAN & Unconditional & Custom & Feed-forward & RGB textures \\
Mesh2Tex \[BTD23\] & GAN+Neu. fields & Uncond./Image & Custom & Feed-forward+Opt. & RGB textures \\
ShaDDR \[CCZZ23\] & GAN & 3D shape & Custom & Feed-forward & RGB textures \\
3StyleNet \[YGS\*21\] & GAN & 3D shape & Pre-trained+Custom & Optimization & RGB textures \\
SPSG \[DST\*21\] & GAN & Image & Custom & Feed-forward & RGB textures \\
AUV-Net \[CYF22\] & GAN & Uncond./Image/3D shape & Custom & Feed-forward+Opt. & RGB textures \\
Chaudhuri _et al._ \[CSST21\] & VAE+GAN & Uncond./Image & Pre-trained+Custom & Feed-forward & RGB textures \\
Lazova _et al._ \[LIPM19\] & GAN & Image & Custom & Feed-forward & RGB textures \\
Grigorev _et al._ \[GSVL19\] & GAN & Image & Custom & Feed-forward & RGB textures \\
Neverova _et al._ \[NGK19\] & GAN & Image & Custom & Feed-forward & RGB textures \\
UV-GAN \[DCX\*18\] & GAN & Image & Custom & Feed-forward & RGB textures \\
Dream Fields \[JMB\*22\] & CLIP & Text & Pre-trained+Custom & Optimization & RGB textures \\
Text2Mesh \[MBOL\*22\] & CLIP & Text & Pre-trained+Custom & Optimization & RGB textures \\
X-Mesh \[MZS\*23\] & CLIP & Text & Pre-trained+Custom & Optimization & RGB textures \\
TANGO \[CCL\*22\] & CLIP & Text & Pre-trained+Custom & Optimization & PBR materials \\
CLIP-Mesh \[KXBP22\] & CLIP & Text & Pre-trained & Optimization & RGB textures \\
TEXTure \[RMA\*23\] & Diffusion (2D) & Text & Pre-trained & Iterative & RGB textures \\
Text2Tex \[CSL\*23\] & Diffusion (2D) & Text & Pre-trained & Iterative & RGB textures \\
TexFusion \[CKF\*23\] & Diffusion (2D)+Neu. fields & Text & Pre-trained+Custom & Synchronized + Opt. & RGB textures \\
Paint3D \[ZCQ\*24\] & Diffusion (2D+UV) & Text/Image & Pre-trained+Custom & Iterative (+UV refine) & RGB textures \\
SyncMVD \[LXLW24\] & Diffusion (2D) & Text & Pre-trained & Synchronized & RGB textures \\
MVPaint \[CMZ\*25\] & Diffusion (2D+UV) & Text & Pre-trained+Custom & Synchronized (+refine) & RGB textures \\
TexPainter \[ZPZ\*24\] & Diffusion (2D) & Text & Pre-trained & Synchronized+Opt. & RGB textures \\
VCD-Texture \[LYC\*24\] & Diffusion (2D) & Text & Pre-trained & Synchronized (+refine) & RGB textures \\
TexGen \[HGZ\*24\] & Diffusion (2D) & Text & Pre-trained & Synchronized & RGB textures \\
GenesisTex \[GJL\*24\] & Diffusion (2D) & Text & Pre-trained & Synchronized (+refine) & RGB textures \\
GenesisTex2 \[LZZ\*25\] & Diffusion (2D) & Text & Pre-trained & Synchronized & RGB textures \\
FlexiTex \[JYZ\*25\] & Diffusion (2D) & Text/Image & Pre-trained & Synchronized & RGB textures \\
RoomPainter \[HYC\*25\] & Diffusion (2D) & Text & Pre-trained & Synchronized & RGB textures \\
InstanceTex \[YGC\*24\] & Diffusion (2D)+Neu. fields & Text & Fine-tuned+Custom & Iterative+Opt. & RGB textures \\
RoomTex \[WLX\*24\] & Diffusion (2D) & Text & Pre-trained & Iterative & RGB textures \\
Make-A-Texture \[XGE\*25\] & Diffusion (2D) & Text & Pre-trained & Iterative & RGB textures \\
AlignTex \[ZXW\*25\] & Diffusion (2D) & Image & Fine-tuned & Feed-forward+Sync. & RGB textures \\
TEXGen (700M) \[YYG\*24\] & Diffusion (UV) & Text/Image & Custom & Feed-forward & RGB textures \\
Single-Mesh DM \[MEM24\] & Diffusion (on surface) & Unconditional & Custom & Feed-forward & RGB textures \\
Diffu. Tex. Paint. \[HDAA\*24\] & Diffusion (2D) & Image/Brush & Fine-tuned & Feed-forward (interactive) & RGB textures \\
TextureDreamer \[YHK\*24\] & Diffusion (2D) & Image & Fine-tuned+Custom & Optimization & PBR materials \\
StyleTex \[XZT\*24\] & Diffusion (2D) & Image & Pre-trained & Optimization & RGB textures \\
FlashTex \[DOW\*24\] & Diffusion (2D) & Text & Fine-tuned+Custom & Synchronized+Opt. & RGB textures \\
DreamMat \[ZLX\*24\] & Diffusion (2D) & Text & Fine-tuned+Custom & Optimization & PBR materials \\
MaPa \[ZPX\*24\] & Diffusion (2D) & Text & Fine-tuned+Custom & Optimization & PBR materials \\
Decorate3D \[GZD\*23\] & Diffusion (2D) & Text/Image & Pre-trained+Custom & Optimization & RGB textures \\
3D Paintbrush \[DLAH24\] & Diffusion (2D) & Text & Pre-trained+Custom & Optimization & RGB textures \\
EASI-Tex \[PWMAZ24\] & Diffusion (2D) & Image & Pre-trained & Iterative & RGB textures \\
Paint-it \[YJPMO24\] & Diffusion (2D) & Text & Pre-trained+Custom & Optimization & PBR materials \\
Fantasia3D \[CCJJ23\] & Diffusion (2D) & Text & Pre-trained+Custom & Feed-forward & PBR materials \\
Material Anything \[HWLW25\] & Diffusion (2D+UV) & Text/3D Mesh & Fine-tuned & Feed-forward & RGB textures \\
TexDreamer \[LZT\*24\] & Diffusion (2D/UV) & Text/Image & Fine-tuned & Feed-forward & RGB textures \\
Make-It-Vivid \[TZF\*24\] & Diffusion (2D/UV) & Text & Fine-tuned & Feed-forward & RGB textures \\
FabricDiffusion \[ZWC\*24\] & Diffusion (2D) & Image & Fine-tuned & Feed-forward (UV/tile) & RGB textures \\
TexGarment \[LWG\*25\] & Diffusion (2D/UV) & Text & Fine-tuned+Custom & Feed-forward & RGB textures \\
Point-UV Diffusion \[YDL\*23\] & Diffusion (Point+UV) & Uncond./Text/Image & Custom & Feed-forward & RGB textures \\
SeqTex \[YYS\*25\] & Diffusion (Video+UV) & Text/Image & Fine-tuned & Synchronized & RGB textures \\
RomanTex \[FYY\*25\] & Diffusion (2D) & Image & Fine-tuned & Synchronized & RGB textures \\
MaterialMVP \[HYY\*25a\] & Diffusion (2D) & Image & Fine-tuned & Synchronized & PBR materials \\
CLAY \[ZWZ\*24\] & Diffusion (2D) & Text/Image & Custom & Synchronized & PBR materials \\
VideoMat \[MWL\*25\] & Diffusion (Video+PBR) & Text/Image & Fine-tuned & Synchronized & PBR materials \\
DreamPBR \[XZP\*25\] & Diffusion (2D+PBR) & Text+Multimodal & Fine-tuned+Custom & Feed-forward & PBR materials \\
\end{tabular}

** 1:** _A summary of representative works in **Neural 3D Mesh Texturing**. Each work is characterized by **Model Type** (the neural model or backbone used), **Guidance** (the Stylistic Guidance controlling texture appearance), **Training Strategy** (whether the model is Pre-trained, Fine-tuned, or Custom trained for the texturing task), **Generation Strategy** (how textures are generated: Optimization, Iterative, Synchronized, or Feed-forward), and output **Texture Type** (RGB textures, often with baked-in lighting effects, or disentangled PBR materials)._


### B.2.2 Quantitative Analysis

Additionally, we present the quantitative analysis of the Janus prevention capability of the CaPa. Before the discussion, we acknowledge that directly evaluating multi-view inconsistency is challenging, as traditional metrics often do not capture the specific artifacts introduced by the Janus problem. To circumvent this problem, we assessed the impact of the Janus effect by measuring CLIP similarity between rendered normal maps and texture. We hypothesize that the presence of Janus artifacts leads to a misalignment between the geometry and the texture’s appearance, resulting in a decrease in the CLIP similarity score. Using this assumption, CLIP similarity serves as a proxy metric to evaluate the Janus artifacts assessment.

As shown in  3, with spatially decoupled attention, the average similarity score was 85.37, compared to 81.28 without it. Although the difference is modest, likely due to initial geometry guidance aligning texture and mesh. This result supports that spatially decoupled attention resolves the Janus effect and improves multi-view consistency in generated 3D assets.

### B.3 . Analysis of the Occlusion

In this section, we provide an in-depth analysis of occlusion inpainting to address limitations in our main method and clarify its comparative strengths and weaknesses. While our paper demonstrates the effectiveness of our 3D-aware occlusion inpainting approach across diverse scenarios, there are complex cases that challenge even the most advanced techniques. This supplementary section highlights these edge cases and evaluates the relative performance of three methods: our 3D-aware inpainting, automatic view selection \[5\], and UV ControlNet \[59\]. By examining these approaches, we aim to shed light on the specific strengths and limitations of our method in comparison to alternatives, ultimately guiding future improvements. To explore occlusion handling, we compare (a) our proposed 3D-aware occlusion inpainting, (b) automatic view selection, and (c) UV ControlNet, with an emphasis on texture fidelity, seam visibility, and processing efficiency.

As seen in Figure 13, both our method and automatic view selection exhibit high fidelity and maintain strong texture coherence, effectively blending textures with the surrounding context in most instances. This results in fewer visible seams, a<tbc>

\begin{tabular}{cc}
Method & CLIP (N-I) \(\uparrow\) \\
w/ Spatially Decoupled Attention & **85.37** \\
w/o Spatially Decoupled Attention & 81.28 \\
\end{tabular}

(a)
(b)
(c)

3. Quantitative analysis of Janus Artifacts, measuring a CLIP score between rendered normals and textures across random views.

Figure 13. **Qualitative results for different occlusion inpainting methods**. (a) shows results from our 3D-aware occlusion inpainting method, (b) uses automatic view selection, and (c) employs UV ControlNet.


## APPENDIX

<tbc>Supplementary Material

### .1 Explanation of Comparisons to Neumanifold

As indicated in  5 of NeuManifold paper [78], enhancing rendering quality necessitates a trade-off with rendering speed. Furthermore, antialiasing alone cannot mitigate the loss of geometric detail. As shown in Fig. P, we observe that NeuManifold encounters difficulties in accurately rendering fine structures, such as the ropes on a ship, as depicted in Figure 19 of NeuManifold paper [78].

### .2 Comparisons of 3D Semantic Extraction

We evaluate the accuracy of 3D semantic extraction across six cases, three from the DTU dataset [20] and three from the NeRF 360\(^\circ\) Synthetic dataset [40]. For DTU [20], we compare our approach with GARField [27], which learns an affinity radiance field from multi-level SAM masks [28] to enable open-vocabulary 3D semantic extraction. However, GARField [27] fails to reconstruct the object on NeRF 360\(^\circ\) Synthetic [40]. Consequently, we compare our method with SAM3D [86] on the NeRF 360\(^\circ\) Synthetic dataset [40]. To ensure a fair comparison, the same input mesh is provided to both SAM3D [86] and our method. For all methods, the input semantic prompt is defined by a single click on an image, as shown in Fig. R (a) and (d). As DTU [20] and NeRF 360\(^\circ\) Synthetic [40] lack ground-truth 3D semantic masks, we conduct a user study to quantitatively assess accuracy. For each case, a question is posed to the participants. Based on the provided input click prompt (Fig. R (a) and (d)) and the semantic text description in the question, participants are tasked with selecting the 3D semantic extraction result that best meets the following criteria: "(1) The extracted 3D semantic part most accurately corresponds to the given point prompt and semantic description (text); (2) Multi- view consistency; (3) Completeness: all relevant 3D semantic parts are fully extracted."

The quantitative results are presented in Tab.I, with 25 participants participating in the user study. Over 95% of participants preferred the 3D semantic extraction results produced by our method compared to GARField[27] and SAM3D [86]. Qualitative results are shown in Fig. R. Our approach demonstrates superior performance in extracting local semantic structures, generating more complete and multi-view consistent 3D masks compared to other methods, such as the entire rooftop of the house and the blue body and hands of the Smurfs in Fig. R (c), as well as left and right track of Lego and whole sausage of Hotdog in Fig. R (f).

### .3 Editing Ablations to Neuralanglo

**Geometry Editing.** Neuralangelo [32] itself does not support geometry editing. To empower Neuralangelo [32] with the ability of geometry editing, we apply a naïve mesh- guided field warping solution to Neuralangelo [32]. Since<tbc>

<tbc>the original and the deformed mesh share identical vertex and triangle topologies, we map query points from the deformed space to the canonical space by computing their warping, which is interpolated based on the offsets of the three nearest mesh vertices. As illustrated in the first row of Fig. S, Neuralangelo produces "ghost" geometry when applying large deformation, where the wire moving too far away from the original position makes the query point find the wrong closest mesh vertices for computing warping. In contrast, our mesh-based representation tightly fits the neural field to the mesh surface and the geometry can be synchronously deformed.

**Texture Editing.** Our vertex-bounded design stores the local textures in the mesh vertices that allow users to swap the<tbc>

\begin{tabular}{ccc}
Methods on DTU [20] & Ours & GARField [27] \\
Percent. of Favorite \(\uparrow\) & **96.0%** & 4.0% \\
Methods on NeRF Syn. [40] & Ours & SAM3D [86] \\
Percent. of Favorite \(\uparrow\) & **98.7%** & 1.3% \\
\end{tabular}

NeuManifold
Ours
Ground-truth

Original Rendered Object
Our Front View of Geometry Edited Object
Our Side Views of Geometry Edited Object

TABLE I: **User study of 3D Semantic Extraction**. We show the percent of favorite 3D semantic methods chosen by participants.

Fig. P: **Compare with Neumanifold.** We show the comparison between our method and Neumanifold. Since they do not release the code, we compare our renderings to the figures shown in their paper.

Fig. Q: **Extreme Geometry Editing Cases.** We show our extreme geometry editing results to demonstrate the robustness of our method. We deform different parts of the object to touch each other like two intersecting legs of the chair and the bear’s hand touching the body.


<tbc>We also analyze the runtime of the editing process of our method, where our previous NeuMesh \[83\] is compared as a reference to show our improvement, as shown in Tab. 7. The experiments are conducted on a single Nvidia RTX 3090 GPU with rendering 800\(\times\)800 images. Our method shows more significant efficiency than NeuMesh in texture painting. For geometry editing, our method needs an extra update on the occupancy grid compared to the NeuMesh, which only takes an additional 1 second. For texture swapping and filling, NeuMesh and our method both do not require fine-tuning.

## 4.6 Ablation Studies

We conduct ablation studies on novel view synthesis and editing.<br>
**Architecture.** We ablate the order of MLP calculations and interpolations. As shown in Tab. 2 and Tab. 3, our proposed post-interpolation outperforms pre-interpolation (Ours early interp.). The local coordinates **h**_<sub>k</sub>_ and normal vectors **n**_<sub>k</sub>_ get perturbed during early interpolations and lose fine-grained local information when decoded by MLPs. Besides, we ablate the differences of quality when training with distillation from the teacher model \[32\] and without distillation. As shown in Tab. 5, our method has a comparable or slightly better quality than training with distillation. This demonstrates our method is robust when training only with multi-view images.<br>
**Hyperparameteres.** To find the balance between KNN searching cost and the rendering quality, the ablation on the number of retrieved vertices for the query point is shown in Fig. 10. Since the edge of retrieving more than 4 vertices is minor, we set _K_=4 as the default. As shown in Fig. 13, we evaluate the impact of MLP decoder sizes and neural code dimensions (#Geo.+#Tex.). We choose 64 as the size of the MLP, 6 and 15 as the sizes of the geometry and texture codes, as further increases in size yield diminishing improvements in rendering quality. In order to test the robustness of our model, we half geometry codes \(l_k^g\) and texture codes \(l_k^t\) (Our LITE in Tab. 2) and get close rendering qualities as our full model.<br>
**Editing.** We conduct ablation studies on and editing pipelines. As shown in Tab. 2, our model without normal conditions performs similarly to our full model. However, if normal conditions are eliminated from our model, as depicted in Fig. 11, the delicate view-dependent effect, such as shining gold material would disappear. Ablations on painting effects are also conducted. As shown in Fig. 12, if the modification color **_c_**_<sup>m</sup>_ is not included, the painted results will be noisy.

## 4.7 Hybrid Editing

We further show hybrid editing results combining geometry editing, texture painting and texture filling in Fig. 14, which<tbc>

<tbc>demonstrate versatile editing capabilities of our representation on both real-world and synthetic data. In the synthetic chair scene, we bend the chair’s arms and legs while swap<tbc>

\begin{tabular}{cccc}
Time (sec.) & Geo. Editing\(\downarrow\) & Tex. Swap/Fill\(\downarrow\) & Tex. Painting\(\downarrow\) \\
NeuMesh \[83\] & **0** & **0** & 5492 \\
Ours & 1 & **0** & **1** \\
\end{tabular}

Original scene
Texture source
Ours w/o normal
Ours

Original & Canvas
Ours w/o cm
Ours

Hybrid Editing on Original Object
Our Rendered Edited Objects

TABLE 7: **Editing Time Comparison.** We compare the time of the editing process with the NeuMesh \[83\].

Fig. 11: **Ablation on texture swapping.** We compare different texture-swapping qualities. Models without normal information cannot produce authentic golden reflections based on object geometry.

Fig. 12: **Ablation on painting.** We compare different painting qualities. Model without modification color **_c_**_<sup>m</sup>_ produces noisy results after finetuning for the same iterations compared to our method.

Fig. 14: **Hybrid editing.** We show examples of hybrid object editing by combining multiple editing operations.


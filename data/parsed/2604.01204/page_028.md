<tbc>For a tetrahedron with vertices **v**<sub>1</sub>,**v**<sub>2</sub>,**v**<sub>3</sub>,**v**<sub>4</sub>:

\(V_1=\frac{1}{6}\|(\mathbf{v}_2-\mathbf{p})\times(\mathbf{v}_3-\mathbf{p})\cdot(\mathbf{v}_4-\mathbf{p})\|,\)<br>
\(V_2=\frac{1}{6}\|(\mathbf{v}_3-\mathbf{p})\times(\mathbf{v}_4-\mathbf{p})\cdot(\mathbf{v}_1-\mathbf{p})\|,\)<br>
\(V_3=\frac{1}{6}\|(\mathbf{v}_4-\mathbf{p})\times(\mathbf{v}_1-\mathbf{p})\cdot(\mathbf{v}_2-\mathbf{p})\|,\)<br>
\(V_4=\frac{1}{6}\|(\mathbf{v}_1-\mathbf{p})\times(\mathbf{v}_2-\mathbf{p})\cdot(\mathbf{v}_3-\mathbf{p})\|.\) (6)

## 2.1 Optimization choices and hyperparameters

Tab. 10 ablates the individual contributions of the training strategies described in the main paper (learning rate scheduling, EMA on the MLP weights, loss scaling, color-refinement phase, and opacity and scale regularization). Tab. 12 lists the full set of hyperparameters and optimization details used for radiance field reconstruction.

GT
Ours
GT
Ours

**Fig.3:** LSEG feature PCA visualizations on test views from MipNeRF360. Rows from top to bottom: _bicycle, garden, bonsai, kitchen_. Each pair shows the ground-truth LSEG features (GT) alongside our rendered features (Ours). Our method faithfully reconstructs semantic feature maps while preserving sharp boundaries, at higher resolutions, and real-time.


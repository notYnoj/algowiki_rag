<tbc>are suitable for learning a multi-chart UV atlas and texture map \[20\], we first propose **geometry regularization** losses that condition the ray-surface intersections to accurately reflect the true geometry (Sec. 4.1). Then, to preserve texture attachment during edits, we introduce a **deformation-aware canonical correspondence** mechanism (Sec. 4.3). This explicitly maps the deformed- space intersections reliably back to the original canonical space for consistent UV lookup, ensuring that texture edits persist seamlessly regardless of the applied geometric deformation.

### 4.1 Learning PAPR with Geometry Regularization

To enable reliable UV learning and stable editing, we require accurate and well- conditioned ray-surface intersection points. In PAPR, the predicted surface point for ray _i_ is an attention-weighted average of _K_ ray-nearest neighbors (Eq. 2), which can be sensitive to sparse attention and imperfect point geometry. Without additional constraints, predicted intersection points may _collapse_ toward discrete support points and/or be supported by noisy off-surface neighborhoods (Fig. 6 and 7a), which harms the sampled surface point set used to train the UV atlas. We therefore add two geometry regularizers during PAPR pre-training.

#### On-ray regularizer (close-to-ray).

As shown in Fig. 6, sparse attention weights can cause predicted intersection points to cluster around discrete point supports. This degrades the effective geometric resolution of **x**_<sub>i</sub>_ to the resolution of the point cloud and yields unstable surface samples for UV supervision. Since a valid ray-surface intersection point should lie on its ray by definition, we minimize the distance between each predicted point **x**_<sub>i</sub>_ and its orthogonal projection \(\mathbf{x}'_i\) onto the corresponding ray **r**_<sub>i</sub>_:

\(\mathcal{L}_\mathrm{close2ray}=\frac{1}{M}\sum_{i=1}^M\|\mathbf{x}_i-\mathbf{x}'_i\|_2,\) (5)

where _M_ is the number of rays in a batch.

#### On-surface neighborhood regularizer (close-to-surface).

Even when intersections can be predicted, the underlying point cloud may contain off-surface points. This is problematic when starting from sparse points and densifying: new points may gather around an off-surface location, and a ray may then select a neighborhood whose convex hull does not cover the true surface. To regularize neighborhood geometry, we encourage each selected neighbor point **p**_<sub>ij</sub>_ to move toward the predicted surface point **x**_<sub>i</sub>_:

\(\mathcal{L}_\mathrm{close2surface}=\frac{1}{MK}\sum_{i=1}^M\sum_{j=1}^K\|\mathbf{p}_{ij}-\mathrm{sg}(\mathbf{x}_i)\|_2\) (6)

that encourages all the nearby points to move closer to the predicted intersection point. Note that we stop the gradients backpropagating to **x**_<sub>i</sub>_ from this regularizer for training stability. To prevent early geometry collapse, we apply L<sub>close2surface</sub> in the middle of training after a coarse geometry is learned.


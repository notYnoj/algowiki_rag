\(+\mathrm{i}\left(\mathrm{k}_2\frac{E^3+E^3}{2}-\mathrm{k}_3\frac{E^2+E^2}{2}\right),\)<br>
\((\mathcal{A}E_h)_{i-\frac{1}{2},j,k-\frac{1}{2}}=\frac{E^1-E^1}{h}-\frac{E^3-E^3}{h}\)<br>
\(+\mathrm{i}\left(\mathrm{k}_3\frac{E^1+E^1}{2}-\mathrm{k}_1\frac{E^3-E^3}{2}\right),\)<br>
\((\mathcal{A}E_h)_{i-\frac{1}{2},j-\frac{1}{2},k}=\frac{E^2-E^2}{h}-\frac{E^1-E^1}{h}\)<br>
\(+\mathrm{i}\left(\mathrm{k}_1\frac{E^2+E^2}{2}-\mathrm{k}_2\frac{E^1+E^1}{2}\right).\)

Likewise, for any \(H_h\in\mathcal{F}_h\), the discrete divergence is formulated by

\((\mathcal{B}H_h)_{i-\frac{1}{2},j-\frac{1}{2},k-\frac{1}{2}}=\frac{H^1-H^1}{h}+\frac{H^2-H^2}{h}\)<br>
\(+\frac{H^3-H^3}{h}+\mathrm{i}\left(\mathrm{k}_1\frac{H^1+H^1}{2}\right).\)<br>
\(+\mathrm{k}_2\frac{H^2+H^2}{2}+\mathrm{k}_3\frac{H^3+H^3}{2}\)

The notations of **_E_**_<sub>h</sub>_ and **_H_**_<sub>h</sub>_ are adopted from (2.3). We may formulate the explicit matrix representations through circulant matrix below:

\(\mathbf{D}_1:=\frac{1}{h}\left(\begin{array}{ c c c }
1 &  & -1 \\
-1 & 1 &  \\
 & \ddots &  \\
 &  & -1 \end{array}\right)\in\mathbb{R}^{N\times N},\mathbf{D}_0:=\frac{1}{2}\left(\begin{array}{ c c c }
1 &  & 1 \\
1 & 1 &  \\
 & \ddots &  \\
 &  & 1
\end{array}\right)\in\mathbb{R}^{N\times N}.\) (2.5)

Then directional derivatives combined with actions of **k** can be represented by the following matrix blocks using Kronecker product \(\otimes\) (**_I<sub>N</sub>_** denotes the identity matrix of dimension **_N_**):

\(\mathcal{D}_i=\mathcal{D}_{1,i}+\mathrm{i}\mathrm{k}_i\mathcal{D}_{0,i}i=1,2,3,\text{where}\mathcal{D}_{s,1}=I_{N^2}\otimes\mathbf{D}_s,\mathcal{D}_{s,2}=I_N\otimes\mathbf{D}_s\otimes I_N,\mathcal{D}_{s,3}=\mathbf{D}_s\otimes I_{N^2},s=1,2.\) (2.6)

Therefore the matrix representations of A and B are given by

\(\mathcal{A}=\left(\begin{array}{ c c c }
 & -\mathcal{D}_3 & \mathcal{D}_2 \\
\mathcal{D}_3 &  & -\mathcal{D}_1 \\
-\mathcal{D}_2 & \mathcal{D}_1 &  \\
\end{array}\right),\mathcal{B}=\left(\mathcal{D}_1\mathcal{D}_2\mathcal{D}_3\right).\) (2.7)


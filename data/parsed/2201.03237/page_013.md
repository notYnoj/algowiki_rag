We illustrate the possibility in combination with Figure 3. First we consider the case in two dimensional space, and the relevant conclusions can be extended to higher dimensional space. Point _A_ is the current point selecting neighbors, where point _C_ is one of existing neighbors, point _B_ is the candidate neighbor. Line _l_’ is the line segment <o>_AC_</o> ’s perpendicular bisector. Line _l_’ intersects the circle with node _B_ as center and _r_ as radius at points _D_ and _E_. \(\varphi=\angle DBE\). Line \(l'_B\) is parallel to line \(l'\) and passes through the point B. We can show that

\(distance(l',B)=distance(l',l'_B)=distance(l'_B,A)-distance(l',A)\)<br>
\(=\Pi_\overrightarrow{AC}\overrightarrow{AB}-\frac{1}{2}\left|\overrightarrow{AC}\right|=\frac{lsin(2\alpha+\theta)}{2sin(\alpha+\theta)}\)

The line _l_’ divides the circle into two parts: upper part and lower part. When the query point _Q_ locates at the upper part, since \(\delta(C,Q)<\delta(A,Q)\), the monotonic search from point _A_ can continue. However, when the query _Q_ locates at the lower part, the monotonic search will fail without the edge \(\overrightarrow{AB}\). That is to say, the probability of achieving monotonous search from node _A_ can be represented as the proportion of the area (volume) of the upper part. In high dimensional space, the line _l_’ is a hyperplane. The circle with point _B_ as center and _r_ as radius becomes a hypersphere. If we set up a cartesian coordinate system _x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>d</sub>_ in _d_ dimensional space with point _B_ as origin and we specify that the positive direction of axis _x_<sub>1</sub> is same as \(\overrightarrow{AC}\). The probability can be represented as

\(\frac{\int_{-rcos\frac{\varphi}{2}}^rdx_1\int_{-\sqrt{r^2-x_1^2}}^\sqrt{r^2-x_1^2}dx_2\dots\int_{-\sqrt{r^2-x_1^2-x_2^2-\dots-x_{d-1}^2}}^\sqrt{r^2-x_1^2-x_2^2-\dots-x_{d-1}^2}dx_d}{\int_{-r}^rdx_1\int_{-\sqrt{r^2-x_1^2}}^\sqrt{r^2-x_1^2}dx_2\dots\int_{-\sqrt{r^2-x_1^2-x_2^2-\dots-x_{d-1}^2}}^\sqrt{r^2-x_1^2-x_2^2-\dots-x_{d-1}^2}dx_d}\) (3)

The probability is difficult to calculate in high dimension, but we prove that it must not be less than \(1-\frac{\varphi}{2\pi}\). Therefore we define<tbc>

\(min\text{\textit{-}}prob=1-\frac{\varphi}{2\pi}=1-\frac{arccos(\frac{l}{r}\frac{sin(2\alpha+\theta)}{2sin(\alpha+\theta)})}{\pi}\) (4)

<tbc>We calculate the probabilities in 2, 3 and 4 dimensional spaces and we can see how they vary with \(\varphi\) in Figure 4. With the increase of dimension, the<tbc>


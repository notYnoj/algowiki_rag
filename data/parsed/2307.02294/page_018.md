of _W_ if _i<sub>L</sub>\>i<sub>R</sub>_. For example, when _i<sub>L</sub>\<i<sub>R</sub>_,

\(W''=\left(\begin{array}{ c c c c c }
 &  &  &  & \bullet \\
 &  &  & \bullet &  \\
 &  &  &  &  \\
 &  & \bullet &  &  \\
 &  &  & \bullet &  \\
 &  &  & \bullet &  \\
 &  &  & \bullet &  \\
 &  &  & \bullet &  \\
 &  &  & \bullet &  \\
 &  &  &  & \bullet
\end{array}\right)\)

It is known \[Pet15a, Niv10\] that \(\mathrm{Ex}(\genfrac(){pt}{2}{\cdot\bullet}{i,j},n,m)=2n\alpha(n,m)\pm O(n+m)\).

## 6 Concluding Remarks

Demaine et al.\[DHI<sup>+</sup>09\] and Pettie \[Pet10\] introduced the idea of representing the behavior of a data structure by a 0-1 matrix in which the axes correspond to _time_ and data structure _elements_. Applying results on forbidden 0-1 matrices in this context is very natural, and has led to sharp or nearly sharp bounds on certain path compression schemes \[Pet10\], structured inputs to binary search trees \[CGK<sup>+</sup>15b, CGK<sup>+</sup>15a, CGJ<sup>+</sup>23, Pet10\], and heaps \[KS20\].

Although the forbidden 0-1 matrix framework is perfectly suited to proving that sorting \(\pi\)-free sequences takes _near-linear_ time, it might be inadequate to establishing an optimal _O<sub>k</sub>(n_) time bound. As we have shown, any \(o(n2^{\alpha(n)})\)-time analysis must use some property _beyond_ \(P_\pi\otimes\left(\bullet\right)\)- freeness. Here it may be useful to consider different ways to decompose a 0-1 matrix; see Guillemot and Marx \[GM14\] and Chalermsook, Gupta, Jiamjitrak, Acosta, Pareek, and Yinghcareonthaworn- chai \[CGJ<sup>+</sup>23\].


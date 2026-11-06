**Lemma 2.2.** \[22, 9\] Let \(\gamma\in(1,2)\). The generating function of \(\{T_N^\gamma\}_{N\in\mathbb{N}}\) in (2.1) is real-valued and even, and its specific form is as follows:

\(f_\gamma(\theta)=-2^{\gamma+1}(\mathrm{sin}\frac{|\theta|}{2})^\gamma\mathrm{cos}(|\theta|(1-\frac{\gamma}{2})+\frac{\gamma\pi}{2}).\) (2.6)

_Proof._ It is noted that the generating function of \(\{T_N^\gamma\}_{N\in\mathbb{N}}\) is<tbc>

\(f_\gamma(\theta)=\sum_{k=-\infty}^\infty f_ke^{\mathbf{i}k\theta},\)

<tbc>where the coefficients are given by<tbc>

\(f_0=-2g_1^{(\gamma)},f_1=f_{-1}=-g_0^{(\gamma)}-g_2^{(\gamma)},f_k=f_{-k}=-g_{k+1}^{(\gamma)},k\ge 2.\)

<tbc>Furthermore, we obtain that<tbc>

\(\sum_{k=-\infty}^\infty f_ke^{\mathbf{i}k\theta}=-\sum_{k=-1}^\infty g_{k+1}^{(\gamma)}e^{\mathbf{i}k\theta}-\sum_{k=-1}^\infty g_{k+1}^{(\gamma)}e^{-\mathbf{i}k\theta}.\)

<tbc>By virtue of the results in \[9\], we have<tbc>

\(-\sum_{k=-1}^\infty g_{k+1}^{(\gamma)}e^{\mathbf{i}k\theta}=-e^{-\mathbf{i}\theta}(1-e^{\mathbf{i}\theta})^\gamma,\)

<tbc>and<tbc>

\(-\sum_{k=-1}^\infty g_{k+1}^{(\gamma)}e^{-\mathbf{i}k\theta}=-e^{\mathbf{i}\theta}(1-e^{-\mathbf{i}\theta})^\gamma.\)

<tbc>Owing to<tbc>

\(1-e^{\mathbf{i}\theta}=\left\{\begin{array}{ c c }
2\left|\mathrm{sin}\frac{\theta}{2}\right|e^{\frac{1}{2}(\theta-\pi)}, & 0\le\theta\le\pi, \\
2\left|\mathrm{sin}\frac{\theta}{2}\right|e^{\frac{1}{2}(\theta+\pi)}, & -\pi\le\theta<0,
\end{array}\right.\text{and}1-e^{-\mathbf{i}\theta}=\left\{\begin{array}{ c c }
2\left|\mathrm{sin}\frac{\theta}{2}\right|e^{-\frac{1}{2}(\theta-\pi)}, & 0\le\theta\le\pi, \\
2\left|\mathrm{sin}\frac{\theta}{2}\right|e^{-\frac{1}{2}(\theta+\pi)}, & -\pi\le\theta<0.
\end{array}\right.\)

<tbc>When \(0\le\theta\le\pi\),

\(f_\gamma(\theta)=-e^{-\mathbf{i}\theta}(1-e^{\mathbf{i}\theta})^\gamma-e^{\mathbf{i}\theta}(1-e^{-\mathbf{i}\theta})^\gamma\)<br>
\(=-e^{-\mathbf{i}\theta} 2^\gamma\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|e^{\frac{\mathrm{i}\gamma}{2}(\theta-\pi)}-e^{\mathbf{i}\theta} 2^\gamma\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|e^{\frac{-\mathrm{i}\gamma}{2}(\theta-\pi)}\)<br>
\(=-2^\gamma\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|\left(e^{\mathbf{i}\left(\theta(\frac{\gamma}{2}-1)-\frac{\pi\gamma}{2}\right)}+e^{\mathbf{i}\left(-\theta(\frac{\gamma}{2}-1)+\frac{\pi\gamma}{2}\right)}\right)\)<br>
\(=-2^{\gamma+1}\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|\mathrm{cos}\left(\theta(1-\frac{\gamma}{2})+\frac{\pi\gamma}{2}\right).\)

When \(-\pi<\theta\le 0\),

\(f_\gamma(\theta)=-2^\gamma\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|\left(e^{\mathbf{i}\left(\theta(\frac{\gamma}{2}-1)+\frac{\pi\gamma}{2}\right)}+e^{\mathbf{i}\left(-\theta(\frac{\gamma}{2}-1)-\frac{\pi\gamma}{2}\right)}\right)\)<br>
\(=-2^{\gamma+1}\left|\mathrm{sin}^\gamma\frac{\theta}{2}\right|\mathrm{cos}\left(-\theta(1-\frac{\gamma}{2})+\frac{\pi\gamma}{2}\right).\)


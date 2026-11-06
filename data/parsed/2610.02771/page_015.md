**Lemma 13** (Estimate Validity via MEDIANEST)**.** _Let X be a random variable with mean_ \(\mu\in[-\lambda,\lambda]\) _and variance proxy_ \(\sigma^2\)_. Let the continuous domain_ \([-\lambda,\lambda]\) _be discretized into a uniform grid with step size_ \(\Delta x=\kappa\cdot\sigma\)_. If the_ MEDIANEST _routine successfully identifies an_ \(\varepsilon'\)_-good interval_ \[_x<sub>i</sub>,x_<sub>_i_+1</sub>\] _for the target_ \(\tau=1/2\)_, then the returned midpoint_ \(\widehat{c}=(x_i+x_{i+1})/2\) _satisfies:_<tbc>

\(|\widehat{c}-\mu|\le\left(\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}+\frac{\kappa}{2}\right)\sigma.\)

<tbc>_Proof._ Because the returned interval is \(\varepsilon'\)-good, the probability range \([Pr(X\le x_i),Pr(X\le x_{i+1})]\) must intersect the target window \((1/2-\varepsilon',1/2+\varepsilon')\). Since cumulative probabilities are non- decreasing, this intersection gives us two conditions:

\(Pr(X\le x_i)<\frac{1}{2}+\varepsilon'\text{and}Pr(X\le x_{i+1})>\frac{1}{2}-\varepsilon'\)

We can use these to bound the tails. The upper tail satisfies \(Pr(X>x_i)=1-Pr(X\le x_i)>1/2-\varepsilon'\), while the lower tail directly satisfies \(Pr(X\le x_{i+1})>1/2-\varepsilon'\). We evaluate the distance from \(\mu\) to the grid step by considering three cases:

**Case 1 (**\(\mu<x_i\)**):** Applying Cantelli’s inequality gives \(Pr(X\ge x_i)\le\frac{\sigma^2}{\sigma^2+(x_i-\mu)^2}\). Combining with our known tail bound, we get:<tbc>

\(\frac{1}{2}-\varepsilon'<Pr(X>x_i)\le Pr(X\ge x_i)\le\frac{\sigma^2}{\sigma^2+(x_i-\mu)^2}\)

<tbc>Solving for the distance yields \(x_i-\mu<\sigma\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}\). Because the returned estimate \(\widehat{c}\) is the midpoint of the grid interval, its distance to the true mean is<tbc>

\(|\widehat{c}-\mu|=\frac{\Delta x}{2}+(x_i-\mu)<\frac{\kappa\sigma}{2}+\sigma\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}.\)

<tbc>**Case 2 (**\(\mu>x_{i+1}\)**):** Applying a symmetric Cantelli bound gives \(Pr(X\le x_{i+1})\le\frac{\sigma^2}{\sigma^2+(\mu-x_{i+1})^2}\). Combining with our lower tail condition, we have:<tbc>

\(\frac{1}{2}-\varepsilon'<Pr(X\le x_{i+1})\le\frac{\sigma^2}{\sigma^2+(\mu-x_{i+1})^2}\)

<tbc>Rearranging the inequality yields \(\mu-x_{i+1}<\sigma\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}\). The distance from the midpoint is

\(|\widehat{c}-\mu|=(\mu-x_{i+1})+\frac{\Delta x}{2}<\sigma\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}+\frac{\kappa\sigma}{2}.\)

**Case 3 (**\(x_i\le\mu\le x_{i+1}\)**):** The true mean is inside the identified interval. The absolute maximum distance from the midpoint \(\widehat{c}\) to any point inside this grid step is trivially bounded by half the step size, \(\frac{\Delta x}{2}=\frac{\kappa\sigma}{2}\) . This is strictly smaller than the bounds derived in Cases 1 and 2.

We conclude that in all possible scenarios, the initial estimate satisfies:

\(|\widehat{c}-\mu|\le\left(\sqrt{\frac{1/2+\varepsilon'}{1/2-\varepsilon'}}+\frac{\kappa}{2}\right)\sigma\)

With \(\varepsilon'=0.05\) and \(\kappa=0.2\), the guaranteed bound becomes \(|\widehat{c}-\mu|\le 1.205\sigma\). We can, in principle, choose \(\varepsilon'\) and \(\kappa\) to bring this bound arbitrarily close to \(\sigma\), but doing so will negatively affect the sample complexity. Because the sample requirement of the MEDIANEST routine scales as \(O(1/(\varepsilon')^2)\) and logarithmically with the grid size \(n\propto 1/\kappa\), shrinking these parameters heavily inflates the initialization cost. Ultimately, pushing for this precision is unnecessary; a difference of \(O(\sigma)\) in the anchor’s distance from the mean will only affect the constant factors in the estimator’s time-uniform confidence sequence (Theorem 5) and the final best-arm identification sample complexity bounds (Theorem 8 and Theorem 10).


**Algorithm 1**

procedure LessThan\((x,y,\delta)\)<br>
   \(a\leftarrow\frac{1}{2}\)<br>
   while true do<br>
   if NoisyComparison(x,y)=1 then<br>
   \(a\leftarrow\frac{(1-p)a}{(1-p)a+p(1-a)}\)<br>
   else<br>
   \(a\leftarrow\frac{pa}{pa+(1-p)(1-a)}\)<br>
   if \(a\ge 1-\delta\) then return true \(\triangleright x<y\)<br>
   if \(a\le\delta\) then return false \(\triangleright x>y\)

_Proof._ Consider Algorithm 1 which maintains the posterior probability that x\<y.

Because of the return condition, if prior distribution of \(\unknown\{x<y\}\) is Bern\((\frac{1}{2})\), then probability of error is \(\le\delta\). However, by symmetry, probability of error of the algorithm does not depend on the ground truth, so the probability of error is \(\le\delta\) regardless of the ground truth.

In the following, let us analyze the number of queries used.

Let a<sub>t</sub> be the value of a after the t-th query. If the ground truth is x\<y, then<tbc>

\(log\frac{a_{t+1}}{1-a_{t+1}}=log\frac{a_t}{1-a_t}+\left\{\begin{array}{ c c }
+log\frac{1-p}{p} & \text{w.p.}1-p, \\
-log\frac{1-p}{p} & \text{w.p.}p.
\end{array}\right.\)

<tbc>Thus,

\(\mathbb{E}\left[log\frac{a_{t+1}}{1-a_{t+1}}\right]=log\frac{a_t}{1-a_t}+(1-2p)log\frac{1-p}{p},\)

where the expectation is over the randomness of the (t+1)-th query.

Define two sequences \((X_t)_{t\ge 0}\), \((Y_t)_{t\ge 0}\) as \(X_t=log\frac{a_t}{1-a_t}\) and \(Y_t=X_t-t(1-2p)log\frac{1-p}{p}\) . Let \(\tau\) be the stopping time \(\tau:=min\{t:a_t\le\delta\text{or}a_t\ge 1-\delta\}\).

By the above discussion, \((Y_t)_{t\ge 0}\) is a martingale. Using Optional Stopping Theorem, we have<tbc>

\(\mathbb{E}[Y_{\tau\wedge n}]=\mathbb{E}[Y_0]=0\)

<tbc>for every \(n\ge 0\), so<tbc>

\(\mathbb{E}[X_{\tau\wedge n}]=\mathbb{E}[\tau\wedge n](1-2p)log\frac{1-p}{p}.\)

<tbc>By the bounded convergence theorem, \(\mathbb{E}[X_{\tau\wedge n}]\) goes to \(\mathbb{E}[X_\tau]\) as \(n\rightarrow\infty\). By the monotone convergence theorem, \(\mathbb{E}[\tau\wedge n]\) goes to \(\mathbb{E}[\tau]\) as \(n\rightarrow\infty\). Therefore,<tbc>

\(\mathbb{E}[X_\tau]=\mathbb{E}[\tau](1-2p)log\frac{1-p}{p},\)

<tbc>which leads to<tbc>

\(\mathbb{E}[\tau]=\frac{\mathbb{E}[X_\tau]}{(1-2p)log\frac{1-p}{p}}\le\frac{1}{1-2p}\left[\frac{log\frac{1-\delta}{\delta}}{log\frac{1-p}{p}}\right]\)


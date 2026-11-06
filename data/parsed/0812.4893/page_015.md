output ‘failure’ and stop); denote by _Z_ the number of red nodes obtained (that is, failure occurs if and only if _Z\<N_). For each red node, we determine whether it is matched in _M<sub>j</sub>_; denote by _Y_ the number of selected red nodes that are matched in _M<sub>j</sub>_. Output

\(\hat{m}=n\cdot\frac{X}{N}\cdot\frac{Y}{N}\)

and stop.

To analyse the procedure, let us first derive upper bounds for the probabilities of certain "bad" events.

Let us first derive an upper bound for the probability of failure. Let<tbc>

\(p=\frac{|R|}{n},k=2(\Delta+1)N,\text{and}\beta=\frac{1}{2p(\Delta+1)}.\)

<tbc>By (7) we have \(\beta\le 1/2\). Furthermore, by (7) we have that _Z\<N_ implies \(|Z-pk|\ge N=\beta pk\). Thus, from (1), (7), and (8) it follows that

\(Pr(Z<N)\le 2exp\big(-\frac{\beta^2pk}{3}\big)\)<br>
\(=2exp\big(-\frac{Nn}{6(\Delta+1)|R|}\big)\)<br>
\(\le 2exp\big(-\frac{N}{6(\Delta+1)}\big)\le\frac{\delta}{3}.\)

Let us now derive an upper bound for the probability that the random variable _X/N_ significantly deviates from its expectation |_R|/n_. Let<tbc>

\(p=\frac{|R|}{n},k=N,\text{and}\beta=\gamma.\)

<tbc>Observe that \(\beta\le 1\) by (2). By (1), (7), and (8), we have

\(Pr\big(\big|\frac{X}{N}-p\big|\ge\beta p\big)=Pr\big(|X-pk|\ge\beta pk\big)\)<br>
\(\le 2exp\big(-\frac{\beta^2pk}{3}\big)\)<br>
\(=2exp\big(-\frac{\beta^2|R|N}{3n}\big)\)<br>
\(\le 2exp\big(-\frac{\beta^2N}{3(\Delta+1)}\big)\le\frac{\delta}{3}.\)

Finally, let us now derive a similar bound for the probability that the random variable _Y/N_ significantly deviates from its expectation |_M<sub>j</sub>|/|R_|. Let<tbc>

\(p=\frac{|M_j|}{|R|},k=N,\text{and}\beta=\gamma.\)


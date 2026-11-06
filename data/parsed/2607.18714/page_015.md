_Proof._ Using Theorem 4.7 and Theorem 4.8, \(\mathrm{G}(\gamma)\) contain both p<sub>s</sub>z and sp<sub>s</sub> path (which is a subpath of st). Thus, after executing \(\mathrm{UPDATEFROM}(z,\gamma)\), we get a good estimate between s and z.<tbc>

\(\mathrm{est}(s,z)\le|\mathrm{sp}_s|+|\mathrm{p}_sz|\)

<tbc>Since \(z\in\mathrm{TRUECLOSE}(\mathrm{p}_s)\), it is at a distance at most 2c+1 from p<sub>s</sub>. Thus, we have<tbc>

\(\le|\mathrm{sp}_s|+2c+1\)

<tbc>We now bound est(z,t). Again, using Theorem 4.7 and Theorem 4.8, \(\mathrm{G}(\gamma)\) contain both p<sub>s</sub>z and p<sub>s</sub>t path (which is a subpath of st). Thus, est(z,t) can be bounded as:<tbc>

\(\mathrm{est}(z,\mathrm{t})\le|\mathrm{zp}_s|+|\mathrm{p}_st|\)

<tbc>As above, \(|\mathrm{zp}_s|\le 2c+1\). Thus, we have:

\(\le 2c+1+|\mathrm{p}_st|\)

In Algorithm 4, we construct the matrix B, which contains the estimates between all vertices of V and all vertices of \(\mathrm{L}_\gamma\). Thus, it contains our revised estimates est(s,z) and est(z,t) calculated in the above lemma. Using Theorem 3.11, we get a \((1+\varepsilon)\) approximation C of B★B<sup>T</sup>. Thus, we get a new estimate between s and t using C as follows:

\(\mathrm{est}(s,\mathrm{t})\le(1+\varepsilon)\mathrm{min}_{w\in\mathrm{L}_\gamma}\{\mathrm{est}(s,w)+\mathrm{est}(w,\mathrm{t})\}\)<br>
\(\le(1+\varepsilon)(\mathrm{est}(s,z)+\mathrm{est}(z,\mathrm{t}))\)

Using Theorem 4.9, \(\mathrm{est}(s,z)\le|\mathrm{sp}_s|+2c+1\) and \(\mathrm{est}(z,\mathrm{t})\le 2c+1+|\mathrm{p}_st|\). Thus, we get:

\(\le(1+\varepsilon)((|\mathrm{sp}_s|+2c+1)+(2c+1+|\mathrm{p}_st|))\)<br>
\(=(1+\varepsilon)(|\mathrm{st}|+4c+2)\)

If we set \(\varepsilon=1/2\), then \(\mathrm{est}(s,\mathrm{t})\le 2|\mathrm{st}|\) when \(|\mathrm{st}|\ge 12c+6\).

### 4.3 Summary of the result in this section

Our algorithm runs through two cases. In Section 4.1, we described the first case when \(|\mathrm{ESTIMATEDCLOSE}(\mathrm{p}_s)|\le\mathrm{n}^{0.875}\). In this case our algorithm ran with the running time of \(\tilde{\mathrm{O}}(\mathrm{n}^2)\) and gave an additive c+1 approximation of st path. This is a 2-approximation of st path when \(|\mathrm{st}|\ge c+1\). In Section 4.2, we described the second case when |ESTIMATEDCLOSE(p<sub>s</sub>)|_\>_n<sup>0.875</sup>. In this case our algorithm ran with the running time \(\tilde{\mathrm{O}}(\mathrm{n}^2)\) and gave a 2 approximation of st path when \(|\mathrm{st}|\ge 12c+6\) (if we set \(\varepsilon=1/2\)). Overall our algorithm gives a 2-approximation of st path when \(|\mathrm{st}|\ge 12c+6\) and runs in \(\tilde{\mathrm{O}}(\mathrm{n}^2)\) time.

Armed with this result, the proof of Theorem 1.2 becomes extremely simple.

## 5 Proof of Theorem 1.2

We first run ENSUREBALLPROXIMITY in \(\tilde{\mathrm{O}}(\mathrm{n}^2)\) time. ENSUREBALLPROXIMITY ensures that for each s,t pair, either \(\mathrm{est}(s,\mathrm{t})\le 2|\mathrm{st}|\) or the balls of s and t are close. If \(\mathrm{est}(s,\mathrm{t})\le 2|\mathrm{st}|\), then we are already done. Otherwise, we use the guarantees provided by ENSUREBALLPROXIMITY to compute a 2-approximation of the st path if \(|\mathrm{st}|\ge 12c+6\). This is done in the previous section and its running time is \(\tilde{\mathrm{O}}(\mathrm{n}^2)\). Thus, in total, the running time of our algorithm is \(\tilde{\mathrm{O}}(\mathrm{n}^2)\), and it gives a 2-approximation of the st path for all pairs that are at a distance of at least 12c+6, where c is a constant. This proves Theorem 1.2. The only remaining step is to prove the guarantees provided by ENSUREBALLPROXIMITY, which we do in the next section.


**Theorem A.5.** _An oracle solving_ Z-k\(\mathsf{OV}_{n,\ell+1}\) _where_ \(\ell=(3k+1)^{\mathrm{log}^*n}\) _in_ \(O(n^{k-\delta})\) _time for some_ \(\delta>0\) _can be used to construct an_ \(O(n^{k-\delta+o(1)})\) _time algorithm for_ kOV_<sub>n,c</sub>_log_n for an arbitrary constant c\>_0.

_Proof._ Given \(\ell=(3k+1)^{\mathrm{log}^*n}\) and any positive constant _c_, we have

\(\mathrm{log}\ell^{O((3k)^{\mathrm{log}^*d\cdot d/\ell})}=\mathrm{log}\ell\cdot O((3k)^{\mathrm{log}^*d\cdot d/\ell})\)<br>
\(=O\big(\frac{\mathrm{log}^*n\cdot(3k)^{\mathrm{log}^*n}\cdot c\cdot\mathrm{log}n}{(3k+1)^{\mathrm{log}^*n}}\big)\)<br>
\(=O\big(\mathrm{log}^*n\cdot\big(\frac{3k}{3k+1}\big)^{\mathrm{log}^*n}\cdot c\cdot\mathrm{log}n\big)\)<br>
\(=o(\mathrm{log}n).\)

By the calculation above, Lemma A.4 shows that we can reduce kOV_<sub>n,c</sub>_log_n_ to _n_<sup>_o_(1)</sup> instances of Z-k\(\mathsf{OV}_{n,\ell+1}\) in time _n_<sup>1+_o_(1)</sup>. The reduced vectors have bit-length _o_(log_n_). Therefore, we can solve these _n_<sup>_o_(1)</sup> instances with our oracle in time \(O(n^{k-\delta+o(1)})\) and this gives an \(O(n^{k-\delta+o(1)})\) time algorithm for 3OV_<sub>n,d</sub>_.

The reduction from Z-kOV<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub> to kMin-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub> is trivial, so we have completed the full reduction from SAT to kMin-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub>, and thereby have the following hardness result.

**Theorem A.6.** _Assuming_ SETH_, there is no algorithm for_ kMin-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub> _with running time_ \(O(n^{k-\varepsilon})\) _for any_ \(\varepsilon>0\).


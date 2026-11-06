By definition, it immediately follows that \(f^*(a,b)\le c^*(a,b)\). Moreover, for \(a\in V^*\backslash\{s^*,t^*\}\), it holds that

\(\sum_{b\in N_{in}(a)}f^*(b,a)=\sum_{b\in N_{in}(a)}\sum_{v\in\chi^{-1}(a),u\in\chi^{-1}(b),(u,v)\in E}f(u,v)\)<br>
\(=\sum_{v\in\chi^{-1}(a)}\sum_{u\in N_{in}(v)}f(u,v)\)<br>
\(=\sum_{v\in\chi^{-1}(a)}\sum_{w\in N_{out}(v)}f(v,w)\)<br>
\(=\sum_{b\in N_{out}(a)}\sum_{v\in\chi^{-1}(a),w\in\chi^{-1}(b),(v,w)\in E}f(v,w)\)<br>
\(=\sum_{b\in N_{out}(a)}f^*(a,b).\)

Hence, _f_<sup>∗</sup> is a flow in \(G/\chi_\infty\). Finally,

\(val(f^*)=\sum_{a\in N_{out}(s^*)}f(s^*,a)=\sum_{a\in N_{out}(s^*)}\sum_{w\in\chi^{-1}(a),(s,w)\in E}f(s,w)=\sum_{w\in N_{out}(s)}f(s,w)=val(f).\)

**Lemma A.12.** _Let G_=(_V,E,c,s,t_) _be an instance of_ Maximum Flow_, and let f_<sup>∗</sup> _be a flow in_ \(G/\chi_\infty\)_. Then there is a flow f in G such that_ \(val(f)\ge val(f^*)\).

_Proof._ For \((a,b)\in E(G/\chi_\infty)\), we define \(E_{a,b}:=\{(v,w)\in E|\chi_\infty^G(v)=a,\chi_\infty^G(w)=b\}\). We define

\(f(v,w):=\frac{f^*(a,b)}{c^*(a,b)}\cdot c(v,w),\)

for all \((v,w)\in E_{a,b}\). Clearly, \(f(v,w)\le c(v,w)\) for all \((v,w)\in E_{a,b}\), because \(f^*(a,b)\le c^*(a,b)\) due to _f_<sup>∗</sup> being a flow.

Now let \(v\in\chi^{-1}(a)\) where _a_ is an arbitrary color in the image of \(\chi_\infty^G\). We claim that

\(\sum_{u\in N_{in}(v)}f(u,v)=\frac{1}{|\chi^{-1}(a)|}\sum_{b\in N_{in}(a)}f^*(b,a).\) (4)

Indeed, we have that<tbc>

\(\sum_{u\in N_{in}(v)}f(u,v)=\sum_{u^\prime\in N_{in}(v^\prime)}f(u',v')\)

<tbc>for all \(v,v'\in\chi^{-1}(a)\) by Lemma A.10. It follows that

\(|\chi^{-1}(a)|\cdot\sum_{u\in N_{in}(v)}f(u,v)=\sum_{v^\prime\in\chi^{-1}(a)}\sum_{u^\prime\in N_{in}(v^\prime)}f(u',v')\)<br>
\(=\sum_{v^\prime\in\chi^{-1}(a)}\sum_{b\in N_{in}(a)}\sum_{u^\prime\in N_{in}(v^\prime),\chi(u^\prime)=b}f(u',v')\)<br>
\(=\sum_{v^\prime\in\chi^{-1}(a)}\sum_{b\in N_{in}(a)}\sum_{u^\prime\in N_{in}(v^\prime),\chi(u^\prime)=b}\frac{f^*(b,a)}{c^*(b,a)}\cdot c(u',v')\)<br>
\(=\sum_{b\in N_{in}(a)}\sum_{v^\prime\in\chi^{-1}(a),u^\prime\in\chi^{-1}(b),(u^\prime,v^\prime)\in E}\frac{f^*(b,a)}{c^*(b,a)}\cdot c(u',v')\)<br>
\(=\sum_{b\in N_{in}(a)}f^*(b,a).\)


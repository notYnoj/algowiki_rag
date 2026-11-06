## 5 Superadditivity of the Funnel Bound

We prove Theorem 20 in this section.

**Proof of Theorem 20.** The proof is mostly by picture (see Figure 6). Take some point _p_=(_x,t_) in _G<sub>X</sub>_, the geometric view of _X_. Its funnel will include:

Its _external funnel_: the points corresponding to its funnel from \(\widetilde{X}\).<sup>10</sup> This is because e.g. if \(j\in[l]\) is the most recent access that’s close to _j<sub>x</sub>_ on its left side, then the corresponding access in the composed sequence will definitely be the most recent access that’s close to _x_ on its left side, too.

Its _internal funnel_: the accesses corresponding to its funnel points from _X_<sup>(_j<sub>x</sub>_)</sup>.<sup>11</sup> This is because e.g. if \(y\in S_{j_x}\) is the most recent access that’s close to _x_ on its left side, then the other sequences _X_<sup>(_j_)</sup> for \(j\neq j_x\) are not going to interfere with that.

And maybe some extra funnel points.

In addition, all points of the external funnel are later in time than all points of the internal funnel. Suppose by contradiction there is an internal funnel point (_x<sub>I</sub>,t<sub>I</sub>_) that comes later than an external funnel point (_x<sub>E</sub>,t<sub>E</sub>_), i.e., _t<sub>I</sub>\>t<sub>E</sub>_. Also assume w.l.o.g. that _j<sub>x<sub>E</sub></sub>\<j<sub>x</sub>_. This means in \(G_\widetilde{X}\) we must have _j<sub>x</sub>=j<sub>xi<sub>I</sub></sub>_, then it means the point (_j<sub>xi<sub>I</sub></sub>,t<sub>I</sub>_) is in the rectangle formed by (_j<sub>x</sub>,t_) and (_j<sub>x<sub>E</sub></sub>,t<sub>E</sub>_) since _t\>t<sub>I</sub>\>t<sub>E</sub>_ and _j<sub>x</sub>=j<sub>xi<sub>I</sub></sub>\>j<sub>x<sub>E</sub></sub>_, and this contradicts with the definition that (_j<sub>x<sub>E</sub></sub>,t<sub>E</sub>_) is a funnel point in \(G_\widetilde{X}\).

<sup>10</sup> Or, more precisely, corresponding to the funnel of (_j<sub>x</sub>,t_) in the geometric view \(G_\widetilde{X}\). <sup>11</sup> Or, more precisely, corresponding to the funnel of \((x,\sigma(t))\) in the geometric view _G_<sub>_X_(_j<sub>x</sub>_)</sub>, where \(\sigma\) is defined as in Definition 17.


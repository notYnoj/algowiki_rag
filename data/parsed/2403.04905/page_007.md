_Observation 1._ Consider a crossing \(x=h_{ij}\cap h_{k\ell}\). If \(d(x,m_{k\ell})\le d(x,m_{ij})\) then all crossings \(y\in\pi_{k\ell}[x,m_{k\ell}]\) are contained in _D<sub>i</sub>_, and otherwise all crossings \(y\in\pi_{ij}[x,m_{ij}]\) are contained in _D<sub>k</sub>_.

Let \(K:=\sum_{x\in\mathcal{X}}\mathrm{ply}(x)\) denote the total ply of all crossings. The following claim bounds _K_ in terms of the labels \(\{\lambda_1(x),\lambda_2(x)\}\).

_Claim 1._ \(K>\frac{1}{2|\mathcal{D}_1|}\sum_{x\in\mathcal{X}}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\).

_Proof._ Define \(K(D_i):=\left|\{x\in\mathcal{X}:x\in D_i\}\right|\) to be the contribution of _D<sub>i</sub>_ to the total ply _K_, and note that

\(K=\sum_{x\in\mathcal{X}}\mathrm{ply}(x)=\sum_{x\in\mathcal{X}}\left|\{D_i\in\mathcal{D}_1:x\in D_i\}\right|=\sum_{D_i\in\mathcal{D}_1}\left|\{x\in\mathcal{X}:x\in D_i\}\right|=\sum_{D_i\in\mathcal{D}_1}K(D_i).\)

Now consider a crossing \(x=h_{ij}\cap h_{k\ell}\). If \(d(x,m_{k\ell})\le d(x,m_{ij})\) then we assign _x_ to _D<sub>i</sub>_, and otherwise we assign _x_ to _D<sub>k</sub>_. Let X(_D<sub>i</sub>_) be the set of crossings assigned to _D<sub>i</sub>_. By Observation 1 and the definition of the label \(\{\lambda_1(x),\lambda_2(x)\}\), the disk _D<sub>i</sub>_ contains at least \(\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\) crossings \(y\in\pi_{k\ell}[x,m_{k\ell}]\), for any \(x=h_{ij}\cap h_{k\ell}\in\mathcal{X}(D_i)\). Thus, summing over all crossings \(x\in\mathcal{X}(D_i)\cap h_{ij}\) and all half-edges _h<sub>ij</sub>_ incident to _D<sub>i</sub>_, we find that

\(K(D_i)\ge\frac{1}{2\mathrm{deg}(D_i)}\sum_{h_{ij}}\sum_{x\in\mathcal{X}(D_i)\cap h_{ij}}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}>\frac{1}{2|\mathcal{D}_1|}\sum_{x\in\mathcal{X}(D_i)}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\},\)

where deg(_D<sub>i</sub>_) denotes the degree of _D<sub>i</sub>_ in \(\mathcal{G}^\times(\mathcal{D}_1)\). The factor \(\frac{1}{2\mathrm{deg}(D_i)}\) arises because a crossing \(y\in h_{k\ell}\) can be counted up to 2deg(_D<sub>i</sub>_) times in the expression \(\sum_{x\in\mathcal{X}(D_i)}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\), namely at most twice for every half-edge incident to _D<sub>i</sub>_; see Fig. 1(ii). (Twice, because a pair of paths in a proper path set may cross twice.) Since each crossing is assigned to exactly one set X(_D<sub>i</sub>_), we obtain

\(K=\sum_{D_i\in\mathcal{D}_1}K(D_i)>\sum_{D_i\in\mathcal{D}}\left(\frac{1}{2|\mathcal{D}_1|}\sum_{x\in\mathcal{X}(D_i)}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\right)\)<br>
\(=\frac{1}{2|\mathcal{D}_1|}\sum_{x\in\mathcal{X}}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}.\)<br>
\(\triangleleft\)

From the Crossing Lemma and our initial assumption that \(|E_1|>\sqrt{\frac{4}{c}}\cdot n^\frac{3+\alpha}{2}\) , we have that

\(|\mathcal{X}|\ge c\frac{|E_1|^3}{n^2}>4|E_1|n^{1+\alpha}=2|\mathcal{E}_1|n^{1+\alpha}.\) (1)

In order to get a rough bound for \(\sum_{x\in\mathcal{X}}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\), we will ignore crossings with small labels, while ensuring that we don’t ignore too many crossings in total. More precisely, for every half-edge _h<sub>ij</sub>_, we disregard its first \(n^{1+\alpha}\) crossings, starting from the one closest to _m<sub>ij</sub>_. We let X<sup>∗</sup> denote the set of remaining crossings. Note that \(|\mathcal{X}^*|\ge|\mathcal{X}|-|\mathcal{E}_1|n^{1+\alpha}\), and \(\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}\ge n^{1+\alpha}\) for every \(x\in\mathcal{X}^*\). Therefore

\(K>\frac{1}{2|\mathcal{D}_1|}\sum_{x\in\mathcal{X}^*}\mathrm{min}\{\lambda_1(x),\lambda_2(x)\}=\frac{1}{2|\mathcal{D}_1|}\cdot|\mathcal{X}^*|\cdot n^{1+\alpha}\ge\frac{\left(|\mathcal{X}|-|\mathcal{E}_1|n^{1+\alpha}\right)n^{1+\alpha}}{2|\mathcal{D}_1|}\ge\frac{|\mathcal{X}|}{4}n^\alpha.\)

This means that there exists a crossing \(x\in\mathcal{X}\) of ply at least \(\frac{1}{4}n^\alpha\), which contradicts the condition of the lemma and thus finishes the proof. \(\blacktriangleleft\)


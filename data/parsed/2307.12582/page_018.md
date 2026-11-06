Consider \(\mathcal{I}_2^{\overline{W^+}}\) first. For any \(w\in\overline{W^+}\), _w_ is not frequent in I<sub>2</sub>. That is, \(|\mathcal{I}_2\cap\mathcal{I}^w|<w_\mathrm{max}^{1/5}\). We have

\(\Delta(\mathcal{I}_2^{\overline{W^+}})\le\sum_{i\in\mathcal{I}_2^{\overline{W^+}}}w_i=\sum_{w\in\overline{W^+}}w|\mathcal{I}_2\cap\mathcal{I}^w|\le|\overline{W^+}|w_\mathrm{max}w_\mathrm{max}^{1/5}=w_\mathrm{max}^{9/5}.\)

Now consider \(\mathcal{I}_1^{\overline{W^+}}\). Suppose, for the sake of contradiction, that \(\Delta(\mathcal{I}_1^{\overline{W^+}})>2c_Bw_\mathrm{max}^{9/5}>2c_Bw_\mathrm{max}^{8/5}\). That is, we delete a large volume of items in \(\mathcal{I}_1^{\overline{W^+}}\). Clearly, \(\mathcal{I}_1^{\overline{W^+}}\) is not empty, so there are exactly \(2c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights that are frequent in I<sub>2</sub>. Recall that, by frequent, we mean \(|\mathcal{I}^w\cap\mathcal{I}_2|\ge 2w_\mathrm{max}^{1/5}\). Then at least one of the following two cases are true.

(i) there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\mathbf{z}(\mathcal{I}_2)|\ge w_\mathrm{max}^{1/5}\).<tbc>

(ii) there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\overline{\mathbf{z}}(\mathcal{I}_2)|\ge w_\mathrm{max}^{1/5}\).

**Case (i).** \(\overline{\mathbf{z}}(\mathcal{I}_1^{\overline{W^+}})\) is a set of deleted items whose total weight is \(\Delta(\mathcal{I}_1^{\overline{W^+}})>2c_Bw_\mathrm{max}^{8/5}\). **z**(I<sub>2</sub>) is a set of items remaining in **z**, and there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\mathbf{z}(\mathcal{I}_2)|\ge w_\mathrm{max}^{1/5}\). One can verify that the weight multisets of \(\overline{\mathbf{z}}(\mathcal{I}_1^{\overline{W^+}})\) and **z**(I<sub>2</sub>) satisfy the conditions of Lemma 3.2. By Lemma 3.2, there is a subset D of \(\overline{\mathbf{z}}(\mathcal{I}_1^{\overline{W^+}})\) and a subset Z of **z**(I<sub>2</sub>) such that D and Z have the same total weight. Then \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{Z})\cup\mathcal{D}\) would be a better solution than **z**. Contradiction.

**Case (ii).** there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\overline{\mathbf{z}}(\mathcal{I}_2)|\ge w_\mathrm{max}^{1/5}\). \(\Delta(\mathcal{I}_1^{\overline{W^+}})>2c_Bw_\mathrm{max}^{8/5}\) implies that

\(\Delta(\mathcal{I}_{\unknown b})\ge\Delta(\mathcal{I}_1^{\overline{W^+}})-w_\mathrm{max}\ge c_Bw_\mathrm{max}^{8/5}.\)

Note that the total weight of \(\mathbf{z}(\mathcal{I}_{\unknown b})\) is exactly \(\Delta(\mathcal{I}_{\unknown b})\). One can verify that the weight multisets of <o>**z**</o>(I<sub>2</sub>) and \(\mathbf{z}(\mathcal{I}_{\unknown b})\) satisfy the condition of Lemma 3.2. By Lemma 3.2, there is a subset D of <o>**z**</o>(I<sub>2</sub>) and a subset A of \(\mathbf{z}(\mathcal{I}_{\unknown b})\) such that D and A have the same total weight. Then \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{A})\cup\mathcal{D}\) would be a better solution than **z**. Contradiction.

Due to symmetry, it can be similarly proved that \(\Delta(\mathcal{I}_k^{\overline{W^+}})\le 2c_Bw_\mathrm{max}^{9/5}\) for \(k\in\{3,4\}\). We provide a full proof for completeness. Consider \(\mathcal{I}_3^{\overline{W^+}}\). For any \(w\in\overline{W^+}\), _w_ is not frequent in I<sub>2</sub>. That is, \(|\mathcal{I}_3\cap\mathcal{I}^w|<w_\mathrm{max}^{1/5}\).

\(\Delta(\mathcal{I}_3^{\overline{W^+}})\le\sum_{i\in\mathcal{I}_3^{\overline{W^+}}}w_i=\sum_{w\in\overline{W^+}}w|\mathcal{I}_3\cap\mathcal{I}^w|\le|\overline{W^+}|w_\mathrm{max}w_\mathrm{max}^{1/5}=w_\mathrm{max}^{9/5}.\)

Consider \(\mathcal{I}_4^{\overline{W^+}}\). Suppose, for the sake of contradiction, that \(\Delta(\mathcal{I}_4^{\overline{W^+}})>2c_Bw_\mathrm{max}^{9/5}>2c_Bw_\mathrm{max}^{8/5}\). That is, we add a large volume of items from \(\mathcal{I}_4^{\overline{W^+}}\) when obtaining **z** from **g**. Clearly, \(\mathcal{I}_4^{\overline{W^+}}\) is not empty, so there are exactly \(2c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights that are frequent in I<sub>3</sub>. Recall that, by frequent, we mean \(|\mathcal{I}^w\cap\mathcal{I}_3|\ge 2w_\mathrm{max}^{1/5}\). Then at least one of the following two cases are true.

(iii) there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\overline{\mathbf{z}}(\mathcal{I}_3)|\ge w_\mathrm{max}^{1/5}\).<tbc>

(iv) there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\mathbf{z}(\mathcal{I}_3)|\ge w_\mathrm{max}^{1/5}\).

**Case (iii).** \(\mathbf{z}(\mathcal{I}_4^{\overline{W^+}})\) has a total weight of \(\Delta(\mathcal{I}_4^{\overline{W^+}})>2c_Bw_\mathrm{max}^{8/5}\). For <o>**z**</o>(I<sub>3</sub>), there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\overline{\mathbf{z}}(\mathcal{I}_3)|\ge w_\mathrm{max}^{1/5}\). One can verify that the weight multisets of \(\mathbf{z}(\mathcal{I}_4^{\overline{W^+}})\) and <o>**z**</o>(I<sub>3</sub>) satisfy the conditions of Lemma 3.2. By Lemma 3.2, there is a subset Z of \(\mathbf{z}(\mathcal{I}_4^{\overline{W^+}})\) and a subset D of <o>**z**</o>(I<sub>3</sub>) such that D and Z have the same total weight. Then \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{Z})\cup\mathcal{D}\) would be a better solution than **z**. Contradiction.

**Case (iv).** there are at least \(c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights _w_ such that \(|\mathcal{I}^w\cap\mathbf{z}(\mathcal{I}_3)|\ge w_\mathrm{max}^{1/5}\). \(\Delta(\mathcal{I}_4^{\overline{W^+}})>2c_Bw_\mathrm{max}^{8/5}\) implies that

\(\Delta(\mathcal{I}_{<b})\ge\Delta(\mathcal{I}_4^{\overline{W^+}})-w_\mathrm{max}\ge c_Bw_\mathrm{max}^{8/5}.\)

Note that the total weight of <o>**z**</o>(I_<sub>\<b</sub>_) is exactly \(\Delta(\mathcal{I}_{<b})\). One can verify that the weight multisets of **z**(I<sub>3</sub>) and <o>**z**</o>(I_<sub>\<b</sub>_) satisfy the conditions of Lemma 3.2. By Lemma 3.2, there is a subset A of **z**(I<sub>3</sub>) and a subset D of <o>**z**</o>(I_<sub>\<b</sub>_) such that D and A have the same total weight. Then \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{A})\cup\mathcal{D}\) would be a better solution than **z**. Contradiction. \(\sqcap\sqcup\)


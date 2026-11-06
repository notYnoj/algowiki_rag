• Now consider the case when \(\gamma_{i^\prime}\in\{\widetilde{\psi}_i,\widetilde{\tau}_i\}\) and one of the following holds: i) \(\theta_{i^\prime}=\mathsf{e}\), or \(\widetilde{\gamma}_i\in\Gamma_{\alpha,R,\gamma_{i^\prime}}[\psi_{i^\prime},\tau_{i^\prime}]\backslash\{\psi_{i^\prime},\tau_{i^\prime}\}\). As \(\beta_i\) must be _d_-good (see Definitions 5.11 and 5.12 (1)), it follows that \(w(\widetilde{\beta}_i\cap\check{\beta}_{i^\prime})\le d\).<tbc>

• Finally consider the case when \(\gamma_{i^\prime}\in\Gamma_{\alpha,R,\widetilde{\gamma}_i}[\widetilde{\psi}_i,\widetilde{\tau}_i]\backslash\{\widetilde{\psi}_i,\widetilde{\tau}_i\}\) and \(\widetilde{\gamma}_i\in\{\psi_{i^\prime},\tau_{i^\prime}\}\). Then, as \(\widehat{\mathcal{C}}\) is a solution we have that \(w(\widehat{\beta}_i\cap\check{\beta}_{i^\prime})\le d\). Also, since \(\widehat{\beta}_i\) and \(\widetilde{\beta}_i\) are \(\widetilde{\theta}_i\)-abiding, we must have \(E(\widehat{\beta}_i\cap\check{\beta}_{i^\prime})\subseteq E(\widetilde{\gamma}_i\cap\gamma_{i^\prime})=E(\widehat{\beta}_i\cap\gamma_{i^\prime})=E(\widetilde{\beta}_i\cap\gamma_{i^\prime})\). Thus, we can obtain that \(E(\widehat{\beta}_i\cap\check{\beta}_{i^\prime})=E(\widetilde{\beta}_i\cap\check{\beta}_{i^\prime})\), and hence, \(w(\widetilde{\beta}_i\cap\check{\beta}_{i^\prime})\le d\).

This concludes the proof.

We will now prove that C is at least as good a solution as \(\widehat{\mathcal{C}}\), for \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\).

**Lemma 5.9.** _We have_ \(w(\mathcal{C}\cup\mathcal{P})\ge w(\widehat{\mathcal{C}}\cup\mathcal{P})\).

_Proof._ We recall the following property which we will be using in our proof. Consider distinct \(i_1,i_2,i_3\in[b]\) and \(\mathcal{D}\in\{\mathcal{C},\widehat{\mathcal{C}}\}\). Also consider \(C_1\in\mathcal{D}\cap V(\mathcal{T}_{\gamma_{i_1}})\), \(C_2\in\mathcal{D}\cap V(\mathcal{T}_{\gamma_{i_2}})\), and \(C_3\in\mathcal{D}\cap V(\mathcal{T}_{\gamma_{i_3}})\). From Lemma 5.2 and Observation 5.4 we have that \(E(C_1)\cap E(C_2)\cap E(C_3)=\emptyset\) and \(E(C_1\cap C_2)\subseteq E(\delta_{i_1}\cap\gamma_{i_1})\), where \(\gamma_{i_1}\) is the \((\alpha,\mathcal{D})\)-representative for \(\delta_{i_1}\in\mathcal{D}\). In the above, the first part will be used in the arguments that an edge cannot be part of three distinct cycles from \(\{\widetilde{\beta}_i|i\in[\tilde{p}]\}\) (resp. \(\{\widehat{\beta}_i|i\in[\tilde{p}]\}\)).

Let \(I=[b]\backslash\{i_j|i\in[\tilde{p}]\}\), and \(\mathcal{C}_\mathsf{cm}=\{\alpha\}\cup(\cup_{q\in I}\mathcal{C}_i)\). Note that \(\mathcal{C}_\mathsf{cm}=\{\alpha\}\cup(\cup_{q\in I}\widehat{\mathcal{C}}_i)\). Let \(\widetilde{\mathcal{C}}_\mathsf{ex}=\cup_{i\in[\tilde{p}]}\widetilde{\mathcal{C}}_i\) and \(\widehat{\mathcal{C}}_\mathsf{ex}=\cup_{[i\in\tilde{p}]}\widehat{\mathcal{C}}_i\). Notice that \(\mathcal{C}=\mathcal{C}_\mathsf{cm}\unknown\widetilde{\mathcal{C}}_\mathsf{ex}\) and \(\widehat{\mathcal{C}}=\mathcal{C}_\mathsf{cm}\unknown\widehat{\mathcal{C}}_\mathsf{ex}\). Let _w_cm=_w(E_(C<sub>cm</sub>)\\_E_(P)). Also,

\(w(\mathcal{C}\cup\mathcal{P})=w(\widetilde{\mathcal{C}}_\mathsf{ex}\cup\mathcal{P})-w\big((E(\widetilde{\mathcal{C}}_\mathsf{ex})\cap E(\mathcal{C}_\mathsf{cm}))\backslash E(\mathcal{P})\big)+w_\mathsf{cm}\)<br>
\(w(\widehat{\mathcal{C}}\cup\mathcal{P})=w(\widehat{\mathcal{C}}_\mathsf{ex}\cup\mathcal{P})-w\big((E(\widehat{\mathcal{C}}_\mathsf{ex})\cap E(\mathcal{C}_\mathsf{cm}))\backslash E(\mathcal{P})\big)+w_\mathsf{cm}\) (2)

As \(\widehat{\mathcal{C}}\) is a solution for \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\), using the property we stated towards the beginning of the proof of this lemma, and the construction of \(\widetilde{\mathcal{C}}_i\), for \(i\in[\tilde{p}]\), we can obtain:

\(w(\widetilde{\mathcal{C}}_\mathsf{ex}\cup\mathcal{P})=\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widetilde{\beta}_i,\widetilde{h}_i)-(\tilde{p}-1)w(\mathcal{P})-\sum_{i,i^\prime\in[\tilde{p}],i<i^\prime} w(E(\widetilde{\beta}_i\cap\widetilde{\beta}_{i^\prime})\backslash E(\mathcal{P}))\)<br>
\(w(\widehat{\mathcal{C}}_\mathsf{ex}\cup\mathcal{P})\le\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widehat{\beta}_i,\widetilde{h}_i)-(\tilde{p}-1)w(\mathcal{P})-\sum_{i,i^\prime\in[\tilde{p}],i<i^\prime} w(E(\widehat{\beta}_i\cap\widehat{\beta}_{i^\prime})\backslash E(\mathcal{P}))\) (3)

From Definition 5.13 we can obtain the following:

\(w\big((E(\widetilde{\mathcal{C}}_\mathsf{ex})\cap E(\mathcal{C}_\mathsf{cm}))\backslash E(\mathcal{P})\big)+\sum_{i,i^\prime\in[\tilde{p}],i<i^\prime} w(E(\widetilde{\beta}_i\cap\widetilde{\beta}_{i^\prime})\backslash E(\mathcal{P}))\)<br>
\(=w^\mathsf{ovr}(\varepsilon_1^*,\varepsilon_\tilde{p}^*)+w^2(\mathcal{C})+w^3(\mathcal{C})+\sum_{i\in[\tilde{p}-1]}w(E(\widetilde{\beta}_i\cap\widetilde{\beta}_{i+1})\backslash E(\mathcal{P}))\)<br>
\(w\big((E(\widehat{\mathcal{C}}_\mathsf{ex})\cap E(\mathcal{C}_\mathsf{cm}))\backslash E(\mathcal{P})\big)+\sum_{i,i^\prime\in[\tilde{p}],i<i^\prime} w(E(\widehat{\beta}_i\cap\widehat{\beta}_{i^\prime})\backslash E(\mathcal{P}))\)


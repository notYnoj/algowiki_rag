## 3.3 The Neighborhood Structures

We also investigate the structure surrounding a random independent set \(I\sim\mathsf{IS}_\lambda(G)\). In the following two lemmas, we analyze the expected size of \(I\cup N(I)\).

**Lemma 11.** _Let_ \(\lambda>0\)_, and let G_=(_V,E_) _be a graph. Then,_

\(\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|I|]=\lambda\cdot\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|V\backslash(I\cup N(I))|].\)

_Proof._ Fix \(v\in V\) . Let \(\mathcal{I}_v^\mathrm{in}=\{I\in\mathcal{I}:v\in I\}\), and \(\mathcal{I}_v^\mathrm{out}=\{I\in\mathcal{I}:v\in V\backslash(I\cup N(I))\}\). Then, the relationship \(\mathcal{I}_v^\mathrm{in}=\{I\cup\{v\}:I\in\mathcal{I}_v^\mathrm{out}\}\) holds (Figure 5), as shown below:

• For every \(I\in\mathcal{I}_v^\mathrm{out}\), \(I\cup\{v\}\in\mathcal{I}_v^\mathrm{in}\) because \(I\cup\{v\}\) is an independent set due to \(v\notin I\cup N(I)\).<tbc>

• For every \(I\cup\{v\}\in\mathcal{I}_v^\mathrm{in}\), \(I\in\mathcal{I}_v^\mathrm{out}\) because _I_ is an independent set and \(v\notin N(I)\).

Here, for each \(I\in\mathcal{I}_v^\mathrm{out}\), the probability that \(I\cup\{v\}\) is chosen is \(\lambda\) times the probability that _I_ is chosen. Therefore,

\(\mathrm{Pr}_{I\sim\mathsf{IS}_\lambda(G)}[I\in\mathcal{I}_v^\mathrm{in}]=\lambda\cdot\mathrm{Pr}_{I\sim\mathsf{IS}_\lambda(G)}[I\in\mathcal{I}_v^\mathrm{out}](\forall v\in V)\)<br>
\(\text{Equivalently,}\mathrm{Pr}_{I\sim\mathsf{IS}_\lambda(G)}[v\in I]=\lambda\cdot\mathrm{Pr}_{I\sim\mathsf{IS}_\lambda(G)}[v\in V\backslash(I\cup N(I))](\forall v\in V)\)

Summing this equation over all \(v\in V\) , we have \(\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|I|]=\lambda\cdot\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|V\backslash(I\cup N(I))|]\) by linearity of expectation. □

**Lemma 12.** _Let_ \(\lambda\in(0,1]\)_, and let G_=(_V,E_) _be a k-colorable graph. Then,_

\(\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|I\cup N(I)|]\le\left(1-\frac{1}{3k\mathrm{ln}(3k)}\right)|V|.\)

_Proof._ By Lemma 11, \(\mathbb{E}[|V\backslash(I\cup N(I))|]=\frac{1}{\lambda}\cdot\mathbb{E}[|I|]\). Thus, by Lemma 10,

\(\mathbb{E}[|I\cup N(I)|]=|V|-\frac{1}{\lambda}\cdot\mathbb{E}[|I|]\)<br>
\(\le|V|-\frac{1}{\lambda}\cdot\frac{\lambda}{3k\mathrm{ln}(3k)}|V|=\left(1-\frac{1}{3k\mathrm{ln}(3k)}\right)|V|.\) □


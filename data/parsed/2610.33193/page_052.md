logically reversible fashion even after the actual value of \(x_i^j\) has been erased.<sup>42</sup> We will use the same reversible demultiplexer / multiplexer gadget as in the compaction circuit with controlled erasure gates to selectively pick the optimal heat function to use for each erasure.

Now we argue that this approach gives us a circuit with zero circuit entropy production. First we consider the drop in entropy from the mapping \(x\mapsto\text{Sort}(x)\). Let \(C(x)\in\mathbb{Z}_{\ge 0}^{\{0,1\}^m}\) be the vector of counts for the number of times each possible \(b\in\{0,1\}^m\) appears in the input _x_. Then we have that S(D)-S(Sort(D))=S(D|Sort(D))=S(D|_C_(D)) and thus when _x_∼D:

\(\mathcal{S}(\mathcal{D})-\mathcal{S}(\text{Sort}(\mathcal{D}))=\sum_{c\in\mathbb{Z}_{\ge 0}^{\{0,1\}^m}}\mathrm{Pr}_{x\sim\mathcal{D}}[C(x)=c]\mathcal{S}(x|C(x)=c)\)<br>
\(=\sum_{c\in\mathbb{Z}_{\ge 0}^{\{0,1\}^m}}\mathrm{Pr}_{x\sim\mathcal{D}}[C(x)=c]\mathrm{log}\frac{n!}{\prod_{b\in\{0,1\}^m}c_b!}\) (13)

Note that this term only has support on _c_ where the 1-norm (i.e. Manhattan norm) of _c_ is exactly _n_.

As before, we will now show that our choices of heat functions _Q<sub>i,j</sub>_ for erasing each bit release \(\mathrm{log}(n!/\prod_bc_b!)\) expected heat on every input with count vector _c_. Our heat function for erasing the _j_’th bit of the _i_’th input will take the form:

\(Q_{i,j}\left(x_i^j,\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}},\left|x_{\le i}^{\ge j}\right|_{0\cdot x_i^{\ge j+1}},\left|x_{\le i}^{\ge j}\right|_{1\cdot x_i^{\ge j+1}}\right)=\left\{\mathrm{log}\left(\frac{\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}}{\left|x_{\le i}^{\ge j}\right|_{0\cdot x_i^{\ge j+1}}}\right)x_i^j=0\right.\)<br>
\(\left.\mathrm{log}\left(\frac{\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}}{\left|x_{\le i}^{\ge j}\right|_{1\cdot x_i^{\ge j+1}}}\right)x_i^j=1\right.\)<br>
\(=\mathrm{log}\left(\frac{\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}}{\left|x_{\le i}^{\ge j}\right|_{x_i^{\ge j}}}\right)\)

Let’s fix any _x_ and let _c=C(x_). Then the total expected heat released on input _x_ is exactly

\(\sum_{i\in[n],j\in[m]}Q_{i,j}\left(x_i^j,\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}},\left|x_{\le i}^{\ge j}\right|_{0\cdot x_i^{\ge j+1}},\left|x_{\le i}^{\ge j}\right|_{1\cdot x_i^{\ge j+1}}\right)=\sum_{i\in[n],j\in[m]}\mathrm{log}\left(\frac{\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}}{\left|x_{\le i}^{\ge j}\right|_{x_i^{\ge j}}}\right)\)<br>
\(=\sum_{i\in[n]}\sum_{j\in[m]}\mathrm{log}\left(\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}\right)-\mathrm{log}\left(\left|x_{\le i}^{\ge j}\right|_{x_i^{\ge j}}\right)\)<br>
\(=\sum_{i\in[n]}\mathrm{log}\left(\left|x_{\le i}^{\ge m+1}\right|_{x_i^{\ge m+1}}\right)-\mathrm{log}\left(\left|x_{\le i}^{\ge 1}\right|_{x_i^{\ge 1}}\right)\)<br>
\(=\sum_{i\in[n]}\mathrm{log}(i)-\mathrm{log}(C_{x_i}(x_{\le i}))\text{since}x_i^{\ge m+1}\text{is the empty string}\)

<sup>42</sup>The counts of 0’s versus 1’s for erased prefixes can be deduced from the sorted output and the non erased part of the input. For example, \(\left|x_{\le i}^{\ge j}\right|_{0\cdot x_i^{\ge j+1}}=\left|\text{Sort}(x)\right|_{0\cdot x_i^{\ge j+1}}-\left|x_{>i}^{\ge j}\right|_{0\cdot x_i^{\ge j+1}}\) and the terms on the right can be computed after \(x_i^j\) has been erased. Control gates can be used to ensure that we only count the number of 0’s and 1’s for inputs with the desired suffix.


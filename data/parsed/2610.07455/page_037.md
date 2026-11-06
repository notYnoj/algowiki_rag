Indeed, fix \(S\in\Gamma\), \(x\in S\), and an arbitrary tuple _z_. Write \(\delta(z)\) for the tuple obtained by applying \(\delta\) to every coordinate of _z_. Since \(\Gamma\) is shift-closed, \(S^{x-z}\in\Gamma\), and \(z\in S^{x-z}\). Applying _h_ gives \(h(z)\in S^{x-z}\), or equivalently \(x+\delta(z)\in S\). Thus translation by \(\delta(z)\) maps _S_ into itself. Since translation is a bijection and _S_ is finite, it preserves _S_. Comparing two tuples \(z,z'\) that differ only in coordinate _i_, taking the values _a_ and _b_ there, shows that translation by \((\delta(a)-\delta(b))e_i\) preserves _S_. Since _S_ and _i_ were arbitrary, (A.4) follows.

Now suppose that _h(a_)=_h(b_). Then \(b-a=\delta(a)-\delta(b)\in H\). Hence an endomorphism cannot identify elements from distinct _H_-cosets. Every endomorphism therefore has image size at least |_D/H_|, while \(\rho\) has exactly this image size. Thus \(\rho\) is a core endomorphism.

Let \(\Delta:=\rho(\Gamma)=\mathrm{core}(\Gamma)\). For \(S\in\Gamma\), write \(S^\rho:=\rho(S)\). By (A.3),

\(x\in S\Longleftrightarrow\rho(x)\in S^\rho.\) (A.5)

Moreover, the map \(S\mapsto S^\rho\) is injective. If \(S^\rho=T^\rho\), then (A.5) implies _S=T_.

Now take any positive \(\Gamma\)-instance _I_, and replace every relation _S_ by \(S^\rho\), obtaining a \(\Delta\)-instance \(I^\rho\). This correspondence preserves the number of constraints. Moreover, (A.5) shows that an assignment and its image under \(\rho\) have the same satisfaction pattern, constraint by constraint. Consequently, if _a_ is a witness for a constraint in _I_, then \(\rho(a)\) is a witness for the corresponding constraint in \(I^\rho\). Hence \(I^\rho\) is nonredundant whenever _I_ is nonredundant.

Conversely, every \(\Delta\)-instance can be lifted to a \(\Gamma\)-instance using the unique preimage of each relation, and every witness assignment over _C_ remains a witness after this lift. Thus nonredundant instances of the same size exist in both directions, proving \(\mathsf{NRD}_n^+(\Gamma)=\mathsf{NRD}_n^+(\Delta)\).

Applying the lemma to the shift closure gives the desired connection to the literal model.

**Corollary A.6.** _For every_ \(R\subseteq\mathbb{Z}_q^k\), \(\mathsf{NRD}_n^\mathrm{lit}(R)=\mathsf{NRD}_n^+\big(\mathrm{core}(\Gamma_R^\mathrm{lit})\big)\)_. Hence our general core characterization recovers the previous streaming characterization for_ CSPs _with literals._

_Proof._ A literal _R_-instance is exactly a positive \(\Gamma_R^\mathrm{lit}\)-instance, so \(\mathsf{NRD}_n^\mathrm{lit}(R)=\mathsf{NRD}_n^+(\Gamma_R^\mathrm{lit})\). Since \(\Gamma_R^\mathrm{lit}\) is shift-closed, Lemma A.2 gives \(\mathsf{NRD}_n^+(\Gamma_R^\mathrm{lit})=\mathsf{NRD}_n^+\big(\mathrm{core}(\Gamma_R^\mathrm{lit})\big)\). Together with Corollary A.1, this recovers the one-pass satisfiability characterization for CSPs with literals.

## A.2 Non-constant-satisfiable Boolean CSPs

We next recover the previous characterization for positive Boolean CSPs. A Boolean constraint language \(\Gamma\) is _constant-satisfiable_ if there is a value \(c\in\{0,1\}\) such that the constant tuple (_c,...,c_) belongs to every relation in \(\Gamma\). Equivalently, assigning the value _c_ to every variable satisfies every positive instance over \(\Gamma\). The next lemma shows that excluding this case is exactly the same as requiring the language to be a core.

**Lemma A.7.** _Let_ \(\Gamma\) _be a Boolean constraint language in which every relation is nonempty. Then_ \(\Gamma\) _is a core if and only if it is not constant-satisfiable._

_Proof._ Every non-bijective map from {0,1} to itself is constant. The constant map with value _c_ is an endomorphism of \(\Gamma\) exactly when (_c,...,c_) belongs to every relation in \(\Gamma\). One direction is immediate. For the other, apply the constant map to any tuple in each nonempty relation. Thus \(\Gamma\) has a non-bijective endomorphism exactly when it is constant-satisfiable.

It follows that every non-constant-satisfiable Boolean constraint language is already a core. Applying our general CSP core characterization therefore directly recovers the positive Boolean result of Sharma and Velusamy.


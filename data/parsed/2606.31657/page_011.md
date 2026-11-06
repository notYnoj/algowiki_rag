The next lemma shows that any linear locally testable code becomes systematic after permuting coordinates. The proof is deferred to Appendix A.

**Lemma 2.5.** _If_ \(C\subseteq\mathbb{F}_p^n\) _is a linear LTC, then there exists a permutation matrix_ \(\Pi\) _such that_ \(\Pi C\) _is a systematic LTC with the same parameters._

### 2.3 Constraint Satisfaction Problems

Let _V_ be a finite set of variables and let \(\Sigma\) be a finite alphabet. An instance of a _constraint satisfaction problem (CSP)_ over \(\Sigma\) is a tuple \((V,\Sigma,\mathcal{C})\), where C is a finite collection of constraints. Each constraint is given by a pair (_S,R_) with \(S\subseteq V\) its scope and \(R\subseteq\Sigma^S\) the set of allowed local assignments. An assignment \(\alpha\in\Sigma^V\) _satisfies_ (_S,R_) if \(\alpha|_S\in R\), and it is a solution to the instance when it satisfies every constraint in C. The associated _maximum constraint satisfaction problem (Max CSP)_ asks for an assignment \(\alpha\in\Sigma^V\) that maximizes the number of satisfied constraints.

For a CSP instance \(\mathcal{I}=(V,\Sigma,\mathcal{C})\) and a constraint \(c\in\mathcal{C}\), we write I-_c_ for the instance obtained by removing _c_ from C.

## 3 Sensitivity Lower Bounds via LTCs

The goal of this section is to prove Theorem 1.1. We organize the argument in four stages. First, Section 3.1 shows how a systematic LTC induces a CSP whose constraints mirror the tester. Next, in Section 3.2 we discuss the nearest-message decoder, which recovers the planted message from near-optimal assignments, and accompanying stability bounds. Building on these tools, Section 3.3 symmetrizes the decoder’s output distributions and proves a large total-variation gap between neighboring messages. Finally, Section 3.4 converts this gap into an earth mover’s distance lower bound for worst-case sensitivity, and the same argument also yields an average-sensitivity analogue, giving Theorem 1.1.

### 3.1 CSP Induced by an LTC

For \(m\in\Sigma^k\) and a subset \(U\subseteq\Sigma^{n-k}\), we write \(m\oplus U:=\{(m,u):u\in U\}\subseteq\Sigma^n\).

**Definition 3.1.** For a systematic LTC \((C,f,\mathcal{S},\mathcal{V}=\{V_S\}_{S\in\mathcal{S}})\) and a message \(m\in\Sigma^k\), we construct a CSP instance \(\mathcal{I}_{C,f,\mathcal{S},\mathcal{V}}(m)=(V,\Sigma,\mathcal{C})\) as follows:

• \(V:=\{x_i\}_{i=k+1}^n\).<tbc>

• For every \(S\in\mathcal{S}\), let \(S':=S\cap\{k+1,\dots,n\}\) and define<tbc>

<tbc>\(R_S:=\left\{\alpha\in\Sigma^{S^\prime}|\exists\beta\in V_S:\beta|_{[k]}=m\wedge\beta|_{S^\prime}=\alpha\right\}.\)<tbc>

<tbc>The constraint corresponding to _S_ is \((S',R_S)\).<tbc>

• \(\mathcal{C}:=\{(S',R_S):S\in\mathcal{S}\}\).<tbc>

<tbc>For brevity, we write I_<sub>C</sub>(m_) for I<sub>_C,f,_S,V</sub>(_m_).

Intuitively, the message coordinates of a systematic codeword are fixed once we choose _m_, so the only freedom left is the parity part. The tester’s local view on _S_ allows exactly the projections of valid codewords onto _S_. Intersecting _V<sub>S</sub>_ with \(m\oplus\Sigma^{n-k}\) therefore isolates those local patterns that agree with _m_ on the message positions, and projecting them onto the parity indices \(S'\) yields<tbc>


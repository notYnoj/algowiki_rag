## 13:12 Tight Energy Lower Bounds for Distributed Graph Algorithms

some \(i\in[\ell-1]\), with the goal of computing _f(X,Y_), and recall that Alice uses her input to construct the edges of _G_\[_V_<sub>1</sub>\], whereas Bob will construct \(G[V_\ell]\) according to _Y_ . Since \(\mathsf{IC}(f,\epsilon)\ge I\), we know that there exists a distribution \(\mu\) on \(X\times Y\) such that the information cost of protocol \(\pi_i\) is<tbc>

\(\mathsf{IC}_\mu(\pi_i)=\mathbf{I}[X:\Pi|Y]+\mathbf{I}[Y:\Pi|X]\ge I.\)

<tbc>Without loss of generality, we assume that

\(\mathbf{I}[X:\Pi|Y]\ge\frac{I}{2}.\) (5)

Let \(\Pi_{V_i}\) denote the transcript of messages that the nodes in _V<sub>i</sub>_ receive from their neighbors in _V_<sub>_i_+1</sub> and define \(\Pi_{V_{i+1}}\) analogously; note that \(\Pi=(\Pi_{V_i},\Pi_{V_{i+1}})\) contains the entire transcript of the communication between Alice and Bob, i.e., which corresponds to all messages crossing the cut. Our goal is to apply Lemma 1, and hence we need to first argue that (5) holds when only considering the transcript \(\Pi_{V_{i+1}}\).

\(\triangleright\) Claim 5. \(\mathbf{I}\big[X:\Pi_{V_{i+1}}|Y\big]\ge\frac{I}{2}\).

**Proof.** Let _R<sub>B</sub>_ be the private randomness of Bob. Consider the mutual information \(\mathbf{I}[X:R_B|\Pi,Y]\). Conditioned on the transcript \(\Pi\) and Bob’s input _Y_ , we know that Alice’s input _X_ is independent of Bob’s randomness _R<sub>B</sub>_. In other words, \(X\rightarrow(\Pi,Y)\rightarrow R_B\) forms a Markov chain, and hence \(\mathbf{I}[X:R_B|\Pi,Y]=0\). By a similar argument, it follows that **I**\[_X:R<sub>B</sub>|Y_\]=0. Combining these observations and applying the chain rule multiple times yields

\(\mathbf{I}[X:\Pi|Y]=\mathbf{I}[X:\Pi|Y]+\mathbf{I}[X:R_B|\Pi,Y]-\mathbf{I}[X:R_B|Y]\) (6)

\(=\mathbf{I}[X:\Pi,R_B|Y]-\mathbf{I}[X:R_B|Y]\) (7)

\(=\mathbf{I}[X:\Pi|R_B,Y]\) (8)

\(=\mathbf{I}\big[X:\Pi_{V_i},\Pi_{V_{i+1}}|R_B,Y\big]\)<br> \(=\mathbf{I}\big[X:\Pi_{V_{i+1}}|R_B,Y\big]+\mathbf{I}\big[X:\Pi_{V_i}|\Pi_{V_{i+1}},R_B,Y\big]\)<br> \(=\mathbf{I}\big[X:\Pi_{V_{i+1}}|R_B,Y\big],\) (9)

where the final step follows because the conditioning on \(\Pi_{V_{i+1}},R_B,Y\) ensures that the messages sent to the nodes in _V<sub>i</sub>_, i.e., \(\Pi_{V_i}\), do not reveal any information about _X_, and hence \(\mathbf{I}\big[X:\Pi_{V_i}|\Pi_{V_{i+1}},R_B,Y\big]=0\). Finally, we can again remove the conditioning on the private randomness in (9) by simply executing the chain rule applications in (6)-(8) in reverse order (after replacing \(\Pi\) with \(\Pi_{i+1}\)). It follows that \(\mathbf{I}\big[X:\Pi_{V_{i+1}}|Y\big]=\mathbf{I}[X:\Pi|Y]\ge\frac{I}{2}\), which completes the proof of the claim. \(\blacktriangleleft\)

We are now ready to instantiate Lemma 1(ii) for algorithm A with _Z=G_\[_V_<sub>1</sub>\], \(L=\frac{I}{2}\), \(V_A=V_{\ge i+1}\), \(V_B=V_{\le i}\), \(U=V_{i+1}^-\), \(\partial U=V_i^+\), and _d<sub>U</sub>=d<sub>cut</sub>_, which means that \(\mathbf{I}[Z:\Pi_U|S_{V_A}]=\mathbf{I}\big[G[V_1]:\Pi_{V_{i+1}}|S_{V_{\ge i+1}}\big]\ge\frac{I}{2}\), as required by the premise of the lemma. This yields the sought worst case bound per node.

To extend the result to the node-averaged case, we proceed similarly as for the worst case above, with the main difference being that we apply Lemma 1(i) for every cut (_V<sub>i</sub>,V_<sub>_i_+1</sub>) (\(1\le i\le\ell-1\)). Let \(\alpha_i\) be the total number of awake rounds of the nodes in \(V_i\cup V_{i+1}\). It follows that, for all \(i\in[\ell-1]\),

\(\mathbf{E}[\alpha_i]=\Omega\big(\frac{I}{d_{cut}logn}\big),\)


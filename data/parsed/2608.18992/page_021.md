## 13:20 Tight Energy Lower Bounds for Distributed Graph Algorithms

to the end of round _R<sub>i</sub>_-1 is fully determined by _S<sub>V<sub>A</sub></sub>_ and the prefix \((R_{\le i-1},\hat{\Pi}_{\le i-1})\). Clearly, this is also sufficient to determine the state of each node in _V<sub>A</sub>_ at the start of round _R<sub>i</sub>_. Consequently, knowing \((R_i,\hat{\Pi}_i)\) allows us to deterministically compute the state (and wake up steps) of all nodes in _V<sub>A</sub>_ during round _R<sub>i</sub>_, and, in fact, the same applies to all subsequent rounds in which no message is received by a node in _U_ from \(\partial U\). Hence, we have sufficient information to compute the states of the nodes in _V<sub>A</sub>_ up until the end of round _R_<sub>_i_+1</sub>-1. \(\blacktriangleleft\)

Since \(\Pi_U\) denotes only the transcript of the messages received by nodes in _U_ from \(\partial U\), whereas the extended transcript \(\hat{\Pi}\) contains these same messages together with their respective round numbers and source/destination IDs, \(\Pi_U\) is deterministically recoverable from \(\hat{\Pi}\). Thus, by the data processing inequality (see Fact 2.6), we have that

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{V_A}\big]\ge\mathbf{I}[\Pi_U:Z|S_{V_A}]\ge L.\) (13)

Before deriving an upper bound on the mutual information in (13), we first define some additional notation. In Figure 3, we provide a list of variables used throughout the proof. We use _X<sub>\<i</sub>_ as a shorthand for _X_<sub>1</sub>_,...,X_<sub>_i_-1</sub>, when considering a sequence of random variables, and we define \(X_{\le i}\) similarly. Below, we use |_X_| to denote the worst case length of an optimal encoding of a random variable _X_, i.e., \(|X|\le log_2|\text{supp}(X)|\).

We first state some bounds that we rely on in our analysis. By the premise of the lemma, we have

\(L\le n^{c_1},\) (14)

for some constant _c_<sub>1</sub>_\>_0. Moreover, recall that we assume that the message size is at most logarithmic, i.e., there is some constant _c_<sub>2</sub>_\>_0 such that, for every _i_, we have

\(|\hat{\Pi}_i|\le c_2logn.\) (15)

Recall that _c\>_0 is the constant specified in Property (i) of the lemma. We also introduce a constant _C_, where

\(C\ge 4c(c_1+c_2+2).\) (16)

Finally, we define the bounds \(\beta\) and \(\bar{M}\) such that

\(\beta=\frac{L}{C\cdot d_Ulogn},\) (17)

\(\bar{M}=2c\cdot\beta\cdot d_U.\) (18)

Note that we assume \(L=\omega(d_Ulogn)\) throughout the proof, as otherwise the resulting lower bound is trivial.

We are now ready to start our analysis. Assume towards a contradiction that the given algorithm satisfies

\(\mathbf{E}[\alpha_U]\le\beta.\) (19)

Whenever a node \(u\in U\) is awake in a given round, it may receive messages from up to \(e(u,\partial U)\le d_U\) neighbors in \(\partial U\). Thus, we can bound the expectation of the number _M_ of pairs \((R_i,\hat{\Pi}_i)\) in \(\hat{\Pi}\) as \(\mathbf{E}[M]\le\mathbf{E}[\alpha_U]\cdot d_U\). Notice that the event \(M\le\bar{M}\) occurs with


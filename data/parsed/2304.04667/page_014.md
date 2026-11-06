**Lemma 2.2.** _Given a set of node pairs_ \(Q\subseteq V\times V\)_, the nondeterministic complexity of solving Max-Flow for all_ \((u,v)\in Q\) _is_ \(O\left(n^{\omega(\mathrm{log}_n(|Q|),1,1)}+\sum_{(u,v)\in Q}\mathbf{volume}(f_{uv})\right)\).

_Proof of Theorem 2.1._ A nondeterministic algorithm first guesses the random bits of D (if D is randomized Las Vegas) and a set of node pairs to be queried _Q_. It then solves _Q_ nondeterministically using Lemma 2.2. Finally, it simulates D (on a deterministic Turing machine) with the guessed random bits, and whenever encountering a Max-Flow query, it asserts the validity of the corresponding stored answer for the node pair. By Lemma 2.2, verifying the Max-Flow for _Q_ takes a total time of \(O\left(n^{\omega(\mathrm{log}_n(|Q|),1,1)}+\sum_{(u,v)\in Q}\mathbf{volume}(f_{uv})\right)\), and otherwise (for some guess) the total running time is bounded by _t<sub>po</sub>(m_). The correctness follows immediately from the correctness of D, and so the proof of Theorem 2.1 is concluded.

_Proof of Lemma 2.2._ First, guess a list \(\{p_{uv}\}_{(u,v)\in Q}\) for the node pairs in _Q_. We want to verify quickly two things for each pair (_u,v_):

1. that there exists a _uv_-flow _f<sub>uv</sub>_ such that \(\mathbf{value}(f_{uv})\ge p_{uv}\), and<tbc>

2. that there exists a _uv_-cut (_S<sub>uv</sub>,T<sub>uv</sub>_) such that \(\mathbf{value}(S_{uv},T_{uv})\le p_{uv}\).

By the min-cut max-flow theorem \[FF56\], it would imply that the guessed _p<sub>uv</sub>_’s are maximum _uv_-flow values. But how can we verify these conditions quickly? Verifying the cut or flow values explicitly for each pair would be too costly, as it might take at least _m_ time using a straightforward approach. Thus, the total time would be \(O(|Q|\cdot m)\), which does not provide any significant advantage to nondeterminism. Therefore, we need to employ a more careful strategy.

## Verifying lower bounds.

For the flow lower bounds, verifying the guessed values \(\{p_{uv}\}_{(u,v)\in Q}\) in the proper time of \(\sum_{(u,v)\in Q}\mathbf{volume}(f_{uv})\) is simple; just guess succinct flows _f<sub>uv</sub>_ for all pairs \((u,v)\in Q\), and then verify their validity and values _p<sub>uv</sub>_, i.e., that the flow conservation and capacity constraints hold, and that \(\mathbf{value}(f_{uv})\ge p_{uv}\). If any verification step returned "no", reject, otherwise accept. The verification time per flow is proportional to the number of edges in its support, that is _O_(**volume**(_f<sub>uv</sub>_)), as required.

As a side note, the challenge in making this part of Lemma 2.2 useful will be to show for any maximum _uv_-flow _f<sub>uv</sub>_ that _there exists_ a (perhaps alternative) succinct flow \(f'_{uv}\) shipping the same amount of flow in _G_ while keeping the flow constraints, or to find a proper algorithm with few calls to Max-Flow. This will be elaborated on in Section 2.1.

## Verifying upper bounds.

For the cut upper bounds, the proof is similar across all variants, and it can even be applied to directed graphs with general _edge_ capacities. Therefore, we will only present a proof for this particular variant, while noting that folklore reductions from the other variants are sufficient for our purposes.

Technically, the nondeterministic algorithm guesses a partition (_S<sub>uv</sub>,T<sub>uv</sub>=V_\\_S_) for every pair \((u,v)\in Q\), and then it utilizes fast matrix multiplication to simultaneously verify that the cut values are smaller than the guessed values \(\{p_{uv}\}_{(u,v)\in Q}\), i.e. it checks that for all \((u,v)\in Q\), it holds that \(\mathbf{value}(S_{uv},T_{uv})\le p_{uv}\). In more detail, we define a binary matrix \(P_{|Q|\times n}\), where the rows correspond to the pairs in _Q_ and the columns correspond to the nodes in the graph. In this matrix, the entry _P_\[_g<sub>uv</sub>,w_\] is set to 1 if \(w\in S_{uv}\), and to 0 otherwise, where _g<sub>uv</sub>_ is the index of the pair \((u,v)\in Q\) (by some arbitrary order). Lastly, let _M<sub>G</sub>_ be the incidence matrix of the graph _G_, where an entry _M<sub>G</sub>_\[_u,v_\] is the weight of the edge from _u_ to _v_ in _G_, and is 0 if no such edge exists. With these notations, we are now ready to describe the cuts verification algorithm.


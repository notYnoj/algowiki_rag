To satisfy this invariant initially (for \(\ell=1\)) we pick _Y_<sub>1</sub>=_X_ and _p_<sub>1</sub>=1; indeed, then the invariant follows from the assumption \(C\subseteq X+X\). Let \(s=|A|^{\epsilon/k}\). Each iteration depends on the parity of \(\ell\):

• _If_ \(\ell\) _is odd:_ Apply Lemma 4.7 on the 3SUM instance (_A,B,C_), with parameters \(p_\ell\) and _s_ and sets \(X,Y_1,\dots,Y_\ell\); the invariant makes sure that the premise \(C\subseteq Pop(X,Y_1,\dots,Y_\ell;p_\ell)\) is fulfilled. This yields a set of solutions \(\mathcal{T}'\) and a subinstance \((A,B'\subseteq B,C)\). We update:<tbc>

\(\mathcal{T}:=\mathcal{T}\cup\mathcal{T}',\)<br>
\(B:=B',\)<br>
\(Y_{\ell+1}:=-A,\)<br>
\(p_{\ell+1}:=\frac{p_\ell|A|}{s}.\)

Lemma 4.7 states that each 3SUM solution is either in \(\mathcal{T}'\) or part of the instance \((A,B',C)\). Thus, after the update each solution is either in T or part of the instance (_A,B,C_), and therefore the first invariant is maintained.

Lemma 4.7 also guarantees that \(B'\subseteq Pop(X,Y_1,\dots,Y_\ell,-A;p_\ell|A|/s)\). After the update, this precisely maintains the second invariant.<tbc>

• _If_ \(\ell\) _is even:_ Observe that our 3SUM instance (_A,B,C_) is equivalent to the appropriately transposed instance (_A,-C,-B_), i.e., their solutions stand in one-to-one correspondence. Apply Lemma 4.7 on (_A,-C,-B_) with parameters \(p_\ell\) and _s_ and sets \(-X,-Y_1,\dots,-Y_\ell\); the premise \(-B\subseteq Pop(-X,-Y_1,\dots,-Y_\ell;p_\ell)\) is satisfied by our invariant. This yields a set of solutions \(\mathcal{T}'\) and a subinstance \((A,C'\subseteq-C,-B)\). We update:<tbc>

\(\mathcal{T}:=\mathcal{T}\cup\{(a,b,c):(a,-c,-b)\in\mathcal{T}'\},\)<br>
\(C:=-C',\)<br>
\(Y_{\ell+1}:=A,\)<br>
\(p_{\ell+1}:=\frac{p_\ell|A|}{s}.\)

Similarly to before, Lemma 4.7 states that each transposed 3SUM solution is either in \(\mathcal{T}'\) or part of the instance \((A,C',-B)\). Thus, after the update each original solution is either in T or part of the instance (_A,B,C_), and therefore the first invariant is maintained.

Lemma 4.7 also guarantees that \(C'\subseteq Pop(-X,-Y_1,\dots,-Y_\ell,-A;p_\ell|A|/s)\). After the update, this precisely maintains the second invariant.

Once the final _k_-th iteration is complete, we report the set T and the subinstances constructed in step 1. This completes the description of the algorithm.

## Correctness.

The correctness of steps 1 and 2 is fairly obvious; the interesting part is to argue that in step 3 we exhaustively list all solutions of (_A,B,C_). The key correctness claim is that once the _k_-th iteration terminates, _B_ or _C_ must be empty. Suppose otherwise that both are non-empty. Then our invariant implies that

\(Pop(X,Y_1,\dots,Y_{k+1};p_{k+1})\neq\emptyset.\)


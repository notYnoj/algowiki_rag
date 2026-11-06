By induction, in the iteration where level(_s,b_) is set to \(\ell'\), that iteration began with \(\text{level}(s)=\text{level}(s,b)=\ell'-b\) and \(\mathcal{A}(s,b)=\emptyset\) at some point in that iteration (since this is a requirement to trigger `increaseLevel` or `updateScores`). Regardless of which one was triggered, A(_s,b_) is only set to be non-empty if \(\text{level}(s)=\text{level}(s,b)=\ell'\), a contradiction as level(_s_) cannot decrease.

**Claim 5.20.** _At the start of any iteration of the while loop,_

\(\text{level}(s)\le\text{level}(s,b)\le\text{level}(s)+b\)

_for all_ \(s\in S_\text{in}\) _and b._

_Proof of Claim 5.20._ Observe that \(\text{level}(s)\le\text{level}(s,b)\) by definition. Since at most one of `updateScores` or `increaseLevel` is called during any single iteration, level(_s,b_) increases by at most _b_. Furthermore, by Claim 5.19 level(_s,b_) does not increase whenever level(_s,b)\>_level(_s_). Thus, level(_s,b_) can never exceed level(_s_) by more than _b_.

We are ready to prove the required lemmas.

**Claim 5.11.** _In any iteration of the while loop,_ level(_s_) _increases by at most one for all_ \(s\in S_\text{in}\).

_Proof of Claim 5.11._ At the start of any iteration, we have \(\ell=\text{level}(s)\le\text{level}(s,1)\le\text{level}(s)+1\) by Claim 5.20. If \(\text{level}(s,1)=\ell+1\), then by Claim 5.19, level(_s,_1) is not incremented during this iteration, so that \(\text{level}(s)\le\text{level}(s,1)\le\ell+1\) at the end of this iteration. On the other hand, if \(\text{level}(s,1)=\ell\), then since at most one of `increaseLevel` or `updateScores` is invoked during any single iteration, we have \(\text{level}(s)\le\text{level}(s,1)\le\ell+1\) at the end of the iteration, as desired.

**Claim 5.12.** _Let_ \(s\in S_\text{in}\) _and_ \(\ell\le\text{ccc}(s)\)_. Then, for every b such that_ \(\ell\) _is a multiple of b, there exists an iteration where_ \(\text{level}(s)=\text{level}(s,b)=\ell\) _at the beginning of the iteration._

_Proof of Claim 5.12._ From Claim 5.11, we have that level(_s_) increments by at most one in every iteration. Thus, since \(\text{level}(s)\le\text{level}(s,b)\), consider the first iteration where \(\ell=\text{level}(s)\le\text{level}(s,b)\). We claim that in fact level(_s,b_)=level(_s_). Suppose not for contradiction. Then, we have that at the start of this iteration, \(\text{level}(s,b)\ge\ell+b\) since level(_s,b_) increases in increments of size _b_, and the same bound holds at the end of the previous iteration.

Now, consider the previous iteration which began with \(\text{level}(s)=\ell-1\). From Claim 5.20, at the start of this iteration \(\text{level}(s,b)\le\ell-1+b<\ell+b\) so that level(_s,b_) must have been incremented in the previous iteration. Furthermore, at the start of the previous iteration, \(\text{level}(s,b)\ge\text{level}(s)=\ell-1\). We consider two cases.

If _b\>_1, then \(\text{level}(s,b)=\ell\) since \(\ell-1modb\unknown\equiv 0\). Then, regardless of whether level(_s_) is incremented via `updateScores` or `increaseLevel`, level(_s,b_) is only incremented if \(\text{level}(s,b)=\ell-1\) by Claim 5.19, which is impossible unless _b_=1 (again since level(_s,b_) increases in increments of size _b_).

Thus, assume _b_=1. In this case, \(\text{level}(s,b)=\ell-1\) at the start of the previous iteration (otherwise \(\text{level}(s,b)\neq\text{level}(s)\) is not increased) so that \(\text{level}(s,b)=\ell\) at the start of this iteration, as desired.

**Lemma 5.16.** _The total time used by all calls to `increaseLevel` is_ \(\tilde{O}\left(|S_\text{in}|nB\right)=\tilde{O}\left(Bn^2\right)\).

_Proof of Lemma 5.16._ First, we claim that \(\text{level}(s,b)\le Bn\) for all _b_.

**Claim 5.21.** \(\text{level}(s,b)\le Bn\) _for all b_=2_<sup>t</sup> and_ \(s\in S\).

_Proof of Claim 5.21._ Since _G_ is connected, we have \(\text{ccc}(s)\le Bn\) so that by Lemma 5.13, we have that \(\bigcup_{r=0}^{Bn}\hat{L}(s,r)=V\) , so we remove _s_ from _S_ after level _Bn_.


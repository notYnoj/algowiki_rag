**Definition 2.2.** A matrix is \(\sigma\)_-sparse_, for a positive integer \(\sigma\), if each row has at most \(\sigma\) nonzero entries.

Truncation changes at most \(\sigma\) entries per row, so entrywise precision 2<sup>-_k_</sup> gives operator-norm error \(O(\sigma 2^{-k})\) (Lemma 3.3). The regularity we ask of _H_ at fine steps is the following.

**Definition 2.3.** A map _H_ from \[0_,T_\] to the \(d\times d\) matrices is _regulated_ if it has a limit from the right at every \(t\in[0,T)\) and a limit from the left at every \(t\in(0,T]\).

Lipschitz families are regulated, but regulated families may also jump, and their one-sided limits permit the uniform piecewise-constant approximations \[11, (7.6.1)\] needed for the fine-step comparison.

For a regulated family, we read (2.1) in the following sense: _U_ is continuous and unitary-valued, _U_(0)=1, and \(i\dot{U}(t)=H(t)U(t)\) for all but countably many _t_. The same applies to _V_ , and Proposition 2.5 proves existence and uniqueness in this sense. For piecewise-constant _G_, the evolution is _V(t_)=_e_<sup>-_i(t-t<sub>j</sub>)G<sub>j</sub>_</sup>_V(t<sub>j</sub>_) on \[_t<sub>j</sub>,t_<sub>_j_+1</sub>\], so _V(T_)=_W_ in (2.2), whatever the values of _G_ at the piece endpoints _t<sub>j</sub>_.

## 2.1. Comparing two evolutions.

The Duhamel estimate \[4\] allows countably many exceptional times at which the evolutions need not be differentiable.

**Lemma 2.4.** _Let_ \(H,G:[a,b]\rightarrow\mathbb{C}^{d\times d}\)_, let_ \(S\subset[a,b]\) _be countable, and let_ \(U,V:[a,b]\rightarrow\mathbb{C}^{d\times d}\) _be continuous and unitary-valued, with U(a_)=_V(a), such that_ \(i\dot{U}(t)=H(t)U(t)\) _and_ \(i\dot{V}(t)=G(t)V(t)\) _for every_ \(t\in[a,b]\backslash S\)_. If_ \(t\mapsto\|H(t)-G(t)\|\) _is integrable, then_<tbc>

(2.3) \(\|U(b)-V(b)\|\le\int_a^b\|H(t)-G(t)\|dt.\)

<tbc>_Proof._ For \(t\in[a,b]\backslash S\), the product rule and the two evolution equations give \(\frac{d}{dt}(U^\dagger V)=iU^\dagger(H-G)V\) , whose norm is \(\|H-G\|\) by unitarity. The fundamental theorem of calculus for a continuous function with integrable derivative outside a countable set (see \[11, (8.7.1)-(8.7.2)\] for regulated derivatives) gives

\(U(b)^\dagger V(b)-1=i\int_a^bU(t)^\dagger\big(H(t)-G(t)\big)V(t)dt,\)

since _U(a_)<sup>†</sup>_V(a_)=1. Taking norms, using the integral triangle inequality and unitary invariance of the norm, gives (2.3). □

For a uniform bound \(\|H(t)-G(t)\|\le\eta\), integration gives \(\|U(b)-V(b)\|\le\eta(b-a)\), so \(\|U(T)-W\|\le\eta T\) for piecewise-constant _G_. Duhamel also constructs the evolution of a regulated family.

**Proposition 2.5.** _Every regulated family_ \(H:[0,T]\rightarrow\mathbb{C}^{d\times d}\) _is bounded and has at most countably many discontinuities, hence a set of discontinuities of measure zero. It has a unique continuous unitary evolution U, with U_(0)=1_, satisfying_

\(U(t)=1-i\int_0^tH(s)U(s)ds.\)

_At every continuity point of H,_ \(i\dot{U}(t)=H(t)U(t)\)_, with one-sided derivatives at the endpoints. In particular, U satisfies the equation at all but countably many times._

_Proof._ Choose piecewise-constant Hermitian \(H_n\rightarrow H\) uniformly, each equal to _H_ at its piece endpoints \[11, (7.6.1)\]. Uniform convergence makes _H_ bounded and continuous outside the countable union of partition points. Their unitary evolutions _U<sub>n</sub>_ satisfy \(sup_t\|U_n(t)-U_m(t)\|\le Tsup_t\|H_n(t)-H_m(t)\|\) by Lemma 2.4, so they converge uniformly to a continuous unitary _U_ with _U_(0)=1. Passing to the limit in \(U_n(t)=1-i\int_0^tH_n(s)U_n(s)ds\) gives the integral equation, since the integrands converge uniformly. At continuity points of _H_, the integrand _H(s)U(s_) is continuous, so the fundamental theorem of calculus gives the stated derivatives. Finally, Lemma 2.4 with identical generators gives uniqueness. □


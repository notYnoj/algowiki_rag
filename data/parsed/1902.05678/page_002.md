<tbc>write \(q_i\succ_pq_j\) and interpret it as "_p_ prefers _q<sub>i</sub>_ to _q<sub>j</sub>_". In this paper, we denote a preference list in the following form:

_m_<sub>2</sub>: _w_<sub>3</sub> _w_<sub>1</sub> _w_<sub>4</sub> _w_<sub>2</sub>,

which means that _m_<sub>2</sub> prefers _w_<sub>3</sub> best, _w_<sub>1</sub> 2nd, _w_<sub>4</sub> 3rd, and _w_<sub>2</sub> last (this example is for _n_=4).

A _matching_ is a set of _n_ (man, woman)-pairs in which no person appears more than once. For a matching _M_, _M(p_) denotes the partner of a person _p_ in _M_. If, for a man _m_ and a woman _w_, both \(w\succ_mM(m)\) and \(m\succ_mM(w)\) hold, then we say that (_m,w_) is a _blocking pair_ for _M_ or (_m,w_) _blocks M_. Note that both _m_ and _w_ have incentive to be matched with each other ignoring the given partner, so it can be thought of as a threat for the current matching _M_. A matching with no blocking pair is a _stable matching_. It is known that any instance admits at least one stable matching, and one can be found by the _Gale-Shapley algorithm_ (or _GS algorithm_ for short) in _O(n_<sup>2</sup>) time \[2\]. There have been a plenty of research results on this problem from viewpoints of Economics, Computer Science, Mathematics, etc (see \[4, 14, 9\] e.g.).

## 1.1 Strategy-proofness

The stable marriage problem can be seen as a game among participants, who have true preferences in mind, but may submit a falsified preference list hoping to obtain a better partner than the one assigned when true preference lists are used. Formally, let _S_ be a _mechanism_, that is, a mapping from instances to matchings, and we denote _S(I_) the matching output by _S_ for an instance _I_. We say that _S_ is a _stable mechanism_ if, for any instance _I_, _S(I_) is a stable matching for _I_. For a mechanism _S_, let _I_ be an instance, _M_ be a matching such that _M=S(I_), and _p_ be a person. We say that _p has a successful strategy in I_ if there is an instance \(I'\) in which people except for _p_ have the same preference lists in _I_ and \(I'\), and _p_ prefers \(M'\) to _M_ (i.e., \(M'(p)\succ_pM(p)\) with respect to _p_’s preference list in _I_), where \(M'\) is a matching such that \(M'=S(I')\). This situation is interpreted as follows: _I_ is the set of true preference lists, and by submitting a falsified preference list (which changes the set of lists to \(I'\)), _p_ can obtain a better partner \(M'(p)\). We say that _S_ is a _strategy-proof mechanism_ if, when _S_ is used, no person has a successful strategy in any instance. Also we say that _S_ is a _man-strategy-proof mechanism_ if, when _S_ is used, no man has a successful strategy in any instance. A _woman-strategy-proof mechanism_ is defined analogously. A mechanism is a _one-sided-strategy-proof mechanism_ if it is either a man-strategy-proof mechanism or a woman-strategy-proof mechanism.

It is known that there is no strategy-proof stable mechanism for SM \[13\], which is known as _Roth’s impossibility theorem_. By contrast, the man-oriented GS algorithm, _MGS_ for short, (in which men send and women receive proposals; see Appendix A) is a man-strategy-proof stable mechanism for SM \[13, 1\]. Of course, by the symmetry of men and women, the woman-oriented GS algorithm (_WGS_) is a woman-strategy-proof stable mechanism.

## 1.2 Ties and Incomplete Lists

One of the most natural extensions of SM is the _Stable Marriage with Ties and Incomplete lists_, denoted _SMTI_. An instance of SMTI consists of _n_ men, _n_ women, and each person’s preference list. A preference list may include ties, which represent indifference between two or more persons, and may be incomplete, meaning that a preference list may contain only a _subset_ of people in the opposite gender. Such a preference list may be of the following form:

_m_<sub>2</sub>: _w_<sub>3</sub> (_w_<sub>1</sub> _w_<sub>4</sub>),


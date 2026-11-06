[9] if it has minimum sex-equal score over all stable matchings in M. Finding a sex-equal stable matching was shown to be NP-hard by Kato [13]. This result was later strengthened by McDermid and Irving [16] who showed that, even in the case when preference lists have length at most 3, the problem of deciding whether there is a stable matching with sex-equal score 0 is NP-complete. Additionally, a polynomial-time algorithm to find a sex-equal stable matching is described for instances in which men have preference lists of length at most 2 (women’s preference lists remaining unbounded) [16]. A stable matching _M_ is _egalitarian_ [14] if _c(M_) is minimum over all stable matchings in M, and may be found in _O(m_<sup>1.5</sup>) time [4]. Finally, a stable matching _M_ is _minimum regret_ [14] if _d(M_) is minimum among all stable matchings in M. It is possible to find a minimum regret stable matching in _O(m_) time [8]. These definitions of fairness are summarised in  1.

In  1 there are two new natural definitions of fairness that can be studied.

We define the _regret-equality score r(M_) as |_dU(M_)-_dW(M_)| for a given stable matching _M_. _M_ is _regret-equal_ if _r(M_) is minimum, taken over all stable matchings in M. Note that in general we will prefer a regret-equal stable matching _M_ such that _dU(M_)+_dW(M_) is minimised (e.g. _d(M_)=(3,3) rather than _d(M_)=(10,10)).

We define the _regret sum_ as _dU(M_)+_dW(M_) for a given stable matching _M_. _M_ is _min-regret sum_ if _dU(M_)+_dW(M_) is minimum taken over all stable matchings in M.

## 1.2 Motivation

Matching algorithms are widely used in the real world to solve allocation problems based on SMI and its variants. A famous example of this is the _National Resident Matching Program_ (NRMP). This scheme has been running in the US since 1952, and involves the allocation of thousands of graduating medical students to hospitals [18]. Other matching schemes involve the allocation of students to projects [2] and the allocation of kidney donors to kidney patients [3].

Let mentees take the place of men and mentors take the place of women. Thus, mentees (mentors) rank a subset of mentors (mentees) and may only be allocated one mentor (mentee) in any matching. If we used the (renamed) Mentee-Oriented Gale-Shapley Algorithm [5] to find a stable matching of mentees to mentors, then we would find a mentee-optimal stable

\begin{tabular}{ccc}
& Cost & Degree \\ Minimising the maximum & min_M∈M max{c_U(M),c_W(M)} & min_M∈M max{d_U(M),d_W(M)} \\ Minimising the absolute difference & min_M∈M |c_U(M)-c_W(M)| & min_M∈M |d_U(M)-d_W(M)| \\ Minimising the sum & Sex-equal stable matching [9] & Regret-equal stable matching * \\ & min_M∈M (c_U(M)+c_W(M)) & min_M∈M (d_U(M)+d_W(M)) \\ & Egalitarian stable matching [14] & Min-regret sum stable matching * \\ \end{tabular}

** 1** Commonly used definitions of fair stable matchings in SMI. Our contributions are labelled with an \*.


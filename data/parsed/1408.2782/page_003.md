<tbc>found among the accepted proposals, and matched women reject men they do not prefer to their matches. This procedure is iterated until a large fraction of men are either matched or have been rejected by all women.

The analysis of our algorithm follows in two steps. We first show that by quantizing preferences, the matching found by **ASM** cannot contain a large fraction of blocking pairs among the matched (or rejected) players. We bound the number of blocking pairs from the remaining "bad" players by showing there are few such players, and that only a small fraction can participate in many blocking pairs.

The remainder of the paper is organized as follows. In Section 2 we formalize our notion almost stable matchings and our computational model. We also overview methods of computing maximal matchings which our algorithm will require as subroutines. Section 3 describes **ASM** and its subroutines in detail and states basic guarantees for the subroutines. Section 4 proves the performance guarantees for **ASM**. Finally, in Section 5 we describe the randomized variants of **ASM**.

## 2 Preliminaries

### 2.1 Stable and almost stable matchings

We consider the stable marriage problem as originally described by Gale and Shapley \[4\] with incomplete preferences or, equivalently, unacceptable partners (cf. \[5, 10\]). Let _X_ and _Y_ be sets of women and men, respectively. For simplicity, we assume |_X_|=|_Y_|=_n_. Each player \(v\in X\cup Y\) holds a **_preference list_** or **_ranking_** _P<sup>v</sup>_--a linear order on a subset of the members of the opposite sex. We denote the set of all player’s preferences by \(\mathcal{P}=\{P^v|v\in X\cup Y\}\). We refer to the players _u_ that appear on _v_’s preference list _P<sup>v</sup>_ as _v_’s **_acceptable partners_**. We call P **_complete_** if each player ranks all players of the opposite sex. If a man _m_ precedes \(m'\) on woman _w_’s preference list, we write \(m\succ_wm'\), and we say that _w **prefers** m_ to \(m'\). For simplicity, we assume that preferences are symmetric in the sense that if _m_ appears in _P<sup>w</sup>_, then _w_ appears in _P<sup>m</sup>_. Given players _v_ and _u_ of opposite genders, we let _P<sup>v</sup>(u_) denote _v_’s **_rank_** of _u_. For example, _P<sup>v</sup>(u_)=1 means that _u_ is _v_’s most favored partner, et cetera.

We define the **_communication graph_** _G_=(_V,E_) for a set of preferences P to be

\(V=Y\times X,E=\{(m,w)|m\in P^w,w\in P^m\}.\)

For a communication graph _G_=(_V,E_), we denote the degree of \(v\in V\) by deg_v_, which is the number of players that appear on _v_’s preference list.

A **_matching_** \(M\subseteq E\) is a set of edges in _E_ such that no two edges share a vertex. Given a matching _M_ and \((m,w)\in M\), we call _m_ and _w **partners**_ and write _p(w_)=_m_ and _p(m_)=_w_. Given preferences and a matching _M_, we say that an edge \((m,w)\in E\) is a **_blocking pair_** if \((m,w)\notin M\), but _m_ and _w_ mutually prefer each other to their partners in _M_; that is,

\(m\succ_wp(w)\text{and}w\succ_mp(m).\)

By convention, we assume each unmatched player \((p(v)=\emptyset)\) prefers all acceptable partners to being without a partner. A **_stable matching_** is a matching which contains no blocking pairs.

We are primarily concerned with finding matchings which are "almost stable" in the sense that they induce relatively few blocking pairs. We use a definition of almost stability given by Eriksson and Häggström \[2\], modified to allow for incomplete preference lists.

**Definition 2.1.** Given \(\varepsilon\ge 0\) and preferences P, we say that a matching _M_ is \((1-\varepsilon)\)**_-stable_** with respect to P if _M_ induces at most \(\varepsilon|E|\) blocking pairs with respect to P.

We refer to the problem of finding a matching which is \((1-\varepsilon)\)-stable for fixed \(\varepsilon>0\) as the **_almost stable matching problem_**. Note that a 1-stable matching corresponds precisely to the classical stable matching definition.


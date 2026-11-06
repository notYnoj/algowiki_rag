## 7.3 Proof of Thm. 4 -- Huang and Wong’s error

A _generalized binary split tree_ (gbst) is a rooted binary tree where each node _N_ has an _equality_ key _e<sub>N</sub>_ and a _split_ key _s<sub>N</sub>_. A search for query \(v\in\mathcal{Q}\) starts at the root _r_. If _v=e<sub>r</sub>_, the search halts. Otherwise, the search recurses on the left subtree (if _v\<s<sub>r</sub>_) or the right subtree (if \(v\ge s_r\)). The _cost_ of the tree is the expected number of nodes (including, by convention, leaves) visited for a random query _v_.

Huang and Wong demonstrate that equality keys in optimal gbsts do not have the maximum-likelihood property \[11\]. Fig. 10 shows their counterexample: in the optimal gbst (a), the root equality key is E (frequency 20), not B (frequency 22). The cheapest tree with B at the root is (b), and is more expensive. Having B at the root increases the cost because then the other two high-frequency keys E and F have to be the children, so the split key of the root has to split E and F, and low-frequency keys A, C, and D all must be in the left subtree.

Following \[11\], restrict to successful queries (K=Q). Fix any instance \(\mathcal{I}=(\mathcal{K},\beta)\). For any query interval _I_={_K<sub>i</sub>,K_<sub>_i_+1</sub>_,...,K<sub>j</sub>_} and any subset \(D\subseteq I\) of "deleted" keys, let opt(_I,D_) denote the minimum cost of any gbst that handles the keys in _I_\\_D_. This recurrence follows directly from the definition of gbsts:

**Lemma 12.** _For any query set I_\\_D not handled by a single-node tree,_

\(\text{opt}(I,D)=\omega(I\backslash D)+min_{e,s\in\mathcal{K}}\text{opt}(I_{<s},D_e\cap I_{<s})+\text{opt}(I_{\ge s},D_e\cap I_{\ge s})\)

_where D<sub>e</sub>=D_\\{_e}, and_ \(I_{<s}=\{v\in I:v<s\}\) _and_ \(I_{\ge s}=\{v\in I:v\ge s\}\).

The goal is to compute \(\text{opt}(\mathcal{K},\emptyset)\). Using the recurrence above, exponentially many subsets _D_ arise. This motivates the following lemma. For any node _N_ in an optimal gbst, define _N_’s _key interval, I<sub>N</sub>_, and _deleted-key set, D<sub>N</sub>_, according to the recurrence in the natural way. Then the set Q_<sub>N</sub>_ of queries reaching _N_ is _I<sub>N</sub>_\\_D<sub>N</sub>_, and _D<sub>N</sub>_ contains those keys in _I<sub>N</sub>_ that are in equality tests above _N_, and _I<sub>N</sub>_ contains the key values that, if searched for in _T_ with the equality tests removed, would reach node _N_.

(a)
E 20 D
(b)
B
B
22
22
F
20
E
20
C
F
20
H
B
20
F
A
10
C
10
D
5
G
10
C
10
G
10
A
10
C
10
D
5
E
D
5

**Fig.10.** In a gbst, each node has equality key, frequency, and (if internal) split key.


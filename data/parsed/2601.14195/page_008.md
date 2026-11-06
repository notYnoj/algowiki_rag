**Proposition 3.2.** _A matching that admits a minimum number of blocking agents might not admit a minimax number of blocking pairs per agent, and vice versa._

_Proof._ This follows immediately from the examples in the proof of Proposition 3.1: the first example shows that matching _M_ with a minimum number of blocking agents may have an agent in two blocking pairs, while there exists a matching \(M'\) in which no agent is in more than one blocking pair. Similarly, in the second example, _M_ is a matching where no agent is in more than one blocking pair, but \(M'\) has fewer blocking agents.

**Proposition 3.3.** _A matching that admits a minimax number of blocking pairs per agent might not admit a minimum number of blocking pairs._

_Proof._ Consider the sri instance with preferences as follows:

\(a_1:a_2a_3\)<br>
\(a_2:a_3a_1\)<br>
\(a_3:a_1a_2\)<br>
\(a_4:a_5\)<br>
\(a_5:a_4\)

Clearly the collection of matchings _M<sub>r</sub>_={{_a<sub>r</sub>,a_<sub>_r_+1</sub>},{_a_<sub>4</sub>_,a_<sub>5</sub>}} where \(1\le r\le 3\) and addition taken modulo 3 are the matchings with a minimum number of blocking pairs, but notice that any _M<sub>r</sub>_, but also any \(M'_r=\{\{a_r,a_{r+1}\}\}\), satisfies the minimax constraint, while no \(M'_r\) matching satisfies minimality with respect to the number of blocking pairs.

We are not aware of an instance where a minimum number of blocking pairs does not have a minimax number of blocking pairs per agent.

## 3.3 Further Structural Results

While it is not challenging to construct a family of sri instances where the minimum number of blocking pairs grows linearly with the number of agents, it is not straightforward to construct instances where the minimum maximum number of blocking pairs that any agent is contained in is higher than 1. Hence, one might falsely conclude that this number is constant or even just 1. However, we will now give a construction that shows that, with sufficiently many agents, this number can be arbitrarily large.

**Proposition 3.4.** _For every positive integer k, there exists an_ sri _instance_ \(I=(A,\succ)\) _with n_=3_<sup>k</sup> agents and complete preference lists such that_ \(min_{M\in\mathcal{M}}max_{a_i\in A}|bp_i(M)|=k\).

_Proof._ Suppose that \(k\ge 1\). We will first describe the construction and then prove the desired invariant inductively. The main idea is to build a symmetrical preference system consisting of partitions of sizes that are multiples of 3 (up until a single partition consisting of all agents of size 3_<sup>k</sup>_), such that we have many nested _preference cycles_, where a preference cycle (_f_<sub>_c_<sub>1</sub></sub>_,f_<sub>_c_<sub>2</sub></sub>_,...,f<sub>c<sub>r</sub></sub>_) of length _r_ has the property that each agent _f<sub>c<sub>k</sub></sub>_ prefers their successor _f_<sub>_c<sub>k</sub>_+1</sub> to their predecessor _f_<sub>_c<sub>k</sub>_-1</sub> (where addition and subtraction is taken modulo _r_) in the cycle. Notice that odd-length cycles where every agent ranks their successor and their predecessor in the first and second position of their preference list, respectively, make an instance unsolvable. Here, we draw inspiration from the concept of stable partitions, which characterise the existence of stable matchings in sri instances (see \[38\] for more details).

We construct the instance, which we will denote by _I<sub>k</sub>_, as follows: first, create 3_<sup>k</sup>_ agents _A_={_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a_<sub>3_k_</sub>}. Now partition the agents _a<sub>i</sub>_ into sets of 3 in increasing order of _i_ (starting from 1) and initialise the preference lists such that (_a_<sub>3_r_+1</sub>_,a_<sub>3_r_+2</sub>_,a_<sub>3_r_+3</sub>) form a preference cycle<tbc>


<tbc>at the top of their preference list for all \(0\le r\le\frac{n}{3}-1\). Next, partition the agents _a<sub>i</sub>_ into sets of 9 in increasing order of _i_ (starting from 1) and append the preference lists such that<tbc>

\((\{a_{9r+1},a_{9r+2},a_{9r+3}\},\{a_{9r+4},a_{9r+5},a_{9r+6}\},\{a_{9r+7},a_{9r+8},a_{9r+9}\})\)

<tbc>form a preference cycle for all \(0\le r\le\frac{n}{9}-1\), i.e., such that all agents _a_<sub>9_r_+1</sub>_,a_<sub>9_r_+2</sub>_,a_<sub>9_r_+3</sub> prefer all of _a_<sub>9_r_+4</sub>_,a_<sub>9_r_+5</sub>_,a_<sub>9_r_+6</sub> to all of _a_<sub>9_r_+7</sub>_,a_<sub>9_r_+8</sub>_,a_<sub>9_r_+9</sub>, and so on (we may assume that agents within these sets are listed in increasing indicial order in the preference lists). Continue this process for increasing partition sizes 3_<sup>j</sup>_ up until 3_<sup>k</sup>_, in which case we append the preference lists such that<tbc>

\((\{a_1,a_2,\dots,a_\frac{n}{3}\},\{a_\frac{n}{3}+1,a_\frac{n}{3}+2,\dots,a_\frac{2}{3}n\},\{a_\frac{2}{3}n+1,a_\frac{2}{3}n+2,\dots,a_n\})\)

<tbc>form a preference cycle (notice that at each step _j_, each agent adds \(2\cdot 3^{j-1}\) other agents to the end of their preference list). Figure 2 illustrates the construction of _I_<sub>3</sub> schematically for (i.e., _k_=3, so we have 27 agents).

Notice that, at the end of this construction, all preference lists are complete. Furthermore, notice that, at every step _j_ with partitions of size 3_<sup>j</sup>_, we create nested odd-length cycles such that, from every set in the partition, we are forced to match at least one agent to someone of rank at least 3_<sup>j</sup>_ on their preference list (or leave the agent unmatched). However, due to the preference cycles, this incurs at least _j_ blocking pairs for this agent in every matching of _I_.

Formally, let _P(k_) be the statement that, for the instance _I<sub>k</sub>_ constructed as described above with 3_<sup>k</sup>_ agents, it is the case that \(min_{M\in\mathcal{M}(I_k)}max_{a_i\in A}|bp_i(M)|\ge k\) (where M(_I<sub>k</sub>_) indicates the sets of all matchings of _I<sub>k</sub>_).

Consider the base case where _k_=1: clearly, with three agents that form a preference cycle, any one of the three maximum-cardinality matchings of the instance leaves one agent unmatched and minimises the maximum number of blocking pairs that any agent is contained in. However, the unmatched agent must prefer both matched agents to being unmatched, and exactly one of the matched agents must prefer the unmatched agent to their partner. Thus, \(min_{M\in\mathcal{M}(I_k)}max_{a_i\in A}|bp_i(M)|\ge 1=k\).


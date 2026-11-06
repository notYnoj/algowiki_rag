# Matching Dynamics with Constraints<sup>⋆</sup>

**Abstract.** We study uncoordinated matching markets with additional local constraints that capture, e.g., restricted information, visibility, or externalities in markets. Each agent is a node in a fixed matching network and strives to be matched to another agent. Each agent has a complete preference list over all other agents it can be matched with. However, depending on the constraints and the current state of the game, not all possible partners are available for matching at all times.

For correlated preferences, we propose and study a general class of hedonic coalition formation games that we call coalition formation games with constraints. This class includes and extends many recently studied variants of stable matching, such as locally stable matching, socially stable matching, or friendship matching. Perhaps surprisingly, we show that all these variants are encompassed in a class of "consistent" instances that always allow a polynomial improvement sequence to a stable state. In addition, we show that for consistent instances there always exists a polynomial sequence to every reachable state. Our characterization is tight in the sense that we provide exponential lower bounds when each of the requirements for consistency is violated.

We also analyze matching with uncorrelated preferences, where we obtain a larger variety of results. While socially stable matching always allows a polynomial sequence to a stable state, for other classes different additional assumptions are sufficient to guarantee the same results. For the problem of reaching a _given_ stable state, we show NP-hardness in almost all considered classes of matching games.

### 1 Introduction

Matching problems are at the basis of many important assignment and allocation tasks in computer science, operations research, and economics. A classic approach in all these areas is _stable matching_, as it captures distributed control and rationality of participants that arise in many assignment markets. In the standard two-sided variant, there is a set of men and a set of women. Each man (woman) has a preference list over all women (men) and strives to be matched to one woman (man). A (partial) matching _M_ has a blocking pair (_m,w_) if both _m_ and _w_ prefer each other to their current partner in _M_ (if any). A matching<tbc>

<sup>⋆</sup> Supported by DFG Cluster of Excellence MMCI and grant Ho 3831/3-1.

Martin Hoefer<sup>1</sup> and Lisa Wagner<sup>2</sup>

<sup>1</sup> Max-Planck-Institut für Informatik and Saarland University, Germany `mhoefer@mpi-inf.mpg.de`

<sup>2</sup> Dept. of Computer Science, RWTH Aachen University, Germany `lwagner@cs.rwth-aachen.de`


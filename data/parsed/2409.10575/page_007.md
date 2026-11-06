<tbc>variant, TBLS-E. The TBLS algorithm is illustrated in Algorithm 1. TBLS starts to find an efficient strategy _S<sub>best</sub>_ and a maximum stable matching _M<sub>best</sub>_ by arbitrarily breaking all the ties and implementing a base algorithm, as outlined in lines 2-5 of Algorithm 1. In each iteration, TBLS performs three steps. First, it refines the current tie-breaking strategy _S_ using the subroutine `RefineTieBreakingStrategy`. Following this refinement, it obtains a corresponding stable matching _M_ using the subroutine `ObtainStableMatching`. Lastly, if _M<sub>best</sub>_ is found to be worse than _M_ according to the evaluation function _E_, then _M_ and _S_ are assigned to _M<sub>best</sub>_ and _S<sub>best</sub>_, respectively, as specified in lines 10-13 of Algorithm 1. TBLS-E is developed by incorporating two key modifications into the original TBLS framework, the details of which are provided in Section 4.4.

In each iteration, the time complexity of TBLS using GS as the base algorithm is _O(n_<sup>2</sup>), whereas that of TBLS-E using PDB as the base algorithm is _O(n_<sup>3</sup>). The overall space complexity of both algorithms is _O(n_<sup>3</sup>). A detailed complexity analysis is provided in Section S1 of Online Resource 1.

Next, we describe the main concepts of these two subroutines:

`RefineTieBreakingStrategy` refines the current tie-breaking strategy by adjusting the relative order within ties. These adjustments, based on preference ranks and the current stable matching, aim to improve the rank of selected free agents in the preference lists of their respective candidates, thereby increasing their chances of being matched. Each adjustment targets a free agent and one of its candidates, purposefully introducing a BP to alter the current stable matching. When this subroutine is invoked, an adjustment is selected randomly to refine the strategy. Moreover, when no adjustments are available, or with a small probability, the current tie-breaking strategy is disrupted to prevent local optima by randomly adjusting some ties.

`ObtainStableMatching` obtains a stable matching by either removing BPs or directly using the base algorithm. Given the minor updates to the preference lists during each refinement, attaining a stable matching from the existing matching by removing BPs is typically more efficient than applying the base algorithm. Moreover, this characteristic enables the examination of only a specific subset of agents to identify and eliminate potential BPs, rather than re-evaluating the entire set of agents. Therefore, to effectively obtain a stable matching after the refinement process, a BP removal process is developed to identify and eliminate UBPs. To prevent this process from becoming trapped in an endless cycle, a time threshold is established. Once this threshold is exceeded, the subroutine shifts to applying the base algorithm to secure a stable matching.

The rest of this section is structured as follows: Section 4.1 discusses the evaluation function, Section 4.2 examines the subroutine `RefineTieBreakingStrategy`,<tbc>

\begin{tabular}{cc}
Men’s preference list & Women’s preference list \\
_m_<sub>1</sub>:(_w_<sub>1</sub>_w_<sub>3</sub>)_w_<sub>2</sub> & _w_<sub>1</sub>:_m_<sub>1</sub>_m_<sub>3</sub>_m_<sub>2</sub> \\
_m_<sub>2</sub>:_w_<sub>1</sub>_w_<sub>2</sub>_w_<sub>4</sub> & _w_<sub>2</sub>:(_m_<sub>2</sub>_m_<sub>4</sub>)_m_<sub>1</sub> \\
_m_<sub>3</sub>:_w_<sub>1</sub> & _w_<sub>3</sub>:_m_<sub>1</sub> \\
_m_<sub>4</sub>:_w_<sub>2</sub> & _w_<sub>4</sub>:_m_<sub>2</sub> \\
\end{tabular}

** 1** An SMTI example of size 4


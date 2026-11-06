# Fast Indexes for Gapped Pattern Matching<sup>⋆</sup>

**Abstract.** We describe indexes for searching large data sets for variable- length-gapped (VLG) patterns. VLG patterns are composed of two or more subpatterns, between each adjacent pair of which is a gap-constraint specifying upper and lower bounds on the distance allowed between sub- patterns. VLG patterns have numerous applications in computational biology (motif search), information retrieval (e.g., for language models, snippet generation, machine translation) and capture a useful subclass of the regular expressions commonly used in practice for searching source code. Our best approach provides search speeds several times faster than prior art across a broad range of patterns and texts.

### 1 Introduction

In the classic pattern matching problem, we are given a string P (the pattern or query) and asked to report all the positions where it occures in another (longer) string T (the text). This problem has been very heavily studied and has applications throughout computer science.

In this paper we consider a variant on the classic pattern matching problem, called variable length gap (VLG) pattern matching. In VLG matching, the query P is not a single string but is composed of \(k\ge 2\) strings (subpatterns) that must occur in order in the text. Between each subpattern, a number of characters may be allowed to occur, an upper and lower bound on which is specified as part of the query. Formally, our problem is as follows.

**Definition 1 (Variable Length Gap (VLG) Pattern Matching [4]).** _Let_ T _be a string of n symbols drawn from alphabet_ \(\Sigma\) _and_ P _be a pattern consisting of_ \(k\ge 2\) _subpatterns (i.e. strings) p_<sub>0</sub>_,...,p_<sub>_k_-1</sub>_, each consisting of symbols also drawn from_ \(\Sigma\)_, and having lengths m_<sub>0</sub>_,...,m_<sub>_k_-1</sub>_, and k_-1 _gap constraints C_<sub>0</sub>_,...,C_<sub>_k_-2</sub>_, such that_ \(C_i=\langle\delta_i,\Delta_i\rangle\) _with_ \(0\le\delta_i\le\Delta_i<n\) _specifies the smallest (_\(\delta_i\)_) and largest (_\(\Delta_i\)_) allowable distance between a match of pi and pi_<sub>_i_+1</sub> _in_ T_. Find all matches — reported as k-tuples i_<sub>0</sub>_,...,i_<sub>_k_-1</sub> _where i<sub>j</sub> is the starting position for subpattern p<sub>j</sub> in_ T _-- such that all gap constraints are satisfied._

<sup>⋆</sup> This research is supported by Academy of Finland through grant 319454.

Manuel Cáceres<sup>1</sup>, Simon J. Puglisi<sup>2</sup>, and Bella Zhukova<sup>2</sup>

<sup>1</sup> Department of Computer Science, University of Chile Santiago, Chile **mcaceres@dcc.uchile.cl** <sup>2</sup> Department of Computer Science, University of Helsinki Helsinki Institute for Information Technology (HIIT) Helsinki, Finland {puglisi,bzhukova}@cs.helsinki.fi


<tbc>pattern, from which a representative motif pair is then derived from the sequences labeling the nodes. Motif- driven approaches, by contrast, begin with candidate motif pairs and evaluate their support directly in the PPI network. While both paradigms have been shown to yield biologically meaningful results, the motif-driven approach has several conceptual advantages over its interaction-driven counterpart. First, motif pairs are identified directly rather than derived in post-processing. Second, all proteins containing a given motif are taken into account, rather than an arbitrarily selected subset. Third, when the interactions between two groups of proteins arise from multiple compatible binding sites--e.g., \(\{\mathsf{G}\diamond\diamond\mathsf{P}\diamond\mathsf{NY},\mathsf{P}\diamond\diamond\mathsf{P}\}\) and \(\{\mathsf{R}\diamond\mathsf{R}\diamond\diamond\mathsf{pS},\mathsf{L}\diamond\mathsf{R}\diamond\diamond\mathsf{pS}\}\) in Figure 1.1-- interaction-driven methods are forced to merge them into one motif pair, thereby losing this structural distinction.

## 1.1 The problem and the state of the art.

In this paper, we focus on the motif-driven approach to CMM. The vanilla version of the problem is defined as follows.

We next define the CMM problem _with wildcards_; wildcards are placeholder symbols, denoted by \(\diamond\), that can match any character from the underlying alphabet.

While we formalize the problems in a general form, the motivating application leads us to use the following widely-used support measures \[1,15,25\]: the count _f<sub>E</sub>_ of edges \(\{u,v\}\in E\) such that _X_ matches a substring of _u_<tbc>

<tbc>and _Y_ matches a substring of _v_, or vice versa; and the \(\chi^2\)-score \(f_{\chi^2}\) of _G_ with respect to {_X,Y_} \[25\].

To the best of our knowledge, three techniques have so far been proposed. Unfortunately, these techniques differ not only in their mining method, but also in the matching relation and the support measure used.

The first work by Tan et al. \[25\] introduced D- MOTIF, an exact algorithm for finding correlated motif pairs under the Hamming distance. D-MOTIF considers \(f_{\chi^2}\) to quantify support. The basic idea of the algorithm is to enumerate all possible motif pairs from every pair \(\{u,v\}\in E\), using the _Hamming distance neighborhood_ notion, and then check if they have enough support. The authors also suggested a heuristic counterpart called D- STAR. Unfortunately, neither D-MOTIF nor D-STAR scales to networks with more than 250 proteins.

The second work by Leung et al. \[15\] introduced FindMotif, an exact algorithm for \((\ell,d)\)-CMM. FindMotif uses a different support measure that considers the probability that the observed number of interactions is generated under a null hypothesis. The algorithm builds a table of \(\mathcal{O}(\genfrac(){pt}{2}{\ell}{d}^2|\Sigma|^{2(\ell-d)})\) entries, one per possible motif pair over alphabet \(\Sigma\), and computes the support for each using a _voting_ technique. The authors also suggested a heuristic counterpart called MotifHeuristics, which was able to handle larger networks than D-STAR.

The third work by Boyen et al. \[1\] proved that \((\ell,d)\)-CMM is NP-hard for so-called _compliant bicliquemaximal_ measures, which include _f<sub>E</sub>_ and \(f_{\chi^2}\). They also introduced SLIDER, a generic metaheuristic that incorporates two _steepest-ascent_ procedures. The central component of these procedures is a neighborhood function defined by viewing a motif as a window that slides along the protein sequence of one of the proteins. Unlike more conventional neighborhood functions, this has a clear biological interpretation: if a motif partially overlaps a binding site in a sequence, a few mutations should suffice to convert it into a binding site. In this sense, both neighborhood functions are designed to identify nearby motifs that may correspond to regions close to one another on actual proteins. The difference is that one neighborhood function considers as neighbors all motifs that could, in principle, lie near the given motif on any protein, whereas the other restricts attention to motifs that are actually nearby on a single selected protein. Although SLIDER can be paired with an arbitrary support measure, the authors used \(f_{\chi^2}\), providing compelling evidence that it is biologically the most relevant, and showing that SLIDER outperforms MotifHeuristics.

## 1.2 Our contributions.

Since the motif-driven approach to CMM is computationally hard, in general \[1\], it is widely believed that _exact optimization_ is imprec<tbc>

GRSPPNY
RNRGSpS
PRSP
RRRpPpS
LGRPSpS
GRRPSNY
PGPP

Correlated Motif Mining (CMM)
Input:
A graph G=(V,E), with V
for an alphabet Σ, and an integer >0.
Output:
A pair {X,Y}, with X,Y ∈ Σ
that maximizes a support measure f(G, {X,Y}).

CMM with Wildcards ((Ld)-CMM)
Input:
A graph G=(V,E), with V
for an alphabet Σ, and integers >0 and 0 d
Output:
A pair {X,Y}, with X,Y ∈ Σ {o})
each containing exactly d wildcards, that maximizes a support measure f(G, {X,Y}).

Figure 1.1: Motif pairs \(\{\mathsf{G}\diamond\diamond\mathsf{P}\diamond\mathsf{NY},\mathsf{P}\diamond\diamond\mathsf{P}\}\) and \(\{\mathsf{R}\diamond\mathsf{R}\diamond\diamond\mathsf{pS},\mathsf{L}\diamond\mathsf{R}\diamond\diamond\mathsf{pS}\}\) as correlated motifs. The colored edges show their correlation.


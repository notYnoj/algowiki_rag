to [13], Algorithm _PROJECTION_ due to [14], Algorithm _Gibbs DNA_ due to [15], Algorithm _WINNOWER_ due to [16], and Algorithm _Random Projection_ due to [17]. Some other approximate PMS algorithms are Algorithm _MULTIPROFILER_ due to [18], Algorithm _PatternBranching_ due to [19] and Algorithm _CONSENSUS_ due to [20].

## Algorithm MEME

The MEME algorithm extends the EM algorithm for identifying motifs in unaligned sequences. While a drawback of EM is that the maximum it finds is only local, MEME can either favor motifs that appear exactly once or appear zero or once in each sequence in a training set, or give no preference to a number of occurrences. In 2005 _Hall et al_ acquired a set of correlated genes from genomic, transcriptomic and proteomic analyses. They applied MEME to scan 1000 bp of the 3’ end of stop codon, where a 47 bp motif was found in six of the analyzed sequences. Then it was used to search the entire genome and 20 additional genes were identified to have the same motif. This motif was known to be bound to Puf protein, implying that Puf protein may control the transcription of the analyzed genes.

## Algorithm Projection

This algorithm ameliorates the limitations of existing algorithms by using random projections of input. It extends previous projection-based searching techniques to solve a multiple alignment problem that is not effectively addressed by pairwise alignments. It is designed to efficiently solve the problems from the planted (_l,d_)-motif model and can do more reliably and substantially difficult instances than previous algorithms. For _t_=20 and _n_=600 this algorithm achieves performance close to the best possible, being limited primarily by statistical considerations.

## Algorithm Winnower, SP-STAR, and cWinnower

Winnower first represents motif instances as vertices then it tries to delete spurious edges and recover motifs with the remaining vertices. SP-STAR is a local sum of pairwise score improvement algorithm which considers only the subsequences present in dataset and iteratively updates scores of the motifs. cWinnower improves its running time by a stronger constraint function.


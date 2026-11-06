<tbc>sophisticated. Motif search also has many applications in solving some crucial biological problems. For example, finding motifs in DNA sequences is very important for the determination of open reading frames, identification of gene promoter elements, location of RNA degradation signals and the identification of alternative splicing sites [3]. In protein sequences, patterns have led to domain identification, location of protease cleavage sites, identification of signal peptides, protein interactions, determination of protein degradation elements, identification of protein trafficking elements etc. So we can agree to the fact that, motif identification plays an important role in biological studies.

### 1.1.2 Regulatory Regions and Transcription Factor Binding Sites

DNA regions involved in transcription and transcriptional regulation are called regulatory regions (RR). Every gene contains a RR typically stretching 100-1000 bp upstream of the transcriptional start site. A transcription factor (TF) is a protein that can bind to DNA and regulate gene expression. TFs influence gene expression by binding to a specific location in the respective genes regulatory region which is known as TFBSs or motifs. TFBSs are a part of either the promoter or enhancer region of a gene.

## 1.2 The Motif Finding Problem

Our target is to identify transcription factor binding sites or motif from a DNA sequence. We are given a set of DNA sequences of specified length and the length of the motif. We choose a position from every sequence which will be the starting sequence for the motif candidates Figure 1.1. Taking these sequences we make alignment matrix, profile matrix and finally consensus string. Then we evaluate the consensus string with the help of a scoring function. Now, we have to find the starting position for which the score of the consensus string will be maximum. It is the informal description of the motif searching problem.

### 1.2.1 Classification of Motif Searching Algorithms

For the importance of motifs, various motif finding algorithms have been researched and applied for the last two decades. We can classify these algorithms in to three categories. All motif searching algorithms follow one of the three approaches:

• **Combinatorial Approach :** Tries to explore exhaustively all the ways that a molecular process could happen thus leads to hard combinatorial problems for which efficient algorithms are required.


<tbc>scription factor binding site, and the RNA polymerase binding site. In Figure 2.12 we see a picture of promoter and enhancer. An enhancer is usually far upstream of a gene.

## 2.5 To The Motif Finding Problem

Our target is to identify a motif from a DNA sequence. In our study we only deal with transcription factor binding sites. We will give the formal definition of the motif finding problem later. Assume that we are given some DNA sequence of nucleotides which are generated randomly. Now, we want to find a secret pattern that occurs at least one time in every given DNA sequence without any prior knowledge about how it looks like. This pattern is our motif.

Some complications encountered while finding motifs:

• We do not know the motif sequence.

• Hence we donot know what to search for in the DNA sequence.

• We do not know where the motifs are located relative to the starting index of the sequence.

• Motifs can differ in one or more positions in their sequence which is called mutations.

Regulatory sequence
Regulatory sequence
Enhancer /silencer
Promoter
5'UTR
Open reading frame
/silencer
Proximal
Core
Start
Stop
DNA
Transcription
Exon
Exon
Intron
Intron
mRNA
Post-transcription modification
Protein coding region
5'cap
Poly-A tail
Mature mRNA
Translation
Protein

Enhancer Region
Regulatory Protein Binding Site
Transcription Factor Binding Site
RNA polymerase Binding Site
Transcribed Region (Gene)
Untranscribed DNA
Upstream
Downstream
Promoter Region

Figure 2.11: The structure of a eukaryotic protein-coding gene.

Figure 2.12: Transcription Factor Binding Sites.


## 2.4 Motifs in Details

Motif usually means a pattern. For any sequence of objects to be called a pattern, it has to have at least more than one instance. To define more precisely, a motif should have significantly higher occurrence in a given array or list compared to what you would obtain in a randomized array of same components. Here array means an arranged set such as a genome or a protein structure. Genome is an array of nucleotides and protein structure is an array of amino acids.

### 2.4.1 Sequence Motifs

By sequence motif we mean a pattern of nucleotide or amino acid that has specific biological significance. In other words, they are pattern of a DNA array or protein sequence. They may be also called regulatory sequence motifs. This kind of motifs are commonly studied in bioinformatics. They are becoming increasingly important in the analysis of gene regulation. In our thesis we will only discuss about this type of motifs.

\begin{tabular}{cccccccc}
\multicolumn{8}{c}{**Second base**}\\
 & **U** & **C** & **A** & **G** & & & \\
 & UUU & UU & UAU & TYR & UGU & U & \\
 & UUC & PHE & UCC & UAC & UGC & CYS & \\
 & UUA & UCA & SER & UAA & UGA & STOP & \\
 & UUG & LEU & UCG & UAG & UGG & TRP & A\\
 & & & & & & & \\
 & CUU & CCU & CAU & HIS & CGU & U & \\
 & CUC & CCC & CAC & CGC & ARG & T & \\
 & CUA & LEU & PRO & CAA & GLN & CGA & \\
 & CUG & CCA & CCG & CAG & CGG & G & \\
 & & & & & & & \\
 & AUU & ACU & AAU & ASN & AGU & U & \\
 & AUC & ILE & ACC & AAC & AGC & SER & \\
 & AUA & ACA & THR & AAA & AGA & C & \\
 & AUG & MET or START & ACG & AAG & LYS & AGG & A\\
 & & & & & & & \\
 & GUU & GCU & GAU & ASP & GGU & U & \\
 & GUC & GCC & GAC & GGC & GLY & C & \\
 & GUA & VAL & ALA & GAA & GGA & A & \\
 & GUG & GCA & GCG & GAG & GLU & GGG & G\\
\end{tabular}

Figure 2.10: The genetic code, from the perspective of mRNA.


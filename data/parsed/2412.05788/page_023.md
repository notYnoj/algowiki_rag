## C Experimental Setup

### C.1 Benchmark Problems

In the following benchmarks, we fix the motif placement by taking the median of scaffold length ranges in their specifications like Wu et al. (2023). We isolate this variability to provide a less stochastic comparison of the methods over small sample sizes.

### Motif Scaffolding Benchmark.

Problems in the RFDiffusion motif scaffolding benchmark are listed in  4. Excluding 6VW1, which involves multiple chains, there are 24 problems involving different motif types, lengths, and contiguity. Where the length and configuration define a range, we can design any length scaffold that fits those specifications but choose to fix the configuration in our experiments.

### Multi-Motif Scaffolding Benchmark.

Problems in the Genie2 multi-motif scaffolding benchmark are listed in  5. In the Genie2 pre-print, problem 3NTN had a configuration with ranges in reverse, but the specification differed from their GitHub repository. We chose to work with the ranges specified in their repository and made the correction in  5.

\begin{tabular}{cccc}
**Name** & **Description** & **Configuration** & **Length** \\
1PRW & Double EF-hand motif & 5-20, **A16-35**, 10-25, **A52-71**, 5-20 & 60-105 \\
1BCF & Di-iron binding motif & 8-15, **A92-99**, 16-30, **A123-130**, 16-30, **A47-54**, 16-30, **A18-25**, 8-15 & 96-152 \\
5TPN & RSV F-protein Site V & 10-40, **A163-181**, 10-40 & 50-75 \\
5IUS & PD-L1 binding interface on PD- 1 & 0-30, **A119-140**, 15-40, **A63-82**, 0-30 & 57-142 \\
3IXT & RSV F-protein Site II & 10-40, **P254-277**, 10-40 & 50-75 \\
5YUI & Carbonic anhydrase active site & 5-30, **A93-97**, 5-20, **A118-120**, 10-35, **A198-200**, 10-30 & 50-100 \\
1QJG & Delta5-3-ketosterol isomerase active site & 10-20, **A38**, 15-30, **A14**, 15-30, **A99**, 10-20 & 53-103 \\
1YCR & P53 helix that binds to Mdm2 & 10-40, **B19-27**, 10-40 & 40-100 \\
2KL8 & De novo designed protein & **A1-7**, 20, **A28-79** & 79 \\
7MRX\_60 & Barnase ribonuclease inhibitor & 0-38, **B25-46**, 0-38 & 60 \\
7MRX\_85 & Barnase ribonuclease inhibitor & 0-68, **B25-46**, 0-63 & 85 \\
7MRX\_128 & Barnase ribonuclease inhibitor & 0-122, **B25-46**, 0-122 & 128 \\
4JHW & RSV F-protein Site 0 & 10-25, **F196-212**, 15-30, **F63-69**, 10-25 & 60-90 \\
4ZYP & RSV F-protein Site 4 & 10-40, **A422-436**, 10-40 & 30-50 \\
5WN9 & RSV G-protein 2D10 site & 10-40, **A170-189**, 10-40 & 35-50 \\
5TRV\_short & De novo designed protein & 0-35, **A45-65**, 0-35 & 56 \\
5TRV\_med & De novo designed protein & 0-65, **A45-65**, 0-65 & 86 \\
5TRV\_long & De novo designed protein & 0-95, **A45-65**, 0-95 & 116 \\
6E6R\_short & Ferridoxin Protein & 0-35, **A23-35**, 0-35 & 48 \\
6E6R\_med & Ferridoxin Protein & 0-65, **A23-35**, 0-65 & 78 \\
6E6R\_long & Ferridoxin Protein & 0-95, **A23-35**, 0-95 & 108 \\
6EXZ\_short & RNA export factor & 0-35, **A28-42**, 0-35 & 50 \\
6EXZ\_med & RNA export factor & 0-65, **A28-42**, 0-65 & 80 \\
6EXZ\_long & RNA export factor & 0-95, **A28-42**, 0-95 & 110 \\
\end{tabular}

4: **RFDiffusion motif scaffolding benchmark details.** The specification for each scaffolding problem is under "Configuration", with the motif structures in bold. For example, in motif 2KL8, the problem requires a protein that contains residues 1-7 and 28-79 from chain A of the motif, joined together by a scaffold of 20 residues. Furthermore, the total length of the generated protein must fall in the range specified in the "Length" column.


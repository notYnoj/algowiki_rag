• **Probabilistic Approach :** Makes certain decisions randomly by extending the classical model of deterministic algorithms. They are often faster, simpler and more elegant than their combinatorial counterparts.

• **Phylogenetic Footprinting Approach :** Discovers regulatory elements in a set of orthologous regulatory regions from multiple species by identifying the best conserved motifs in those orthologous regions.

## 1.2.2 Combinatorial Approach

Among the various approaches combinatorial approach that has proven to be more accurate than the others. In our approach we will use combinatorial algorithms for the discovery of motifs. The are several versions of this approach. Mosty used three versions are:

• Planted Motif Search (PMS)

• Simple Motif Search (SMS)

• Edited-distance-based Motif Search (EMS) [4]

## 1.2.3 Planted Motif Search (PMS)

Among different versions of combinatorial approaches the PMS problem is more popular due to its closeness to motif reality. Motifs typically occur with mutations at binding sites. The binding sites are referred to as instances of a motif. A motif in PMS is referred to as a (_l,d_)- motif where _l_ is its length and _d_ is the maximum number of mutations allowed for its instances. Given a set of n sequences, the PMS Algorithm tries to find all the (_l,d_)-motifs in them. The PMS problem is essentially the same as the closest substring problem.

motif start index
gene start
S1
S2
S3
S4
St

Figure 1.1: Starting index of motifs in a DNA sequence .


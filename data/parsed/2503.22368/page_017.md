# Maximum Common Subgraphs

<tbc>_Y_ are connected subgraphs of a molecule, _M_<sub>1</sub>, their intersection (\(Y\cap X\)) may easily be disconnected. This oversight implies that the output might not fulfill the connectedness criterion as claimed, a critical issue that our approach carefully addresses. These shortcomings underscore the necessity for both theoretical validation and practical accessibility, aspects that our work robustly provides.

Finally, the literature exhibits a rich variety of approaches to the MCS problem. While many early methods focused on exact solutions for two molecular graphs using either MCIS or MCES formulations, more recent work has diversified to include approximate methods, DP for special graph classes, and algorithms that extend to multiple molecules. The choice of method, whether it is an exact, connected MCIS algorithm such as that by McGregor [36] or a disconnected MCES approach like RASCAL [34,35], remains highly application- specific and depends on factors such as graph sparsity, the extent of chemical labeling, and the intended scope of similarity assessment. Continued efforts to establish standardized benchmarking [47,48] and to develop publicly available implementations are critical to further advancing this field [49,50].

### Acknowledgements

This work was funded by the Novo Nordisk Foundation as part of the project MATOMIC (Mathematical Modelling for Microbial Community Induced Metabolic Diseases, 0066551) and from the European Unions Horizon Europe Doctoral Network programme under the Marie-Skłodowska-Curie grant agreement No 101072930 (TACsy – Training Alliance for Computational systems chemistry).

### References


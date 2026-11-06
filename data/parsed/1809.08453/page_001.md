# Optimizing a Generalized Gini Index in Stable Marriage Problems: NP-Hardness, Approximation and a Polynomial Time Special Case

**Hugo Gilbert** \(\cdot\) **Olivier Spanjaard**

the date of receipt and acceptance should be inserted later

**Abstract** This paper deals with fairness in stable marriage problems. The idea studied here is to achieve fairness thanks to a Generalized Gini Index (GGI), a well-known criterion in inequality measurement, that includes both the egalitarian and utilitarian criteria as special cases. We show that determining a stable marriage optimizing a GGI criterion of agents’ disutilities is an NP-hard problem. We then provide a polynomial time 2-approximation algorithm in the general case, as well as an exact algorithm which is polynomial time in the case of a constant number of non-zero weights parametrizing the GGI criterion.

**Keywords** Stable marriage problem \(\cdot\) Fairness \(\cdot\) Generalized Gini index \(\cdot\) Complexity

### 1 Introduction

Since the seminal work of Gale and Shapley [1962] on stable marriages, matching problems under preferences have been extensively studied both by economists and computer scientists. These problems involve two sets of agents (also called individuals in the sequel) that should be matched with each other while taking agents’ preferences into account. The results obtained in the field have a tremendous number of applications, among which the National Resident Matching Program in the US (for allocating junior doctors to hospitals), the teacher allocation in France (for allocating newly tenured teachers to schools) or the allocation of lawyers in Germany (for assigning graduating lawyers to legal internship positions). For an overview of the applications of matching models under preferences, the interested reader can refer to a recent book chapter on this topic [Biró, 2017].

The _stable marriage problem_ involves _n_ men and _n_ women, each of whom ranks the members of the opposite sex in order of preference. The goal is to find a _stable_ matching, i.e., a matching between men and women such that there is no man and woman that prefer each other to their current match. Gale and Shapley [1962] provided an algorithm that computes a stable marriage. However, it is well-known that this algorithm favours one group (men or women, according to the way the algorithm is applied) over the other.

H. Gilbert \(\cdot\) O. Spanjaard Sorbonne Université, CNRS, Laboratoire d’Informatique de Paris 6, LIP6, F-75005 Paris, France E-mail: {hugo.gilbert,olivier.spanjaard}@lip6.fr


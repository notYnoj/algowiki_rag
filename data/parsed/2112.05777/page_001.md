Theory of and Experiments on Minimally Invasive Stability Preservation in Changing Two-Sided Matching Markets

**Abstract**

Following up on purely theoretical work of Bredereck et al. [AAAI 2020], we contribute further theoretical insights into adapting stable two-sided matchings to change. Moreover, we perform extensive empirical studies hinting at numerous practically useful properties. Our theoretical extensions include the study of new problems (that is, incremental variants of ALMOST STABLE MARRIAGE and HOSPITAL RESIDENTS), focusing on their (parameterized) computational complexity and the equivalence of various change types (thus simplifying algorithmic and complexity-theoretic studies for various natural change scenarios). Our experimental findings reveal, for instance, that allowing the new matching to be blocked by a few pairs significantly decreases the necessary differences between the old and the new stable matching.

## 1 Introduction

In our dynamic world, change is omnipresent in society and business.<sup>1</sup> Typically, there is no permanent stability. We address this issue in the context of stable matchings in two-sided matching markets and their adaptivity to change. Consider as an example the dynamic nature of centrally assigning students to public schools. Here, students are matched to schools, trying to accommodate the students’ preferences over the schools as well as possible. However, due to students reallocating or deciding to visit a private school, according to Feigenbaum et al. [2020], in New York typically around 10% of the students drop out after a first round of assignments, triggering some readjustments in the school-student matchings in a further round.

Matching students to schools can be modeled as an instance of the HOSPITAL RESIDENTS problem, where we are given a set of residents and hospitals each with preferences over the agents from the other set. One wants to find a "stable" assignment of each resident to at most one hospital such that a given capacity for each hospital is respected. To model the task of adjusting a matching to change, Bredereck et al. [2020] introduced the problem, given a stable matching with respect to some initial preference profile, to find a new matching which is stable with respect to an updated preference profile (where some agents performed swaps in their preferences) and which is as similar as possible to the given matching. They referred to this as the "incremental" scenario and studied the computational complexity of this question for STABLE MARRIAGE and STABLE ROOMMATES (both being one-to-one matching problems).

<sup>1</sup>Motivated by this, Boehmer and Niedermeier [2021] recently challenged the computational social choice community to adapt classical models to also account for dynamic aspects.

Niclas Boehmer, Klaus Heeger, Rolf Niedermeier Technische Universität Berlin, Faculty IV, Algorithmics and Computational Complexity, Berlin, Germany {niclas.boehmer, heeger, rolf.niedermeier}@tu-berlin.de

December 14, 2021


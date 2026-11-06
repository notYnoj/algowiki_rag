## Contents

**1 Introduction 1**<tbc>

1.1 Our Results ..... 2<tbc>

1.2 Techniques ..... 3<tbc>

1.3 Other Related Work ..... 4<tbc>

**2 Preliminaries 5**<tbc>

**3 Technique Overview 5**<tbc>

3.1 High-Level Idea: Storing Flows in \(\widetilde{O}(n^{1.5})\) Space ..... 6<tbc>

3.2 Review of LS Central Path/Interior Point Method ..... 8<tbc>

3.3 Streaming Implementation ..... 10<tbc>

**4 Low Space Implementation of IPM 12**<tbc>

4.1 Overview of Analysis ..... 12<tbc>

4.2 Recap of IPM ..... 13<tbc>

4.3 Implicit Representation of \(\tau\) ..... 15<tbc>

4.4 Implicit Representation of _g_ ..... 16<tbc>

4.5 Implicit Representation of _x_, _s_ ..... 18<tbc>

4.6 Constructing matrix **H**, dual \(\delta_y^t\) and _y<sup>t</sup>_, and artificial variable \(\delta_c^t\) ..... 18<tbc>

4.7 Constructing the Next Transcript ..... 18<tbc>

**5 Constructing the Gradient** _g_ **20**<tbc>

**6 Initial Flow and Complete Algorithm 22**<tbc>

6.1 Initial Point & Auxiliary Graph ..... 22<tbc>

6.2 Final Point & Existence of Nearby Exact Solution ..... 23<tbc>

6.3 Putting Everything Together ..... 24<tbc>

**A Discussion on Space Upper and Lower Bounds 31**<tbc>

**B Basic Algebra Facts and Inequalities 34**<tbc>


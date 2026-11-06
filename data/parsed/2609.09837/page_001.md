# On the Parameterized Complexity of Coloring Discovery

Eric Decker and Sebastian Siebertz

University of Bremen, Bremen, Germany

**Abstract.** Coloring Discovery asks whether a possibly improper initial coloring can be made proper within a prescribed number of allowed changes. We study the parameterized complexity of three modification step models that were studied previously in the literature: recoloring one vertex (color flipping), swapping the colors of arbitrary vertices (color swapping), and swapping colors only across an edge (color sliding). For color flipping, we give exact fixed-parameter algorithms for the parameters vertex cover and distance to complete. For color swapping, we obtain fixed-parameter tractability for the parameter vertex cover plus the number of colors. Our lower bounds show W[1]-hardness for treedepth plus feedback vertex set in the color flipping model and for the number of colors plus bandwidth or distance to disjoint paths in the swapping and sliding models. All three variants remain NP-complete with four colors on graphs of diameter two.

**Keywords:** Solution discovery · parameterized complexity · graph coloring repair · structural parameters

### 1 Introduction

Several established algorithmic models study how existing solutions can be adapted rather than computed from scratch. In combinatorial reconfiguration, one is given two feasible solutions and asks whether one can be transformed into the other by a sequence of small modifications, usually requiring every intermediate configuration to remain feasible [9,23]. Local search explores a prescribed neighborhood of a current solution, aiming to find a solution with improved costs [1,12]. Reoptimization starts with a solution to an original instance and studies how this information can be exploited after the instance changes [4,32]. In recoverable robust optimization, an initial solution is chosen so that, after an uncertain scenario is revealed, it can be turned into a feasible solution using only limited recovery actions [27].

Many graph coloring applications have this dynamic character. Consider an examination timetable that has already been published. The vertices represent exams, an edge joins two exams that cannot take place simultaneously, and the colors represent time slots. A late change in enrollments may introduce a new conflict between two exams that currently occupy the same slot, so that the existing timetable is no longer feasible. Computing an arbitrary proper coloring<tbc>


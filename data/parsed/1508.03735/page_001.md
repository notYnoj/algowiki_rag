# Coordination Complexity: Small Information Coordinating Large Populations

**Abstract**

We study a quantity that we call _coordination complexity_. In a distributed optimization problem, the information defining a problem instance is distributed among _n_ parties, who need to each choose an action, which jointly will form a solution to the optimization problem. The coordination complexity represents the minimal amount of information that a centralized coordinator, who has full knowledge of the problem instance, needs to broadcast in order to coordinate the _n_ parties to play a nearly optimal solution.

We show that upper bounds on the coordination complexity of a problem imply the existence of good jointly differentially private algorithms for solving that problem, which in turn are known to upper bound the price of anarchy in certain games with dynamically changing populations.

We show several results. We fully characterize the coordination complexity for the problem of computing a many-to-one matching in a bipartite graph by giving almost matching lower and upper bounds. Our upper bound in fact extends much more generally, to the problem of solving a linearly separable convex program. We also give a different upper bound technique, which we use to bound the coordination complexity of coordinating a Nash equilibrium in a routing game, and of computing a stable matching.

<sup>∗</sup>Computing and Mathematical Sciences, California Institute of Technology; Email: {`rachelc`, `katrina`}@caltech.edu; Supported in part by NSF grant CNS-1254169, US-Israel Binational Science Foundation grant 2012348, the Charles Lee Powell Foundation, a Google Faculty Research Award, an Okawa Foundation Research Grant, a Microsoft Faculty Fellowship, and a Simons Award for Graduate Students in Theoretical Computer Science. <sup>†</sup>School of Technology and Computer Science, Tata Institute of Fundamental Research; A portion of this work was done while the author was visiting the Simons Institute for Theory of Computing in Berkeley, CA. Email: `jaikumar@tifr.res.in` <sup>‡</sup>Computer and Information Science, University of Pennsylvania; Email:{`aaroth`, `wuzhiwei`}@cis.upenn.edu; Supported in part by NSF Grant CCF-1101389, an NSF CAREER award, and an Alfred P. Sloan Foundation Fellowship.

Rachel Cummings<sup>∗</sup> Katrina Ligett<sup>∗</sup> Jaikumar Radhakrishnan<sup>†</sup> Aaron Roth<sup>‡</sup> Zhiwei Steven Wu<sup>‡</sup>

August 6, 2018


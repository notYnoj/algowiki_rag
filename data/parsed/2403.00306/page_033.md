**Chapter 3**

**Our Approach**

In this chapter we have discussed our approach to solve the generalized Quorum Planted Motif Search problem. We have proposed some increment technique on some existing algorithms for solving qpMS problem more efficiently. We have also proposed the idea to implement parallelism for solving this problem.

### 3.1 Notations and Definitions

We have used some common notations to describe all the algorithms described and reviewed. The notations and definitions have been summarized in table table 3.1. The first five notations (\(\Sigma,si,l,d,q\)) are the input data of the problem. Other notations have been used in several steps the algorithms.

### 3.2 Previous Works

There are several exact algorithms to solve the planted motif search problem. For the sake of completeness we will describe the previous works which have motivated us to develop our approach. In this section we will review qpMSPruneI [9], qpMS7 [1], Traver String Ref [24] and PMS8 [7].

#### 3.2.1 qpMSPrune

Algorithm qpMSPrune for the qpMS problem was proposed by [9]. Algorithm qpMSPrune introduces a tree structure to find the possible motif candidates. Then it uses branch-and-bound technique to reduce the search space and find the expected (_l,d_) motifs for the given set of


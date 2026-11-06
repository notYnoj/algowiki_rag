## 1 Introduction

Among the various formulations of the _n_-Queens problem, the _n_-Queens Completion problem has a special position due to its complexity. In the work, Gent at all [1] showed that _n_-Queens Completion is both _NP_-Complete and \(\sharp P\)-Complete. It is assumed that the solution of this problem may open the way to solve some other problems from the set of _NP_-Complete.

The problem is formulated as follows. There is a composition of _k_ queens, which are consistency distributed on a chessboard of size \(n\times n\). It is required to prove that this composition can be completed to a complete solution, and give at least one solution, or to prove that such a solution does not exist. Here, by consistency, we mean a composition of k queens for which three conditions of the problem are fulfilled: in each row, each column, and also on the left and right diagonals passing through the cell where the queen is located, no more than one queen is located. The problem in this form was first formulated by Nauk [2] in 1850.

### 1.1 Definitions

Hereinafter, we will denote the size of the side of the chessboard by the symbol _n_. A solution will be called complete if all _n_ queens are consistently placed on a chessboard. All other solutions, when the number _k_ of correctly placed queens is less than _n_ - we will call the composition. We call a composition of _k_ queens positive if it can be completed. Accordingly, a composition that can’t be completed is called negative. As an analogue of a "chessboard" of size \(n\times n\), we will also consider a "solution matrix" of size \(n\times n\). Research based on Matlab scripting language.

The study was based on computational simulation. To test different hypothesis, we carried out computational experiments in a wide range of values _n_= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 500, 800, 1000, 3000, 5000, 10000, 30000, 50000, 80000, 10<sup>5</sup>, 3∗10<sup>5</sup>, 5∗10<sup>5</sup>, 10<sup>6</sup>, 3∗10<sup>6</sup>, 5∗10<sup>6</sup>, 10<sup>7</sup>, 3∗10<sup>7</sup>, 5∗10<sup>7</sup>, 8∗10<sup>7</sup>, 10<sup>8</sup>) and generated, depending on the value of _n_, large enough samples for analysis. We call such a list a "basic list of _n_ values" for computational experiments. All calculations were carried out on a regular computer. At the time of assembly (early 2013), it was a fairly successful configuration: CPU - Intel Core _i_7-3820, 3.60 GH, RAM-32.0 GB, GPU- NVIDIA Ge Forse GTX 550 Ti, Disk device- ATA Intel SSD, SCSI, OS- 64-bit Operating system Windows 7 Professional. We call this configuration simply - desktop-13.

## 2 Data preparation

The algorithm begins by reading a file that contains a one-dimensional array of data on the distribution of an arbitrary composition of _k_ queens. It is<tbc>


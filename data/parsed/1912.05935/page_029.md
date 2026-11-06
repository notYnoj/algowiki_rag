4. It was found that in the range of _n_=(7,...,100000), the number of solutions in which the Back Tracking procedure has never been used exceeds 35%. Moreover, in the range of values _n_=(320,...,22500), the number of such cases exceeds 50%.

5. A model for organizing the Back Tracking procedure is proposed based on the division of the solution matrix into basic levels. By a level is meant a certain solution step with a given number of correctly placed queens. Regression formulas are given for calculating the values of the second and third basic levels depending on _n_.

6. The results of a comparative analysis of two random selection methods, which are called _randSet_ & _randSet_ and _rand_ & _rand_, are presented. The _randSet_ & _randSet_ algorithm has been found to be fast, but its use should be limited when reaching the second base level. After that, the _rand_ & _rand_ algorithm is used, which is not so fast, but more efficiently places queens on the chessboard.

7. An effective algorithm for verifying the correctness of the _n_-Queens Problem solution is given. This program is also designed to verify the correctness of a composition of arbitrary size. The program works fast enough. For example, the time required to validate a solution consisting of 5 million positions is 0.85 seconds.

## 9 Remarks

1. The algorithm is independent of the programming language. Matlab, in this case, is selected as a environment for modeling, due to ease of use, speed and variety of features. For this, I would like to thank the MathWorks development team. The program uses only the simplest language operators. Therefore, translating script into another programming language will not be a difficult task.

2. Research to find a solution to this problem continued for a long time. And although, during this period, several tens of millions of solutions were received, the situation is not ruled out when the program, under some conditions, can not cope with the task. I would be glad if you let me know.

3. As indicated at the beginning of the article, investigations were conducted in the range of _n_ values, from 7 to 100 million. However, the program was tested in a wider range of _n_ values, up to one billion. True, in the latter case, I had to slightly adapt the program, given the large size of the arrays.


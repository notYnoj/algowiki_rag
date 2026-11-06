<tbc>constructed where the indices of the columns of the considered matrix are plotted along the abscissa, and the number of remaining free positions along the ordinates. For comparison, the calculations were also carried out for the model of sequential selection of positions. By sequential selection is meant the following. The first row is considered, in which the first free position in this row is selected. Then, the second row is considered, in which the first free position in the row is also selected, etc. Figures 5 and 6 show the results that correspond to the models under consideration. For clarity, the graph shows the results only after steps (10, 40, 60). For the model of sequentially selecting positions, the last one is the graph after the 62nd step, since the search branch breaks due to the lack of a free position in the 63rd row. On the other hand, in the _rand_ & _rand_ model, the last graph is presented after the 70th step of placing the queen, although here, the average number of correctly placed queens reaches 89, which is 26 steps more than in the sequential model. The "strange" type of graphs in the _rand_ & _rand_ model is due to the fact that the row index is randomly selected from the remaining free rows, and therefore they are randomly scattered throughout the solution matrix. A comparison of these two figures shows that in a<tbc>

<tbc>sequential model, the range of variability of the number free positions are higher than in the _rand_ & _rand_ model. This is due to the fact that with regular selection, diagonal constraints non-uniformly exclude free positions<tbc>

100
n=100
90
Step=10
Number of free positions in remaining rows
80
70
60
Step=40
50
40
30
20
Step=60
10
Step=62
0
20
40
60
80
100
Row index in the solution matrix

Figure 5: Decreasing the number of free positions in the remaining free rows after placing queens. Sequentially-regular selection of positions.


.5 .7 .3 .5 .7 .3 .5 .7 .3 .5 .7 .3 .5 .7 .3 .5 .7 .3 .2 .4 .1

Notes: .5 = 1/2 .7 = 2/3 .3 = 1/3 .2 = 19/70 (.271) .4 = 5/14 .1 = 1/7

We may arrange the links to minimize the total number of stages as well. This does not change the overall swap statistics:

+----------------------------+
21 21 9.771
+----------------------------+
1 >+----------------------------+
2 >-|+------------------|++------------------++------------------> 2-4
3 >-|-|+------------------|-|+------------------+------------------> 2-4
4 >+-|-|+------------------|-|+------------------|-+------------------> 2-4
5 >+-|-|+------------------|+------------------++------------------> x
6 >+-|-|+------------------|-> 5-7
7 >+-|-|+------------------|-> 5-7
8 >+-|-|+------------------|-> 5-7
9 >+------------------+------------------> x
I
II
III
IV
V
VI
VII
VIII
IX
+----------------------------+

Exchanges on 21 links occur when presented reverse sorted input, or 9.771 times on average, giving a relative frequency of 47%. Substitution of sort3 gives

+----------------------------+
21 14 7.657 0.35
+----------------------------+
1 >+----------------------------+
2 >-|+------------------|+------------------|-o-++--> 1-4
3 >-|-|+--|-|+++--|-|--> 1-4
4 >-|-|-|--o-|-|+++--|-|--> 1-3
5 >-|-|-|--|-o-|-|--o-|--o--> x
6 >-|-|-|--|-|--|-o-++--|--|-->
7 >+-|-|+--|-|++--|---> 1-4
8 >+-|-+|--|--o-|--|--> 1-7
9 >+------------------+------------------> x
I
II
III
IV
V
VI
+----------------------------+

Full sorting in 25 links adds the four CE elements (2,4) (3,4) (6,8) (6,7); Bare median in 19 omits the final (1,2) and (8,9) from the 2-ops appearing in stage IV. Note that these omissions cannot be made directly on the original net without permutations to allow for median. The final networks are not drawn; the benefits to both hardware and software implementations are now summarized:

Min/Max/Med (in 19)

Full Sort (in 25)


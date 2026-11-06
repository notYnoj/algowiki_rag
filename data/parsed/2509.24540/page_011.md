input array with 51 elements
0
51
splitting input array at i into (roughly) two halves
i
left Mergesort recursion
right Mergesort recursion
determine the co-ranks of i in both halves
j
k
consider elements between co-ranks as one array
rotate this middle array in place by offset i - j = k to the left
all "small" elements are left of i, and all "large" elements are right
recursively merge both array halves in place
all work is done array is now sorted completely



Figure 3 Visualized example of the new in-place Mergesort


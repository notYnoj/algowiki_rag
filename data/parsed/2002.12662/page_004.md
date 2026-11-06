<tbc>Bader et al. use SA-scan as a baseline from which to measure the success of their wavelet-tree-based method. SA-scan is natural enough, to be sure, but it does look suspiciously like a straw man. To start with, is `std::sort` really the best we can do for sorting those arrays of integers? We replaced the `std::sort` call with a call to an LSD radix sort of our own implementation (using a radix of 256) and replicated an experiment from Bader et al.’s paper, searching several text collections (including web data, source code, DNA, and proteins -- see Section 5 for more details) for 20 VLG patterns (_k_=2, \(\delta_i,\Delta_i=\langle 100,110\rangle\)), composed of very frequent subpatterns drawn from the 200 most common substrings of length 3 in each data set.

Figure 2 shows the results obtained on our test machine (see Section 5 for specifications). Using radix sort instead of `std::sort`, SA-scan becomes at least two times faster on the Kernel and Proteins datasets, almost twice as fast on CC, and more than 30% faster on Para. A large if algorithmically-somewhat- unexciting leap forward -- but further improvements are possible<sup>3</sup>.

<sup>3</sup> It is possible that further improvements from sorting alone are possible, using a more heavily engineered sort function that our hand-rolled LSD radix sort. Our point here is that sorting is an important dimension along which SA-scan can be optimized.

SA-scan(string_type p1, string_type p2, int min_gap, int max_gap){
//1:find intervals of SA containing subpattern occurrences
std::pair<int,int> interval1 = search(p1,T,SA);
std::pair<int,int> interval2 = search(p2,T,SA);
//2: copy positions of subpattern occurrence from SA and sort
int m1 = interval1.second-interval1.first+1;
int m2 = interval2.second-interval2.first+1;
int *A = new int[m1];
int *B = new int[m2];
std::memcpy(A,SA+interval1.first,m1);
std::memcpy(B,SA+interval2.first,m2);
std::sort(A,A+m1);
std::sort(B,B+m2);
//3: intersect according to gap constraints
for(int i=0,j=0; i\<m1 && j\<m2; i++){
while(B[j] < (A[i] + min_gap) && j < m2) j++;
while(j < m2 && B[j] <= (A[i] + max_gap)){
result.push_back(B[j]);
j++;
}
}
}

Fig.1: A basic C++ implementation of the SA-scan VLG matching algorithm suitable for _k_=2 subpatterns.


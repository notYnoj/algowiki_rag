• PMSSumMin: For each motif _x_ in _M_, we compute the Score as follows. \(Score=\sum_{1\le i\le n}d(x,S_i)\).<br>
After the score is computed for each _x_, the motifs are sorted based on Score. We choose a subset \(M'\) from PMS motifs using the following techniques.<br>
Find MinScore = Minimum value of score out of Scores of all motifs _x_.<br>
All motifs that have Score = MinScore are added to the list \(M'\).<tbc>

• PMSSumMin10: The top 10 motifs based on minimum Score is added to the list \(M'\).<tbc>

• PMSSumMin500: The top 500 motifs based on minimum Score is added to the list \(M'\).<tbc>

• PMSSumMinD: For each motif _x_ in _M_, we compute the Score as follows. If \((d(x,S_i)\le d)\), then _ScoreD=ScoreD+d(x,S<sub>i</sub>_).<br>
After the score is computed for each _x_, the motifs are sorted based on Score. We choose a subset \(M'\) from PMS motifs using the following techniques.<br>
Find MinScoreD = Minimum value of score out of ScoreD of all motifs _x_. All motifs that have ScoreD = MinScoreD are added to the list \(M'\).<tbc>

• PMSSumMinD10: The top 10 motifs based on minimum ScoreD are added to the list \(M'\).<tbc>

• PMSSumMinD500: The top 500 motifs based on minimum ScoreD are added to the list \(M'\).

**Step 2** Find DME Motifs<br>
The output from DME are the motifs, corresponding PWMs and a Score for each PWM. Since, PMS outputs unique string motifs and DME motifs have some degenerate positions in them, we open the DME motifs to generate a list of unique motifs and then choose a subset \(D'\) from all the DME motifs as follows:

• DMESumMin: Let _x_<sub>5</sub>_,x_<sub>6</sub>_...x_<sub>1</sub>5 be the number of motifs of length 5 to 15 respectively in PMSSumMin. We generate the list of DME motifs where the list has \(x_\ell\) motifs of length \(\ell\), where \(5\le\ell\le 15\).<tbc>

• DMESumMinD: Let _x_<sub>5</sub>_,x_<sub>6</sub>_...x_<sub>1</sub>5 be the number of motifs of length 5 to 15 respectively in PMSSumMinD. We generate the list of DME motifs where the list has \(x_\ell\) motifs of length \(\ell\), where \(5\le\ell\le 15\).<tbc>

• DMESumMin10: The top 10 motifs out of all the motifs from DME are put into \(D'\).<tbc>

• DMESumMin500: The top 500 motifs out of all the motifs from DME are put into \(D'\).<tbc>

• BestDMESumMin: The best m motifs out of all the motifs from DME are included in \(D'\), where _m_ is the number of motifs in PMSSumMin.<tbc>

• BestDMESumMinD: The best m motifs out of all the motifs from DME are included in \(D'\), where _m_ is the number of motifs in PMSSumMinD.

**Step 3** Compute Statistical Measures.<br>
We compute the 7 statistical measures for each motif in all the 9 files generated. For each dataset the computation is done as follows. Plant all the motifs occurring in the dataset with a distance specified in  1 corresponding to the length of the motif. Pick one predicted motif at a time from the file and plant it in the dataset using the distance specified in  1 corresponding to the length of predicted motif. Find the values of nTP, nFP, nFN, nFP,<tbc>


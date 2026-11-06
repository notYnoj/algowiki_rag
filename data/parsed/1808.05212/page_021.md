respectively. This explains all numbers appearing in Figure 1(a) except for the upper right 0, which represents the quotient 0/6, the uncertain positions divided by all positions 3, thus representing a measure of unsortedness.

Similar considerations apply to  3 which corresponds to the network in Figure 2(a).

## Appendix B

As an example of illustrating the use of the accompanying code, we used

`./sn -i -o8 18-27-36-45-24=13=12=34=24=234=45- > samplefigure.txt`

to generate an ASCII version of Figure 28. The = signifies symmetry, so `24=` is a shorthand for `24-57-`. The `234=` illustrates two (symmetrically placed) 2-ops. The output of this code is a text file that can be post-processed with code in Appendix C to generate an `svg` file which were used to produce the figures in this manuscript.

Below is a listing of the `C` source code to generate the networks discussed in this paper.


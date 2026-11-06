# _output the vector list_

$i = 0;

**for** $xs (@xs)

{

**printf** "\<line\_x1=%g\_y1=%g\_x2=%g\_y2=%g\_stroke=\\"black\\"",

$xs, $ys[$i], $xe[$i], $ye[$i];

**if** ($th[$i] != 1)

{ **printf** "\_stroke-width=\\"%g\\"", $th[$i]; }

**print** "/\>\\n";

$i++;

}

**print** "\</svg\>\\n";

}

## Appendix D

Finally, we list list the email with Alan Paeth’s original draft of this manuscript.

From: Alan Paeth \<awpaeth@gmail.com\>

Date: Wed, 28 Mar 2018 13:48:34 -0700

Subject: conex paper

To: Heinz Bauschke \<heinz.bauschke@ubc.ca\>

[other recipients suppressed, obvious spelling mistakes corrected,

formatting of text adjusted for easier reading]

Non-Interfering Concurrent Exchange (NICE) Networks

### Synopsis

In studying the statistical frequency of exchange in comparison-exchange (CE) networks we discover a new elementary form of comparison-exchange which we name the "2-op". The operation supports concurrent and non-interfering operations of two traditional CEs upon one shared element. More than merely improving overall statistical performance, the introduction of NICE (non-interfering CE) networks lowers long-held bounds in the number of stages required for sorting tasks.

-based CEs also benefit from improved average/worst case run time costs.

### Motivation

Comparison-based sorts dominate much of modern sorting; in-place methods such as quicksort are widely employed and well-studied. All seek to minimize the number of comparisons required. For small numbers of input (N), a sequence of predetermined comparisons form a decision tree of N! leaves; if minimal, its height is then ceiling(N log2 N), e.g. for N=5, 7 comparisons suffice to fully<tbc>


## Appendix C

The output file `samplefigure.txt` described in Appendix B can be postprocessed with

`./fix samplefigure.txt \> samplefigure.svg`

to generate Figure 28.

Below is a listing of the `perl` code to generate the networks discussed in this paper.

`#!/usr/bin/perl`

`# fix.pl - convert UTF8 graphics (box characters) into SVG/HTML`

`$xscale = 7.5;`

`$yscale = 15.0;`

`$mscale = $xscale; if ($yscale \< $mscale) { $mscale = $yscale; }`

`# ( )`

`# @ $`

`## unused: \< % ^ &`

**foreach** (_\<\>_)

{

**chomp;**

`# protect hyphens in intervals (convert to underscores)`

`s/([0-9])-([0-9])/$1\_$2/g;`

`# map UTC8 box formers`

`s/`\\e\\[30;3.**m**//g;

`s/`\\e\\[**m**//g;

`s/`\\342\\206\\222/_\>/g; # arrow right`

`s/`\\342\\215\\277/∗/g; # vert dot 2-op`

`s/`\\342\\225\\221/#/g; # double col`

`s/`\\342\\225\\242/{/g; # double col LHS Tee`

`s/`\\342\\225\\237/}/g; # double col RHS Tee`

`s/`\\342\\225\\220/=/g; # double row`

`s/`\\342\\225\\224/;/g; # NW double corner`

`s/`\\342\\225\\227/:/g; # NE double corner`

`s/`\\342\\225\\232/'/g; # SW double corner`

`s/`\\342\\225\\235/'/g; # SE\_double\_corner`

`s/`\\342\\224\\260/~/g; # top\_Tee`

`s/`\\342\\224\\270/!/g; # \_bot\_Tee\_(perpp)`

`s/`\\342\\224\\200/-/g; # single\_row

`s/`\\342\\224\\203/|/g; # single\_col`


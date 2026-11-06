`char` \*cpur = "\\033[30;35m";`

`char` \*ccyn = "\\033[30;36m";`

`char` \*cltw = "\\033[30;37m"; // normal white`

`char` \*cwhi = "\\033[30;39m"; // bright white`

`char` \*cbld = "\\033[1m";`

`char` \*cnrm = "\\033[m";`

`#define` chorz cltw // _horizontal rank lines_

`#define` cdead cred // _dead links_

`#define` cbord ccyn // _text annotations_

`void` display(**int** pt[], **int** lk[], **char** \*anno)

{

**int** i, j, \*p, lnum, lmin, lpen;

`char` \*boxh, \*boxv, \*boxHu, \*boxHd, \*boxHv;`

`char` \*arrR, \*boxCc;`

`char` \*boxH, \*boxV, \*boxDR, \*boxDL, \*boxUL, \*boxUR, \*boxVr, \*boxVl;`

**int** dsplen, tmargin, bmargin, bwidth;

`// double lines , corners`

arrR = "\\342\\206\\222"; // -\> (arrow rt.)`

`// double lines , corners`

boxH = "\\342\\225\\220"; boxV = "\\342\\225\\221"; // = ||

boxUL = "\\342\\225\\232"; boxUR = "\\342\\225\\235"; // || - ||

boxDR = "\\342\\225\\224"; boxDL = "\\342\\225\\227"; // || - ||

`// single / single , single+double lines`

boxCc = "\\342\\227\\213"; // \<or\> \\342\\227\\257 // _o (big)_

boxCc = "\\342\\217\\200"; // _o (line thru)_

`// boxCc = "\\342\\247\\263"; // _o (Alternate)_`

boxCc = "\\342\\215\\277"; // \* (barred)

boxh = "\\342\\224\\200"; boxv = "\\342\\224\\202"; // - |

boxHu = "\\342\\224\\254"; boxHd = "\\342\\224\\264"; // _perp tee_

boxVr = "\\342\\225\\237"; boxVl = "\\342\\225\\242"; // |- -|

boxHv = "\\342\\224\\277"; // \\274 _aka boxvh stock_ + // + (_w/ thick_)

boxHv = boxCc; // _center ’+’ now a ’o’_

boxv = "\\342\\224\\203";

boxHu = "\\342\\224\\260";

boxHd = "\\342\\224\\270";

**if** (ascii)

{

arrR = "\>";

boxHv = "o";

boxH = "="; boxV = "|";

boxh = "-"; boxv = "|";

boxUL = boxUR = boxDR = boxDL = "+";


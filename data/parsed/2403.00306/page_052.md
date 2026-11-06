## Appendix A

## s

### A.1 Compressed String

Here is a sample C++ structure for compressing a 1000 character long DNA string

`1 //letterToInt[i] means a unique id for each character of the alphabet;`

`2 //Here,`

`3 //letterToInt[’A’]=0;`

`4 //letterToInt[’B’]=1;`

`5 //letterToInt[’C’]=2;`

`6 //letterToInt[’D’]=3;`

`7`

`8 **struct** CompressedlMer`

`9 {`

`10 **unsigned** **int** \*\*cs;//[2][32];`

`11 **int** 1;`

`12 CompressedlMer(char \*string, **int** start, **int** 1) {//`

_constructor_

`13 **int** group = 0;`

`14 **int** intPerGroup = ceil(1/sizeof(unsigned **int**));`

`15 **int** temp = 1;`

`16 **while**(temp) {`

`17 group++;`

`18 temp = temp/2;`

`19 }`

`20 cs = new unsigned **int**\*[group];`

`21 **for**(**int** i = 0; i \< group; i++)`


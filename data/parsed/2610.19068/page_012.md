## F Stub-Hallucination Examples

9 shows G1 queries where PtR achieves zero recall (stub abstracts away the brand/product name) while RtP achieves perfect recall via direct embedding match.

## G PtR Win Examples (G1, G2, G3)

**G1 wins (functional-need queries).**

• "_monitor status of video uploads_" \(\rightarrow\) stubs `get\_video\_ingest\_job\_status` + `generate\_temporary\_ upload\_urls` retrieve both correct Fake Brightcove APIs (recall 1.0); RtP retrieves unrelated video encoding tools (recall 0.0).<tbc>

• "_company event in Dallas, need airports_" \(\rightarrow\) stub `airport\_information\_api` retrieves `Airports Finder/Get Airports By City` (recall 1.0); RtP drifts to `Airport Data/Airports By City` (recall 0.0).<tbc>

• "_horoscope app, all zodiac signs_" \(\rightarrow\) stub `get\_all\_zodiac\_signs\_data` retrieves `Zodiac Sign API/Getallsign` (recall 1.0); RtP retrieves unrelated astrology APIs (recall 0.0).

**G2 wins (multi-stub decomposition).**

• "_surprise proposal, romantic lines + Instagram media_" \(\rightarrow\) PtR decomposes into `text\_generation\_ tool` + `instagram\_media\_downloader\_tool`, achieving recall 1.0; RtP achieves 0.5.<tbc>

• "_London trip: hotels + IP forensics + currency_" \(\rightarrow\) 3 stubs span 3 functional areas, achieving recall 0.5; RtP achieves 0.0 (single embedding drifts to hotel listings).

**G3 wins (cross-category decomposition).**

• "_share news article, create shortened URL_" \(\rightarrow\) PtR generates `url\_shortener` + `slashtag\_suggestion` + `domain\_lister`, covering 3 tools in the URL shortening toolchain (recall 0.33); RtP retrieves generic news APIs (recall 0.0).

## H G2/G3 RtP Win Examples

**G2 - RtP wins when stubs over-generalize.**

• "_trip to Greece, explore energy market news_" \(\rightarrow\) PtR generates `general\_news\_search` + `eurosport\_ football\_news` (recall 0.0); RtP matches "Greek" and "Energy" keywords, retrieving `Greek News in English` + `Energy Price News` (recall 0.5).<tbc>

• "_team-building event: trivia + gaming_" \(\rightarrow\) PtR stubs miss specific API brands (recall 0.0); RtP retrieves `Trivia by API-Ninjas` + `Epic Free Games` directly (recall 0.4).<tbc>

\begin{tabular}{ccc}
**Query** & **PtR Stub** & **RtP Retrieved (correct)** \\
"crime news in Germany" & `news\_search\_api` & German Police and Crime News Live \\
"programming memes, & `reddit\_api\_client` & Programming Memes Reddit/Get All \\
Reddit" & & Memes \\
"PLN electricity bill" & `get\_pln\_bill\_details` & Cek ID PLN/Get Data Tagihan \\
"Testing out Sharing w/ & `api\_spec\_retriever` & Testing out Sharing w/ Rachael/Input test \\
Rachael" & & \\
\end{tabular}

** 9** Stub-hallucination examples: PtR’s over-generic stubs miss niche APIs that RtP matches directly.


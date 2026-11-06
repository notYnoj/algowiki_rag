<tbc>used with a scale factor of 35 (over 10 GBs). In this experiment the table was modified by excluding columns that do not participate in any query that comes with this benchmark.

The query under consideration over `lineorder` was as follows:

The PosDB query plan of the considered query is shown in Fig. 3. Essentially, it is equivalent to the PostgreSQL one. Despite the fact that PostgreSQL is a row- based system, whereas PosDB is column-based, the comparison is still valid since the query projects all attributes. As the result, PosDB behaves identically to the row-based system: readers of the Materialize operator access the same amount of data from disk, albeit from several different files. It is also worth mentioning that PostgreSQL uses a heap to merge runs. In all conducted experiments, the number of tapes was greater than the number of runs. This means that the polyphase merge algorithm behaved like a multiway merge both in PosDB and PostgreSQL.

In the first two experiments, the total number of runs was chosen to be 84. PosDB generates 84 runs with 150 megabytes of memory available for the sort operator for all three considered algorithms. PostgreSQL at the same time needs 413 megabytes of `work\_mem`<sup>7</sup> for this, probably because of internal buffers for optimized I/O. To make this comparison more accurate, we measured the performance of PostgreSQL with a total of 84 runs (`work\_mem`=413MB) and with 231 runs (`work\_mem`=150MB, the same amount of memory was given to the PosDB sort operator). In these experiments, the average query execution time<tbc>

<sup>7</sup> `https://www.postgresql.org/docs/current/runtime-config-resource.html`

SELECT
2 LO\_CUSTKEY, LO\_DISCOUNT, LO\_EXTENDEDPRICE, LO\_ORDERDATE,
3 LO\_ORDERPRIORITY, LO\_ORDTOTALPRICE, LO\_PARTKEY,
4 LO\_QUANTITY, LO\_REVENUE, LO\_SUPPKEY, LO\_SUPPLYCOST
5 FROM LINEORDER
6 ORDER BY LO\_ORDERDATE;
The PoDB query plan of the considered query is shown in Fig. 3. Essentially, it is equivalent to the PostgreSQL one. Despite the fact that PostgreSQL is a row- based system, whereas PosDB is column-based, the comparison is still valid since the query projects all attributes. As the result, PosDB behaves identically to the row-based system: readers of the Materialize operator access the same amount of data from disk, albeit from several different files. It is also worth mentioning that PostgreSQL uses a heap to merge runs. In all conducted experiments, the number of tapes was greater than the number of runs. This means that the polyphase merge algorithm behaved like a multiway merge both in PosDB and PostgreSQL.
To user
Operator
Reader
Alternals
local access
remote access
ExternalTupleSort
Tuples
Columns
Read(...)
Materialize
DS(lineorder/trip_data)
Fig.3: PosDB plans for queries used in experiments.


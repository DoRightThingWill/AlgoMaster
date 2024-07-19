1. Server to server. Normally use gPRC for now
2. what does the small company currently use for server-to-server call?
3. 一般来说，服务器间通信，几乎不需要身份验证？不对吧，也是需要设置 security group 的吧？或者 permission check?
4. API gateway 可以干什么？有啥好处？它在 LB 的前面，还是后面？会带来 single point failure 吗？
5. 在 sql 表格中，composite index 的实现机理是，先将第一个 column a 排序，column a 相同的情况下，将 column b 排序。如果分别对 column a 和 column b index，当 column a 相同的时候，column b 未必有序。composite 最适合的查询是, where clumn_a = ？ and columb in some range。他对 where cloumn_a in a range and column_b in range 的查询，并不是很有效果，因为 clumn_a in a range 得到的结果中，colunm_b 未必有序，这样的话，就无法充分使用 composite index
6. 判断连个 geo location，多么接近，并对多个位置进行排序，google S2，以及 geoHash 算法。当然，最朴素的，就是计算直线距离，或者用 sql 自带的距离函数

   - geoHash 算法，是把 geo loation encode 成一个 string。string 的 prefix 越 match，两个位置就越近。prefix 中，有 4 个 letter match，就是 20km，有 5 个 match，就是 3km。对于 uber 来说，们可以只关注 4 个 letter match
   - sql 中，where ... like "prefix%"
   - noSQL 中，column key 用 geohash，对他进行 range query
   - redis 中，其实，分级存储，key 是 geoHash 的 geohash 的前几位 ，比如，前 5 位的，以及前 6 位的 geoHash，value 是一个 set driver_id。

7. SQL query 中的 like query for string match
8. Single Redis server
   - can handle 100k QPS
   - 容易挂掉，比 sql 或者 server 更加容易挂掉
   - 所以，需要 replica 以及 sharding
   - sharding 可以提高 avalability，以及 performance
   - uber 呢，可以按照 geoHash 的 code 来进行 sharding，也可能按照 city 来进行 shard

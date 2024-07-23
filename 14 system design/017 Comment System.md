1. Latency vs response time
   - latency 我们可以控制，主要是服务本身的响应时间
   - response time 有些因素，我们无法控制，比如网速，引号稳定程度，以及用户本身的机器
2. 当我们描述 latency 的时候，可以用 p99 latency 500 ms，为什么不用 max，或者 average latency
   - p99 这个 metrics 更有代表性，max 或者 average，一个单点可能引入很大的误差，比如 p99 的 latency 都低于 0.5 s，但是 max 是 10 秒，那么用 max 以及 average 呢，就都不合适了
3. 设计 api 的时候，需要注意，有些 endpoint 需要 authentication，有些不需要
   - header 里面，authorization，添加 bear token
   - 或者使用 cookie，带有 session_key 等等信息，用来鉴权
4. URL parameter location
   - abc.com/{id}，这种呢，一般就是认为，是 required parameter
   - abc.com?id={id}，这种一般当做 query parameter,算是 optional
5. 如果有很多的 items in response，就做 pagination
   - abc.com?page = {id}
6. read qps 在 1000，write 也在 1000，low latency，p99 500 ms，优先选择 NoSQL，为何？NoSQL 为何更好的支持 high concurrency
7. 为了解决时区不一致的问题，是不是所有的 timestamp，都要用 UTC 时间
   - 可以使用 apple time,就是 1970 年之后，没过一秒，就加 1
8. comment table, in NoSQL
   - comment_id
   - post_id
   - 给定一个 post，如何获得所有的 comment 呢？需要对 post_id 建 index，这在 MongoDB 中，是可以实现的。MongoDB 是可以这么做的
   - 如果不能建 index，就再做一个额外的 table，post_id，【comment_id1, comment_id2】
9. Update MySQL, NoSQL, and ES
   - Distributed transaction, with global lock provided by Zookeeper? Strict data consistence, but low concurrency, and high system complexity, hard to debug
   - Async way, message queue as a buffer job, servcie first update DB, once it succes produce a message into the Kafka, then the message will be consumed by NoSQL, and ES. CDC, capture of data change. Pros: better performanc, decouple and more resilient; Cons: eventual data consistence, not strict

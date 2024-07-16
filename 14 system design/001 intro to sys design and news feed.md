# Storage

##

1. application = algo + data_structure
2. system = services + data_store
3. When to consider when design SQL table
   1. field name
   2. data type
   3. is Forigen key?
   4. relationship, many to one, one to many
4. How to optimize SQL database
   1. normalization
   2. index
      1. single index
      2. composite index
   3. sharding
   4. availability
      1. replica
      2. master-slave cluster
5. push vs pull
   1. when to use push
   2. when to use pull 17. fan out-- 核心概念是一个单一的信号或任务被扩散或分发到多个接收者或子任务 18. fan-out pattern in News Feed pull model 19. https://www.linkedin.com/pulse/fan-out-design-pattern-cory-maklin/
6. multi-index in NoSQL? NoSQL 中有 index 吗？ 18. NoSQL does not have sequential ID. It basically only has UUID to increase the distribution efficiency
7. cassandra 是干嘛的？
8. redis 和 memcached 很像；memcached 不支持 持久化；redis 支持持久化
9. cache aside, vs cache thru
10. two ways for pagination 20. https://abc.com?page=1 21. https://abc.com?max_id = 1000 22. endless pagination, how to use max_id? how to know if we have reached the end?
11. Tiny URL
    1. 不要觉得，一个东西很难，上来就 load balance，sharding 整一堆，你要看看，到底是啥样的需求，做计算，qps, 1000 的 pqs,一台 mysql 基本搞定了
    2. service
       1. get /short_ur。 response：301， moved permenantl，browser 下次不会再访问 bitl，而是记住了这个 directed 地址；如果 302，就是 moved temporaril，下次 browser 还会再 call bitly
       2. 算法：
          1. hash. pro: fast. Cons: hash collision
          2. 随时生成+数据库去重。pro:实现简单；cons:后面，越来越慢
          3. 禁止转换，base62？
             1. 数据库表，首先 insert，获得一个 id，比如说 34567
             2. 然后，把 ID，转换成 62 进制的包括 6 位 62 进制的 char 的 shorturl, 这个 62 进制也比较简单，0-9, a-z, A-Z，一共是 62 个数
             3. 把这个 shortURL 存进 DB
             4. 反过来，给订一个 shortURL，先把他转换成 ID，然后去数据库查询 longURL。
             5. 理论上，完全避免了 collision
    3. what is zookeeper?

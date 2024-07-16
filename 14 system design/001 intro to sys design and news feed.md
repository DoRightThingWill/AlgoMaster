# Storage
## Type
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
    2. when to use pull
        17. fan out-- 核心概念是一个单一的信号或任务被扩散或分发到多个接收者或子任务
        18. fan-out pattern in News Feed pull model 
            19. https://www.linkedin.com/pulse/fan-out-design-pattern-cory-maklin/
17. multi-index in NoSQL? NoSQL 中有index 吗？
    18. NoSQL does not have sequential ID. It basically only has UUID to increase the distribution efficiency
18. cassandra 是干嘛的？
19. redis 和 memcached 很像；memcached 不支持 持久化；redis 支持持久化
18. cache aside, vs cache thru
19. two ways for pagination
    20. https://abc.com?page=1
    21. https://abc.com?max_id = 1000
    22. endless pagination, how to use max_id? how to know if we have reached the end?
20. Tiny URL
    21. 不要觉得，一个东西很难，上来就load balance，sharding 整一堆，你要看看，到底是啥样的需求，做计算，qps, 1000的pqs,一台mysql基本搞定了
    22. service 
        23. get /short_ur。 response：301， moved permenantl，browser下次不会再访问bitl，而是记住了这个directed 地址；如果302，就是moved temporaril，下次browser还会再call bitly
        24. 算法：
            25. hash. pro: fast. Cons: hash collision 
            26. 随时生成+数据库去重。pro:实现简单；cons:后面，越来越慢
            27. 禁止转换，base62？
                28. 数据库表，首先insert，获得一个id，比如说34567
                29. 然后，把ID，转换成62进制的包括6位62进制的char的shorturl, 这个62进制也比较简单，0-9, a-z, A-Z，一共是62个数
                30. 把这个shortURL 存进DB
                31. 反过来，给订一个shortURL，先把他转换成ID，然后去数据库查询longURL。
                32. 理论上，完全避免了collision
    33. what is zookeeper?
    34. 
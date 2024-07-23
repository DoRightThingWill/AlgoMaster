1. Index is a filed stored in Disk?
2. SQL index is implemented via B+ tree. Index 是 storage engine 级别的，不同的 storage engine，具体的 index 实现很可能不同
3. Storage Engine，都是 MySQL 的存储引擎
   - InnoDB, clustered index, leaf nodes stores values
   - MyISAM， non-clustered index. leaf node stores address of value。不支持事物操作，知识有点老
4. 有很多重复值的列，不需要建索引，不太会加速查询，比如性别等，city，或者 state，不是说不行
5. Transcation:
   - Begin Transaction
     - Sql 1
     - sql 2
     - sql 3
   - Commit/Rollback Transaction
6. Feature of Transaction: ACID
7. 4 levels of Transaction Isolation。从上到下，越来越严格
   - read uncommited
   - read commited
   - repeatable read
   - serializable
8. Default isolation level of MySQL and Oracle
   - mysql, repetable read
   - oracle, read commited
   - 都没有采用 serializable，就是为了增加并行能力
9. 并发控制的策略，基本有两种，乐观控制，悲观控制
   - 乐观，让你们执行，出错了回滚
   - 悲观，必须串行，必须控制
10. 具体的并发控制策略
    - lock，read lock, write lock，悲观方式
    - timestamp，准备回滚
11. Transaction 的核心，是 consistence。为了保证 consitence，就要做 isolation。isolation 和并发，基本是互斥的概念，越严格的 isolation，better consistence，但是就糟糕的并发
12. 数据恢复、备份
    - binLog. MySQL
    - write Ahead Log, PgSQL

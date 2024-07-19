1. real time service
2. 点对点通信, end to end communication? or via server
3. is the wechat message stored in the server? Yes.
4. Telegram 就是点对点通信，而且经过加密，不经过服务器，只有对方在线的时候，你才能发消息，否则，你发不过去，server 是不会存你的信息的
5. How to design message table
   - Option 1
     - user_table
       - user_id
     - message_table
       - message_id
       - from_user_id
       - to_user_id
       - content
       - created_at
     - what will be the index or key?
       - composite index
     - how to query?
       - A send a message to B
         - insert into message_table (from_user_id, to_user_id, content) values (user_id_a, user_id_b, content)
       - show chat history betweeen A and B
         - select \* from message_table where (from_user_id = user_id_a and to_user_id= user_id_b) or (from_user_id = user_id_b and to_user_id = user_id_a) order by created_at desc
         - it is slow
   - Option 2
     - user_table
     - thread_table
       - thread_id
       - users: serialized data string???? [] or participant_hash_code???
       - avatar
       - created_at
       - admin_id
     - message_table
       - message_id: incremental
       - thread_id
     - how to query?
       - check if two users already have a thread
         - select \* from thread where users = 'user_id_a,user_id_b'
       - create a thread
         - insert into thread (users) values 'user_id_a,user_id_b'
       - get chat history among A and B
         - input is thread_id for a and b
         - select \* from message_table where thread_id = thread_id order by created_at desc
     - SQL or NoSQL for message?
       - NoSQL, message keep growing faster, and NoSQL has better capability regarding horizontal scaling
       - 在 Cassandra 中, sharing key 和 row key 说的是同一个东西吗？row key = messasge_id
       - what is coloumn key? = created_at，一般用于 range query. value = content
       - MongoDB
6. SQL 中，key 主要用来区分每行数据，index 主要用来加速查询。有 composite key，同时有 composite index。在某些多对多的关系表格中，可以不用单独的 id，而只使用 composite key，也是可以的
7. Redis 是 cache，属于广义上的 NoSQL，但是，我们通常说的 NoSQL 指的是，Cassandra，MongoDB，DynamoDB，RocksDB。Redis, MongoDB, Cassandra，有开源版本，也有托管版本，DynamoDB 是完全托管的。
8. 为了加速查询
   - 避免 join 或者 or
   - 可以用一个 transaction，两个 query 然后 union？
   - 可以用两张表，并行查询？
9. 数据拆分的基本原则：按什么去，query，就按什么拆分，sharding
10. poll vs pull。 poll 是轮询，二者的有 common 的部分，那就是主动的去 ask for data，但是，二者所想表达的侧重点不同，poll 侧重表达，ask for 的行为，是周期性的，会一直进行下去，而不是一次性的；push 呢，则侧重强调，主动去要，但是进行了几次，是不是轮询不知道。
11. 系统设计面试过程中，出了主要的核心功能外，面试官，还可能会问 edge case，或者 special feature，或者 non-fucntional requriement 等等，一方面，是要考察你的设计思维，re-sue component，sizing，trade-off，knowledge base，另一方面，考察你的沟通交流的能力，verbal，written，以及 lay out
12. Instant message system. 主要考点
    - user_table, message_table, thread_table
    - DB optimization, index, sharding
    - SQL vs NoSQL usage, row key, column key,
    - Websocket vs http
    - Micro-servcie
    - Message queue
    - Cache

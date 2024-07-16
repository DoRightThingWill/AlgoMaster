1. Single point failure
2. Sharding

   - Vertical sharding. user, friends talbe in different db
   - Horizontal sharding. user table in multi db.
     - Simple mold --> heavy data re-allocation
     - Consisten hashing, to minize data re-allocation
       - Hash ring, mold a big number. And Hash space is distributed into multi servers. But data allocaiotn is not even.
       - Consistent hashing. 2 \*\* 64. Probability of universe explorsion. After hashing, the first machine when turning clockwise. Virtual node.
         - LeetCode should already have a problem for this.

3. Replica vs backup
   - backup: offline, dead server, cheap, not real time data
   - replica: oneline, alive searver, real time data
4. SQL and NoSQL both can do scaling. NoSQL has built-in scaling algo?
   - NoSQL has builtin Sharding and Replica machanism?
5. Master slave arch
   - master for write
   - slave for read
   - Write Ahead Log, store all statements, which is used to replay and update data in slave node
   - Concensus algo, to elect new leader if the master is down
6. How to shard a user table?

   - how to shard data based on how to query data.
     - select \* from user_table where user_id = ?
   - with multi sharded tables, how to matain a incremental ID?
   - when creating a new user, which table to insert for the new user?
   - How to shard existing table?
     - use UUID
     - with a dedicated UserIDService to generate ID, which is responsible global atomoicty via locking. This should work because user creating QPS is not very big normally.

7. How to shard a friendship table
   - single table row to represent a bi-directional relationship, like small_id, and big_id
     - find all friends of a
       - select \* from friendship where from_user = a_id or to_user = a_id;
       - or two separate queries
       - if we have index on both columns, two separate queries may be faster. Because "or" in query does not use index properly; we can use transaction so that we run two queries in on DB connection. To further check, which one is better, we can use query explain to check the execution plan.
     - check if a and b are friends
       big_id = a_id if a_id > b_id else b_id
       small_id = a_id if a_id < b_id else b_id
       select \* from friendship where from_user = small_id and to_user = big_id;
   - doulbe table row to represent a bi-directional
     - find all friends of a.
       select \* from friendship where from_user = a_id;
     - check if a and b are friend
       selct \* from friendships where from_user = a_id and to_user = b_id
   - sharding can distribute traffic, allow parallel queries, and increase availability
8. How to shard sessions table
   - session_key, user_id, expire_at
   - session_key as sharding_key

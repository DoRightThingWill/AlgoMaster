1. functional requirements
   - set(key, value)
   - get(key)
2. non-functional requirements
   - high avaialbility
   - low latency
3. critical part

   - data structure
     - hashtable, hasing function
     - consistent hashing
   - component to store data

     - cache, partion
     - cache, replica
     - failure detection
       - heart to master? single point failure. Re-elect.
       - peer to peer network, Gossip protocol
         - send heart to mutli peer, and more than peer claim this server is dead. Then we say this server is dead. Avoid single point failure
     - failure recovery
     - strict consistency
     - eventual consistency
     - replay write ahead log

   - 更加底层的实现
   - 一部分数据放在 cache 中
   - 更多的数据，放在 disk 中，通过 sorted string table 存储
   - 拿到一个 key 之后，首先去查 bloom filter
     - 如果没有，就一定没有
     - 如果有，会给一个可能存在的 list，然后再挨个去查，效率很高

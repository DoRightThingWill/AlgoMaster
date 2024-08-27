1. key process
   - map the server and data into a hash ring via a hash function
   - for each data, clockwise go along the hash ring and choose the next server for this data
2. drawbacks
   - unevenly distributed data among servers. Some server has lots of data, or even maybe overloaded. Some server just has no data, waste of resource
3. how to mitigate the drawbacks
   - bring in virutal node, so servers can be more evenly distributed among the hash ring
4. under what kind of situations, we will use consistent hashing
   - DB, sql or nosql, like Cassandra
   - Cache, redis cluster

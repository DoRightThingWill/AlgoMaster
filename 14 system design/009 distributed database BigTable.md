1. Google system design question: how to design a BigTable
2. 内存中排序
3. 外排序
   - 内存 2G，数据本身 8G。
   - 把 8G 数据，均分成 2 G 的数据块
   - 然后进行 k 路归并
   - 从小到大，写入磁盘
4. write ahead log？为啥写这个 log 比较快，因为仅仅是 append 操作，
   - 更加深入的知识
5. Meta, Google 这样的公司，他们的 system design，一般会问什么问题呢？
6. Chubby, Zookeeper，可以提供一个分布式的锁
7. K 路归并的算法
   - k pointer
   - 用 heap 来快速选择 k 个数字中的最小值。整体时间复杂度 O(logK. N)
8. BigTable is built on top of GFS
9. Bloom filter
   - 类似于 hash table
   - 对于一个 key，有多个 hash function
     - 节省空间
     - 检查存在性。没有，肯定没有；但是有，未必有

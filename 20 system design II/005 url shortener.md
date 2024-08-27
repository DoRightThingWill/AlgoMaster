1. 核心算法
   - 终极目标，是在建立，long - short 之间一一对应的关系
   - 一般的 hash function。简单，但是，collision 很多。其他的算法，比如 md5，hashcode，并不短
   - 可以用，md5 hash 之后，取 7 letter，如果有 collision，就加 pre-defined-string，比如 0-9, a-z, A-Z，同时，用数据库，进行查重，对 column 建立 index。为了优化数据库，同时可以使用 bloom filter。在这里使用，就非常合适。假阳性，说存在，未必存在，thats fine, not big deal
   - first generate unique numerial ID, and then convert to 62 base number
     - twitter snowfalke ID, 64 bits
     - convert to 62 base nubmer, 0-9, a - z, A - Z, then you get short url
2. data flow
   - /get-short
     - paramter: long url
     - return short short url
     - first check if long - url in db.
       - longUrl
       - Bloom filter + index
       - if no, then generate short url via base 62 algo
       - if yes, return the short url
   - /get-long
     - parameter: short url
       - cache
       - shortUrl -> convert to ID --> index --> get longUrl, return

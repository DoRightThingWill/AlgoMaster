1. crawl webpage
2. what kind of data format are we going to store? Like image, txt, or what?
   - this is good questions. We shoudl present like: I would say, we would like to crawl the input url or root urls, and also the reference urls in the web page;
   - store the web page as html file
   - avoid crawiling the same URL
   - read the robots.txt file
3. any specific areas of webpage we want to crawl? like legal, e-commerce, travelling, technology?
   - 这个问题可以问，但是，问题的核心，还不是在这个。因为，你一旦提供了 root url，基本就锁定了爬虫的领域，比如体育，健康，军事，等等
4. who will be the end user? how our system will be used by others?
   - 和常见的 app 不同，这个系统没有那种常见的交互界面。
5. 系统设计面试，一般会侧重考察几个点，技术性的，以及非技术性的

- 非技术性的，沟通
  - 能否听懂对方在讲什么？
  - 你说的话，写的字，画的图，对方能否听得懂
- 技术性的
  - UUID，id 的 format，直接影响你的 id 产生逻辑，以及通过什么方式，保证 uniqueness （data consistence），centralized or distributed
  - crawler 中的 url 查重
    - hash --> collision
    - bloom filter --> if not exist, 100% guranteed correct; if exist, 95% or 98% percent corerct, not guaranteed

6. 如果一开始的时候，我们就知道，这是一个高写入的需求，那么，一开始就可以确定用 nosql db，因为，后面再从 sql 换到 nosql，data migration，也很麻烦
   - cassandra, row key, column key
   - cassandra，也支持类似 sql 的那种 table 语法，field 啥的
7. redis 的底层实现原理，是 hash table 吗？
8. fan out，is this good or bad? why?
9. 为什么 crawler 需要 tokenizer？
10. 在面试过程中，需要回头 review requirement，确保我们 on the track，同时 complete 了 requirement
11. 如果我们有 1000 台 crawler 去 run，可以用同一个 scheduler，通过 gPRC 与他们进行通信？如果用 message queue，会不会更好呢？
12. gPRC is not persistent connection. what does this mean?
13. Kafka 通过 partition 来提高读写能力吗？多个 subscriber，可以同时读不同的 partition
14. distributed system 的核心有这个几个
    - 多台机器，同时读
    - 多台机器，同时写
    - 提高性能，保持 data consistence
    - failure discovery and recovery
15. Bloom filter is not full proof

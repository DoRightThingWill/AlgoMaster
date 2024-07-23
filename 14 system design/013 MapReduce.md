1. How to use MapReduce
2. 主要是和大数据相关的岗位
3. Map 就是把数据打散，然后并行计算；Reduce 就是根据上游机器计算结果中的 key，并行合并结果。比如，统计一个文章中的单词频率。第 1-10 段，交给 10 个机器，分别统计，每个机器产生一个 map，key 是 word，value 是 count，这个过程即是 map；然后，用 26 台机器，分别 reduce prefix 位 a-z 的 key 的 count，这个过程就是 reduce
4. Map Reduce 是一个分布式数据处理框架，采用的是 master slave 模式，其中数据划分，机器分配，都是有 master 来完成的。
   - 过程：input, split, map, transfer, reduce, output
   - 其中，只有 map 和 reduce 需要进行写代码，其余部分，均有框架来处理
   - Map Reduce 的核心，就是 map 的 output 是啥，这样，就可以针对性的设计 map 和 reduce 的逻辑了

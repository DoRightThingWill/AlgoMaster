1. Industry practise, general speaking, one master node to store file metadata is big enough
2. Keep it simple and stupid, and make the dirty money
3. What is the checkSum???
   - is hashing?
   - small chagne in the original content, the final checkSum will have a big change
   - checkSum method: MD5, SHA1, SHA256, SHA512
4. MD5, SHA256, SHA512 are all hash function.
   - produce string with fixed length
   - small change in input, will generate big change in output
   - not reversable
5. Encryption algo
   - reversible
6. Heart beat check
   - slave send heart beat to master, it is only one request
   - if master ask heart beat to slave, it needs two requests.
7. 10 billion = 10 GB. billion = 10 ** 9; GB = 10 ** 9
8. 100 M DAU = 1000 QPS

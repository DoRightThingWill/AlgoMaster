1. File system vs online doc system
   - file system. Storage, Search, performance, avaibility
   - online doc. revision and sharing logic
2. User A, B, C udpate the doc same time. User A must see the update immidately
   - User A keep polling from server
   - Server push to User A
3. websocket vs http
   - long liveing connection
   - bidirectional communication
4. Data
   - metadata in DB, SQL
   - content in S3
5. LinkedHashMap to store file content, row based
   - O(1) for row query
   - O(1) for insert and delete
6. Redis to save row based linked list content. Key: file_id+row_id, value: content + next_key.
7. It is a strategy to have duplicate data in data_store. This is called de-normalization
8. Avoid multi user to edit at the same time
   - lock row
   - No lock
     - OT: opertional transform. Google doc is based on OT. 中间，再做一点处理，handle conflict
     - CRDT: Conflict free replicated data type

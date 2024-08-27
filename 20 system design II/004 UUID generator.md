1. auto-incremen for single server. Does not work well for multi-serve
2. UUID version 4, totally random generate
   - 128 bit, 32 hexademical number, 2 \*\* 128
   - easy to scale up since all servers are independent
   - but UUID is not sortable
3. twitter snowfalke id
   - 64 bit
   - timestamp (41 bit), data center Id (5), machine ID (5), counter (12)
   - epoch can be set for snowflake ID
   - 2 \*\* 12 == 4000, IDs can be generated in one milli-second
   - if we have more time-stamp bits, but less counter bits, it can work better for low concurrency and long term project
   - after 69 years, change the epoch
   - mutli-core or multi-machine may not have the clock. So that we can use Internet Clock as the baseline, not machine clock.

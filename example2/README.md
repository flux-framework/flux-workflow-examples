### Using direct job.submit RPC

Schedule/launch compute and io-forwarding jobs on separate nodes

- **salloc -N3 -ppdebug**

- **setenv FLUX_SCHED_OPTIONS "node-excl=true"** # Make sure the scheduler module will do node-exclusive scheduling 

- **srun --pty --mpi=none -N3 /usr/global/tools/flux/toss_3_x86_64_ib/default/bin/flux start -o,-S,log-filename=out**

- **./submitter.lua** # or ./submitter.py

- **flux wreck ls**

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      4 running    2018-05-11T17:41:56       6.446s    [0-1] compute.lua
     2      1 running    2018-05-11T17:41:56       0.105s        2 io-forwarding
```

- **flux kvs get lwj.0.0.1.R_lite**

```
[ { "node": "quartz23", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "0-3" }, "rank": 1 } ]
```

- **flux kvs get lwj.0.0.2.R_lite**

```
[ { "node": "quartz25", "children": { "core": "0" }, "rank": 2 } ]
```

### job.submit RPC example 2

Sschedule/launch both compute and io-forwarding jobs across all nodes

- **salloc -N3 -ppdebug**

- **unsetenv FLUX_SCHED_OPTIONS** # Make sure the scheduler module will do core-level scheduling

- **srun --pty --mpi=none -N3 /g/g0/dahn/workspace/planner_correction/inst/bin/flux start -o,-S,log-filename=out**

- **./submitter2.lua** #or ./submitter2.py

- **flux wreck ls**

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      6 running    2018-05-11T17:48:31       3.416s    [0-2] compute.lua
     2      3 running    2018-05-11T17:48:31       3.408s    [0-2] io-forwarding
```

- **flux kvs get lwj.0.0.1.R_lite**

```json
[ { "node": "quartz23", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "0-3" }, "rank": 1 },
  { "node": "quartz25", "children": { "core": "0-3" }, "rank": 2 } ]
```

- **flux kvs get lwj.0.0.2.R_lite**

```json
[ { "node": "quartz23", "children": { "core": "4" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "4" }, "rank": 1 },
  { "node": "quartz25", "children": { "core": "4" }, "rank": 2 } ]
```


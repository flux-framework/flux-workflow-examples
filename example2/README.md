### Example 2(a) - Using a direct job.submit RPC

#### Description: Schedule and launch compute and io-forwarding jobs on separate nodes

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do node-exclusive scheduling

| Shell     | Command                                        |
| -----     | ----------                                     |
| tcsh      | `setenv FLUX_SCHED_OPTIONS "node-excl=true"`   |
| bash/zsh  | `export FLUX_SCHED_OPTIONS='node-excl=true'`   |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. `./submitter.lua` or `./submitter.py`

5. List jobs in KVS:

`flux wreck ls`

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      4 running    2018-05-11T17:41:56       6.446s    [0-1] compute.lua
     2      1 running    2018-05-11T17:41:56       0.105s        2 io-forwarding
```

7. Get value stored under job key:

`flux kvs get lwj.0.0.1.R_lite`

```
[ { "node": "quartz23", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "0-3" }, "rank": 1 } ]
```

`flux kvs get lwj.0.0.2.R_lite`

```
[ { "node": "quartz25", "children": { "core": "0" }, "rank": 2 } ]
```

### Example 2(b) - Using a direct job.submit RPC

#### Description: Schedule and launch both compute and io-forwarding jobs across all nodes

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do core-level scheduling:

| Shell     | Command                       |
| -----     | ----------                    |
| tcsh      | `unsetenv FLUX_SCHED_OPTIONS` |
| bash/zsh  | `unset FLUX_SCHED_OPTIONS`    |

`srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

`./submitter2.lua` or `./submitter2.py`

3. List jobs in KVS:

`flux wreck ls`

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      6 running    2018-05-11T17:48:31       3.416s    [0-2] compute.lua
     2      3 running    2018-05-11T17:48:31       3.408s    [0-2] io-forwarding
```

4. Get value stored under job key:

`flux kvs get lwj.0.0.1.R_lite`

```json
[ { "node": "quartz23", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "0-3" }, "rank": 1 },
  { "node": "quartz25", "children": { "core": "0-3" }, "rank": 2 } ]
```

`flux kvs get lwj.0.0.2.R_lite`

```json
[ { "node": "quartz23", "children": { "core": "4" }, "rank": 0 },
  { "node": "quartz24", "children": { "core": "4" }, "rank": 1 },
  { "node": "quartz25", "children": { "core": "4" }, "rank": 2 } ]
```

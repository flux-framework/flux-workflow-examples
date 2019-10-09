### Example 1(a) - Partitioning Schedule

#### Description: Launch a flux instance and schedule/launch compute and io-forwarding jobs on separate nodes

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do node-exclusive scheduling:

| Shell     | Command                                        |
| -----     | ----------                                     |
| tcsh      | `setenv FLUX_SCHED_OPTIONS "node-excl=true"`   |
| bash/zsh  | `export FLUX_SCHED_OPTIONS='node-excl=true'`   |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. `flux submit --nnodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120`

5. `flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120`

6. List jobs in KVS:

`flux wreck ls`

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     2      1 running    2018-05-11T14:58:39       2.891s        2 io-forwarding
     1      4 running    2018-05-11T14:58:33       9.284s    [0-1] compute.lua
```

7. Get value stored under job key:

`flux kvs get lwj.0.0.1.R_lite`

```json
[ { "node": "quartz32", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz33", "children": { "core": "0-3" }, "rank": 1 } ]
```

`flux kvs get lwj.0.0.2.R_lite`

```json
[ { "node": "quartz34", "children": { "core": "0-1" }, "rank": 2 } ]
```

### Example 1(b) - Overlapping Schedule

#### Description: Launch a flux instance and schedule/launch both compute and io-forwarding jobs across all nodes

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do core-level scheduling:

| Shell     | Command                       |
| -----     | ----------                    |
| tcsh      | `unsetenv FLUX_SCHED_OPTIONS` |
| bash/zsh  | `unset FLUX_SCHED_OPTIONS`    |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. `flux submit --nnodes=3 --ntasks=6 --cores-per-task=2 ./compute.lua 120`

5. `flux submit --nnodes=3 --ntasks=3 --cores-per-task=1 ./io-forwarding.lua 120`

6. List jobs in KVS:

`flux wreck ls`

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     2      3 running    2018-05-11T15:09:39       2.654s    [0-2] io-forwarding
     1      6 running    2018-05-11T15:09:23      17.956s    [0-2] compute.lua
```

7. Get value stored under job key:

`flux kvs get lwj.0.0.1.R_lite`

```json
[ { "node": "quartz32", "children": { "core": "0-3" }, "rank": 0 },
  { "node": "quartz33", "children": { "core": "0-3" }, "rank": 1 },
  { "node": "quartz34", "children": { "core": "0-3" }, "rank": 2 } ]
```

`flux kvs get lwj.0.0.2.R_lite`

```json
[ { "node": "quartz32", "children": { "core": "4" }, "rank": 0 },
  { "node": "quartz33", "children": { "core": "4" }, "rank": 1 },
  { "node": "quartz34", "children": { "core": "4" }, "rank": 2 } ]
```

### Example 3 - Using Events with Separate Nodes

#### Description: Using events to synchronize compute and io-forwarding jobs running on separate nodes

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do node-exclusive scheduling

| Shell     | Command                                        |
| -----     | ----------                                     |
| tcsh      | `setenv FLUX_SCHED_OPTIONS "node-excl=true"`   |
| bash/zsh  | `export FLUX_SCHED_OPTIONS='node-excl=true'`   |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. `flux submit --nnodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120`

**Output -** `submit: Submitted jobid 1`

5. `flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120`

**Output -** `submit: Submitted jobid 2`

6. List jobs in KVS:

`flux wreck ls`

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      4 running    2018-05-11T17:41:56       6.446s    [0-1] compute.lua
     2      1 running    2018-05-11T17:41:56       0.105s        2 io-forwarding
```

7. Attach to running or completed job output:

`flux wreck attach 1`

```
1: Block until we hear go message from the an io forwarder
2: Block until we hear go message from the an io forwarder
3: Block until we hear go message from the an io forwarder
0: Block until we hear go message from the an io forwarder
1: Recv an event: please proceed
2: Recv an event: please proceed
3: Recv an event: please proceed
0: Recv an event: please proceed
1: Will compute for 10 seconds
2: Will compute for 10 seconds
3: Will compute for 10 seconds
0: Will compute for 10 seconds
```

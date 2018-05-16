### Using events to synchronize compute and io-forwarding jobs running on separate nodes

- **salloc -N3 -ppdebug** 

- **setenv FLUX_SCHED_OPTIONS "node-excl=true"** *# Make sure the scheduler module will do node-exclusive scheduling*

- **srun --pty --mpi=none -N3 /g/g0/dahn/workspace/planner_correction/inst/bin/flux start -o,-S,log-filename=out**

- **flux submit --nnodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120**

- **flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120**

- **flux wreck ls**

```
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      4 running    2018-05-11T17:41:56       6.446s    [0-1] compute.lua
     2      1 running    2018-05-11T17:41:56       0.105s        2 io-forwarding
```

- **flux wreck attach 1**

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


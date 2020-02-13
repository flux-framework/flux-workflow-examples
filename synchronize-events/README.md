### Using Events with Separate Nodes

#### Description: Using events to synchronize compute and io-forwarding jobs running on separate nodes

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `flux mini submit --nodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120`

**Output -** `901355929600`

4. `flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120`

**Output -** `1244299001856`

5. List running jobs:

`flux job list`

```
JOBID		       STATE	  USERID   PRI     T_SUBMIT
901355929600	   R	      58985	   16	   2019-10-22T16:27:02Z
1244299001856	   R	      58985	   16	   2019-10-22T16:27:26Z
```

6. Attach to running or completed job output:

`flux job attach 901355929600`

```
Block until we hear go message from the an io forwarder
Block until we hear go message from the an io forwarder
Recv an event: please proceed
Recv an event: please proceed
Will compute for 120 seconds
Will compute for 120 seconds
Block until we hear go message from the an io forwarder
Block until we hear go message from the an io forwarder
Recv an event: please proceed
Recv an event: please proceed
Will compute for 120 seconds
Will compute for 120 seconds
```

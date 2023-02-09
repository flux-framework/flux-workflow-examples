### Using Events with Separate Nodes

#### Description: Using events to synchronize compute and io-forwarding jobs running on separate nodes

If you haven't already, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/synchronize-events
```

1. Allocate three nodes from the resource manager

  If launching under Flux:

     `flux mini alloc -N3`

  If launching via Slurm:

     A. `salloc -N3 -ppdebug`

     B. Launch a Flux instance on the current allocation by running `flux start`
        once per node, redirecting log messages to the file `out` in the current
        directory:

        `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

2. `flux mini submit --nodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120`

**Output -** `225284456448`

3. `flux mini submit --nodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120`

**Output -** `344889229312`

4. List running jobs:

`flux jobs`

```
JOBID    USER     NAME       ST NTASKS NNODES  RUNTIME RANKS
ƒA4TgT7d moussa1  io-forward  R      1      1   4.376s 2
ƒ6vEcj7M moussa1  compute.lu  R      4      2   11.51s [0-1]
```

5. Attach to running or completed job output:

`flux job attach ƒ6vEcj7M`

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

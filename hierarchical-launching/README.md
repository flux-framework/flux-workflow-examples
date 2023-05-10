## Hierarchical Launching

### Description: Launch an ensemble of sleep 0 tasks

#### Setup

If you haven't already, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/hierarchical-launching
```

#### Execution

1. Allocate three nodes from the resource manager

  If launching under Flux:

     `flux mini alloc -N3`

  If launching via Slurm:

     A. `salloc -N3 -ppdebug`

     B. Launch a Flux instance on the current allocation by running `flux start`
        once per node, redirecting log messages to the file `out` in the current
        directory:

        `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

2. `./parent.sh`

```
Mon Nov 18 15:31:08 PST 2019
13363018989568
13365166473216
13367095853056
First Level Done
Mon Nov 18 15:34:13 PST 2019
```


### Notes

- You can increase the number of jobs by increasing `NCORES` in `parent.sh` and
`NJOBS` in `ensemble.sh`.

### Example 6 - Hierarchical Launching

#### Description: Launch a very large ensemble of sleep 0 tasks

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do core-level scheduling:

| Shell     | Command                       |
| -----     | ----------                    |
| tcsh      | `unsetenv FLUX_SCHED_OPTIONS` |
| bash/zsh  | `unset FLUX_SCHED_OPTIONS`    |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

`./parent.sh`

```
Mon May 14 19:42:08 PDT 2018
submit: Submitted jobid 1
submit: Submitted jobid 2
submit: Submitted jobid 3
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      1 exited     2018-05-14T19:42:08       9.192m        0 children.sh
     2      1 exited     2018-05-14T19:42:08       9.023m        1 children.sh
     3      1 exited     2018-05-14T19:42:08       9.388m        2 children.sh
First Level Done
Mon May 14 19:51:31 PDT 2018
```

#### Notes

- You can increase the number of jobs by increasing `NCORES` in `parent.sh` and
`NJOBS` in `ensemble.sh`.

### Hierarchical Launching

- Launching over one million sleep 0 task

- **salloc -N3 -ppdebug** 

- **setenv FLUX_SCHED_OPTIONS "node-excl=true"** *# Make sure the scheduler module will do core-level scheduling*

- **srun --pty --mpi=none -N3 /g/g0/dahn/workspace/planner_correction/inst/bin/flux start -o,-S,log-filename=out**

- **parent.sh**

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

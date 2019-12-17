### Example 7 - Using Flux Job Status and Control API

#### Description: Submit job bundles and wait until all jobs complete

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `./bookkeeper.py 5`

```
bookkeeper: all jobs submitted
bookkeeper: waiting until all jobs complete
job 1417322430464 changed its state to DEPEND
job 1417322430464 changed its state to SCHED
job 1417758638080 changed its state to DEPEND
job 1417758638080 changed its state to SCHED
job 1418161291264 changed its state to DEPEND
job 1418161291264 changed its state to SCHED
.
.
.
job 282058555392 changed its state to CLEANUP
job 285564993536 changed its state to CLEANUP
.
.
.
job 282058555392 changed its state to INACTIVE
job 285564993536 changed its state to INACTIVE
.
.
.
bookkeeper: all jobs completed
```

### Example 7 - Using Flux Job Status and Control API

#### Description: Submit job bundles and wait until all jobs complete

1. `salloc -N3 -ppdebug`

2. Make sure the scheduler module will do core-level scheduling:

| Shell     | Command                       |
| -----     | ----------                    |
| tcsh      | `unsetenv FLUX_SCHED_OPTIONS` |
| bash/zsh  | `unset FLUX_SCHED_OPTIONS`    |

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. `./bookkeeper.py 5`

```
bookkeeper: all jobs submited
bookkeeper: waiting until all jobs complete
bookkeeper: all jobs completed
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      6 exited     2018-05-18T18:48:01       5.724s    [0-2] compute.py
     2      3 exited     2018-05-18T18:48:01       5.742s    [0-2] io-forwarding
     3      6 exited     2018-05-18T18:48:01       5.729s    [0-2] compute.py
     4      3 exited     2018-05-18T18:48:01       5.647s    [0-2] io-forwarding
     5      6 exited     2018-05-18T18:48:01       5.661s    [0-2] compute.py
     6      3 exited     2018-05-18T18:48:01       5.611s    [0-2] io-forwarding
     7      6 exited     2018-05-18T18:48:01       5.667s    [0-2] compute.py
     8      3 exited     2018-05-18T18:48:01       5.633s    [0-2] io-forwarding
     9      6 exited     2018-05-18T18:48:01       5.583s    [0-2] compute.py
    10      3 exited     2018-05-18T18:48:01       5.608s    [0-2] io-forwarding
```

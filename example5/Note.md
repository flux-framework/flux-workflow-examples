### Using a Flux comms module to comminicate with job elements

- **salloc -N3 -ppdebug** 

- **setenv FLUX_SCHED_OPTIONS "node-excl=true"** *# Make sure the scheduler module will do node-exclusive scheduling*

- **srun --pty --mpi=none -N3 /g/g0/dahn/workspace/planner_correction/inst/bin/flux start -o,-S,log-filename=out**

- **flux submit -N 2 -n 2 compute.lua 120**

- **flux submit -N 2 -n 2 io-forwarding.lua 120**


### 1. Job ensemble submitted with a new flux instance

- Launch a flux instance and submit one instance of io-forwaring job and 50 compute jobs, each spanning the entire set of nodes.

- **salloc -N3 -ppdebug** 

- **cat ensemble.sh**

```sh
#!/usr/bin/env sh

NJOBS=10
MAXTIME=$(expr ${NJOBS} + 2)

flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua ${MAXTIME}
for i in `seq 1 ${NJOBS}`; do
    flux submit --nnodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 1
done

KEY=$(echo $(flux wreck kvs-path 1).state)
kvs-watch-until.lua -t ${MAXTIME} ${KEY} 'v == "complete"'
flux wreck ls -n 100

# print mock-up prevenance data
for i in `seq 1 $(expr ${NJOBS} + 1)`; do
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Jobid: ${i}"
    echo "Cmdline: " "$(flux kvs get $(flux wreck kvs-path ${i}).cmdline)"
    echo "$(R_lite.lua ${i})" | sed -e 's/^/Resource: /'
done
```

- **unsetenv FLUX_SCHED_OPTIONS** *# Make sure the scheduler module will do core-level scheduling*

- **srun --pty --mpi=none -N3 /usr/global/tools/flux/toss_3_x86_64_ib/default/bin/flux start -o,-S,log-filename=out ensemble.sh**

```
submit: Submitted jobid 1
submit: Submitted jobid 2
submit: Submitted jobid 3
submit: Submitted jobid 4
submit: Submitted jobid 5
submit: Submitted jobid 6
submit: Submitted jobid 7
submit: Submitted jobid 8
submit: Submitted jobid 9
submit: Submitted jobid 10
submit: Submitted jobid 11
    ID NTASKS STATE                    START      RUNTIME    RANKS COMMAND
     1      1 exited     2018-05-12T11:29:25      12.053s        0 io-forwarding
     2      4 exited     2018-05-12T11:29:25       1.119s    [0-1] compute.lua
     3      4 exited     2018-05-12T11:29:25       1.111s    [0-1] compute.lua
     4      4 exited     2018-05-12T11:29:25       1.105s    [0-1] compute.lua
     5      4 exited     2018-05-12T11:29:25       1.095s    [0-1] compute.lua
     6      4 exited     2018-05-12T11:29:25       1.092s    [0-1] compute.lua
     7      4 exited     2018-05-12T11:29:25       1.100s    [0-1] compute.lua
     8      4 exited     2018-05-12T11:29:25       1.087s    [0-1] compute.lua
     9      4 exited     2018-05-12T11:29:25       1.074s    [0-1] compute.lua
    10      4 exited     2018-05-12T11:29:25       1.079s    [1-2] compute.lua
    11      4 exited     2018-05-12T11:29:26       1.084s    [0-1] compute.lua
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 1
Cmdline:  ["./io-forwarding.lua","12"]
Resource: rank0: count=2 core=0-1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 2
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=2-5
Resource: rank1: count=4 core=0-3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 3
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=6-9
Resource: rank1: count=4 core=4-7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 4
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=10-13
Resource: rank1: count=4 core=8-11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 5
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=14-17
Resource: rank1: count=4 core=12-15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 6
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=18-21
Resource: rank1: count=4 core=16-19
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 7
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=22-25
Resource: rank1: count=4 core=20-23
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 8
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=26-29
Resource: rank1: count=4 core=24-27
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 9
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=30-33
Resource: rank1: count=4 core=28-31
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 10
Cmdline:  ["./compute.lua","1"]
Resource: rank1: count=4 core=32-35
Resource: rank2: count=4 core=0-3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 11
Cmdline:  ["./compute.lua","1"]
Resource: rank0: count=4 core=2-5
Resource: rank1: count=4 core=0-3
```

## Job Submit CLI

To run the following examples, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/job-submit-cli
```

### Part(a) - Partitioning Schedule

#### Description: Launch a flux instance and schedule/launch compute and io-forwarding jobs on separate nodes

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `flux mini submit --nodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 120`

4. `flux mini submit --nodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua 120`

5. List running jobs:

`flux jobs`

```
       JOBID USER     NAME       ST NTASKS NNODES     TIME INFO
    fBeKwwvw achu     io-forwar+  R      1      1   53.84s corona180
    f8usei1M achu     compute.l+  R      4      2   1.001m corona[181-182]
```

### Part(b) - Overlapping Schedule

#### Description: Launch a flux instance and schedule/launch both compute and io-forwarding jobs across all nodes

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `flux mini submit --nodes=3 --ntasks=6 --cores-per-task=2 ./compute.lua 120`

4. `flux mini submit --nodes=3 --ntasks=3 --cores-per-task=1 ./io-forwarding.lua 120`

5. List running jobs:

`flux jobs`

```
       JOBID USER     NAME       ST NTASKS NNODES     TIME INFO
    fMaFAxLF achu     compute.l+  R      6      3   14.82s corona[183-185]
    fJebX8yd achu     io-forwar+  R      3      3   21.46s corona[183-185]
```

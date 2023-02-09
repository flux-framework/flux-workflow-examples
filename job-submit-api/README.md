## Job Submit API

To run the following examples, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/job-submit-api
```

### Part(a) - Using a direct job.submit RPC

#### Description: Schedule and launch compute and io-forwarding jobs on separate nodes

1. Allocate three nodes from a resource manager:

`salloc -N3 -p pdebug`

2. Launch a Flux instance on the current allocation by running `flux start` once per node, redirecting log messages to the file `out` in the current directory:

`srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. Run the submitter executable:

`./submitter.py`

4. List currently running jobs:

`flux jobs`

```
       JOBID USER     NAME       ST NTASKS NNODES     TIME INFO
    fAWRwsRy achu     io-forwar+  R      1      1   41.41s corona180
    fAVntBPM achu     compute.py  R      4      2   41.44s corona[181-182]
```

### Part(b) - Using a direct job.submit RPC

#### Description: Schedule and launch both compute and io-forwarding jobs across all nodes

1. Allocate three nodes from a resource manager:

`salloc -N3 -p pdebug`

2. Launch another Flux instance on the current allocation:

`srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. Run the second submitter executable:

`./submitter2.py`

4. List currently running jobs:

`flux jobs`

```
       JOBID USER     NAME       ST NTASKS NNODES     TIME INFO
    ƒ3xfmqcs achu     io-forwar+  R      3      3   2.179s corona[186-188]
    ƒ3x2i9aF achu     compute.py  R      6      3   2.204s corona[186-188]
```

---

### Notes

- `f = flux.Flux()` creates a new Flux handle which can be used to connect to and interact with a Flux instance.


- The following constructs a job request using the **JobspecV1** class with customizable parameters for how you want to utilize the resources allocated for your job:
```python
compute_jobreq = JobspecV1.from_command(
    command=["./compute.py", "120"], num_tasks=4, num_nodes=2, cores_per_task=2
)
compute_jobreq.cwd = os.getcwd()
compute_jobreq.environment = dict(os.environ)
```

- `flux.job.submit(f, compute_jobreq)` submits the job to be run, and returns a job ID once it begins running.

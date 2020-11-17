## Using Flux Job Status and Control API

### Description: Submit job bundles and wait until all jobs complete

1. Allocate three nodes from a resource manager:

`salloc -N3 -p pdebug`

2. Launch a Flux instance on the current allocation by running `flux start` once per node, redirecting log messages to the file `out` in the current directory:

`srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. Run the bookkeeper executable along with the number of jobs to be submitted (if no size is specified, 6 jobs are submitted: 3 instances of **compute.py**, and 3 instances of **io-forwarding,py**):

`./bookkeeper.py 2`

```
17341081452544
17341383442432
bookkeeper: all jobs submitted
bookkeeper: waiting until all jobs complete
job 17341081452544 changed its state to DEPEND
job 17341081452544 changed its state to SCHED
job 17341081452544 changed its state to RUN
job 17341383442432 changed its state to DEPEND
job 17341383442432 changed its state to SCHED
job 17341081452544 changed its state to CLEANUP
job 17341081452544 changed its state to INACTIVE
job 17341383442432 changed its state to RUN
job 17341383442432 changed its state to CLEANUP
job 17341383442432 changed its state to INACTIVE
bookkeeper: all jobs completed
```

---

### Notes

- `f = flux.Flux()` creates a new Flux handle which can be used to connect to and interact with a Flux instance.


- The following constructs a job request using the **JobspecV1** class with customizable parameters for how you want to utilize the resources allocated for your job:
```python
compute_jobreq = JobspecV1.from_command(
    command=["./compute.py", "10"], num_tasks=4, num_nodes=2, cores_per_task=2
)
compute_jobreq.cwd = os.getcwd()
compute_jobreq.environment = dict(os.environ)
```

- `flux.job.submit(f, compute_jobreq)` submits the job to be run, and returns a job ID once it begins running.

- Throughout the course of a job, its state will go through a number of changes. The following subscribes to the event messages matching the transition of those states in the jobs submitted.
```python
    f.event_subscribe("job-state")
    f.msg_watcher_create(job_state_cb, 0, "job-state").start()
    submit_bundles(f, njobs)
    print("bookkeeper: waiting until all jobs complete")
    f.reactor_run(f.get_reactor(), 0)
    print("bookkeeper: all jobs completed")
```

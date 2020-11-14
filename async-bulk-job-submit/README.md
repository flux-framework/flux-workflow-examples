## Python Asynchronous Bulk Job Submission

### Description: Asynchronously submit jobspec files from a directory and wait for them to complete in any order

1. Allocate three nodes from a resource manager:

`salloc -N3 -ppdebug`

2. Make a **jobs** directory:

`mkdir jobs`

3. Launch a Flux instance on the current allocation by running `flux start` once per node, redirecting log messages to the file `out` in the current directory:

`srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

4. Store the jobspec of a `sleep 0` job in the **jobs** directory:

`flux mini run --dry-run -n1 sleep 0 > jobs/0.json`

5. Copy the jobspec of **job0** 1024 times to create a directory of 1025 `sleep 0` jobs:

``for i in `seq 1 1024`; do cp jobs/0.json jobs/${i}.json; done``

6. Run the **bulksubmit.py** script and pass all jobspec in the **jobs** directory as an argument with a shell glob `jobs/*.json`:

`./bulksubmit.py jobs/*.json`

```
bulksubmit: Starting...
bulksubmit: submitted 1025 jobs in 3.04s. 337.09job/s
bulksubmit: First job finished in about 3.089s
|██████████████████████████████████████████████████████████| 100.0% (29.4 job/s)
bulksubmit: Ran 1025 jobs in 34.9s. 29.4 job/s
```

### Notes

- `h = flux.Flux()` creates a new Flux handle which can be used to connect to and interact with a Flux instance.

- `job_submit_async(h, jobspec.read(), waitable=True).then(submit_cb)` submits a jobspec, returning a future which will be fulfilled when the submission of this job is complete.

`.then(submit_cb)`, called on the returned future, will cause our callback `submit_cb()` to be invoked when the submission of this job is complete and a jobid is available. To process job submission RPC responses and invoke callabacks, the flux reactor for handle `h` must be run:

```python
if h.reactor_run() < 0:
￼    h.fatal_error("reactor start failed")
```

The reactor will return automatically when there are no more outstanding RPC responses, i.e., all jobs have been submitted.

- `job.wait(h)` waits for any job submitted with the `FLUX_JOB_WAITABLE` flag to transition to the **INACTIVE** state.

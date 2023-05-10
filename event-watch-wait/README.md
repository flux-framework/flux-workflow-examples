## Job Event Watch/Wait

To run the following examples, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/job-event
```

### Part(a) - Event Wait

#### Description: Use the job eventlog to wait for a certain event synchronously.

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `flux python event-wait.py $(flux mini submit -n4 hostname)`

```
node24
node24
node24
node24
```

### Part(b) - Event Watch

#### Description: Asynchronously watch job events via a `.then()` callback.

1. `salloc -N3 -ppdebug`

2. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3. `flux python event-watch.py $(flux mini submit -n4 sleep 1)`

```
1616789213.11403: submit {'userid': 58985, 'urgency': 16, 'flags': 0}
1616789213.12785: depend {}
1616789213.12789: priority {'priority': 16}
1616789213.13040: alloc {'annotations': {'sched': {'resource_summary': 'rank0/core[0-3]'}}}
1616789213.13865: start {}
1616789213.13138: init {}
1616789213.13288: starting {}
1616789213.18925: shell.init {'leader-rank': 0, 'size': 1, 'service': '58985-shell-4548605247488'}
1616789213.20083: shell.start {'task-count': 4}
1616789214.20549: complete {'status': 0}
1616789214.20554: done {}
1616789214.20569: finish {'status': 0}
1616789214.20904: release {'ranks': 'all', 'final': True}
1616789214.21015: free {}
1616789214.21027: clean {}
```

---

### Notes

- `job.event_wait(h, jobid, name, eventlog="eventlog")` waits for an event named `name` in `eventlog` synchronously. It blocks and returns an `EventLogEvent` for the matched event, or `None` if the eventlog ended with no match.

- `job.event_watch_async(h, jobid, name="*", eventlog="eventlog")` returns a `JobEventWatchFuture` which can be used to asynchronously watch job events via a `.then()` callback. Events can be optionally filtered on the `name` glob (default all events). A `JobEventWatchFuture` internally queues events for consumption in the continuation with `future.get_event()`. `future.reset()` must be called to "consume" the event.

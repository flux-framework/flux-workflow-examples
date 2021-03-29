import sys
import flux
from flux import job
from flux.job import JobID

jobid = JobID(sys.argv[1]).dec


def cb(future, h):
    event = future.get_event()
    if event is None:
        return
    if event.name == "start":
        job.event_watch_async(h, jobid, eventlog="guest.exec.eventlog").then(cb, h)
    print(event)
    future.reset()


h = flux.Flux()
job.event_watch_async(h, jobid).then(cb, h)
h.reactor_run()

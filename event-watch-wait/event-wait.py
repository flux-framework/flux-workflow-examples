import sys
import flux
from flux import job
from flux.job import JobID

jobid = JobID(sys.argv[1]).dec

h = flux.Flux()

# block until "start" event, so we know exec.eventlog is available
job.event_wait(h, jobid, "start")

# block until "shell.init" event, so we know output eventlog is available
job.event_wait(h, jobid, "shell.init", eventlog="guest.exec.eventlog")

# process output eventlog (doesn't differentiate between stdout/err)
for event in job.event_watch(h, jobid, eventlog="guest.output"):
    if event.name == "data" and "data" in event.context:
        print(event.context["data"].strip())

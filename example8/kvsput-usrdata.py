#!/usr/bin/env python

import sys
import flux
import os
from flux import kvs

f = flux.Flux ()
job_path = os.environ['FLUX_JOB_KVSPATH']
udata = job_path + ".usrdata"
# using function interface
kvs.put (f, udata, "mydata")
# commit is required to effect the above put op to the server
kvs.commit (f)
print kvs.get (f, udata)

# get on a directory will return KVSDir object which support
# with compound statement. "with" guarantees commit is called
# on the directory if job_path is a valid input.
with kvs.get (f, job_path) as kd:
   kd['usrdata2'] = "mydata2"

print kvs.get (f, job_path + ".usrdata2")

# vi: ts=4 sw=4 expandtab

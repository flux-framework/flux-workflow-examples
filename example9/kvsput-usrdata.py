#!/usr/bin/env python

import sys
import flux
import os
from flux import kvs

f = flux.Flux ()
udata = "hello world"
# using function interface
kvs.put (f, "usrdata", udata)
# commit is required to effect the above put op to the server
kvs.commit (f)
print kvs.get (f, "usrdata")

# get on a directory will return KVSDir object which support
# with compound statement. "with" guarantees commit is called
# on the directory if job_path is a valid input.
with kvs.get (f, ".") as kd:
   kd['usrdata2'] = "hello world again"

print kvs.get (f, "usrdata2")

# vi: ts=4 sw=4 expandtab

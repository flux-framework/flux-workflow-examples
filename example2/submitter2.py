#!/usr/bin/env python

import json
import os
import re
import flux
#from flux.rpc import rpc

def get_environment():
    env = dict()
    for key in os.environ:
        env[key] = os.environ[key]
    return env

compute_jobreq = {
    'nnodes' : 3,
    'ntasks' : 6,
    'ncores' : 12,
    'cmdline' : ["compute.py", "120"],
    'environ' : get_environment (),
    'cwd' : os.getcwd (),
    'walltime' : 0,
    'ngpus' : 0,
}

io_jobreq = {
    'nnodes' : 3,
    'ntasks' : 3,
    'ncores' : 3,
    'cmdline' : ["io-forwarding.py", "120"],
    'environ' : get_environment (),
    'cwd' : os.getcwd (),
    'walltime' : 0,
    'ngpus' : 0,
}

payload = json.dumps (compute_jobreq)
f = flux.Flux ()
resp = f.rpc_send ("job.submit", payload)
if resp is None:
    print "flux.rpc: compute_jobreq", "failed"

payload = json.dumps (io_jobreq)
resp = f.rpc_send ("job.submit", payload)
if resp is None:
    print "flux.rpc: io_jobreq", "failed"


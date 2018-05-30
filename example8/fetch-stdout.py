#!/usr/bin/env python

import sys
import flux
from flux import kz

f = flux.Flux ()
kz.attach (f, "lwj.0.0.1.0.stdout", sys.stdout)
kz.attach (f, "lwj.0.0.1.1.stdout", sys.stdout)

f.reactor_run (f.get_reactor (), 0)

# vi: ts=4 sw=4 expandtab

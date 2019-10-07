#!/usr/bin/env lua

local posix = require 'flux.posix'
local wreck = require 'wreck' .new ()
local f, err = require 'flux' .new ()

if not f then
    error (err)
end

local compute_jobreq = {
    nnodes = 3,
    ntasks = 6,
    ncores = 12,
    cmdline = {"./compute.lua", "120"},
    environ = wreck:get_filtered_env (),
    cwd = posix.getcwd (),
    walltime = 0,
    ngpus = 0,
}

local io_jobreq = {
    nnodes =  3,
    ntasks =  3,
    ncores =  3,
    cmdline = {"./io-forwarding.lua", "120"},
    environ = wreck:get_filtered_env (),
    cwd =     posix.getcwd (),
    walltime = 0,
    ngpus = 0,
}

local resp, err = f:rpc ("job.submit", compute_jobreq)

if not resp then
    print ("flux.rpc: compute_jobreq" .. err)
end
if resp.errnum then
    print ("flux.rpc: compute_jobreq" .. resp.errnum)
end

local resp, err = f:rpc ("job.submit", io_jobreq)

if not resp then
    print ("flux.rpc: compute_jobreq" .. err)
end
if resp.errnum then
    print ("flux.rpc: compute_jobreq" .. resp.errnum)
end

#!/usr/bin/env lua
local flux = require 'flux'
local f = assert (flux.new())

local iow1, err = f:iowatcher {
                      key = "lwj.0.0.1.0.stdout",
                      handler = function (iow1, data)
                          if data ~= nil then
                            io.stdout:write (string.format ("%s", data))
                          end
                      end
                 }
local iow2, err = f:iowatcher {
                       key = "lwj.0.0.1.1.stdout",
                       handler = function (iow2, data)
                          if data ~= nil then
                            io.stdout:write (string.format ("%s", data))
                          end
                       end
                   }

f:reactor ()

-- vi: ts=4 sw=4 expandtab

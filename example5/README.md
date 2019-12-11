### Example 5 - Using a Flux Comms Module

#### Description: Use a Flux comms module to communicate with job elements

1. `salloc -N3 -ppdebug`

2. Point to `flux-core`'s `pkgconfig` directory:

| Shell     | Command                                                      |
| -----     | ----------                                                   |
| tcsh      | `setenv PKG_CONFIG_PATH <FLUX_INSTALL_PATH>/lib/pkgconfig`   |
| bash/zsh  | `export PKG_CONFIG_PATH='<FLUX_INSTALL_PATH>/lib/pkgconfig'` |

3. `make`

4. Add the directory of the modules to `FLUX_MODULE_PATH`; if the module was
built in the current dir:

`export FLUX_MODULE_PATH=${FLUX_MODULE_PATH}:$(pwd)`

5. Make sure the scheduler module will do node-exclusive scheduling:

| Shell     | Command                                        |
| -----     | ----------                                     |
| tcsh      | `setenv FLUX_SCHED_OPTIONS "node-excl=true"`   |
| bash/zsh  | `export FLUX_SCHED_OPTIONS='node-excl=true'`   |

6. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

7. `flux submit -N 2 -n 2 ./compute.lua 120`

8. `flux submit -N 1 -n 1 ./io-forwarding.lua 120`

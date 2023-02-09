### Using a Flux Comms Module

#### Description: Use a Flux comms module to communicate with job elements

##### Setup

If you haven't already, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/comms-module
```

##### Execution

1. Allocate three nodes from the resource manager

  If launching under Flux:

     `flux mini alloc -N3`

  If launching via Slurm:

     A. `salloc -N3 -ppdebug`

     B. Launch a Flux instance on the current allocation by running `flux start`
        once per node, redirecting log messages to the file `out` in the current
        directory:

        `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

2. Point to `flux-core`'s `pkgconfig` directory:

| Shell     | Command                                                      |
| -----     | ----------                                                   |
| tcsh      | `setenv PKG_CONFIG_PATH <FLUX_INSTALL_PATH>/lib/pkgconfig`   |
| bash/zsh  | `export PKG_CONFIG_PATH='<FLUX_INSTALL_PATH>/lib/pkgconfig'` |

3. `make`

4. Add the directory of the modules to `FLUX_MODULE_PATH`; if the module was
built in the current dir:

| Shell     | Command                                              |
| -----     | ----------                                           |
| tcsh      | `setenv FLUX_MODULE_PATH=${FLUX_MODULE_PATH}:$PWD`   |
| bash/zsh  | `export FLUX_MODULE_PATH=${FLUX_MODULE_PATH}:$(pwd)` |

5. `flux mini submit -N 2 -n 2 ./compute.lua 120`

6. `flux mini submit -N 1 -n 1 ./io-forwarding.lua 120`

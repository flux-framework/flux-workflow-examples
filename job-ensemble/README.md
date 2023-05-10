### Job Ensemble Submitted with a New Flux Instance

#### Description: Launch a flux instance and submit one instance of an io-forwarding job and 50 compute jobs, each spanning the entire set of nodes.

#### Setup

If you haven't already, download the files and change your working directory:

```
$ git clone https://github.com/flux-framework/flux-workflow-examples.git
$ cd flux-workflow-examples/job-ensemble
```

#### Execution

1. `cat ensemble.sh`

```
#!/usr/bin/env sh

NJOBS=10
MAXTIME=$(expr ${NJOBS} + 2)
JOBIDS=""

JOBIDS=$(flux mini submit --nodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua ${MAXTIME})
for i in `seq 1 ${NJOBS}`; do
    JOBIDS="${JOBIDS} $(flux mini submit --nodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 1)"
done

flux jobs
flux queue drain

# print mock-up prevenance data
for i in ${JOBIDS}; do
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Jobid: ${i}"
    KVSJOBID=$(flux job id --from=dec --to=kvs ${i})
    flux kvs get ${KVSJOBID}.R | jq
done
```

2. Allocate three nodes from the resource manager

  If launching under Flux:

     `flux mini alloc -N3`

  If launching via Slurm:

     A. `salloc -N3 -ppdebug`

     B. Launch a Flux instance on the current allocation by running `flux start`
        once per node, redirecting log messages to the file `out` in the current
        directory:

        `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

3.  Run the ensemble

`./ensemble.sh`

```
       JOBID USER     NAME       ST NTASKS NNODES  RUNTIME NODELIST
   f3faERxGo achu     compute.lu  R      4      2   0.163s opal[63,65]
   f3fV7vRuq achu     compute.lu  R      4      2   0.363s opal[63,65]
   f3fPrWyro achu     compute.lu  R      4      2   0.569s opal[63,65]
   f3fJWfZxj achu     compute.lu  R      4      2   0.777s opal[63,65]
   f3fCwUGXZ achu     compute.lu  R      4      2   0.998s opal[63-64]
   f3efRVY4P achu     io-forward  R      1      1   2.228s opal65
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: f3efRVY4P
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "2",
        "children": {
          "core": "34-35"
        }
      }
    ],
    "nodelist": [
      "opal65"
    ],
    "starttime": 1675955769,
    "expiration": 1676560569
  }
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: f3ekdw1Yj
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "2",
        "children": {
          "core": "30-33"
        }
      },
      {
        "rank": "1",
        "children": {
          "core": "32-35"
        }
      }
    ],
    "nodelist": [
      "opal[64-65]"
    ],
    "starttime": 1675955770,
    "expiration": 1676560570
  }
}
.
.
.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: f3faERxGo
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "0",
        "children": {
          "core": "16-19"
        }
      },
      {
        "rank": "2",
        "children": {
          "core": "18-21"
        }
      }
    ],
    "nodelist": [
      "opal[63,65]"
    ],
    "starttime": 1675955771,
    "expiration": 1676560571
  }
}

```

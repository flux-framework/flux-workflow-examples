### Job Ensemble Submitted with a New Flux Instance

#### Description: Launch a flux instance and submit one instance of an io-forwarding job and 50 compute jobs, each spanning the entire set of nodes.

1. `salloc -N3 -ppdebug`

2. `cat ensemble.sh`

```
#!/usr/bin/env sh

NJOBS=10
MAXTIME=$(expr ${NJOBS} + 2)
JOBIDS=""

JOBIDS=$(flux mini submit --nodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua ${MAXTIME})
for i in `seq 1 ${NJOBS}`; do
    JOBIDS="${JOBIDS} $(flux mini submit --nodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 1)"
done

flux job list
flux job drain
flux job undrain

# print mock-up prevenance data
for i in ${JOBIDS}; do
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Jobid: ${i}"
    KVSJOBID=$(flux job id --from=dec --to=kvs ${i})
    flux kvs get ${KVSJOBID}.R | jq
done
```

3. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out ./ensemble.sh`

```
JOBID		STATE	USERID	PRI	T_SUBMIT
36507222016	S	58985	16	2019-11-18T23:07:05Z
34644951040	R	58985	16	2019-11-18T23:07:05Z
32782680064	R	58985	16	2019-11-18T23:07:04Z
30903631872	R	58985	16	2019-11-18T23:07:04Z
29007806464	R	58985	16	2019-11-18T23:07:04Z
27078426624	R	58985	16	2019-11-18T23:07:04Z
25165824000	R	58985	16	2019-11-18T23:07:04Z
23219666944	R	58985	16	2019-11-18T23:07:04Z
21239955456	R	58985	16	2019-11-18T23:07:04Z
19243466752	R	58985	16	2019-11-18T23:07:04Z
17196646400	R	58985	16	2019-11-18T23:07:04Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 17196646400
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "0",
        "node": "quartz20",
        "children": {
          "core": "34-35"
        }
      }
    ]
  }
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 19243466752
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "0",
        "node": "quartz20",
        "children": {
          "core": "30-33"
        }
      },
      {
        "rank": "1",
        "node": "quartz21",
        "children": {
          "core": "32-35"
        }
      }
    ]
  }
}
.
.
.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jobid: 36507222016
{
  "version": 1,
  "execution": {
    "R_lite": [
      {
        "rank": "0",
        "node": "quartz20",
        "children": {
          "core": "30-33"
        }
      },
      {
        "rank": "1",
        "node": "quartz21",
        "children": {
          "core": "32-35"
        }
      }
    ]
  }
}

```

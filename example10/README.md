### A data conduit strategy

- **salloc -N3 -ppdebug**

- **setenv PKG_CONFIG_PATH /usr/global/tools/flux/toss_3_x86_64_ib/default/lib/pkgconfig**

- make

- **setenv FLUX_SCHED_OPTIONS "node-excl=true"** *# Make sure the scheduler module will do node-exclusive scheduling*

- **srun --pty --mpi=none -N3 /usr/global/tools/flux/toss_3_x86_64_ib/default/bin/flux start -o,-S,log-filename=out**

- **flux submit -N 1 -n 1 ./datastore.py**

- **flux submit -N 1 -n 1 ./compute.lua 1**
- **flux submit -N 1 -n 1 ./compute.lua 1**
- **flux submit -N 1 -n 1 ./compute.lua 1**
- **flux submit -N 1 -n 1 ./compute.lua 1**

- **flux wreck attach 1**
```
Starting....
Waiting for a packet
{u'test': 101}
Waiting for a packet
{u'test': 101, u'1527743330': u'os.time'}
Waiting for a packet
{u'test': 101, u'1527743331': u'os.time', u'1527743330': u'os.time'}
Waiting for a packet
{u'test': 101, u'1527743331': u'os.time', u'1527743330': u'os.time'}
Waiting for a packet
{u'test': 101, u'1527743332': u'os.time', u'1527743331': u'os.time', u'1527743330': u'os.time'}
Waiting for a packet
{u'test': 101, u'1527743333': u'os.time', u'1527743332': u'os.time', u'1527743331': u'os.time', u'1527743330': u'os.time'}
Waiting for a packet
Bye bye!
```

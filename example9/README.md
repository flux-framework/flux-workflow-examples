<<<<<<< HEAD
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
=======
### Example 9 - KVS Python Binding Example

#### Description: Use the KVS Python interface to store user data into KVS

1. Launch a Flux instance by running `flux start`, redirecting log messages to the file `out` in the current directory:

`flux start -s 1 -o,-S,log-filename=out`

2. Submit the Python script:

`flux submit -N 1 -n 1 ./kvsput-usrdata.py`

```
6705031151616
```

3. Attach to the job and view output:

`flux job attach 6705031151616`

```
hello world
hello world again
```

4. Each job is run within a KVS namespace. `FLUX_KVS_NAMESPACE` is set, which is automatically read and used by the KVS operations in the handle. To take a look at the job's KVS, convert its job ID to KVS:

`flux job id --from=dec --to=kvs 6705031151616`

```
job.0000.0619.2300.0000
```

5. The keys for this job will be put at the root of the namespace, which is mounted under "guest". To get the value stored under the first key "usrdata":

`flux kvs get job.0000.0619.2300.0000.guest.usrdata`

```
"hello world"
```

6. Get the value stored under the second key "usrdata2":

`flux kvs get job.0000.0619.2300.0000.guest.usrdata2`
>>>>>>> master

- **flux wreck attach 1**
```
<<<<<<< HEAD
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
=======
"hello world again"
>>>>>>> master
```

##### Notes

- `f = flux.Flux()` creates a new Flux handle which can be used to connect to and interact with a Flux instance.

- `kvs.put()` places the value of _udata_ under the key **"usrdata"**. Once the key-value pair is put, the change must be committed with `kvs.commit()`. The value can then be retrieved with `kvs.get()`

- `kvs.get()` on a directory will return a KVSDir object which supports the `with` compound statement. `with` guarantees a commit is called on the directory.

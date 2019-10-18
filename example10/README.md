### Example 10: A Data Conduit Strategy

#### Description: Use a data stream to send packets through

1. `salloc -N3 -ppdebug`

2. Point to `flux-core`'s `pkgconfig` directory:

| Shell     | Command                                                                                  |
| -----     | ----------                                                                               |
| tcsh      | `setenv PKG_CONFIG_PATH <FLUX_INSTALL_PATH>/lib/pkgconfig`   |
| bash/zsh  | `export PKG_CONFIG_PATH='<FLUX_INSTALL_PATH>/lib/pkgconfig'` |

3. `make`

4. Make sure the scheduler module will do node-exclusive scheduling:

| Shell     | Command                                        |
| -----     | ----------                                     |
| tcsh      | `setenv FLUX_SCHED_OPTIONS "node-excl=true"`   |
| bash/zsh  | `export FLUX_SCHED_OPTIONS='node-excl=true'`   |

5. `srun --pty --mpi=none -N3 flux start -o,-S,log-filename=out`

6. `flux submit -N 1 -n 1 ./datastore.py`

7. `flux submit -N 1 -n 1 ./compute.lua 1`

8. `flux submit -N 1 -n 1 ./compute.lua 1`

9. `flux submit -N 1 -n 1 ./compute.lua 1`

10. `flux submit -N 1 -n 1 ./compute.lua 1`

11. Attach to running/completed job:

`flux wreck attach 1`

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

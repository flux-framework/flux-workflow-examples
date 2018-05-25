### KZ stream examples

- Using kz stream interface to fetch a job's stdout

- **/usr/global/tools/flux/toss_3_x86_64_ib/default/bin/flux start -s 2 -o,-S,log-filename=out**

- **flux submit -N 2 -n 2 hostname**

```
submit: Submitted jobid 1
```

- **fetch-stdout.py**
```
quartz1922
quartz1922
```

- **fetch-stdout.lua**
```
quartz1922
quartz1922
```


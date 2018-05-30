### Simple KVS Python binding examples

- Using kvs python interfaces to store user data into kvs

- **/usr/global/tools/flux/toss_3_x86_64_ib/default/bin/flux start -s 1 -o,-S,log-filename=out**

- **flux submit -N 1 -n 1 kvsput-usrdata.py **

```
submit: Submitted jobid 1
```

- **flux wreck attach 1**

```
mydata
mydata2
```

- **flux kvs get lwj.0.0.1.usrdata**

```
"mydata"
```

- **flux kvs get lwj.0.0.1.usrdata2**

```
"mydata2"
```

### Example 9 - Simple KVS Python Binding Example

#### Description: Use KVS Python interfaces to store user data into KVS

1. `flux start -s 1 -o,-S,log-filename=out`

2. `flux submit -N 1 -n 1 ./kvsput-usrdata.py`

```
submit: Submitted jobid 1
```

3. Attach to running/completed job:

`flux wreck attach 1`

```
mydata
mydata2
```

4. Get data stored in KVS:

`flux kvs get lwj.0.0.1.usrdata`

```
"mydata"
```

`flux kvs get lwj.0.0.1.usrdata2`

```
"mydata2"
```

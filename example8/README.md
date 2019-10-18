### Example 8 - Using a KZ stream

#### Description: Use a KZ stream interface to fetch a job's stdout

1. `flux start -s 2 -o,-S,log-filename=out`

2. `flux submit -N 2 -n 2 hostname`

```
submit: Submitted jobid 1
```

3. `./fetch-stdout.py`

```
node1922
node1922
```

4. `./fetch-stdout.lua`

```
node1922
node1922
```

#!/usr/bin/env sh

NJOBS=750
MAXTIME=$(expr ${NJOBS} + 2)

for i in `seq 1 ${NJOBS}`; do
    flux submit --nnodes=1 --ntasks=1 --cores-per-task=1 sleep 0
done

KEY=$(echo $(flux wreck kvs-path ${NJOBS}).state)
./kvs-watch-until.lua -t ${MAXTIME} ${KEY} 'v == "complete"'
flux wreck ls -n 100
echo "Final Level Done"

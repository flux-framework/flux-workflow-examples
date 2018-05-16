#!/usr/bin/env sh

NJOBS=10
MAXTIME=$(expr ${NJOBS} + 2) 

flux submit --nnodes=1 --ntasks=1 --cores-per-task=2 ./io-forwarding.lua ${MAXTIME}
for i in `seq 1 ${NJOBS}`; do
    flux submit --nnodes=2 --ntasks=4 --cores-per-task=2 ./compute.lua 1 
done

KEY=$(echo $(flux wreck kvs-path 1).state)
kvs-watch-until.lua -t ${MAXTIME} ${KEY} 'v == "complete"'
flux wreck ls -n 100

# print mock-up prevenance data
for i in `seq 1 $(expr ${NJOBS} + 1)`; do
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Jobid: ${i}"
    echo "Cmdline: " "$(flux kvs get $(flux wreck kvs-path ${i}).cmdline)"
    echo "$(R_lite.lua ${i})" | sed -e 's/^/Resource: /'
done

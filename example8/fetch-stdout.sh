JOBID=$(flux mini submit --nodes=1 --ntasks=1 --cores-per-task=2 hostname)
KVSJOBID=$(flux job id --from=dec --to=kvs ${JOBID})
flux kvs get ${KVSJOBID}.R | jq '.execution.R_lite[0].node'

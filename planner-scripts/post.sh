#! /bin/bash

# moves the output files

vmv -f output.sas $SAS 2> /dev/null
for groups in $(ls *.groups 2> /dev/null)
do
    vmv -f $groups $PROBLEM_NAME.$groups
done
vmv -f output $SAS_PLUS 2> /dev/null
vmv -f elapsed.time $PROBLEM_NAME.time 2> /dev/null
vmv -f plan_numbers_and_cost $PROBLEM_NAME.cost 2> /dev/null

for plan in $(ls sas_plan* 2> /dev/null)
do
    if [[ $(cat $plan) != "" ]]
    then
        vmv -f $plan $PROBLEM_NAME.${plan##*_}
    fi
done

vecho $'\x1b[34;1m'---- process $PPID finished ----------------------------
vecho Result:
if ls $PROBLEM_NAME.plan* 2> /dev/null
then
    $VERBOSE && cat $PROBLEM_NAME.cost
else
    vecho "Search Failed: No path was found in the current configuration."
fi
vecho --------------------------------------------------------$'\x1b[0m'

# cleanup
$DEBUG || rm -rf $TMPDIR

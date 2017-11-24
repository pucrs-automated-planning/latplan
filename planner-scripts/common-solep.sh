#!/bin/bash

. $SCRDIR/util.sh

################################################################
#### option processing

shift $(($OPTIND - 1))

if [[ ( $1 == "" ) || $OPT_ERROR ]]
then
    cat >&2 <<EOF
usage: ./$0
       [-o OPTIONS]        -- search options
       problemfile [domainfile=domain.pddl]
EOF
    exit 2
fi

################################################################
#### argument processing

problem=$(readlink -ef $1)
probname=$(basename $problem .pddl)
probdir=$(dirname $problem)

if [[ $2 != "" ]]
then
    domain=$(readlink -ef $2)
else
    domain=$probdir/domain.pddl
fi
if [[ ! -e $domain ]]
then
    domain=$probdir/$probname-domain.pddl
fi
if [[ ! -e $domain ]]
then
    echo "no domain file $domain!" >&2
    exit 1
fi

################################################################
#### common finalization hook (further call finalize)
# automatically copies the log and stat file
# but not plan files: because they are planner specific

_interrupt (){
    echo "Interrupted!"
    mykill $pid
    exit 1
}
_finalize (){
    cp $STAT $probdir/$probname.stat
    cp log $probdir/$probname.log
    negatively-proven && touch $probdir/$probname.negative
    finalize
    vecho $'\x1b[34;1m'--------------------------------------------------------
    vecho Result:
    report-results 2> /dev/null
    local status=$?
    [[ $status == 0 ]] || \
        vecho "Search Failed: No path was found in the current configuration."
    vecho --------------------------------------------------------$'\x1b[0m'
    exit $status
}

################################################################
#### run

trap "_interrupt" SIGHUP SIGQUIT SIGABRT SIGSEGV SIGTERM SIGXCPU SIGXFSZ
trap "_finalize" EXIT
pushd $TMP > /dev/null

cp -t . $probdir/t01.pddl
cp -t . $probdir/t02.pddl
cp -t . $probdir/t03.pddl
cp $problem problem.pddl
cp $domain domain.pddl
plan &> log &
pid=$!

if $VERBOSE
then
    touch log
    tail -f --pid $pid log
else
    wait $pid
fi


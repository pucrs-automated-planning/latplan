#!/bin/bash

. $SCRDIR/util.sh

################################################################
#### option processing

shift $(($OPTIND - 1))

if [[ ( $1 == "" ) || $OPT_ERROR ]]
then
    cat >&2 <<EOF
Usage: ./$0
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
    echo "common.sh($$): received $1, exiting..."
    exit 1
}
_finalize (){
    $VERBOSE && echo "common.sh($$): forcibly killing all subprocesses"
    $SCRDIR/killall.sh $pid -9
    cp log $probdir/$probname.log
    negatively-proven && touch $probdir/$probname.negative
    finalize                    # call planner-specific finalizer
    vecho $'\x1b[34;1m'--------------------------------------------------------
    vecho Result:
    $VERBOSE && report-results 2> /dev/null
    vecho --------------------------------------------------------$'\x1b[0m'
    plan-found
    exit $?
}

################################################################
#### run

for sig in SIGHUP SIGQUIT SIGABRT SIGSEGV SIGTERM SIGXCPU SIGXFSZ
do
    trap "_interrupt $sig" $sig
done

trap "_finalize" EXIT
pushd $TMP > /dev/null

cp $problem problem.pddl
cp $domain domain.pddl
plan &> log &
pid=$!

if $VERBOSE
then
    touch log
    tail -f log --pid=$pid &
fi

wait $pid


#!/bin/bash

echo "Running limit.sh($$): $@"

# ********  Exported variables: **********
# 
# SCRDIR -- script dir. the dir of this file
# DIR -- original PWD when this file is invoked
# VERBOSE -- verbosity flag
# DEBUG -- debug flag, disable removing tmp dir when enabled
# TMP -- temprary working directory for the planner.

export SCRDIR=$(dirname $(readlink -ef $0))
. $SCRDIR/util.sh
export OPTIONS
export DIR=$PWD
export VERBOSE=false
export DEBUG=false

mem=
time=
export ITERATED=false

while getopts ":-vido:t:m:" opt; do {
        case ${opt} in
            o)  # specifies the search option
                OPTIONS=${OPTARG:-$OPTIONS} ;;
            v)  # increase verbosity: tail -f search.log during the search
                VERBOSE=true ;; # true
            d)  # do not remove the temporary directory for debugging
                # assume -v
                DEBUG=true ;
                VERBOSE=true ;;
            i)  # use iterated run if possible
                ITERATED=true ;;
            t)  # hard limit of the execution time, in sec.
                time=${OPTARG} ;
                [[ $time == -1 ]] && time= ;
                [[ $time == 'unlimited' ]] && time= ;;
            m)  # limit on the memory usage, in kB.
                mem=${OPTARG};
                [[ $mem == -1 ]] && mem= ;
                [[ $mem == 'unlimited' ]] && mem= ;;
            -)  break ;;
            \?) OPT_ERROR=1; break;;
            * ) echo "limit.sh($$): unsupported option $opt" ;;
        esac
    }
done

shift $(( $OPTIND - 1 ))
if [[ ( $1 == "" ) || $OPT_ERROR ]] ; then {
        cat >&2 <<EOF
usage: ./limit.sh
       [-v] [-d]
       [-t time (sec)]
       [-m memory (kB)] [--] command args...
 examples:
  limit.sh -v -t 100 -- macroff-clean problem.pddl domain.pddl
EOF
        exit 2
    }
fi

interrupt (){
    target=$(pgrep -P $pid)
    echo "limit.sh($$): received $1, killing subprocess $target with $1"
    vechodo kill -s $1 $target
    while ps -p $target &>/dev/null
    do
        sleep 0.5
        pstree -pl $pid
    done
    echo "limit.sh($$): killed subprocess $target died"
}

finalize (){
    $DEBUG || rm $($VERBOSE && echo -v) -rf $TMP
    $DEBUG && echo "limit.sh($$): Debug flag is on, $TMP not removed!"
}

for sig in SIGHUP SIGQUIT SIGABRT SIGSEGV SIGTERM SIGXCPU SIGXFSZ
do
    trap "interrupt $sig" $sig
done 
trap "finalize" EXIT

mkdir $($VERBOSE && echo -v) -p /tmp/newtmp
export TMP=$(mktemp -d --tmpdir=/tmp/newtmp limit.XXXXXXXXXX )
command=$(readlink -ef "$SCRDIR/$1") ; shift ;

vecho "limit.sh($$): mem: ${mem:-unlimited} kB, time: ${time:-unlimited} sec"
vecho "limit.sh($$): running at $TMP"
vecho "limit.sh($$): command to execute: $command"
vecho "limit.sh($$): current planner options : $OPTIONS"
vecho "limit.sh($$): note: time precision is 0.5 sec"

vecho TIMEOUT_IDSTR="LIMIT_SH " $SCRDIR/timeout/timeout -x 0.1 -c \
    $([ -z $mem  ] || echo "--memlimit-rss $mem") \
    $([ -z $time ] || echo "-t            $time") \
    $command $@

TIMEOUT_IDSTR="LIMIT_SH " $SCRDIR/timeout/timeout -x 0.1 -c \
    $([ -z $mem  ] || echo "--memlimit-rss $mem") \
    $([ -z $time ] || echo "-t            $time") \
    $command $@

exitstatus=$?
case $exitstatus in
    0) $VERBOSE && echo "limit.sh($$): The program successfully finished." ;;
    *) echo "limit.sh($$): Error occured. status: $exitstatus" ;;
esac

exit $exitstatus

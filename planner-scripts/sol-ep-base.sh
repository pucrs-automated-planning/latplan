#!/bin/bash

SCRDIR=$(dirname $0)
FF=$SCRDIR/macroff
VALIDATE=~/repos/downward/src/validate
# ulimit -t 300
# ulimit -v 1000000
# ulimit -c 0
validate() {
    local DIR=$1
    local PDDL=$2
    local PFILE=$3

    local SOLUTION=$PFILE.soln
    local VALOUTPUT=`$VALIDATE $DIR$PDDL $DIR$PFILE $SOLUTION`
    if echo $VALOUTPUT | grep -q 'Failed plans:'; then
        echo "VALIDATION FAILED:"
        echo $VALOUTPUT
        return -1
    elif ! echo $VALOUTPUT | grep -q 'Successful plans:'; then
        echo "VALIDATION ERROR:"
        echo $VALOUTPUT
        return -1
    fi
    echo "VALIDATION SUCCESSFUL"
    rm $SOLUTION
    return 0
}

run() {
    local MACROS=$1
    local DIR=$2
    local PDDL=$3
    local PFILE=$4
    local PROBLEM=$5
    local FILTER=$6

    echo --------------------------------------------------------------------
    echo $PDDL - $PFILE
    echo --------------------------------------------------------------------
    rm -f ffua.out
    if (( FILTER == 1 )); then
        $FF -q $MACROS -p $DIR -o $PDDL -f $PFILE -m D 
    else
        $FF -q $MACROS -p $DIR -o $PDDL -f $PFILE -M 1
    fi
    echo -ne "$PDDL\t$PFILE\t" >> macrocollection.out
    if test -f ffua.out; then
        echo -ne "$PROBLEM\t" >> macrocollection.out
        echo -ne "1\t" >> macrocollection.out
        if validate $DIR $PDDL $PFILE; then
            echo -ne "0\t" >> macrocollection.out
        else
            echo -ne "1\t" >> macrocollection.out
        fi
        cat ffua.out >> macrocollection.out
    else
        #  echo -e "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" >> macrocollection.out
        echo >> macrocollection.out
    fi
}

accumulate() {
    local DIR=$2
    local PDDL=$3
    local PFILE=$4
    local MACROFILE=$1
    echo --------------------------------------------------------------------
    echo Processing training step $PDDL - $PFILE
    echo --------------------------------------------------------------------
    rm -f ffua.out
    $FF -m P -r $MACROFILE -p $DIR -o $PDDL -f $PFILE
    echo -ne "$PDDL\t$PFILE\t" >> trainingcollection.out
    if test -f ffua.out; then
        echo -ne "$PROBLEM\t" >> trainingcollection.out
        echo -ne "1\t" >> trainingcollection.out
        if validate $DIR $PDDL $PFILE; then
            echo -ne "0\t" >> trainingcollection.out
        else
            echo -ne "1\t" >> trainingcollection.out
        fi
        cat ffua.out >> trainingcollection.out
    else
        echo -e "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1000000\t0\t0" >> trainingcollection.out
        #   echo >> macrocollection.out
    fi
}

filtering() {
    local DIR=$2
    local PDDL=$3
    local PFILE=$4
    local MACROFILE=$1
    echo --------------------------------------------------------------------
    echo Performing static filtering $PDDL
    echo --------------------------------------------------------------------
    rm -f ffua.out
    $FF -m F -r $MACROFILE -p $DIR -o $PDDL -f $PFILE
}

train_one_domain() {
    local appname=$1
    local path=$2
    local domain=$3
    shift 3
    local nrprobs=$(($#))
    local times=times.out

    echo -ne "Starting time for training in domain $appname: " > $times
    date >> $times
    echo -ne "" >> $times
    i=0;
    for name in "$@" ; do
        problem[$i]=${name}
        echo "problem[$i] = ${problem[$i]}"
        i=$(( $i + 1 ))
    done

    rm -f $appname.macros
    echo solve each training problem
    for ((i=0;i<$nrprobs;i++)) ; do
        accumulate $appname.macros $path $domain ${problem[$i]}
    done
    mv -f trainingcollection.out $appname.trainingcollection.out
    $SCRDIR/extract.pl $appname.nomacrossummary.txt $appname.trainingcollection.out
    
    echo step 1 for static filtering and ranking
    cp $appname.macros $appname.macros.all
    filtering $appname.macros $path $domain ${problem[0]}
    cp $appname.macros $appname.macros.filtered
    rm -f *soln
    echo generate one file for each macro
    $FF -q $appname.macros.filtered -m  E -p $path -o $domain -f ${problem[0]}
    for ((i=1;i<=15;i++)) ; do
        rm -f macrocollection.out
        macrofile="$appname.macros.filtered.$i"
        outputfile="$appname.collection.$i"
        if test -f $macrofile; then
            for ((j=0;j<$nrprobs;j++)) ; do
                run $macrofile $path $domain ${problem[$j]}
            done
            mv -f macrocollection.out $outputfile
        fi
    done
    echo reorder macros
    $SCRDIR/extract.pl $appname.summary.txt $appname.collection.*
    echodo ls -la
    echodo pwd
    # echodo "$FF -a $appname.summary.txt -q $appname.macros.filtered -m  R -p $path -o $domain -f ${problem[0]}"
    echo "run with top k macros (iterate after k)"
    for ((i=1;i<=15;i++)) ; do
        rm -f macrocollection.out
        macrofile="$appname.macros.filtered.top.$i"
        outputfile="$appname.collection.top.$i"
        if test -f $macrofile; then
            for ((j=0;j<$nrprobs;j++)) ; do
                run $macrofile $path $domain ${problem[$j]}
            done
            mv -f macrocollection.out $outputfile
        fi
    done
    echo process stats of running with top k macros
    $SCRDIR/extract.pl $appname.summary.top.txt $appname.collection.top.*
    echo find the top k macros with the best performance and set their file as macros.best
    $SCRDIR/selectbestmacrofile.pl $appname.nomacrossummary.txt $appname.summary.top.txt $appname.macros.filtered.top $appname.macros.best
    echo -ne "End time for training in domain $appname: " >> $times
    date >> $times
    echo -ne "" >> $times
    mv $times $appname.$times
}

learn (){
    # learn domain.pddl [problems ...]
    local dir=$(dirname $domain)
    train_one_domain $(basename $dir) $dir/ $@
}
solve (){
    # solve /path/to/domain.pddl /path/to/problem.pddl
    local pname=$(basename $2 .pddl)
    local pnum=${pname#p}
    local pnum=${pname#0}
    local dir=$(dirname $1)
    local appname=$(basename $dir)
    run $appname.macros.best $dir/ $(basename $1) $(basename $2)
}

echodo (){
    echo $*
    $*
}


domain=$(readlink -ef $1)
main_problem=$(readlink -ef $2)
shift 2
training_instances=$@

learn $(basename $domain) $training_instances
echo "*************** solving **********"
solve $domain $main_problem

# optical() {
# run optical.macros.best /home/users/abotea/experiments/data/ipc4/DOMAINS/promela/optical-telegraph/adl/ domain.pddl p01-opt2.pddl 1
# run optical.macros.best /home/users/abotea/experiments/data/ipc4/DOMAINS/promela/optical-telegraph/adl/ domain.pddl p48-opt49.pddl 48

# mv -f onemacrocollection.out onemacroopticalcollection.out
# mv *soln ./optical
# }

# if test -f philosophers.macros.best; then
#   philosophers
# fi

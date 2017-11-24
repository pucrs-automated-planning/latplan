#!/bin/bash

vechodo (){
    vecho $*
    $*
}

echodo (){
    echo $*
    $*
}

vecho (){
    $VERBOSE && echo $@
}

v (){
    name=$1
    shift
    if $VERBOSE
    then
        $name -v $@
    else
        $name $@
    fi
}

vmv (){
    v mv $@
}
vrm (){
    v rm $@
}
vcp (){
    v cp $@
}

export -f vecho vrm vmv vcp v

sleep=3
mykill (){
    ps $1 &> /dev/null && {
        pstree -p -H $1 $1
        vechodo $SCRDIR/killall.sh $1 -SIGXCPU
        vechodo $SCRDIR/killall.sh $1 -SIGTERM
        vechodo sleep $sleep
        vecho sleep end
        ps $1 &> /dev/null && {
            vechodo $SCRDIR/killall.sh $1 -SIGKILL
        }
    }
}
export -f mykill

#!/bin/bash


finalize (){

    echo "finish!"
}

trap finalize EXIT

sleep 1
echo "status: $?"

sleep 30 &

pid=$!

{
    echo pid: $pid
    sleep 1
    kill -s TERM $pid
} &
echo aa
jobs
wait $pid
echo "status: $?"



exit 1

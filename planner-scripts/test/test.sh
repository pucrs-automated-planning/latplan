#!/bin/bash

. ../test-common.sh

# quick tests
../clean.sh

# success ../limit.sh -v -d -- yahsp3-clean p01.pddl domain.pddl
# 
# exit

test-non-ff (){
    # this should finish normally (because it is easy)
    ../clean.sh

    section $1
    success ../limit.sh $1 p01.pddl domain.pddl
    success ../limit.sh -- $1 p02.pddl domain.pddl
    success ../limit.sh -v -- $1 p03.pddl domain.pddl

    fail ../limit.sh -t 1 -- $1 p22.pddl domain.pddl
    fail test -e p22.negative

    # # increased verbosity
    # success ../limit.sh -t 1 -v -- $1 p01.pddl domain.pddl
    # 
    # # debugging: do not remove temporary directory
    # success ../limit.sh -t 1 -d -- $1  p03.pddl domain.pddl

    # what happens when there are no solution?
    fail ../limit.sh -v -- $1 unsolvable.pddl domain.pddl

    success test -e unsolvable.negative
}


#  mff doesnt work at all
for planner in cached-fd fd yahsp-mco jasper mercury ff lpg marvin1 marvin2 mpc mp m probe yahsp3
do
    test-non-ff $planner-clean
done

# section marvin1-typetest
# 
# fail ../limit.sh -t 1 -v -- marvin1-clean tidy-p01.pddl tidy-domain.pddl


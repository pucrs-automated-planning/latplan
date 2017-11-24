#!/bin/bash

## metric ff
# this should finish normally (because it is easy)
../clean.sh
../limit.sh mff-clean p01.pddl domain.pddl

../limit.sh -t 1 -- mff-clean p01.pddl domain.pddl

../limit.sh -t 1 -- mff-clean p18.pddl domain.pddl

# increased verbosity
../limit.sh -t 1 -v -- mff-clean p01.pddl domain.pddl


# debugging: do not remove temporary directory
../limit.sh -t 1 -d -- mff-clean  p03.pddl domain.pddl

# what happens when there are no solution?
../limit.sh -t 1 -v -- mff-clean unsolvable.pddl domain.pddl

# action-cost domain

../limit.sh -t 1 -v -- mff-clean barman-problem.pddl barman-domain.pddl

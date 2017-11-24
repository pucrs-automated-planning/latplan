#!/bin/bash

## ff
# this should finish normally (because it is easy)
../clean.sh
../limit.sh solep-clean p01.pddl domain.pddl

../limit.sh -t 1 -- solep-clean p18.pddl domain.pddl

# increased verbosity
../limit.sh -t 1 -v -- solep-clean p18.pddl domain.pddl

# debugging: do not remove temporary directory
../limit.sh -t 1 -d -- solep-clean p18.pddl domain.pddl

# what happens when there are no solution?
../limit.sh -t 1 -v -- solep-clean unsolvable.pddl domain.pddl


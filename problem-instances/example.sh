#!/bin/bash

parallel --files <<EOF

./generate.py 7 100 noise saltpepper 0.06 noise gaussian 0.3 hanoi 4 3
./generate.py 14 100 noise saltpepper 0.06 noise gaussian 0.3 hanoi 4 3

EOF

echo "done!"

#!/bin/sh

rm $0

python "manage.py"

echo "

------------------
(program exited with code: $?)" 		



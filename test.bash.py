#!/bin/bash -xv
# SPDX-FileCopyringhtText: 2022 Takato Tanimoto
# SPDX-License-Identifier: BSD-3-Clause

ng () {
        echo NG at Line $1
        res=1
}

res=0

### I/O TEST ###

out=$(seq 5 | ./plus_stdin.py)

[ "${out}" = 15 ] || ng ${LINENO}

### STRANGE INPUT ###
out=$(echo あ | ./plus_stdin.py)
[ "$?" =1 ]       || ng ${LINENO}
[ "${out}" ="" ]  || ng ${LINENO}

out=$(echo | ./plus_stdin.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" ="" ]  || ng ${LINENO}

[ "$res" = 0 ] && echo OK
exit $res

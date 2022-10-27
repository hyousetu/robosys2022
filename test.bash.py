#!/bin/bash

out=$(seq 5 | ./plus_stdin.py)

[ "${out}" = 14 ]

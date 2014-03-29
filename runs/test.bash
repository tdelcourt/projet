#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -o test.out
#PBS -N test

module load python/2.7.2

python2.7 /work/tdelcour/test.py blug -tmp $TMPDIR
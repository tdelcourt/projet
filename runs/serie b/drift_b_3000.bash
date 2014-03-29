#!/bin/bash -l

#PBS -l nodes=1:ppn=1

#PBS -o drift_b_3000.out
#PBS -N drift_b_3000


module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_drift.py 3000

#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=150:00:00
#PBS -o coev_c_5000.out
#PBS -N coev_c

module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_coev.py 5000
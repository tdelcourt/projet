#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=150:00:00
#PBS -o hetero_5000_0.0001.out
#PBS -N hetero_5000_0.0001

module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_hetero_taux_stables.py 5000 0.0001
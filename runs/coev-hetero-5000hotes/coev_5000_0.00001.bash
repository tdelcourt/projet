#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=150:00:00
#PBS -o coev_5000_0.00001.out
#PBS -N coev_5000_0.00001

module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_coev_taux_stables.py 5000 0.00001
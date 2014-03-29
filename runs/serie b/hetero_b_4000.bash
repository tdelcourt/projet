#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=90:00:00
#PBS -o hetero_b_4000.out
#PBS -N hetero_b_4000



module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_hetero.py 4000

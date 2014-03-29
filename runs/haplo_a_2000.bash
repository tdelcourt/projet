#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=60:00:00
#PBS -o haplo_a_2000.out
#PBS -N haplo_a

module load python/2.7.2

python2.7 /work/tdelcour/projet_py2_haplo.py 2000
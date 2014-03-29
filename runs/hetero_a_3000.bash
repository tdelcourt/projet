#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=70:00:00
#PBS -o hetero_a_3000.out
#PBS -N hetero_a_3000



module load python/3.4.0a1 

python3.4 $HOME/hetero_hydra_3000.py

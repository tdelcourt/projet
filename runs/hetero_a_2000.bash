#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=50:00:00
#PBS -o hetero_a_2000.out
#PBS -N hetero_a_2000



module load python/3.4.0a1 

python3.4 $HOME/hetero_hydra_2000.py
